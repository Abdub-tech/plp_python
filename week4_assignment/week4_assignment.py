# Week 4 Assignment - File Handling & Error Handling
# Author: Abdub Golicha

# --- File Read & Write Challenge ---
try:
    # Create or open a file and write to it
    with open("hello.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is my Week 4 assignment.\n")

    # Read back the contents
    with open("hello.txt", "r") as file:
        content = file.read()
        print("📂 File Contents:")
        print(content)

except Exception as e:
    print("⚠️ An error occurred while handling the file:", e)


# --- Error Handling Lab ---
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"✅ The result of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    except TypeError:
        print("❌ Both inputs must be numbers.")
    except Exception as e:
        print("⚠️ An unexpected error occurred:", e)

# Test cases
divide_numbers(10, 2)    # Valid
divide_numbers(5, 0)     # ZeroDivisionError
divide_numbers("x", 2)   # TypeError
