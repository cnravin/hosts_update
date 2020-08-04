mkdir c:\temp1
cd /d c:\temp1
powershell (new-object system.Net.webclient).DownloadFile('https://it.digitalchina.com/dcit/hosts/update_hosts_local.ps1', 'update_hosts.ps1')
powershell Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
powershell -f update_hosts.ps1
cd /d c:\
del c:\temp1\*.* /s /q
rd c:\temp1 /s /q
@pause