#Write a function,to reverse the user input string

def reverse_str(str1):
    rev_list = []
    
    for i in range(len(str1),0,-1):
        rev_list.append(str1[i-1])

    print("The Reverse string of {0} is {1}".format(str1,''.join(rev_list)))

reverse_str(input("Enter a String : "))