import datetime

fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
fecha_nacimiento=datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
edad=datetime.datetime.now().year - fecha_nacimiento.year

print("Tu edad es:", edad)
