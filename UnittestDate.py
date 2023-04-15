
import unittest
import datetime

class TestToday(unittest.TestCase):
    def test_today(self):
        today = datetime.date.today()
        self.assertEqual(today, datetime.date(2023, 4, 15))

if __name__ == '__main__':
    unittest.main()
