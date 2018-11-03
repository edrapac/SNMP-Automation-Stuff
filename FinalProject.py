#Emerson Drapac IT 462
#This Program will SSH to pre-configured router interfaces and configure FastEthernet0/0 on both routers and then configure SNMP services
import time
import paramiko


address_list = ['10.10.10.10','10.10.10.11'] #these are the addresses pre configured on seperate interfaces that I will ssh to, in order to configure SNMP and fast ethernet0/0
netid = '10.1.1.' # the net ID for FastEthernet0/0 on both routers
hostid = 1 #host ID on router 1 is 1, router 2 is 2

ssh_client  = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in range(len(address_list)):
    ssh_client.connect(hostname = str(address_list[i]),port=22,username='emerson',password = 'cisco') #connects the client to the specified devices
    remote_command = ssh_client.invoke_shell() #creates a shell for passing commands to the devices
    
    remote_command.send('enable\n')
    remote_command.send('configure terminal\n')
    time.sleep(3)
    remote_command.send('interface FastEthernet0/0\n')
    remote_command.send('ip address '+netid+str(hostid)+' 255.255.255.0\n') #here we set the IP address and then increment the host ID in the next line
    hostid+=1
    remote_command.send('media-type 100BaseX\n')
    time.sleep(3)
    remote_command.send('full-duplex\n')
    remote_command.send('no shutdown\n')
    time.sleep(5)
    remote_command.send('exit\n')
    time.sleep(3) #sleep is necessary so the routers do not get overwhelmed with commands before executing the previous command
    remote_command.send('snmp-server community public RO\n')
    remote_command.send('snmp-server community cisco@123 RW\n')
    remote_command.send('snmp-server host 10.10.10.5 public\n')
    remote_command.send('snmp-server enable traps\n')
    remote_command.send('exit\n')
    output = remote_command.recv(9999) #the max this channel can receive is 9999 bytes, which this is set to to make sure we dont miss anything
    print(output.decode('utf-8')) #initially the output is encoded, so it needs to be decoded in a human readable format such as ascii or utf-8
ssh_client.close #lastly we close the client

