#Given an input string, count occurrences of all characters within a string

str1 = "Apple"
result = {}

for i in str1:
    result[i] = str1.count(i)

print(result)    