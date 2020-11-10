import re

class Password:
    def ValidPassword(self, pwd):
        """Takes two integers and adds them together to produce the result
        >>> c = Password()
        >>> c.ValidPassword(332132133)
        False
        >>> c.ValidPassword('dsa')
        False
        >>> c.ValidPassword('dsadasdasdasdas')
        False
        >>> c.ValidPassword('@@@32321321@@')
        False
        >>> c.ValidPassword('zaq1@WSX')
        True
        >>> c.ValidPassword('H@s10')
        False
        >>> c.ValidPassword(c)
        Traceback (most recent call last):
           File "C:\\Users\\Marek\\AppData\\Local\\Programs\\Python\\Python39\\lib\\doctest.py", line 1336, in __run
              exec(compile(example.source, filename, "single",
           File "<doctest __main__.Password.ValidPassword[7]>", line 1, in <module>
              c.ValidPassword(c)
           File "F:\\Marek\\ug\\testowanie-automatyczne\\laboratorium-6-marekpolom\\zadanie2.py", line 28, in ValidPassword
              raise TypeError("Invalid type: {}".format(type(pwd)))
        TypeError: Invalid type: <class '__main__.Password'>
        """
        if (type(pwd) == str or type(pwd) == int):
            if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', str(pwd)):
                return True
            else:
                return False
        else:
            raise TypeError("Invalid type: {}".format(type(pwd)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': Password()})