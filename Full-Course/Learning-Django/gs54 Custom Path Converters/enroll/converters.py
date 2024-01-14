class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return f'{value:4d}'
        # return '%4d' % value


class UsernamePathConverter:
    regex = '^[a-zA-Z0-9_.-]+$'

    def to_python(self, value):
        # convert value to its corresponding python datatype
        return value

    def to_url(self, value):
        # convert the value to str data 
        return value