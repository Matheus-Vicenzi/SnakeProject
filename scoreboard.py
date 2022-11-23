from turtle import Turtle

ALINHAMENTO = "center"
FONTE = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    """
    Classe que representa os textos marcadores de pontuação
    e o texto de mensagem de fim de jogo
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.shape()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Escreve no topo da tela a pontuação do jogador
        :return:
        """
        self.clear()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score} Higher Score: {self.highscore}", align=ALINHAMENTO, font=FONTE)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        """
        Incrementa 1 ponto ao Score total do jogador, limpa o texto com a pontuação
        antiga e atualiza com a nova pontuação do jogador
        :return:
        """
        self.score += 1
        self.update_scoreboard()
