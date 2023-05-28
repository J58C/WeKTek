start cmd.exe /c "cd .\studynet_django\studynet_vue && npm run serve"
start cmd.exe /c "ping localhost -n 25 -w 60000 > nul && start http://localhost:8080/"
call .\venv\Scripts\Activate
cd .\studynet_django
start /B python manage.py runserver
cls