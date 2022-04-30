import unittest

class test_apps(unittest.TestCase):
    def test_vehicle_config(self):
        self.assertEqual(self.vehicle_model, 'Vehicle')


if __name__ == '__main__':
    unittest.main()
