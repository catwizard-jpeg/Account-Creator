import unittest
from Account_Creator import generateUsername
from Account_Creator import calculateYearGroup
from Account_Creator import isPasswordSecure

class TestGenerateUsername(unittest.TestCase):
    def test_username_01(self):
        username = generateUsername("Ronald Smith", "2022")
        self.assertEqual(username, "22SmithR", "username incorrect")
    def test_username_02(self):
        username = generateUsername("John Doe", "2023")
        self.assertEqual(username, "23DoeJ", "username incorrect")
        
class TestCalculateYearGroup(unittest.TestCase):
    def test_year_group_01(self):
        yearGroup = calculateYearGroup("22smithR")
        self.assertEqual(yearGroup,"Year 9", "year group incorrect")

class TestIsPasswordSecure(unittest.TestCase):
    def test_is_password_secure_01(self):
        password = "password"
        username = "22SmithR"
        isSecure = isPasswordSecure(password, username)
        self.assertEqual(isSecure,False, "password security incorrect")

if __name__ == "__main__":
    unittest.main()