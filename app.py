# -*- coding:utf-8 -*-

import urllib.request
import os
import shutil

HOST_URL = ''
LOCAL_PATH = ''


def main():
    urllib.request.urlretrieve(HOST_URL, 'hosts')

    if (os.path.exists(LOCAL_PATH + '.bak')):
        os.remove(LOCAL_PATH)
    else:
        shutil.copyfile(LOCAL_PATH, LOCAL_PATH + '.bak')

    shutil.move('hosts', LOCAL_PATH)
    os.system('ipconfig /flushdns')


if __name__ == '__main__':
    main()
