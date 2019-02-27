import unittest
import atm_machine
class TestAtm_Machine(unittest.TestCase):
	def test_get_money_success(self):
		Money = atm_machine.get_money(122)
		ExpectedOutput = 378
		self.assertEqual(Money,ExpectedOutput)
	def test_get_money_failed(self):
		Money = atm_machine.get_money(122)
		ExpectedOutput = 400
		self.assertNotEqual(Money,ExpectedOutput)
	def test_transfer_money_success(self):
		Money = atm_machine.transfer_money(122)
		ExpectedOutput = 622
		self.assertEqual(Money,ExpectedOutput)
	def test_transfer_money_failed(self):
		Money = atm_machine.transfer_money(122)
		ExpectedOutput = 800
		self.assertNotEqual(Money,ExpectedOutput)	
if __name__ == '__main__':
	unittest.main()