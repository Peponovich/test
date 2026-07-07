import math
import time
import random
from decimal import Decimal, getcontext

first_command = input("Hellow! I am Victor, Yiannis' trusted calculator. If you don't know the comands, the comands are=+,-,x, and / for the division: ")

if first_command == "+":
    n1 = float(input("First number:"))
    n2 = float(input("Second number"))
    print(n1 + n2)

elif first_command == "-":
    n1 = float(input("First number:"))
    n2 = float(input("Second number"))
    print(n1 - n2)

elif first_command == "x":
    n1 = float(input("First number:"))
    n2 = float(input("Second number"))
    print(n1 * n2)

elif first_command == "/":
    n1 = float(input("First number:"))
    n2 = float(input("Second number"))

    if n2 == 0:
        print("Error")
    else:
        print(n1 / n2)

elif first_command == "secure":
    password = input("")

    if password != "Haaland9":
        print("Wrong password. Access denied.")

    else:
        getcontext().prec = 110

        def arctan(x):
            x = Decimal(x)
            total = Decimal(0)
            term = Decimal(1) / x
            n = 0

            while abs(term) > Decimal("1e-110"):
                total += term
                n += 1
                term *= -Decimal(2 * n - 1) / Decimal(2 * n + 1) / (x * x)

            return total

        pi = 16 * arctan(5) - 4 * arctan(239)

        command = input("")

        if command == "sr":
            number = float(input(""))

            if number < 0:
                print("Error")
            else:
                print(math.sqrt(number))

        elif command == "pi":
            print(pi)

        elif command == "aoac":
            radius = Decimal(input(""))
            print(pi * radius ** 2)

        elif command == "aot":
            base = float(input(""))
            height = float(input(""))
            print(base * height / 2)

        elif command == "d":
            n1 = float(input(""))
            n2 = float(input(""))

            if n2 == 0:
                print("Error")
            else:
                print(n1 / n2)

        elif command == "m":
            n1 = float(input(""))
            n2 = float(input(""))
            print(n1 * n2)

        elif command == "a":
            n1 = float(input(""))
            n2 = float(input(""))
            print(n1 + n2)

        elif command == "s":
            n1 = float(input(""))
            n2 = float(input(""))
            print(n1 - n2)

        elif command == "v":
            length = float(input(""))
            width = float(input(""))
            height = float(input(""))
            print(length * width * height)

        elif command == "p":
            base = float(input(""))
            power = float(input(""))
            print(base ** power)

        elif command == "rmg":
            print("⚡ REACTION TIME GAME ⚡")

            best_time = None

            while True:
                input("Ready? then press enter")

                time.sleep(random.randint(2, 5))

                print("GO!")
                start = time.time()

                input("")
                reaction = round(time.time() - start, 3)

                if best_time is None or reaction < best_time:
                    best_time = reaction
                    print(reaction, "NEW BEST!")
                else:
                    print(reaction, "| Best:", best_time)

                again = input("")

                if again != "y":
                    break

        elif command == "hsimp":
            test_password = input("")

            score = 0
            length = len(test_password)

            length_points = min(length * 12, 300)
            score += length_points

            uppercase_count = sum(char.isupper() for char in test_password)
            lowercase_count = sum(char.islower() for char in test_password)
            number_count = sum(char.isdigit() for char in test_password)
            symbol_count = sum(not char.isalnum() for char in test_password)

            uppercase_points = min(uppercase_count * 18, 120)
            lowercase_points = min(lowercase_count * 8, 80)
            number_points = min(number_count * 20, 120)
            symbol_points = min(symbol_count * 25, 150)

            score += uppercase_points
            score += lowercase_points
            score += number_points
            score += symbol_points

            different_characters = len(set(test_password))
            variety_points = min(different_characters * 11, 150)
            score += variety_points

            repeated_characters = length - different_characters
            repeat_penalty = repeated_characters * 7
            score -= repeat_penalty

            score = max(1, min(score, 1000))

            print("Score:", score, "/ 1000")

            if score >= 900:
                print("Excellent password!")
            elif score >= 700:
                print("Strong password!")
            elif score >= 500:
                print("Good password.")
            elif score >= 300:
                print("Weak password.")
            else:
                print("Very weak password.")

else:
    print("Error")
