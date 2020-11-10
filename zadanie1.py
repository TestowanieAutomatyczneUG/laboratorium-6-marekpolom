class FizzBuzz:
    def gameWithDocString(self, num):
        """Takes two integers and adds them together to produce the result
        >>> c = FizzBuzz()
        >>> c.gameWithDocString(3)
        'Fizz'
        >>> c.gameWithDocString(6)
        'Fizz'
        >>> c.gameWithDocString(5)
        'Buzz'
        >>> c.gameWithDocString(10)
        'Buzz'
        >>> c.gameWithDocString(15)
        'FizzBuzz'
        >>> c.gameWithDocString(45)
        'FizzBuzz'
        >>> c.gameWithDocString(1)
        Traceback (most recent call last):
           File "C:\\Users\\Marek\\AppData\\Local\\Programs\\Python\\Python39\\lib\\doctest.py", line 1336, in __run
              exec(compile(example.source, filename, "single",
           File "<doctest __main__.FizzBuzz.gameWithDocString[7]>", line 1, in <module>
              c.gameWithDocString(1)
           File "F:\\Marek\\ug\\testowanie-automatyczne\\laboratorium-6-marekpolom\\zadanie1.py", line 37, in gameWithDocString
              raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> c.gameWithDocString('dsadsad')
        Traceback (most recent call last):
           File "C:\\Users\\Marek\\AppData\\Local\\Programs\\Python\\Python39\\lib\\doctest.py", line 1336, in __run
              exec(compile(example.source, filename, "single",
           File "<doctest __main__.FizzBuzz.gameWithDocString[7]>", line 1, in <module>
              c.gameWithDocString('dsadsad')
           File "F:\\Marek\\ug\\testowanie-automatyczne\\laboratorium-6-marekpolom\\zadanie1.py", line 30, in gameWithDocString
              raise TypeError("Invalid type: {}".format(type(num)))
        TypeError: Invalid type: <class 'str'>
        """
        if (type(num) == int):
            if ((num % 15) == 0):
                return "FizzBuzz"
            elif ((num % 3) == 0):
                return "Fizz"
            elif ((num % 5) == 0):
                return "Buzz"
            else:
                raise Exception("Error in FizzBuzz")
        else:
            raise TypeError("Invalid type: {}".format(type(num)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': FizzBuzz()})