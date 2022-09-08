import pygame
from CardGame.button import button
from CardGame import ptext, SoundsUtil

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FONT = 'Assets\Fonts\Pixeltype.ttf'
scrInfo = pygame.display.Info()


def endGame(endResult):
    SoundsUtil.musicPause()
    if endResult:
        SoundsUtil.winSoundPlay()
        bg = pygame.image.load("Assets/Images/winTempPic.jpg")
        msg = "YOU \n" \
              "WON"
        clr = 'black'
        pos = (250, 250)
        txt_size = 500
        playAgainButtonPos = (350, 1000)
        mainMenuButtonPos = (700, 1000)
    else:
        SoundsUtil.loseSoundPlay()
        bg = pygame.image.load("Assets/Images/loseTempPic.jpg")
        msg = "YOU LOST"
        clr = 'white'
        pos = (575, 700)
        txt_size = 300
        playAgainButtonPos = (700, 1000)
        mainMenuButtonPos = (1260, 1000)
    bg = pygame.transform.scale(bg, (scrInfo.current_w, scrInfo.current_h))
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.blit(bg, (0, 0))

        playAgainButton = button(position= playAgainButtonPos, clr='white', cngclr='#ffcc99', size=(200, 50), text='PLAY AGAIN', font="Assets\Fonts\Pixeltype.ttf", font_size=30)
        mainMenuButton = button(position= mainMenuButtonPos, clr='white', cngclr='#ffcc99', size=(200, 50), text='MAIN MENU', font="Assets\Fonts\Pixeltype.ttf", font_size=30)

        playAgainButton.draw(screen)
        mainMenuButton.draw(screen)

        if playAgainButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                SoundsUtil.buttonClickSoundPlay()
                done = True
                return True

        if mainMenuButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                SoundsUtil.buttonClickSoundPlay()
                pygame.display.update()
                done = True

        clock = pygame.time.Clock()
        ptext.draw(msg, pos, color=clr, fontsize=txt_size, fontname=FONT)
        pygame.display.flip()
        clock.tick(60)

    PHOTO = pygame.image.load("Assets/Images/frameFromGif.jpg")
    PHOTO = pygame.transform.scale(PHOTO, (scrInfo.current_w, scrInfo.current_h))
    screen.blit(PHOTO, (0, 0))
    pygame.display.update()
    return False

