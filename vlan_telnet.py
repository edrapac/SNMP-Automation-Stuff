import getpass
import telnetlib

HOST = "10.10.10.7"
user = input('please enter username')

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")

tn.write(user.encode('ascii')+b'\n')

if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b'\n')

tn.write("enable\n".encode('ascii'))
tn.write("vlan database\n".encode('ascii'))
tn.write('vlan 2 name PYTHON_VLAN\n'.encode('ascii'))
tn.write('exit\n'.encode('ascii'))
tn.write('exit\n'.encode('ascii'))
# tn.set_debuglevel(1000)
print(tn.read_all().decode('ascii'))