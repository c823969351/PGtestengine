#coding:utf8
from common.Remote_ssh import *
from config.sources.readconfig import *
#dict1={}
host = eval(hosts)
password = eval(passwords)

try:
    for (k, v) in zip(host, password):
        ssh = Remote_ssh('22', 'root', k, v)
        ssh.command('ls /')
except Exception as e:
    print('error',e)