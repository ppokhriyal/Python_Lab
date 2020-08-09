#Write a function,which will accept a string and create a new string in such a way that
#lowercase letters should come first


def arrange_lower_to_uppper_str(str1):
    lower_case = ''
    upper_case = ''

    for i in str1:
        if i.isupper():
            upper_case = upper_case + i
        else:
            lower_case = lower_case + i

    new_arng_str = lower_case+upper_case        

    print("Lower to Upper String : {0}".format(new_arng_str))
    return        




arrange_lower_to_uppper_str(input("Enter a mixed string with Lowercase and Upper case : "))