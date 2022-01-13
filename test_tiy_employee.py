import unittest
from tiy_employee import Employee

class testemployee (unittest.TestCase):
    def setUp (self):
        """creates employee for test"""
        self.travailleur=Employee('souad','mimouni', 5000)

    def test_defaultraise (self):
        """test getting a default raise of 5 000"""
        self.travailleur.give_raise ()
        self.assertEqual(self.travailleur.salary, 10000)

    def test_specificraise (self):
        "test getting a specific raise of 1000"
        self.travailleur.give_raise (1000)
        self.assertEqual(self.travailleur.salary, 6000)

if __name__ == '__main__':
    unittest.main()