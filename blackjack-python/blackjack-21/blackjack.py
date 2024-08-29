# JOGO DE 21 (BLACKJACK) FEITO COM PYTHON

import random

VALORES_CARTAS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"
    
class Baralho:
    def __init__(self):
        self.cartas = []
        self.naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
        self.valores = list(VALORES_CARTAS.keys())

        for naipe in self.naipes:
            for valor in self.valores:
                self.cartas.append(Carta(valor, naipe))

        
    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_carta(self):
        return self.cartas.pop()
    
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def valor_mao(self):
        valor = 0
        ases = 0

        for carta in self.mao:
            valor += VALORES_CARTAS[carta.valor]
            if carta.valor == "A":
                ases =+ 1
        
        while valor > 21 and ases:
            valor -= 10
            ases -= 1
        return valor
    
    def __repr__(self):
        return f"{self.nome} - Mão: {self.mao} - Valor {self.valor_mao()}"
    
class Dealer(Jogador):
    def __init__(self):
        super().__init__("Dealer")

    def jogar(self):
        while self.valor_mao() < 17:
            self.receber_carta(baralho.distribuir_carta())

def jogo():
    global baralho
    baralho = Baralho()
    baralho.embaralhar()

    jogador = Jogador("Jogador")
    dealer = Dealer()

    jogador.receber_carta(baralho.distribuir_carta())
    jogador.receber_carta(baralho.distribuir_carta())
    dealer.receber_carta(baralho.distribuir_carta())
    dealer.receber_carta(baralho.distribuir_carta())

    print(jogador)
    print(dealer)

    while True:
        acao = input("O que você deseja fazer? (1) Hit (2) Stand: ")
        if acao == "1":
            jogador.receber_carta(baralho.distribuir_carta())
            print(jogador)
            if jogador.valor_mao() > 21:
                print("Você estourou! O dealer venceu!")
                return
        elif acao == "2":
            break

    dealer.jogar()
    print(dealer)

    if dealer.valor_mao() > 21:
        print("O dealer estourou! Você venceu!")
    elif dealer.valor_mao() < jogador.valor_mao():
        print("Você venceu!")
    elif dealer.valor_mao() > jogador.valor_mao():
        print("O dealer venceu!")
    else:
        print("Empate!")


jogo()