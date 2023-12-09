from tkinter import Tk, Canvas
from game import game

if __name__ == "__main__":
    root = Tk()
    root.title("Platformer")

    canvas = Canvas(root, width = 400, height = 250, bg="cyan2")
    canvas.pack()

    newGame = game(root, canvas)
    root.mainloop()