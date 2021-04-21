import random
account_list = {}
account_details =[]
totalBalance = 0


def init():
		print("welcome to emmy bank")
		print("DO YOU HAVE ACCOUNT WITH US")
		user_option=int(input("1.Yes\n 2.No \n"))

		if user_option==2:
			user_registration()

		elif user_option==1:
			user_login()
		else:
			"print invalid option"



def user_login():
		print("Please enter your Login Details")
		user_account_number=int(input("please enter your account number: "))
		user_password = input("enter your password: ")
		print (account_list)

		for account_number, user_details in account_list.items():
				if account_number != user_account_number:
					continue
				if user_password != account_list[account_number][2]: continue
		print("invalid account or password")
		login()

def account_number_validation(account_number):
    if account_number:

        if len(str(account_number)) ==10:

            try:
                int(account_number)
                return True
            except valueError:
                print("invalid username, account number should be integer")
                return False

    else:
        print("account number is a required field")
        return False



def user_registration():
		print("welcome \n enter your details to register")
		first_name=input("enter your first name")
		last_name=input("enter your last name")
		email=input("enter your email")
		password=input("enter your password")
		name=first_name+" "+last_name
		account_number=generate_account_number()
		account_details.append(name)
		account_details.append(email)
		account_details.append(password)
		print("registration successful"),
		account_list.update({account_number: account_details})
		print(f"your account details is {name}\nyour account email os :{email}\n your password :{password}\n your account number is {account_number}")
		print("keep your account safe")

def bank_operations():
		print("select just one of the option bellow")
		print("press 1 for withdrawal\n 2. for deposit \n 3. for transfer \n 4.to login")
		option_selected=int(input("please select an option"))
		if option_selected != 1:
			pass
		else:
			withdrawal()
		if option_selected != 2:
			pass
		else:
			deposit()
		if option_selected != 3:
			pass
		else:
			transfer()
		if option_selected == 4:
			logout()

def generate_account_number():
	return random.randrange(1111111111,999999999)

def withdrawal():
	global total_balance
	withdraw_amount=int(input("enter the amount you would like to withdraw\n "))
	if withdraw_amount < total_balance:
		if total_balance> 0:
			total_balance=total_balance - withdraw_amount
			print('your new balance is :' + str(total_balance))
			bank_operations()
		else:
			print('insufficient funds')

def deposit(balance=0):
		global total_balance
		deposit_amount = int(input('enter the amount deposited'))
		if deposit_amount > 0:
			total_balance = balance + deposit_amount
			print("your new balance is: " + str(total_balance))
			bank_operations()
		else:
			print("invalid amount")


def transfer(balance=0):
		global total_balance
		transfer_account = int(input('enter your account number'))
		amount =int(input("enter the amount to transfer"))
		if amount > balance:
			total_balance = balance + amount
			print(f"your transfer to {transfer_account} is successful")
			print("your new balance is: " + str(total_balance))
			bank_operations()
		else:
			print("invalid amount")

def logout():
		user_login()

		Begin()

		

class Begin:
    pass


if __name__ = "__main__":
	Begin()

#init()