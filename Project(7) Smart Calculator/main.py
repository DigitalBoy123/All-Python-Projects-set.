from calculator_functions import add_num, sub_num, mul_num, div_num, mod_num, sqrt_num, cube_root_num, factorial_num, square_num, pow_num, cube_num, table_of_num, percentage_marks, simple_interest, complex_interest, average_num, rectangle, check_prime, GCD_hcf, lcm, area_circle, sin, cos, tan, asin, acos, atan

def main():
    while True:
        print("*" * 130)
        print("Welcome to Advance calculator!")
        print("=" * 130)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. HCF / GCD of numbers")
        print("8. LCM of numbers")
        print("9. Factorial")
        print("10. Square Root")
        print("11. Cube Root")
        print("12. Square")         
        print("Imported main.")
        print("13. Cube")
        print("14. Table")
        print("15. percentage of marks")
        print("16. Sin")
        print("17. Cos")
        print("18. Tan")
        print("19. Sin-1")
        print("20. Cos-1")
        print("21. Tan-1")
        print("22. Area of Circle")
        print("23. Check Prime number")
        print("24. Average number")
        print("25. Simple interest")
        print("26. Complex interest")
        print("27. Area of rectangle")
        try:
            choice = int(input("Enter your choice (1-27): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 27.")
            continue

            # Multi-number input for add, sub, mul, div, GCD, LCM
        if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
            try:
                nums_input = input("Enter numbers separated by space: ")
                nums = [float(x) for x in nums_input.split()]
                if len(nums) < 2:
                    print("Please enter at least two numbers.")
                    continue
                if choice == 1:
                    result = add_num(*nums)
                elif choice == 2:
                    result = sub_num(*nums)
                elif choice == 3:
                    result = mul_num(*nums)
                elif choice == 4:
                    result = div_num(*nums)
                elif choice == 5:
                    result = mod_num(*nums)
                elif choice == 6:
                    result = pow_num(*nums)
                elif choice == 7:
                    result = GCD_hcf(*[int(x) for x in nums])
                elif choice == 8:
                    result = lcm(*[int(x) for x in nums])
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            except OverflowError:
                print("Error: The result is too large to be represented.")
                continue
            except ZeroDivisionError:
                print("Error: Division by zero encountered.")
                continue

        elif choice in [10, 11, 12, 13, 14]:
            try:
                a = float(input("Enter your number: "))
                if choice == 10:
                    result = sqrt_num(a)
                elif choice == 11:
                    result = cube_root_num(a)
                elif choice == 12:
                    result = square_num(a)
                elif choice == 13:
                    result = cube_num(a)
                elif choice == 14:
                    result = table_of_num(a)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

        elif choice == 9:
            try:
                a = int(input("Enter a whole number for factorial: "))
                if a < 0:
                    print("Factorial is not defined for negative numbers.")
                    continue
                result = factorial_num(a)
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

        elif choice == 15:
            try:
                marks = float(input("Enter your marks: "))
                total = float(input("Enter your total: "))
                if marks <= 0 or total <= 0:
                    print("marks and total can't be negative and zero!")
                    continue
                result = percentage_marks(marks, total)
            except ValueError:
                print("Invalid choice! Please enter numeric value!")
                continue

        elif choice in [16, 17, 18]:
            try:
                Angle = float(input("Enter your angle: "))
                if choice == 16:
                    result = sin(Angle)
                elif choice == 17:
                    result = cos(Angle)
                elif choice == 18:
                    result = tan(Angle)
            except ValueError:
                print("Invalid choice! Enter a numeric value")
                continue

        elif choice in [19, 20, 21]:
            try:
                Radian = float(input("Enter your radians: "))
                if choice == 19:
                    result = asin(Radian)
                elif choice == 20:
                    result = acos(Radian)
                elif choice == 21:
                    result = atan(Radian)
            except ValueError:
                print("Invalid choice! Enter a numeric value")
                continue

        elif choice == 22:
            try:
                radius = float(input("Enter your radius: "))
                result = area_circle(radius)
            except ValueError:
                print("Invalid choice!Please enter a numeric value!")
                continue

        elif choice == 23:
            try:
                num = int(input("Enter your number: "))
                result = check_prime(num)
            except ValueError:
                print("Invalid input.Please enter a numeric value!.")
                continue

        elif choice == 24:
            try:
                nums_input = input("Enter your numbers with just space, not(,): ")
                nums = [float(item) for item in nums_input.split()]
                result = average_num(nums)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

        elif choice in [25, 26]:
            try:
                nums_input = input("Enter your principle, rate and time: ")
                nums = [float(item) for item in nums_input.split()]
                if len(nums) != 3:
                    print("Please enter exactly three values: principle, rate, and time.")
                    continue
                if choice == 25:
                    result = simple_interest(*nums)
                elif choice == 26:
                    result = complex_interest(*nums)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

        elif choice == 27:
            try:
                inp_len = float(input("Enter your length: "))
                inp_width = float(input("Enter your width: "))
                result = rectangle(inp_len, inp_width)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"The result is/are: \n{result}")

        while True:
            try:
                content = input("Do you want to perform another operation? (yes/no): ").strip().lower()
                if content == 'yes':
                    break
                elif content == 'no':
                    print("<" * 100)
                    print("Thanks for using the calculator! Goodbye!")
                    print(">" * 100)
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            except Exception:
                print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()