#Write a function,which will accept two strings and create a new string
#by appending the second string in the middle of the first string.

def append_in_middle(str1,str2):
    mid_str1 = len(str1)//2
    str3 = str1[:mid_str1]+str2+str1[mid_str1:]
    print("After appending Second string in the Middle of First string : {0}".format(str3))
    return


append_in_middle(input("Enter First String : "),input("Enter Second String : "))