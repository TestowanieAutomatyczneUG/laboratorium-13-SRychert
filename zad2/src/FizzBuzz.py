class FizzBuzz:
    def game(self, num):
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        elif type(num) == int:
            return '"' + str(num) + '"'
        else:
            raise Exception("Error in FizzBuzz")
