from unittest.mock import patch
import unittest
import atm_machine

class TestAtm_Machine(unittest.TestCase):
	def test_valid_inputs_username_success(self):
		user_input = [
			"saran"
		]	
		expected_output = "saran"
		with patch('builtins.input', side_effect=user_input):
			name_output = atm_machine.valid_inputs("[a-zA-Z_][a-zA-Z0-9]*","Name","Invalid")
		self.assertEqual(name_output, expected_output)

	def test_valid_inputs_username_failed(self):
		user_input = [
			"saran"
		]	
		expected_output = "saran123"
		with patch('builtins.input', side_effect=user_input):
			name_output = atm_machine.valid_inputs("[a-zA-Z_][a-zA-Z0-9]*","Name","Invalid")
		self.assertNotEqual(name_output, expected_output)

	def test_valid_inputs_mobile_success(self):
		user_input = [
			"9976668922"
		]	
		expected_output = "9976668922"
		with patch('builtins.input', side_effect=user_input):
			mobile_output = atm_machine.valid_inputs("(0/91)?[7-9][0-9]{9}","Mobile Number","Invalid")
		self.assertEqual(mobile_output, expected_output)
	
	def test_valid_inputs_mobile_failed(self):
		user_input = [
			"9976668922"
		]	
		expected_output = "9976689122"
		with patch('builtins.input', side_effect=user_input):
			mobile_output = atm_machine.valid_inputs("(0/91)?[7-9][0-9]{9}","Mobile Number","Invalid")
		self.assertNotEqual(mobile_output, expected_output)

	def test_valid_inputs_email_success(self):
		user_input = [
			"sarandeveloper@gmail.com"
		]	
		expected_output = "sarandeveloper@gmail.com"
		with patch('builtins.input', side_effect=user_input):
			email_output = atm_machine.valid_inputs(r"[^@]+@[^@]+\.[^@]+","Email Id","Invalid")
		self.assertEqual(email_output, expected_output)	

	def test_valid_inputs_email_failed(self):
		user_input = [
			"sarandeveloper@gmail.com"
		]	
		expected_output = "sarandeveloper94@gmail.com"
		with patch('builtins.input', side_effect=user_input):
			email_output = atm_machine.valid_inputs(r"[^@]+@[^@]+\.[^@]+","Email Id","Invalid")
		self.assertNotEqual(email_output, expected_output)	

	def test_valid_inputs_deposit_success(self):
		user_input = [
			"500"
		]	
		expected_output = "500"
		with patch('builtins.input', side_effect=user_input):
			deposit_output = atm_machine.valid_inputs(r"[1234567890]\d{2}$","Deposit Amount","Invalid")
		self.assertEqual(deposit_output, expected_output)		
	
	def test_valid_inputs_deposit_failed(self):
		user_input = [
			"500"
		]	
		expected_output = "599"
		with patch('builtins.input', side_effect=user_input):
			deposit_output = atm_machine.valid_inputs(r"[1234567890]\d{2}$","Deposit Amount","Invalid")
		self.assertNotEqual(deposit_output, expected_output)		

	def test_get_money_success(self):
		atm_machine.Balance = 500
		debit_money = atm_machine.get_money(122)		 
		expected_output = 378
		self.assertEqual(atm_machine.Balance,expected_output)

	def test_get_money_failed(self):
		atm_machine.Balance = 500 
		debit_money = atm_machine.get_money(122)
		expected_output = 400
		self.assertNotEqual(atm_machine.Balance,expected_output)

	def test_transfer_money_success(self):
		atm_machine.Balance = 500
		credit_money = atm_machine.transfer_money(122)		 
		expected_output = 622
		self.assertEqual(atm_machine.Balance,expected_output)

	def test_transfer_money_failed(self):
		atm_machine.Balance = 500 
		credit_money = atm_machine.transfer_money(122)	
		expected_output = 822
		self.assertNotEqual(atm_machine.Balance,expected_output)

if __name__ == '__main__':
	unittest.main()