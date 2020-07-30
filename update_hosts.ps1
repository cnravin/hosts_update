## update hosts file from github
$local_path = 'C:\Windows\System32\drivers\etc\hosts'
$host_url = 'https://raw.githubusercontent.com/cnravin/hosts/master/hosts.txt'
$bak_path = 'C:\Windows\System32\drivers\etc\hosts.bak'
$temp_file = 'C:\temp1\hosts.txt'
$client = New-Object System.Net.WebClient
$client.DownloadFile($host_url, $temp_file)

if (!(Test-Path $local_path)){
    Move-Item $temp_file $local_path
}
elseif (Test-Path $bak_path) {
    Remove-Item $bak_path
    Rename-Item $local_path $bak_path
    Move-Item $temp_file $local_path
}
else {
    Rename-Item $local_path $bak_path
    Move-Item $temp_file $local_path
}

cmd /c 'ipconfig /flushdns'
