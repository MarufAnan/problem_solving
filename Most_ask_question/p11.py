# Comparing Two Strings for Anagrams

print("--:Checking Anagrams:--")
str1 = list(input("Enter the 1st word: ").upper())
str2 = list(input("Enter the 2nd word: ").upper())

str1.sort(), str2.sort()

if (str1 == str2):
    print("True , its an anagram")
else:
    print("False, its not an angram")