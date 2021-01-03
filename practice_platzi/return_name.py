import datetime
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ASCIIMATICS", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

def len_name(name):
    number_letters = len(name)
    return number_letters

def age(year_age):
    actual_year = datetime.datetime.now().year
    born_year = actual_year - year_age
    return born_year

if __name__ == "__main__":

    print("Bienvenido, ahora sabras la longitud de caractares de tu nombre")

    Screen.wrapper(demo)
    
    name = input("Inserte su nombre, por favor: \n")
    result = len_name(name)

    year_age = int(input("Inserte su edad, por favor: \n"))
    result_year = age(year_age)

    print(f'La cantidad de letras en tu nombre {name} es {result} :D \n Tu año de nacimiento es: {result_year}')

