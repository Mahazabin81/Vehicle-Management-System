import unittest
import views
from unittest.mock import patch



class TestViews(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_home_view(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        print("this method works fine")

    def tearDown(self):
        print('tearDown\n')
        print("this method works fine")

    def test_customer_email(self):
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        print("this method works fine")

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        print("this method works fine")

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        print("this method works fine")

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        print("this method works fine")
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')
            print("this method works fine")
    def test_admin(self):
        self.assertEqual(True, True)
     
        print("this method works fine")

    def test_customerClick(self):
        self.assertEqual(True, True)
        print("this method works fine")

    def test_customer_view(self):
        def test_vehicle_config(self):
        self.assertEqual(self.customer_viewe, 'Vehicle')

    def test_admin_view(self):
         def test_vehicle_config(self):
        self.assertEqual(self.admin_view, 'Premio')
    def test_customer(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'iftid'
        self.emp_2.first = 'ashrafee'

        self.assertEqual(self.cst_1.fullname, 'Iftid')
        self.assertEqual(self.cst_2.fullname, 'Ashrafee')
        print("this method works fine")

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        print("this method works fine")

        self.assertEqual(self.cst_1.pay, 52500)
        self.assertEqual(self.cst_2.pay, 63000)
        print("this method works fine")
   def tearDown(self):
        print('tearDown\n')
        print("this method works fine")

   def test_customer_email(self):
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        print("this method works fine")

   def test_mechanic_name(self):
        
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        print("this method works fine")

    def test_apply_for_job(self):
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        print("this method works fine")
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')
            print("this method works fine")
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        print("this method works fine")

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        print("this method works fine")

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        print("this method works fine")

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)




   def tearDownClass(cls):
    print('teardownClass')



   def monthly_schedule(self, month):
       response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
          return response.text
        else:
          return 'Bad Response!'
if __name__ == '__main__':
        unittest.main()
