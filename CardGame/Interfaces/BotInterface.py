import random
import pygame

from CardGame import SoundsUtil
from CardGame.button import button

def card_blit(card,x,y):
    screen.blit(card,(x,y))
def pc_cards(x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    player_show = font.render("PC Cards To Submit: ", True, (255, 255, 255))
    # player_show=pygame.transform.scale(player_show,(50,80))
    screen.blit(player_show, (x, y))
def play(mode, handChosen, self_cards):
    global screen, scrInfo
    scrHeight = scrInfo.current_h
    scrWidth = scrInfo.current_w
    buttonsX = scrWidth // 4
    buttonsY = scrHeight // 4
    incrementButtonY = scrHeight // 6
    incrementButtonX = scrWidth // 6
    clock = pygame.time.Clock()
    bot_solution = ()
    hasChosen = False
    pygame.init()
    pygame.display.update()
    done = False
    option = 0
    while not done:

        screen.blit(back1, (0, 0))
        pygame.event.get()
        findSol = False
        if hasChosen == False:
            if mode == 'Easy':

                if handChosen :
                    valueOfCard, nr = handChosen[-1]
                else:
                    valueOfCard = 1
                    nr = 1
                # retinem un vector de frecventa pentru carti
                freqOfCards = dict()
                for card in self_cards:
                    if card.valoare in freqOfCards:
                        freqOfCards[card.valoare] += 1
                    else:
                        freqOfCards[card.valoare] = 1

                # s-ar putea sa nu mearga
                sortedKeys = sorted(freqOfCards.keys())

                # daca avem o mana mai mare in pachet, o alegem
                for key in sortedKeys:
                    if key == valueOfCard:
                        if freqOfCards[key] > nr and findSol == False:
                            findSol = True
                            bot_solution = (key, nr + 1)

                    elif key > valueOfCard and findSol == False:
                        if freqOfCards[key] >= nr:
                            findSol = True
                            bot_solution = (key, nr)


                # daca nu avem o mana mai mare, o alegem pe prima
                # mai mare decat cea zisa de jucator
                if valueOfCard < 14 and findSol == False:
                    findSol = True
                    bot_solution = (valueOfCard + 1, nr)
                elif findSol == False:
                    findSol = True
                    bot_solution = (2, nr + 1)


            else:

                if handChosen:
                    valueOfCard, nr = handChosen[-1]
                else:
                    valueOfCard = 1
                    nr = 1
                rdm = random.randint(0, 1)  # generam random un nr
                if rdm % 2 == 0:
                    freqOfCards = dict()
                    for card in self_cards:
                        if card.valoare in freqOfCards:
                            freqOfCards[card.valoare] += 1
                        else:
                            freqOfCards[card.valoare] = 1

                    # s-ar putea sa nu mearga
                    sortedKeys = sorted(freqOfCards.keys())

                    for key in sortedKeys:
                        if key == valueOfCard:
                            if freqOfCards[key] > nr and findSol == False:
                                findSol = True
                                bot_solution = (key, nr + 1)

                        elif key > valueOfCard and findSol == False:
                            if freqOfCards[key] >= nr:
                                findSol = True
                                bot_solution = (key, nr)

                    if valueOfCard < 14 and findSol == False:
                        findSol = True
                        bot_solution = (valueOfCard + 1, nr)
                    elif findSol == False:
                        findSol = True
                        bot_solution = (2, nr + 1)

                else:
                    if valueOfCard < 14 and findSol == False:
                        findSol = True
                        bot_solution = (valueOfCard + 1, nr)
                    elif findSol == False:
                        findSol = True
                        bot_solution = (2, nr + 1)
            hasChosen = True
            print(f"Botul a ales mana{bot_solution}\n")

        card_submit_bot=bot_solution[0]
        card_repeat=bot_solution[1]
        card_to_print=pygame.image.load(f"Assets\\cards\\white\\{card_submit_bot}_inima.png")
        x_start=scrWidth//8
        y_start=scrHeight//3
        pc_cards(scrWidth//5*2,scrHeight//5)
        card_to_print= pygame.transform.scale(card_to_print, (70, 90))
        for x_c in range(0,card_repeat):
               card_blit(card_to_print,x_start,y_start)
               x_start=x_start+scrWidth//8



        liedButton = button(position=(buttonsX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#ffcc99',
                            size=(200, 50), text='PC LIED', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
        continueButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY + 3 * incrementButtonY),
                                clr='white', cngclr='#ffcc99', size=(200, 50), text='CONTINUE',
                                font='Assets\Fonts\Pixeltype.ttf', font_size=30)

        liedButton.draw(screen)
        continueButton.draw(screen)
        if liedButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                SoundsUtil.buttonClickSoundPlay()
                option = 0
                done = True
        if continueButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                SoundsUtil.buttonClickSoundPlay()
                option = 1
                done = True
        pygame.display.update()

    return (bot_solution, option)


pygame.init()
scrInfo = pygame.display.Info()
screen = pygame.display.set_mode((scrInfo.current_w, scrInfo.current_h), pygame.FULLSCREEN, pygame.RESIZABLE)
background = pygame.image.load('background_play.jpg')
back1 = pygame.transform.scale(background, (scrInfo.current_w, scrInfo.current_h))
