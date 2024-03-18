import unittest
from portfolio_balances import Portfolio

"""
the command to do unittesting, taken from the GeekTrust default readme
    
    python -m unittest discover
    coverage run -m unittest discover
    python -m coverage run -m unittest
"""


class TestingPortfolioClass(unittest.TestCase): #not sure why "TestCase" is being summoned but it's being advised in ChatGPT and is also in friend's similar coding challenge
    def test_target_allocation_upon_portfolio_construction(self):
        #ARRANGE
        portfolio_instance = Portfolio() #not sure why I need to instantiate this
        hypothetical_allocation_inputs = [17000,2000,1000]
        expected_output_allocation = {'equities': 0.85, 'debt': 0.1, 'gold': 0.05}

        #ACT
        portfolio_instance._create_new_asset_classes(hypothetical_allocation_inputs) ##proces the hypotheticals

        # ASSERT, https://docs.python.org/3/library/unittest.html
        actual_results = portfolio_instance._get_target_allocations() #this only worked bc I had a GET function made, could test it out later by touching the field directly?
        self.assertEqual(expected_output_allocation, actual_results)

"""
try without this code and see what happens

if __name__ == '__main__':
    unittest.main()

"""