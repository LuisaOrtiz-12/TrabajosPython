archivo = open('palabras500.csv', encoding = "utf-8")
palabra = archivo.readlines()
archivo.close

def rima(tex):
    for i in palabra:
       if i[-3:] == tex:
        print(i) 
       else:
        print('No se encuentran palabras en el archivo')
            

rima('an')

