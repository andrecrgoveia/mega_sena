"""
A simple program that generate 6 aleatory numbers.
"""

from random import randint

# Mega Sena is the name of a lotery in brazil
mega_sena = []

# Creating a loop
for i in range(1, 7):
    mega_sena.append(randint(1, 60))

for numero in mega_sena:
    #print(numero, end=' ')

    print(numero, end = ' ')
# Show the results
#print(f'Your numbers are {mega_sena}, good lucky!')
