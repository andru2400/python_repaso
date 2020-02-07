import turtle

def main():
    window = turtle.Screen()
    Andres = turtle.Turtle()
    make_square(Andres)
    turtle.mainloop()

def make_square(Andres):
    legth = int(input('Tamaño de cuadrado'))    

    for i in range(4):
        make_line_and_turn(Andres, legth)

def make_line_and_turn(Andres, legth):
    Andres. forward(legth)
    Andres. left(90)    

if __name__ == '__main__':
    main()
