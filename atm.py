# First Main
def get_input_user():
	print("User Details")
	UserName = input("Enter the User Name:")
	MobileNumber = int(input("Enter the Your Mobile Number:"))
	EmailId = input("Enter the Your EmailId:")
	UserBalance = int(input("Enter the amount:"))
	return(UserName,MobileNumber,UserBalance)

def instruct_account_list():	
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")

def get_debit_balance(Debit,Balance):
	Balance = Balance - Debit 
	return Balance

def get_credit_balance(Credit,Balance):
	Balance = Credit + Balance 
	return Balance

def get_balance_details(Name,Mobile,Balance):

	while True:
		ChoiceNumber = int(input("Enter Your Choice:"))

		if ChoiceNumber == 1:
			print("Currently Your Available Balance:",Balance)

		elif ChoiceNumber == 2:			
			Debit = int(input("Enter the Debit Amount:"))
			Balance = get_debit_balance(Debit,Balance)							
			print(Balance)
				
		elif ChoiceNumber == 3:
			Credit = int(input("Enter the Credit Amount:"))
			Balance = get_credit_balance(Credit,Balance)		
			print(Balance)

		elif ChoiceNumber == 4:
			print("Profile Details\nUser Name : {}\nMobile Number : {}\nAvailable Balance : {}".format(Name,Mobile,Balance)) 
				
		elif ChoiceNumber == 5:
			print("Your transcation cancel")
			exit()

		else:
			print("Doesn't exist")

def main():
	Name,Mobile,Balance = get_input_user()
	AccountBalance = instruct_account_list()
	Result = get_balance_details(Name,Mobile,Balance)
	
if __name__ == '__main__':
  main()

#Second Program
"""def get_input_user():
	print("User Details")
	UserName = input("Enter the User Name:")
	MobileNumber = int(input("Enter the Your Mobile Number:"))
	EmailId = input("Enter the Your EmailId:")
	UserBalance = int(input("Enter the amount:"))
	return UserBalance

def instruct_account_list():

	UserBalance = get_input_user()
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")
	return UserBalance

def get_debit_balance(Debit,AccountBalance):
	AccountBalance = AccountBalance - Debit 
	return AccountBalance

def get_credit_balance(Credit,AccountBalance):
	AccountBalance = Credit + AccountBalance 
	return AccountBalance


def get_account_balance(AccountBalance):

	while True:

		ChoiceNumber = int(input("Enter Your Choice:"))

		if ChoiceNumber == 1:
			print("Currently Your Available Balance:",AccountBalance)

		elif ChoiceNumber == 2:			
			Debit = int(input("Enter the Debit Amount:"))
			AccountBalance = get_debit_balance(Debit,AccountBalance)				
			#AccountBalance = AccountBalance - Debit
			print(AccountBalance)
				
		elif ChoiceNumber == 3:
			Credit = int(input("Enter the Credit Amount:"))
			AccountBalance = get_credit_balance(Credit,AccountBalance)
			#AccountBalance = Credit + AccountBalance 
			print(AccountBalance)

		"elif ChoiceNumber == 4:
			#UserBalanceList = "Profile Details\nUserName : {}\nMobileNumber : {}\nEmailId : {}\nAvailableBalance : {}".format(Name,Mobile,Email,UserBalance)
			print("Profile Details\nUserName : {}\nMobileNumber : {}\nEmailId : {}\nAvailableBalance : {}".format(Name,Mobile,Email,UserBalance)) 
				

		elif ChoiceNumber == 5:
			print("Your transcation cancel")
			exit()	
	
def main():

	AccountBalance = instruct_account_list()
	Result = get_account_balance(AccountBalance)
	
if __name__ == '__main__':
  main() """








#Third Main

"""def get_input_user():
	print("User Details")
	UserName = input("Enter the User Name:")
	MobileNumber = int(input("Enter the Your Mobile Number:"))
	EmailId = input("Enter the Your EmailId:")
	Balance = int(input("Enter the amount:"))
	return(UserName,MobileNumber,EmailId,Balance) 

def check_account_balance(Name,Mobile,Email,UserBalance):
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")

	while True:
		UserBalanceList = []
		ChoiceNumber = int(input("Enter Your Choice:"))
		if ChoiceNumber == 1:
			print("Currently Your Available Balance:",UserBalance)
			#UserBalanceList = "Currently Your Available Balance:",UserBalance

		elif ChoiceNumber == 2:			
			Debit = int(input("Enter the Debit Amount:"))	

			if UserBalance >= Debit:
				UserBalance = UserBalance - Debit
				print(UserBalance)
				#UserBalanceList.append(UserBalance)
			else:
				UserBalanceList = "No Available Balance"

				
		elif ChoiceNumber == 3:
			Credit = int(input("Enter the Credit Amount:"))
			UserBalance = Credit + UserBalance 
			#UserBalanceList.append(UserBalance)
			print(UserBalance)			

		elif ChoiceNumber == 4:
			#UserBalanceList = "Profile Details\nUserName : {}\nMobileNumber : {}\nEmailId : {}\nAvailableBalance : {}".format(Name,Mobile,Email,UserBalance)
			print("Profile Details\nUserName : {}\nMobileNumber : {}\nEmailId : {}\nAvailableBalance : {}".format(Name,Mobile,Email,UserBalance))
			
		
		elif ChoiceNumber == 5:
			#UserBalanceList = "Your transcation cancel"
			print("Your transcation cancel")
			exit()	
	return UserBalanceList		

def main():
	UserName,MobileNumber,EmailId,Balance = get_input_user()
	Name = UserName
	Mobile = MobileNumber
	Email = EmailId
	UserBalance = Balance
	AccountBalance = check_account_balance(Name,Mobile,Email,UserBalance)
	#print(AccountBalance)	

if __name__ == '__main__':
  main() """






#Fourth Main

"""def get_input_user():
	print("User Details")
	UserName = input("Enter the User Name:")
	MobileNumber = int(input("Enter the Your Mobile Number:"))
	EmailId = input("Enter the Your EmailId:")
	Balance = int(input("Enter the amount:"))
	return(Balance)
	

def check_account_balance(UserBalance):
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Exit")

	while True:
		ChoiceNumber = int(input("Enter Your Choice:"))
		if ChoiceNumber == 1:
			print("Currently Your Available Balance:",UserBalance)

		elif ChoiceNumber == 2:			
			Debit = int(input("Enter the Debit Amount:"))				
			UserBalance = UserBalance - Debit
			print(UserBalance)
				
		elif ChoiceNumber == 3:
			Credit = int(input("Enter the Credit Amount:"))
			UserBalance = Credit + UserBalance 
			print(UserBalance)			

		elif ChoiceNumber == 4:
			print("Your transcation cancel")
			exit()	

def main():
	Balance = get_input_user()
	UserBalance = Balance
	AccountBalance = check_account_balance(UserBalance)	

if __name__ == '__main__':
  main() """ 