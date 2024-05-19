##Exception Handling
a=int(input("Enter a number"))

b=7/a
print(b)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except:
    print("This is a wrong input")

l=[1,2,3,4,5,6]
for i in l:
    print(i)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except:
    print("This is a wrong input")
finally :
    print("This will execute always")

l=[1,2,3,4,5,6,7]
for i in l:
    print(i)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except Exception as e:
    print(e)
finally :
    print("This will execute always")

l=[1,2,3,4,5,6,7]
for i in l:
    print(i)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)

except ZeroDivisionError as e:
    print(e)

except ValueError as v :
    print(v)
finally :
    print("This will execute always")

l=[1,2,3,4,5,6,7]
for i in l:
    print(i)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
finally :
    print("This will execute always")


l=[1,2,3,4,5,6,7]
for i in l:
    print(i)

try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except Exception as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
    print("Hii")
finally :
    print("This will execute always")

    
l=[1,2,3,4,5,6,7]
for i in l:
    print(i)

#There can be multiple try and except block in single try block.
try:
    # Outer try block
    x = int(input("Enter a number: "))

    try:
        # Nested try block
        result = 10 / x
        print("Result:", result)

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero in the nested try block.")

except ValueError:
    print("ValueError: Invalid input. Please enter a valid number in the outer try block.")

# # Code after the try-except blocks continues to execute if no exception occurs.
print("Program continues after exceptions.")