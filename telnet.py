import telnetlib
import getpass
#http://srijit.com/working-cisco-ios-gns3/
HOST = input('Please enter ip:')

user = input('enter username:')

password = getpass.getpass() 

tn = telnetlib.Telnet(HOST, timeout = 20)


tn.read_until(b"Username: ")

tn.write(user.encode('ascii')+b'\n')

if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b'\n')

tn.write('enable\n'.encode('ascii'))

tn.write('cisco\n'.encode('ascii'))
tn.write('conf t\n'.encode('ascii'))
tn.write('int f0/1\n'.encode('ascii'))
tn.write('ip add 10.10.10.7 255.255.255.0 \n'.encode('ascii'))
tn.write('no shut\n'.encode('ascii'))
tn.write('exit\n'.encode('ascii'))
tn.write('exit\n'.encode('ascii'))

# tn.set_debuglevel(1000)
print(tn.read_very_eager())