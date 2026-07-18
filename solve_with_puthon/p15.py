# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


a = input("Enter a number:")

n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)

# another solution :
# n = input("Enter a number: ")

# n1 = int(n)
# n2 = int(n * 2)
# n3 = int(n * 3)
# n4 = int(n * 4)

# print(n1 + n2 + n3 + n4)

# by f string:
# n = input("Enter a number: ")

# n1 = int(f"{n}")
# n2 = int(f"{n}{n}")
# n3 = int(f"{n}{n}{n}")
# n4 = int(f"{n}{n}{n}{n}")

# print(n1 + n2 + n3 + n4)