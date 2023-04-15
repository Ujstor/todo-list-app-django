from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.user.todolist.all():

        if response.method == 'POST':
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid input")

        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {})


@login_required
def home(request):
    num_lists = ToDoList.objects.filter(user=request.user).count()

    items_per_list = []
    for todolist in ToDoList.objects.filter(user=request.user):
        num_items = Item.objects.filter(todolist=todolist).count()
        items_per_list.append({"todolist": todolist, "num_items": num_items})

    return render(request, "main/home.html", {"num_lists": num_lists, "items_per_list": items_per_list})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})

@require_POST
def delete(request, id):
    ls = ToDoList.objects.get(id=id)
    ls.delete()
    return redirect("/view")