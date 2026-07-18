# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


s = input("Enter a sentence:")

d={"upperCase":0,"lowerCase":0}

for c in s:
    if c.isupper():
        d["upperCase"]+=1
    elif c.islower():
        d["lowerCase"]+=1
    else:
        pass

print(f"upperCase: {d['upperCase']} \nlowerCase: {d["lowerCase"]}")