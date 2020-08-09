#Write a function,which will take two string inputs and print True if all the character
#in string1 is available in string2


def check_str1_in_str2(str1,str2):
    
    bal_num = 0

    for i in str1:
        if i in str2:
            bal_num = bal_num + 1

    if len(str1) != bal_num:
        print("False")
    else:
        print("True")


check_str1_in_str2(input("Enter the First string : "),input("Enter the Second string : "))