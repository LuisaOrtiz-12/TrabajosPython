archivo = open('palabras500.csv', encoding = "utf-8")
palabra = archivo.readlines()
archivo.close

dat = []

def rima(tex):
  for i in palabra:
    dat = i[-3:]
    if dat == tex:
      print(dat) 
    else:
      print('No se encuentran palabras en el archivo')
            
rima('an')

