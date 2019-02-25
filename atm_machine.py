import re
def get_input_user():
	print("User Details")
	global UserName,MobileNumber,EmailId,UserBalance
	UserName = input("Enter the User Name:")
	return UserName

def get_input_mobile():

	MobileNumber = input("Enter the Your Mobile Number:")
	regex = "(0/91)?[7-9][0-9]{9}"
	return MobileNumber
	#UserBalance = int(input("Enter the amount:")) 

def get_input_email():
	EmailId = input("Enter the Your EmailId:")
	return EmailId

def valid_inputs():	
	while True:
		Name = get_input_user()
		NameMatch = re.search("[a-zA-Z_][a-zA-Z0-9]*", Name)
		if NameMatch:
			break
		else:
			print("Invalid UserName")

	while True:
		Mobile= get_input_mobile()
		MobileMatch = re.search("(0/91)?[7-9][0-9]{9}",Mobile)
		if MobileMatch:
			break	
		else:
			print("Invalid Mobile Number")

	while True:
		Email = get_input_email()
		EmailMatch = re.search(r"[^@]+@[^@]+\.[^@]+", Email)
		if EmailMatch:
			break
		else:
			print("Invalid EmailId Address")


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
	#get_input_user()
	#get_input_mobile()
	Inputs = valid_inputs()
	AccountBalance = instruct_account_list()
	Result = manage_account()
if __name__ == '__main__':
  main()  