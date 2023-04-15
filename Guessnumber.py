import unittest
from io import StringIO
from unittest.mock import patch
import random

def guess_number():
    number = random.randint(1, 100)

    while True:
        guess = int(input("Pick a number between 1 and 100: "))
        if guess < number:
            print("This number is too low, try again.")
        elif guess > number:
            print("This number is higher than required, try again.")
        else:
            print("Well done, you have won an electric car!")
            return

class TestGuessNumber(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_number(self, mock_stdout):
        # test a correct guess
        with patch('builtins.input', side_effect=['50', str(random.randint(1, 49)), str(random.randint(51, 100))]):
            guess_number()
        self.assertIn("Well done, you have won an electric car!", mock_stdout.getvalue())

        # test a low guess
        with patch('builtins.input', side_effect=['50', '25', str(random.randint(1, 24))]):
            guess_number()
        self.assertIn("This number is too low, try again.", mock_stdout.getvalue())

        # test a high guess
        with patch('builtins.input', side_effect=['50', str(random.randint(51, 100)), '75']):
            guess_number()
        self.assertIn("This number is higher than required, try again.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

