# Compound interest calculator

principle = 0
interest_rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be less than 0, please try again.")
    else:
        break

while True:
    interest_rate = float(input("Enter the interest rate (in %): "))
    if interest_rate < 0:
        print("Interest rate must be a positive number, please try again.")
    else:
        break

while True:
    time = int(input('Enter the time (in years): '))
    if time < 0:
        print("Time cant be less than 0, please try again.")
    else:
        break

total = principle * pow((1 + interest_rate / 100), time)

print(f"Your total amount after {time} years will be R{total:.2f}")
