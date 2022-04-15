#coding:utf8
from common.Remote_ssh import *
from config.sources.readconfig import *
#dict1={}
host = eval(hosts)
password = eval(passwords)

try:
    '''for (k, v) in zip(host, password):
        ssh = Remote_ssh(k, v)'''
    ssh = Remote_ssh(host[1],password[1])
    #ssh.command('echo "hello">> /etc/apk/repositories')
    ssh.command('vi /etc/apk/repositories')
except Exception as e:
    print('error',e)