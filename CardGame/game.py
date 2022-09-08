import random

import pygame

import CardClass as dk
from Interfaces import HumanInterface, WinnerInterface, BotInterface
import time

def showChoiseInfo(text,x, y):

    font =  HumanInterface.pygame.font.Font('freesansbold.ttf', 32)
    player_show = font.render(text, True, (255, 255, 255))
    # player_show=pygame.transform.scale(player_show,(50,80))
    HumanInterface.screen.blit(player_show, (x, y))
    HumanInterface.pygame.display.update()
class Game:
    def __init__(self, mode):
        # self.deck = Deck()
        self.player = Player(0)
        self.bot = Player(1)
        self.handsChosen = []
        self.mode = mode
        # in mom in care apasam pe submit, carte_aleasa = .. , mana = ..
        # verif_minti(cartea_aleasa, mana, carti_bot, carti_player)
        # in cartile de bot + cartilde de player se gasesc carte* mana, atunci return 1, else return 0

    def checkGame(self,handsChosen, playerCards, botCards):
        valueOfCard , nr = handsChosen[-1]

        freqVal = 0
        for x in playerCards:
            if x.valoare == valueOfCard:
                freqVal += 1
        for x in botCards:
            if x.valoare == valueOfCard:
                freqVal +=1

        return freqVal < nr

    def playGame(self):
        turn = 0
        while True:
            print(f"Player: {self.player.numberOfCards}, PC: {self.bot.numberOfCards}")
            # la inceput trebuie sa am tot pachetul
            deck = dk.Deck()
            if self.player.numberOfCards == 6:
                # trebuie creata o functie final
                print("Bot wins!")
                return WinnerInterface.endGame(False)

            elif self.bot.numberOfCards == 6:
                print("Player wins!")
                return WinnerInterface.endGame(True)
            else:
                deck.shuffle()
                # au fost impartite cartile
                self.player.cards = [deck.drawCard() for i in range(self.player.numberOfCards)]
                self.bot.cards = [deck.drawCard() for i in range(self.bot.numberOfCards)]

                while True:
                    if turn == 0:
                        x=self.player.chooseOption()
                        if x:
                            self.handsChosen.append(x)
                            turn=turn+1

                            x_coord = HumanInterface.scrInfo.current_w // 5
                            y_coord= HumanInterface.scrInfo.current_h // 5 * 4
                            print("SUNT AICI")
                            print(self.handsChosen)
                            if self.bot.youLied(self.mode, self.player.cards, self.bot.cards,self.handsChosen, self.checkGame(self.handsChosen, self.player.cards, self.bot.cards)) or x == (14,4):
                                if self.checkGame(self.handsChosen, self.player.cards, self.bot.cards):

                                    showChoiseInfo('The PC says you lied, You must take a card',x_coord, y_coord)
                                    time.sleep(2)
                                    print("Castigator e calculator. Ai spus o mana care nu exista la masa")
                                    self.player.numberOfCards += 1
                                    self.handsChosen = []
                                    break
                                else:
                                    showChoiseInfo('The Pc says you lied, It must take a card', x_coord, y_coord)
                                    time.sleep(2)
                                    print("Tu ai castigat. Chiar sunt cartile in maini!")
                                    self.bot.numberOfCards += 1
                                    self.handsChosen = []
                                    break
                        else:
                            pygame.quit()
                            exit()
                            break

                    else:
                        #option=0 daca noi apasam pe minti 1 daca apasam pe continua
                        handBot, option = self.bot.chooseOption(self.handsChosen, self.mode)
                        self.handsChosen.append(handBot)
                        turn=(turn+1)%2
                        if option == 0:
                            if self.checkGame(self.handsChosen, self.player.cards, self.bot.cards):
                                showChoiseInfo('You are right, The PC must take one card', x_coord, y_coord)
                                time.sleep(2)
                                print("Tu ai castigat! Botul a pus o mana care nu exista la masa!")
                                self.handsChosen = []
                                self.bot.numberOfCards += 1
                                break
                            else:
                                showChoiseInfo('You are wrong, You must take one card', x_coord, y_coord)
                                time.sleep(2)
                                print("Caculatorul a castigat! Chiar sunt cartile in maini")
                                self.player.numberOfCards += 1
                                self.handsChosen = []
                                break



# tip = 0 - player, tip = 1 - bot
# Player: lista de carti, functie de alegere(selecteaza)
# Bot: list de carti, functie de alegere(calculeaza alegerea)

class Player:
    def __init__(self, tip):
        self.type = tip
        self.cards = []
        self.numberOfCards = 1

    def youLied(self, mode, playerHand, botHand, handsChosen, valueOfYouLied):
        '''
        Modul easy : calculatorul alege sa spuna minti mereu
        Modul advanced : se genereaza random un numar de la 1 la 4, daca numarul e 1, atunci calculatorul va sti ce carti sunt in ambele maini, deci daca va spune minti va avea sigur dreptate,
                         altfel, daca numarul e 4, va spune minti, dar nu va sti daca are drepate sigur sau nu, iar daca e 2 sau 3 atunci el alege sa continuie jocul
        '''
        if mode == 'Easy':
            return 1
        else:
            i = random.randint(1,4)

            if i == 1:
                if valueOfYouLied == True:
                    return 1
                else:
                    return 0
            elif i == 4:
                return 1
            else:
                return 0




    def chooseOption(self, handsChosen = [], mode = 'Easy'):
        if self.type == 0:
           return HumanInterface.play_option(self.cards)

        else:
            print("TEST")
            return BotInterface.play(mode, handsChosen, self.cards)