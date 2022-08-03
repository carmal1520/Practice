import unittest

class Employee():
    
    def __init__(self, first_name, last_name, salary=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def give_raise(self, custom_raise=''):
        if custom_raise:
            self.salary = int(custom_raise) + int(self.salary)
        else:
          self.salary += 5000



class TestCaseEmployee(unittest.TestCase):

    def setUp(self):
        self.carlos = Employee("Carlos", "Maldonado", 65000)

    def test_give_default_raise(self):
        self.carlos.give_raise()
        self.assertEqual(self.carlos.salary, 70000)
    
    def test_give_custom_raise(self):
        self.carlos.give_raise(10000)
        self.assertEqual(self.carlos.salary, 75000)

if __name__ == '__main__':
    unittest.main()

# carlos = Employee("Carlos", "Maldoando")
# print(carlos.salary)
# carlos.give_raise()
# print(carlos.salary)