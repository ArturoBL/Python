call nssm.exe install myflaskservice "%cd%\run_server.bat"
call nssm set myflaskservice Description "My flask service"
call nssm.exe set myflaskservice AppStdout "%cd%\logs\my_flask_app_logs.log"
call nssm.exe set myflaskservice AppStderr "%cd%\logs\my_flask_app_logs.log"
call nssm set myflaskservice AppRotateFiles 1
call nssm set myflaskservice AppRotateOnline 1
call nssm set myflaskservice AppRotateSeconds 86400
call nssm set myflaskservice AppRotateBytes 1048576
call nssm start myflaskservice

