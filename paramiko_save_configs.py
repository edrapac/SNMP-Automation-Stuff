import time
import paramiko
import getpass

hostlist = open('switches.txt','r')

username = 'emerson'
HOST=str()
password = getpass.getpass()
ssh_client  = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for line in hostlist:
    HOST = line.strip()
    ssh_client.connect(hostname = HOST,port=22,username=username,password = password)
    remote_command = ssh_client.invoke_shell()
    remote_command.send('ena\n')
    remote_command.send('copy running-config startup-config\n')
    remote_command.send('\n')
    time.sleep(5)

    remote_command.send('exit\n')
    remote_command.send('exit\n')
    
    output = remote_command.recv(9999)
    print(output.decode('utf-8'))
ssh_client.close
hostlist.close

