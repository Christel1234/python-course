import unittest
from cryptography import rot13


class testCryptography(unittest.TestCase):
    def testLetters(self):
        self.assertEqual(rot13("abc"), "nop")

    def testSpace(self):
        self.assertEqual(rot13("n arj fbpvny zrqvn cyngsbez"),
                         "a new social media platform")
        self.assertEqual(rot13(" "),
                         " ")

    def testUppercase(self):
        self.assertEqual(rot13("HELLO"),
                         "URYYB")

    def testLowercase(self):
        self.assertEqual(rot13("world"),
                         "jbeyq")

    def testUpperAndLower(self):
        self.assertEqual(rot13("HELLO world"),
                         "URYYB jbeyq")

    def testNumber(self):
        self.assertEqual(rot13("123"),
                         "123")

    def testNumberAndLetters(self):
        self.assertEqual(rot13("123 hello WORLD"),
                         "123 uryyb JBEYQ")


if __name__ == "__main__":
    unittest.main()
