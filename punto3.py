intentos = 0

def login (user,password):

    usuario = user
    passwo = password
    if(usuario.endswith("admin") and password.endswith("admin123")):
        return True    
    else:
        return False
    


while True:
    user = input("Ingrese el usuario:  ")
    password = input("Ingrese la contaseña:  ")

    resultado = login(user,password)
    print(f"numeros de intentos: {intentos}")
    if(resultado):
        print("ingreso correctamente")
        break
    else:
        intentos = intentos + 1
        print(f"numeros de intentos: {intentos}")