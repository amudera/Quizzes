
class Fizzbuzzer:

    def __init__(self,start=0):
        self.number = start

    def next(self):
        self.number += 1
        if self.number % 3 == 0 and self.number % 5 == 0:
            print("fizzbuzz")
        elif self.number % 3 == 0:
            print("fizz")
        elif self.number % 5 == 0:
            print("buzz")
        else:
            print(self.number)
    



