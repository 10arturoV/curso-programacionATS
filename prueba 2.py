par1 = int(input("ingrese primer parcial "))
par2 = int(input("ingrese segundo parcial "))
par3 = int(input("ingrese tercer parcial "))

parTot = (par1+par2+par3)/3*.55
print("el parcial total es "+str(parTot))

exam = int(input("ingresa la calif de tu examen "))
exa = exam *.15
print("calificacion examen es "+str(exa))

pro = int(input("calificacion de tu proyecto "))
proy = pro *.30
print("tu proyecto saco "+str(proy))

final = parTot+exa+proy
print("tu calificacion final es "+str(final))
