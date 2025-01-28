import math

factorial_10 = str(math.factorial(10))
 
with open ("C:/Users/Usuario/Desktop/Coursera/Python/modulo2/txt.txt", "w") as afile:
    afile.write(factorial_10)

