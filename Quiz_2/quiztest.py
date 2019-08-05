from unittest import TestCase
import quiz2 import Fizzbuzzer

class TestFizzbuzzer(TestCase):

    def testnumber(self):
        x= Fizzbuzzer()
        self.assertEqual(x.number,0,"Starting Num = 0")
    
    def testnext(self):
        x = Fizzbuzzer()
        self.assertEqual(x.next(),1,"next = 1")
    
    def testnextagain(self):
        x = Fizzbuzzer()
        x.next(2) = "fizz"
        x.next(3) = 4
        self.assertEqual(x.next)
        

    