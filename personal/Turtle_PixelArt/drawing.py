"""
This program will take the user's input and turn it into colored pixels. To end the program, press enter.
author: Jason Yeung
"""
import turtle

PIXEL_SIZE = 10
ROW = 65
COLUMNS = 65

def initialize():
    turtle.up()
    x = -COLUMNS / 2 * PIXEL_SIZE
    y = ROW / 2 * PIXEL_SIZE
    turtle.goto(x, y)
    turtle.speed(0)

def colors(a_string, count):
    color_map = {
        "0": "black", "1": "white", "2": "red", "3": "yellow", "4": "orange",
        "5": "green", "6": "yellowgreen", "7": "sienna", "8": "tan", "9": "grey",
        "A": "darkgrey", "a": "#fbf9f0", "b": "#0b0c1c", "c": "#f8e6d5", "d": "#f9f9f5",
        "e": "#d5c6b2", "f": "#3c2e44", "g": "#f0e3cd", "h": "#d6a184", "i": "#d0d0c4",
        "j": "#b6bdbd", "k": "#a58c79", "l": "#f9eaea", "m": "#e5dbcf", "n": "#fcdd87",
        "o": "#985245", "p": "#2b406c", "r": "#704235", "s": "#a399a5", "t": "#3c3e81",
        "u": "#7490bb", "v": "#725c6a", "w": "#7d8482", "x": "#e5e8e2", "y": "#797284",
        "z": "#5b79aa", ".": "#c6a357", "?": "#484644", "<": "#cb4e5d", ">": "#e9dee4",
        " ": "skip"
    }
    return color_map.get(a_string[count], False)

def draw_pixel_string(a_string):
    turtle.up()
    turtle.goto(-300, 300)
    turtle.speed(0)
    count = 0
    length = len(a_string)
    while count < length:
        color = colors(a_string, count)
        count += 1
        if color == False:
            return False
        elif color == "skip":
            continue
        else:
            turtle.fillcolor(color)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(PIXEL_SIZE)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(PIXEL_SIZE)
    return True

def Rows():
    a_string = input("Enter a series of strings: ")
    count = 0
    turtle.tracer(0)
    while count < ROW:
        turtle.speed(0)
        x = -COLUMNS / 2 * PIXEL_SIZE
        y = (ROW / 2 * PIXEL_SIZE) - (count * PIXEL_SIZE)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        length = len(a_string)
        countcol = 0
        count += 1
        if a_string == "":
            return False
        while countcol < length:
            color = colors(a_string, countcol)
            countcol += 1
            if color == False:
                return False
            elif color == "skip":
                pass
            else:
                turtle.fillcolor(color)
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(PIXEL_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(PIXEL_SIZE)
        a_string = input("Enter a series of strings: ")

def main():
    initialize()
    Rows()
    turtle.update()

if __name__ == "__main__":
    main()