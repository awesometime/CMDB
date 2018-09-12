#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
print(BASE_DIR) # G:\PyCharm\PythonProjects\cmdb\Client
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
# print(sys.path)
# ['G:\\PyCharm\\PythonProjects\\cmdb\\Client\\bin',
# 'G:\\PyCharm\\PythonProjects\\cmdb',
# 'G:\\PyCharm\\Python Projects',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\Scripts\\python36.zip',
# 'G:\\Python\\python-3.6.5\\DLLs',
# 'G:\\Python\\python-3.6.5\\lib',
# 'G:\\Python\\python-3.6.5',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\lib\\site-packages',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\lib\\site-packages\\setuptools-28.8.0-py3.6.egg',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\lib\\site-packages\\win32',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\lib\\site-packages\\win32\\lib',
# 'G:\\PyCharm\\PythonProjects\\python_virtualenv_for_django\\lib\\site-packages\\Pythonwin',
# 'G:\\PyCharm\\PythonProjects\\cmdb\\Client']

from core import handler

if __name__ == '__main__':

    handler.ArgvHandler(sys.argv)
