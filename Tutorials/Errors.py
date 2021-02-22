# Catching multiple errors
n = input("Please enter an integer: ")
try:
 x=2/0
 n = int(n)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Requires a valid integer!")
except Exception:
    print("There is something wrong")
