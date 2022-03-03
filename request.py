import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在known_hosts文件上的主机
# 即允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面，允许连接前的yes或no
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname="10.0.0.7", port=22, username="root", password="123456")
# 执行命令
#stdin, stdout, stderr分别代表标准输入，标准输出，标准错误
stdin, stdout, stderr = ssh.exec_command('df')
# 结果放到stdout中，如果有错误将放到stderr中
result = stdout.read().decode()
# 获取错误提示（stdout、stderr只会输出其中一个）
err = stderr.read()
# 关闭连接
ssh.close()
print(stdin, result, err)