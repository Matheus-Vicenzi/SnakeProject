from turtle import Turtle
from random import randint

COLOR = "red"

class Food(Turtle):
    """
    Classe que representa a fruta
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        """
        Método que altera para a fruta para uma posição aleatória
        :return:
        """
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
