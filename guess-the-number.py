import random
def guessing():
    answer = random.randint(0, 100)
    while True:
        user = int(input("Your guess: "))
        if user == answer:
            print(f'Good! The answer is {user}')
            break
        if user < answer:
            print(f'Try a higher number than {user}')
        else:
            print(f'Try a lower number than {user}')

guessing()

# Your guess: 5
# Try a higher number than 5
# Your guess: 90
# Try a lower number than 90
# Your guess: 65 
# Try a higher number than 65
# Your guess: 78
# Try a lower number than 78
# Your guess: 70
# Good! The answer is 70