# Checking for Palindrome Using Extended Slicing Technique

print("--:Checking  Pallindrome:--")
string = input("Enter a word:").upper()

if (string == string[::-1]):
    print("its a pallindrome")
else:
    print("its not a pallindrome.")