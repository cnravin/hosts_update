# -*- coding:utf-8 -*-

import os
import time

# 手动更改hosts.git的目录位置
HOST_PATH = r'D:\py_project\hosts'

os.chdir(HOST_PATH)
os.system('git add .\hosts.txt')
os.system('git commit -m "update host {}"'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
time.sleep(5)
os.system('git push')