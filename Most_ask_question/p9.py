# Converting a List into a String

def listToString(lst):
    return ''.join(lst)

# Converting a string into a list

def stringToList(string):
    return list(string)

lst = ["m", "a", "r", "u", "f"]
string = "halder"

print(listToString(lst))
print(stringToList(string))