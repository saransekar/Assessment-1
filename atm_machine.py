import re
def get_input_user():
	print("User Details")
	global UserName,MobileNumber,EmailId,UserBalance
	UserName = input("Enter the User Name:")
	return UserName

def get_input_mobile():
	#global MobileNumber,EmailId,UserBalance
	MobileNumber = input("Enter the Your Mobile Number:")
	regex = "(0/91)?[7-9][0-9]{9}"
	return MobileNumber
	#UserBalance = int(input("Enter the amount:")) 


def valid_inputs(demo1):	
	while True:
		Input = get_input_user()
		NameMatch = re.search("[a-zA-Z_][a-zA-Z0-9]*", UserName)
		if NameMatch:
			break
		else:
			print("Invalid Mobile Number")

	"""while True:
		Input1= get_input_mobile()
		EmailMatch = re.search("(0/91)?[7-9][0-9]{9}",Input1)
		if EmailMatch:
			break	
		else:
			print("Invalid Mobile Number")"""


def instruct_account_list():	
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")

def get_money(Debit):
	global UserBalance
	UserBalance = UserBalance - Debit  
	
def transfer_money(Credit):
	global UserBalance
	UserBalance = Credit + UserBalance 
	
def manage_account():
	while True:
		try:
			Option = int(input("Enter Option:"))
			if Option == 1:
				print("Currently Your Available Balance:",UserBalance)
			elif Option == 2:
				Debit = int(input("Enter the Debit Amount:"))
				if UserBalance >= Debit:						
					get_money(Debit)							
					print(UserBalance)
				else:
					print("No Available Balance")								
			elif Option == 3:
				Credit = int(input("Enter the Credit Amount:"))
				transfer_money(Credit)		
				print(UserBalance)
			elif Option == 4:
				print("Profile Details\nUser Name : {}\nMobile Number : {}\nEmail Id : {}\nAvailable Balance : {}".format(UserName,MobileNumber,EmailId,UserBalance)) 				
			elif Option == 5:
				print("Your transcation cancel")
				exit()
			else:
				print("Doesn't exist")
		except (SyntaxError, ValueError):		
			print("You didn't enter a number")	

def main():
	demo1 = get_input_user(valid_inputs())
	#get_input_mobile()
	demo = valid_inputs(demo1)
	AccountBalance = instruct_account_list()
	Result = manage_account()
if __name__ == '__main__':
  main()  







"""import re
def get_input_user():
	print("User Details")
	global UserName,MobileNumber,EmailId,UserBalance
	UserName = input("Enter the User Name:")
	

	MobileNumber = input("Enter the Your Mobile Number:")
	regex = "(0/91)?[7-9][0-9]{9}"
	return MobileNumber,regex

	while True:
		MobileNumber = input("Enter the Your Mobile Number:")
		if re.search("(0/91)?[7-9][0-9]{9}",MobileNumber):
			break
		else:
			print("Invalid Mobile Number")

	while True:			
		EmailId = input("Enter the Your EmailId:")
		if re.search(r"[^@]+@[^@]+\.[^@]+", EmailId):
			break
		else:
			print("Invalid Email Address")	

	UserBalance = int(input("Enter the amount:")) 


def valid_inputs():
	MobileNumber,regex = get_input_user()

	while True:

		if re.search(regex,MobileNumber):
			break
		else:
			print("Invalid Mobile Number")

def instruct_account_list():	
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")

def get_money(Debit):
	global UserBalance
	UserBalance = UserBalance - Debit  
	
def transfer_money(Credit):
	global UserBalance
	UserBalance = Credit + UserBalance 
	
def manage_account():
	while True:
		try:
			Option = int(input("Enter Option:"))
			if Option == 1:
				print("Currently Your Available Balance:",UserBalance)
			elif Option == 2:
				Debit = int(input("Enter the Debit Amount:"))
				if UserBalance >= Debit:						
					get_money(Debit)							
					print(UserBalance)
				else:
					print("No Available Balance")								
			elif Option == 3:
				Credit = int(input("Enter the Credit Amount:"))
				transfer_money(Credit)		
				print(UserBalance)
			elif Option == 4:
				print("Profile Details\nUser Name : {}\nMobile Number : {}\nEmail Id : {}\nAvailable Balance : {}".format(UserName,MobileNumber,EmailId,UserBalance)) 				
			elif Option == 5:
				print("Your transcation cancel")
				exit()
			else:
				print("Doesn't exist")

		except (SyntaxError, ValueError):		
			print("You didn't enter a number")	

def main():
	regex = "(0/91)?[7-9][0-9]{9}"
	get_input_user()
	demo = valid_inputs()
	AccountBalance = instruct_account_list()
	Result = manage_account()
if __name__ == '__main__':
  main()  """