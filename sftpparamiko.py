import paramiko

ssh = paramiko.SSHClient() #initializes an SSH client

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #very important, without this your client would reject the server's public key
 
ssh.connect(hostname = 'ip_address_of_server',port = 22,username='username',password='password') # here you fill in the IP address of the server, your user credentials and password. Dont change the port number

localpath = '/path/you/want/to/put/file' #the path you want to download the file to on YOUR machine

remotepath = '/path/on/server/where/file/is' #the full path to the file on the server

sftp = ssh.open_sftp() #opens an sftp tunnel

sftp.get(remotepath,localpath) #gets the file and writes it to your localpath 

sftp.close()

ssh.close()