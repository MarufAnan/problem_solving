# Counting the Number of Occurances of a Character in a String

word= input("Enter a word for counting the specific letter in it :")

char = input("Enter the letter which you count in word:")

count =0

for letter in word:
    if letter == char:
        count+=1

print(count)