
class Fizzbuzzer:

    def __init__(self,start=0):
        self.start = start
        
    number = start

    def next():
        number += 1
        while number >=0:
            if number % 3 == 0 and number % 5 == 0:
                print("fizzbuzz")
            elif number % 3 == 0:
                print("fizz")
            elif number % 5 == 0:
                print("buzz")
            else:
                print(number)
            break


buzzer = Fizzbuzzer(11)
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
