#Write a function,which will accept two strings and create a new string made of the first
#middle and last char of each input string

def build_new_str(str1,str2):
    first_char_str1 = str1[0]
    first_char_str2 = str2[0]
    mid_char_str1 = str1[len(str1)//2]
    mid_char_str2 = str2[len(str2)//2]
    last_char_str1 = str1[len(str1) -1]
    last_char_str2 = str2[len(str2) -1]
    new_str = first_char_str1+first_char_str2+mid_char_str1+mid_char_str2+last_char_str1+last_char_str2
    print("New String is : {0}".format(new_str))

build_new_str(input("Enter First String : "),input("Enter Second String : "))