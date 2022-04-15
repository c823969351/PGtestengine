#-*- encoding:utf8 -*-
import paramiko


class Remote_ssh():
    def __init__(self, host, password, port=22, user='root'):
        self.port = port
        self.user = user
        self.password = password
        self.host = host

    def command(self, command):
        self.command = command
        self.myclient = paramiko.SSHClient()
        self.myclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.myclient.connect(hostname=self.host,
                              port=self.port,
                              username=self.user,
                              password=self.password)
        stdin, stdout, stderr = self.myclient.exec_command(self.command)
        print('{}===>>>'.format(self.host))
        print(stdout.readlines())
