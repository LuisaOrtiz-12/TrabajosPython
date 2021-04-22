año = 1999

def bisiesto(año):
 if año%4 == 0 and (not(año%100 == 0) or año%400 == 0):
   print(año, 'El año es bisiesto')
 else:
   print(año, 'El año NO es bisiesto')

bisiesto(año)