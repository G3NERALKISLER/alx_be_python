Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> number1 = 10
>>> number2 = 5
>>> 
>>> print("sum:", number1 + number2)
sum: 15
>>> print("Difference:", number1 - number2)
... print("Product:", number1 * number2)
SyntaxError: multiple statements found while compiling a single statement
>>> 
====================== RESTART: Shell ======================
>>> number1= 10
>>> number2 = 5
>>> 
>>> print("Sum:", number1 + number2)
Sum: 15
>>> print("Difference:", number1 - number2)
Difference: 5
>>> print("Product:", number1 * number2)
Product: 50
