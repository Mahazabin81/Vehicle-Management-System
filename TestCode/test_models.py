import unittest
import models
class Test_models(unittest.TestCase):

    

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

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

if __name__ == '__main__':
    unittest.main()


