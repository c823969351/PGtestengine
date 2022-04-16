#coding:utf8
from config.sources.readconfig import *
import sys
from common.Remote_ssh import *


arg_list = []
arg_list.extend(sys.argv)


def help():
    print(
        "General usage:\n==============\nusage: python exec.py --help \n[-h hostname or hostname1,hostname2,...hostnamen] [--host hostname or hostname1,hostname2,...hostnamen] [hostgroup from *.conf file example:web01 web02 ... ]\n[-p hostnamepassword or hostname1password,hostname2password,...hostnamenpassword]\n[-c shellcommand]\n[-d ]"
    )


if len(arg_list) <= 1:
    print("请输入参数，具体用法用python exec.py --help查看")
    sys.exit()
for arg in arg_list:
    if arg == '--help':
        help()
        sys.exit()
command = ''
d_remotefile = ''
d_localfile = ''
p_remotefile = ''
p_localfile = ''

for arg in arg_list:
    if arg == '--host' or arg == '-h':
        location = arg_list.index(arg)
        host_list = []
        str = arg_list[location + 1]
        hosts = str.split(',')
    elif arg == '--password' or arg == '-p':
        location = arg_list.index(arg)
        pass_list = []
        pass_list.append(arg_list[location + 1])
        str = arg_list[location + 1]
        passwords = str.split(',')
    elif arg == '--command' or arg == '-c':
        location = arg_list.index(arg)
        comm_list = []
        comm_list.append(arg_list[location + 1])
        command = (arg_list[location + 1])

    elif arg in secs:
        hosts = cf.get(arg, "host")
        passwords = cf.get(arg, "password")

        hosts = eval(hosts)
        passwords = eval(passwords)

for arg in arg_list:
    if arg == '-d--remotefile':
        location = arg_list.index(arg)
        d_remotefile = (arg_list[location + 1])
    elif arg == '-d--localfile':
        location = arg_list.index(arg)
        d_localfile = (arg_list[location + 1])
    elif arg == '-p--remotefile':
        location = arg_list.index(arg)
        p_remotefile = (arg_list[location + 1])
    elif arg == '-p--localfile':
        location = arg_list.index(arg)
        p_localfile = (arg_list[location + 1])


##定义调用执行命令的函数
def exec_command():
    if type(hosts) == tuple:
        for k, v in zip(hosts, passwords):
            remote = Remote(k, v)
            remote.command(command)
    else:
        remote = Remote(hosts, passwords)
        remote.command(command)


##定义上传文件的函数
def exec_put():
    if type(hosts) == tuple:
        for k, v in zip(hosts, passwords):
            remote = Remote(k, v)
            remote.put(p_localfile, p_remotefile)
    else:
        remote = Remote(hosts, passwords)
        print(p_localfile,p_remotefile)
        remote.put(p_localfile, p_remotefile)


##定义下载文件的函数
def exec_download():

    if type(hosts) == tuple:
        for k, v in zip(hosts, passwords):
            remote = Remote(k, v)
            remote.download(d_remotefile, d_localfile)
    else:
        remote = Remote(hosts, passwords)
        remote.download(d_remotefile, d_localfile)


if len(command) > 0:
    exec_command()

if len(p_remotefile) > 0 and len(p_localfile) > 0:
    exec_put()

if  len(d_remotefile) > 0 and len(d_localfile) > 0 and type(hosts) == tuple:
    if len(hosts) < 2:
        exec_download()
    elif len(hosts) >= 2:
        print('download的时候请只指定一个主机,如果是配置文件配置的主机组，请检查配置文件主机组中是不是有多个主机')
elif len(d_remotefile) > 0 and len(d_localfile) > 0:
    exec_download()
