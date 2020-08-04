# -*- coding:utf-8 -*-
import os
import shutil


src_path = ['/opt/hosts_update/local_update/update_hosts_local.ps1',
            '/opt/hosts_update/local_update/update_local.bat',
            '/opt/hosts_update/local_update/update_local.py',
            '/opt/hosts/hosts.txt']
dst_path = ['/usr/share/nginx/www/dcit/hosts/update_hosts_local.ps1',
            '/usr/share/nginx/www/dcit/hosts/update_local.bat',
            '/usr/share/nginx/www/dcit/hosts/update_local.py',
            '/usr/share/nginx/www/dcit/hosts/hosts.txt']

# LOCAL_PATH = '/opt/hosts/hosts.txt'
# DST_PATH = '/usr/share/nginx/www/dcit/hosts/hosts.txt'


def mov_file():
    i = 0
    while i < len(src_path):
        if os.path.exists(dst_path[i] + '.bak'):
            os.remove(dst_path[i] + '.bak')
            shutil.copyfile(dst_path[i], dst_path[i] + '.bak')
        else:
            shutil.copyfile(dst_path[i], dst_path[i] + '.bak')

        shutil.move(src_path[i], dst_path[i])
        i += 1


if __name__ == '__main__':
    mov_file()
