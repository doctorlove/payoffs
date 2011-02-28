import unittest
from script import payoff

class ATM(unittest.TestCase):
	def test_that_long_put_payoff_is_zero_for_atm_option(self):
		E = 10
		S,P = payoff.long_put(E)
		pair = next( ( (s,p) for (s,p) in zip(S,P) if s==E), None)
		self.assertEqual(pair[0], E)
		self.assertEqual(pair[1], 0)

	def test_that_long_call_payoff_is_zero_for_atm_option(self):
		E = 10
		S,P = payoff.long_call(E)
		pair = next( ( (s,p) for (s,p) in zip(S,P) if s==E), None)
		self.assertEqual(pair[0], E)
		self.assertEqual(pair[1], 0)

	def test_that_short_put_payoff_is_zero_for_atm_option(self):
		E = 10
		S,P = payoff.short_put(E)
		pair = next( ( (s,p) for (s,p) in zip(S,P) if s==E), None)
		self.assertEqual(pair[0], E)
		self.assertEqual(pair[1], 0)

	def test_that_short_call_payoff_is_zero_for_atm_option(self):
		E = 10
		S,P = payoff.short_call(E)
		pair = next( ( (s,p) for (s,p) in zip(S,P) if s==E), None)
		self.assertEqual(pair[0], E)
		self.assertEqual(pair[1], 0)



if __name__ == "__main__":
	unittest.main()
