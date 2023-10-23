#Strings
my_name="Nicolas"
print("My name =", my_name)
my_name="Santiago"
print("My name =", my_name)

#Int
my_age=20
print("My age =", my_age)

#Input
your_age=input("¿Cual es su edad?")
print("My age =", your_age)

#String
name= "Karol"
last_name= "Soler"
Full_name= name+ last_name
print(Full_name)

#Format
name= "Karol"
last_name= "Soler"

template= "my name is {} y mi apellido es {}".format(name, last_name)

print(template)

#number
live=1
live -= 1
print(live)
#El resultado es 0 por que es otra forma de restar las variables 

is_single= True
print(type(is_single)) #Este nos permite ver que clase de valor es

is_single= False
print(type(is_single)) #Este nos permite ver que clase de valor es

is_single= not is_single
print(is_single) #Invierte el ultimo valor de la variable
