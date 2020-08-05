# -*- coding:utf-8 -*-

import os
import sys
import time

# 手动更改hosts.git的目录位置


def push_hosts():
    # get hosts information from dns query, then schedule push it to github

    if sys.platform == 'win32':
        host_path = r'D:\py_project\hosts'

    else:
        host_path = '/opt/hosts'

    os.chdir(host_path)
    os.system('git add hosts.txt')
    os.system('git commit -m "update host {}"'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(5)
    os.system('git push')
