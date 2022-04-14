# -*- coding:utf8 -*-
import configparser

cf = configparser.ConfigParser()
# 读取配置文件，如果写文件的绝对路径，就可以不用os模块
cf.read(r"D:\PGtestengine\config\ansible.conf")

# 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，
#secs = cf.sections()
#print(secs)

# 获取某个section名为Mysql-Database所对应的键
#options = cf.options("Mysql-Database")
#print(options)

# 获取section名为Mysql-Database所对应的全部键值对
#items = cf.items("Mysql-Database")
#print(items)

# 获取[Mysql-Database]中host对应的值
hosts = cf.get("hosts", "host")
passwords = cf.get("passwords","password")
