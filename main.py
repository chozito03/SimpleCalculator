import tools


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Add from file")

        choice = input("Enter choice(1, 2, 3, 4, 5): ")
        print(choice)

        if choice in ("1", "2", "3", "4", "5"):
            if choice == "5":
                nums = tools.load_nums_from_file()
                for pair in nums:
                    x = pair[0]
                    y = pair[1]
                    print(f"{x} + {y} = add {x + y}")
            else:
                x = float(input("Enter the first digit: "))
                y = float(input("Enter the second digit: "))
                if choice == "1":
                    print(f"The result is {add(x, y)}")
                    print("\n")

                elif choice == "2":
                    print(f"The result is {subtract(x, y)}")
                    print("\n")

                elif choice == "3":
                    print(f"The result is {multiply(x, y)}")
                    print("\n")

                elif choice == "4":
                    print(f"The result is {divide(x, y)}")
                    print("\n")

        else:
            print("Invalid input, try your choice again")
            print("\n")


if __name__ == "__main__":
    main()
