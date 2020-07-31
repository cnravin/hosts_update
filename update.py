# -*- coding:utf-8 -*-

import urllib.request
import os
import shutil

HOST_URL = 'http://10.0.2.96/hosts'
# HOST_URL = 'https://raw.githubusercontent.com/cnravin/hosts/master/hosts.txt'
LOCAL_PATH = r'C:\Windows\System32\drivers\etc\hosts'


def main():
    urllib.request.urlretrieve(HOST_URL, 'hosts')
    # f = open('hosts','rb')
    # content = f.read()
    # hs = open(LOCAL_PATH,'wb')
    # hs.write(content)
    # hs.close()
    # f.close()

    if (os.path.exists(LOCAL_PATH + '.bak')):
        os.remove(LOCAL_PATH)
    else:
        shutil.copyfile(LOCAL_PATH, LOCAL_PATH + '.bak')

    shutil.move('hosts', LOCAL_PATH)
    os.system('ipconfig /flushdns')


if __name__ == '__main__':
    main()
