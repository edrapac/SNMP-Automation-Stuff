import getpass
import telnetlib
hostlist = open('switches.txt','r')
password = getpass.getpass()
user = 'emerson'

for line in hostlist:
	HOST = line.strip()
	client = telnetlib.Telnet(HOST)
	client.read_until(b"Username: ")
	client.write(user.encode('ascii')+b'\n')

	if password:
		client.read_until('Password: '.encode('ascii'))
		client.write(password.encode('ascii')+b'\n')
	client.write('enable\n'.encode('ascii'))
	client.write('terminal length 0\n'.encode('ascii'))
	client.write('show run\n'.encode('ascii'))
	client.write('exit\n'.encode('ascii'))
	client.write('exit\n'.encode('ascii'))

	print(client.read_all().decode('ascii'))

hostlist.close()