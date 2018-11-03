import paramiko
import getpass
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass()
HOST = '10.10.10.8'
ssh_client.connect(HOST,port=22,username='emerson',password=password)

remote_command = ssh_client.invoke_shell()

remote_command.send('ena\n')
remote_command.send('vlan database\n')
remote_command.send('vlan 10 name IT462\n')
time.sleep(1)

remote_command.send('vlan 10 state active\n' )
remote_command.send('exit\n')
remote_command.send('conf t\n')
time.sleep(3)


for i in range(3,6):
    time.sleep(2)
    remote_command.send('interface f1/'+str(i)+'\n')
    remote_command.send('switchport mode access\n')
    remote_command.send('switchport access vlan 10\n')
    time.sleep(4)
    remote_command.send('exit\n')
remote_command.send('exit\n')
remote_command.send('sh vlan-switch\n')
time.sleep(2)
output = remote_command.recv(9999)

print(output.decode('ascii'))

ssh_client.close()
