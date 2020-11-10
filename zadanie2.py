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
        """

        if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', str(pwd)):
            return True
        else:
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': Password()})