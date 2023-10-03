#!/bin/bash
echo "Create migations"
sleep 5
python manage.py makemigrations main
echo "================================"

echo "Migrate"
python manage.py migrate
echo "================================"

echo "Start server"
python manage.py runserver 0.0.0.0:8050