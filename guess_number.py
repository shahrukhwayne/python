import random

print("======= Welcome To Number Guessing System =======")
name = input("==== What's Your Good Name === ")
print("=== Hello", name, "===")
print("Guess the number between 1 and 100")

Secret_Number = random.randint(1,100)
# print(Secret_Number)  # Debug ke liye dekhna ho toh

attempt = 0

while True:
    Guess = int(input("Enter your guess: "))
    attempt += 1

    # Difference nikalo
    diff = abs(Guess - Secret_Number)

    if Guess == Secret_Number:
        print(f"🎉 Correct! You guessed it in {attempt} attempts.")
        break
    elif diff <= 2:
        print("🔥 You are very close! Try again.")
    elif Guess < Secret_Number:
        print("📉 Too Low, Try again.")
    elif Guess > Secret_Number:
        print("📈 Too High, Try again.")
