@echo off
cd C:\inetpub\wwwroot\Report\env\Scripts
call activate
cd C:\inetpub\wwwroot\Report\vitoux_report\automated-pivot-report-main\daily-scripts\aced\recruitment
python execute.py >> log.txt 2>&1
