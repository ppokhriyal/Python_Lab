#Write a function,which will take two strings input and create a new string in pattern of
#first char of str1 then last char of str2

def mixed_char(str1,str2):
    rev_srt2 = str2[::-1]
    new_str = ''
    if len(rev_srt2) > len(str1):
        for i in range(len(str1)):
            new_str = new_str+str1[i]+rev_srt2[i]
        new_str = new_str+rev_srt2[len(rev_srt2)-1]
    else:
        for i in range(len(str1)):
            new_str = new_str+str1[i]+rev_srt2[i]

    print(new_str)    

mixed_char(input("Enter First string : "),input("Enter Second string : "))