from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Cria um segmento da cobra para cada elemento da lista 'STARTING_POSITION' (3)
        :return:
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adiciona um segmento à cobra, altera o formato para um quadrado, muda a cor
        para branca, retira o traço padrão da biblioteca Turtle, insere o novo seguimento na posição
        recebida como parâmetro e finalmente adiciona a lista de seguimentos da cobra
        :param position:
        :return:
        """
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """
        Adiciona um novo seguimento por meio do metodo add_segment e insere na ultima posição da lista de
        seguimentos, fazendo com que o ultimo seguimento seja inserido na extremidade da cobra
        :return:
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Faz cada seguimento da cobra seguir a movimentação da cabeça
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Altera o sentido da movimentação da cobra para cima, caso a cobra esteja virada para baixo, nada acontece
        :return:
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
         Altera o sentido da movimentação da cobra para baixo, caso a cobra esteja virada para cima, nada acontece
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Altera o sentido da movimentação da cobra para esquerda, caso a cobra esteja virada para direita, nada acontece
        :return:
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Altera o sentido da movimentação da cobra para direita, caso a cobra esteja virada para esquerda, nada acontece
        :return:
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


