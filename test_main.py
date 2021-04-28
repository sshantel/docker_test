import unittest 
import main_file

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main_file.isValid("()"), True)
        self.assertEqual(main_file.isValid("()[]{}"), True)
    def test_two(self):
        self.assertEqual(main_file.isValid("(]"), False)
        self.assertEqual(main_file.isValid("([)]"), False)
        self.assertEqual(main_file.isValid("{[]}"), True)

if __name__ == '__main__':
    unittest.main()