#Given a string, return the sum and average of the digits that appear in the string, 
#ignoring all other characters

str1 = "English = 78 Science = 83 Math = 68 History = 65"
num = 0
av_count = 0

for i in str1.split():
    if i.isnumeric():
        num = num + int(i)
        av_count = av_count + 1
        

print("The Sum of Digits is : {0} and Average is {1}".format(num,num/av_count))

