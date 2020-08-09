#Write a function,which will accept a string containing following characters :
#lower case, upper case, digits, special symbols
#from the input string count the lower,upper,digits and special symbols

def count_chars(str1):
    char = ''
    digits = ''
    special_symbol = ''

    for i in str1:
        if i.isalpha():
            char = char + i
        elif i.isdigit():
            digits = digits + i
        else:
            special_symbol = special_symbol + i

    print("Chars = {0}\nDigits = {1}\nSymbol = {2}\n".format(len(char),len(digits),len(special_symbol)))
    return


count_chars(input("Enter the String : "))
