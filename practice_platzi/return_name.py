
def len_name(name):
    number_letters = len(name)
    return number_letters


if __name__ == "__main__":

    print("Bienvenido, ahora sabras la longitud de caractares de tu nombre")
    
    name = input("Inserte su nombre, por favor: \n")
    result = len_name(name)

    print(f'La cantidad de letras en tu nombre {name} es {result} :D')
