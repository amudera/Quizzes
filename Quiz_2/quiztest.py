from unittest import TestCase
from quiz2 import Fizzbuzzer

class TestFizzbuzzer(TestCase):

    def testnumber(self):
        x = Fizzbuzzer()
        self.assertEqual(x.number,0,"Starting Num = 0")
    
    def testnext(self):
        x = Fizzbuzzer()
        x.next()
        self.assertEqual(x.number,1,"next = 1")
    
    def testnextagain(self):
        x = Fizzbuzzer()
        x.next()
        self.assertEqual(x.number,2,"number changed")
        self.assertEqual(x.number,3,"number changed")
        

    