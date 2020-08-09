#Write a function,which will accept user input as a string and find out the middle three chars
#of the given string.

def get_middle_three_char(user_str):

    char_len_mid = len(user_str)//2
    print("The Middle 3 characters of string {0} is {1} ".format(user_str,user_str[char_len_mid -1:char_len_mid +2]))
    return


get_middle_three_char(input("Enter the String : "))