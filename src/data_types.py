from datetime import datetime

def add_ints(a: int, b: int) -> int:
    '''
    Take two integers and return their sum
    
    Args:
    a: first integer
    b: second integer

    Return:
    sum of a and b
    '''
    return a+b

def add_floats(a: float, b: float) -> float:
    '''
    Take two floats and return their sum
    
    Args:
    a: first float
    b: second float

    Return:
    sum of a and b
    '''
    return a+b

def print_string(s: str) -> None:
    '''
    Prints the given string

    Args:
    s: String given by user

    Return:
    None
    '''
    print('This is your string:', str)

def boolean_test(a: bool, b: bool) -> bool:
    '''
    Return True only if both a and b are True

    Args:
    a: first boolean value
    b: second boolean value

    Returns:
    Whether or not both a and b are True
    '''
    return a and b

def string_to_float(s: str) -> float:
    '''
    Converts currency string to float

    Args:
    s: currency string(in format '$1234.56')

    Returns:
    float version of currency
    '''
    return float(s[1:])

def validate_datetime(s: str) -> bool:
    '''
    Validates whether or not date string is in a valid format

    Args:
    s: date string

    Return:
    True if s is in valid date format, False if not
    '''
    valid_formats = ["%Y-%m-%d","%d/%m/%Y", "%m-%d-%Y","%d-%b-%Y", "%b %d, %Y"]

    for form in valid_formats:
        try:
            parsed = datetime.strptime(s, form)
            return True
        except ValueError:
            continue
        return False
    
def calc_percentage(a: float, b: float) -> float:
    '''
    Returns percentage that a is of b

    Args:
    a : first number, the 'part'
    b : second number, the 'whole'

    Returns:
    float, percentage that a is of b
    '''
    return (a/b)*100