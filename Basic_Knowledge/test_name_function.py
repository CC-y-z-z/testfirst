import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):#必须继承unittest.TestCase
    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')#断言
    def test_first_last_middle_name(self):
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
if __name__=='__main__':
    unittest.main()