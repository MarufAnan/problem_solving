# Counting Vowels in a Given Word


vowel = ['a','e','i','o','u']

word= input("Enter a word for counting vowels in  it :")
count =0

for char in word:
    if char in vowel:
        count += 1

print(count)