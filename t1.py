def register(roundl):
	f=0
	spl=['!','@','#','$','%','^','&','*','(',')','+','-','/',',','.','?',':',';','\"','\'','|','\\','~','`','{','}','[',']']
	if roundl>0:
		print('Do you want to register (y/n):',end=' ')
		sec_reg=input()
		if sec_reg=='n':
			exit()
	while f==0:
		print("Enter E-mail:",end=" ")
		mail=input()
		l=list(mail)
		at=mail.find('@')
		dot=mail.find('.',at)
		if '@' not in mail:
		    print("Incorrect e-mail. Enter correct e-mail")
		elif l.count('@')>=2:
			print("Incorrect e-mail. Enter correct e-mail")
		elif mail[at+1]=='.':
		    print("Incorrect e-mail format. Enter correct e-mail format")
		elif len(mail[at+1:dot])<4 or [True for i in mail[at+1:dot] if i in spl] :
		    print("Incorrect e-mail. Enter correct e-mail")
		elif len(mail[:at])<3 or mail[0] in spl or mail[0].isdigit():
		    print("Incorrect e-mail. Enter correct e-mail")
		elif mail[-4:]!='.com' or [True for i in mail[-4:] if i in spl and i!='.']:
		    print("Incorrect e-mail. Enter correct e-mail")
		else:
			with open("Mail and Pwd.txt", "r") as file:
				filemail=file.readlines()
			for line in filemail:
				word=line.split(':')
				if mail in word[0]:
					print("E-mail already registered.")
					print('Enter \'login\'/\'register\'with different id:',end=' ')
					a_reg=input()
					if a_reg.lower()=='register':
						register(roundl)
						exit()
					elif a_reg.lower()=='login':
						login(roundl)
						exit()
			f=1
	u=lo=s=d=0
	while f==1:
		print("Enter password:",end=" ")
		pwd=input()
		if len(pwd)<=5 or len(pwd)>15:
			print('Not satisfied condition. Enter password in correct format')
		else:
			for i in range(len(pwd)):
				if pwd[i].isupper():
					u=1
				elif pwd[i].islower():
					lo=1
				elif pwd[i] in spl:
					s=1
				elif pwd[i].isdigit():
					d=1
				if u==1 and lo==1 and s==1 and d==1:
					f=0
					break
				elif i==len(pwd)-1:
					print('Not satisfied condition. Enter password in correct format')
	print("Successfully registered.")
	file=open('Mail and Pwd.txt','a')
	file.write(mail+':'+pwd+'\n')
	file.close()

def login(roundl):
	f=round=m=0
	while f==0:
		if round>0:
			print('Enter login details again.')
		print('Enter E-mail:',end=" ")
		mail=input()
		print('Enter Password:',end=" ")
		pwd=input()
		f=0
		with open("Mail and Pwd.txt", "r") as file:
			filemail=file.readlines()
		for line in filemail:
			word=line.split(':')
			if mail in word[0] and pwd in str(word[1]):
				print("Successfully logged in")
				f=1
				break
		if f==0:
			print('Incorrect e-mail/password. Go for registration. Enter \'try again\'/\'register\'/\'forget password\':',end=' ')
			fp=input()
			if fp.lower()=='try again':
				round+=1
			elif fp.lower()=='forget password':
				print("Enter your mail id:",end=" ")
				mail=input()
				for line in range(len(filemail)):
					word = filemail[line].split(":")
					if mail in word:
						m=1
						print("Enter \'retrieve password\' or Enter \'new password\':",end=" ")
						opt=input()
						if opt.lower()=='retrieve password':
							retpwd=str(word[1])
							print('Your password is:',retpwd)
							round+=1
							break
						elif opt.lower()=='new password':
							print('Enter your new password:',end=' ')
							newpwd=input()
							filemail[line]=mail+':'+newpwd+'\n'
							with open("Mail and Pwd.txt",'w') as mp:
								change=mp.writelines(filemail)
							print('Your password is changed.')
							round+=1
							break
				if m==0:
					print('Entered mail id not registered. Go for registration.')
					roundl+=1
					register(roundl)
					exit()
			elif fp.lower()=='registration':
				roundl+=1
				register(roundl)
				exit()

print('Register  Login')
entry=input()
roundl=0
if entry.lower()=='register':
	register(roundl)
elif entry.lower()=='login':
	login(roundl)

