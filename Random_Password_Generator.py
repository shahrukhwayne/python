import random
import string

print("==== Welcome To Random Password Generator ====")
Length = int(input("Enter Length of Your Password : "))
print(range(Length))
Include_Digits = input("Include Digits ? (y/n)")
Include_Character = input("Include Characters ? (y/n)")
characters = string.ascii_letters
if Include_Digits == 'y':
    characters += string.digits
if Include_Character == 'y':
    characters += string.punctuation

if len(characters) == 0:
    print("❌ You did not select any character set!")
else:
    password = ""
    for i in range(Length):   # jitna length user chahe utne chars lo
        password = password + random.choice(characters)

    print("✅ Your Random Password is:", password)

