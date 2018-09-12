项目原地址  [实战二：CMDB之资产管理系统](http://www.liujiangblog.com/course/django/116)

#### 细节
sn 唯一必须不能变 不变是刷新 变了是添加


#### 问题1  导包问题 python
```
import sys
import os

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
```

#### 问题2  error [WinError 10061] 由于目标计算机积极拒绝，无法连接。
```
pycharm  终端运行django 虚拟环境
cmd      终端运行Client 都需要虚拟环境

cmd
G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts>activate
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts>cd ..
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\python_virtualenv_for_django>cd ..
(python_virtualenv_for_django) G:\PyCharm\PythonProjects>cd cmdb/Client/bin
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\cmdb\Client\bin>main.py report_data
G:\PyCharm\PythonProjects\cmdb\Client
G:\PyCharm\PythonProjects\cmdb\Client\log\cmdb.log
正在将数据发送至： [http://127.0.0.1:8000/assets/report/]  ......
[31;1m发送完毕！[0m
返回结果：资产已经加入或更新待审批区！
日志记录成功！


# pycharm 中关闭django后：
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\cmdb\Client\bin>main.py report_data
G:\PyCharm\PythonProjects\cmdb\Client
G:\PyCharm\PythonProjects\cmdb\Client\log\cmdb.log
正在将数据发送至： [http://127.0.0.1:8000/assets/report/]  ......
[31;1m发送失败，<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>[0m
日志记录成功！

(python_virtualenv_for_django) G:\PyCharm\PythonProjects\cmdb\Client\bin>
```
#### 问题3

BUG 在8000/admin/页面添加软件/系统资产后在dashboard中显示不正常

未解决
