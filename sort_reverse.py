#-------------------------------------------------------------------------------
# Name:        Sorting, reversing, enumerate and appending list
# Purpose:
#
# Author:      Jadranko
#
# Created:     18.11.2021
# Copyright:   (c) Jadranko 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

lista = [5, 9, 7, 3, 1]

lista.sort()
print("1.", lista)

lista.reverse()
print("12.", lista)

lista.append(55)
print("3.", lista)

lista[3] = 99

sorted(lista)
print("4.", lista)

print("5.", lista[-1], ", ",lista[-2])

lista.sort(reverse=True)
print("6.", lista)

print("7.", sorted(lista))

print("8.", lista[:-1])

#import sys
#print("Test", file=sys.stderr)

# enumerate with start index with 1
for key_index, value in enumerate(lista,1):
    print(key_index, value)
