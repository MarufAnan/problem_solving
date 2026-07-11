import re

text = "i am a 20 years old man. #maruf@gmail"

# Counting Digits, Letters, Spaces, and Special Characters

digitCount = re.findall(r"\d", text)
letterCount = re.findall(r"[a-zA-Z]", text)
spaceCount = re.findall(r"\s", text)
spcharCount = re.findall(r"[^a-zA-Z0-9\s]", text)

print("Digits:", len(digitCount))
print("Letters:", len(letterCount))
print("Spaces:", len(spaceCount))
print("Special Characters:", len(spcharCount))