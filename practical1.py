# Define a Dictionary mapping digits to their word form
digits = {

    '0': 'zero',

    '1': 'one',

    '2': 'two',

    '3': 'three',

    '4': 'four',

    '5': 'five',

    '6': 'six',

    '7': 'seven',

    '8': 'eight',

    '9': 'nine',

}
number = ""
output = ""

def word_to_num(string : str) - > str:

    """

    Converts a word representing a number to its numerical value.

    Args:

    string (str): A string representing a number in word form.

    Returns:

    str: The numerical value of the input string as a string.

    Raises:

    Type Error; If Input String does not start with a valid word.
    """


    if string.startswith('zero'):

        return number + '0' + word_to_num((string[4:]))

    elif string.startswith('one'):

        return number + '1' + word_to_num((string[3:]))

    elif string.startswith('two'):

        return number + '2' + word_to_num((string[3:]))

    elif string.startswith('three'):

        return number + '3' + word_to_num((string[5:]))

    elif string.startswith('four'):

        return number + '4' + word_to_num((string[4:]))

    elif string.startswith('five'):

        return number + '5' + word_to_num((string[4:]))

    elif string.startswith('six'):

        return number + '6' + word_to_num((string[3:]))

    elif string.startswith('seven'):

        return number + '7' + word_to_num((string[5:]))

    elif string.startswith('eight'):

        return number + '8' + word_to_num((string[5:]))

    elif string.startswith('nine'):

        return number + '9' + word_to_num((string[4:]))

    elif not string:

        return "" 

    else:

        raise TypeError



def num_to_word(num : str) -> str:

    """

    Converts a number to a word representing that number.

    Args:

    num (str): A string representing a number.

    Returns:

    str: A string representing the input number in word form.

    """

    if num == '':

        return ''

    return output + digits[num[0]] + num_to_word(num[1:])



def gcd(number1 : int, number2 : int) -> int:

    """

    Computes the GCD of two numbers using recursion.

    Args:

    number1 (int): The first integer.

    number2 (int): The second integer.

    Returns:

    int: The GCD of the input Integers.

    Raises:

    TypeError

    """

    if number2 == 0:

        return number1

    else:

        return gcd(number2, number1 % number2)

try:

#Prompt the user to enter the Input In a word form
# And then Convert the String Into a numerical value

    inputstr1 = input("Please enter input 1: ").lower()
    
    
    inputnum1 = int(word_to_num(inputstr1))

    inputstr2 = input("Please enter input 2: ").lower()

    inputnum2 = int(word_to_num(inputstr2))

    gcd_num = str(gcd(inputnum1, inputnum2))

    print(f"GCD of {inputstr1} and {inputstr2} is {num_to_word(gcd_num)}")


except TypeError:

    print("Please Enter a valid Word.")

except Exception:

    print("An error occurred. Please try again.")


