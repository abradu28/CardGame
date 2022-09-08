import pygame
import ptext
from CardGame import SoundsUtil
from button import button
from PIL import Image
import time
import game


FONT = 'Assets\Fonts\Pixeltype.ttf'
MODE = 'Easy' # predefinit ca fiind EASY

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")

def loadBackground():
    global screen, scrInfo
    backgroundImage = Image.open("Assets\Gifs\poker-full-house.gif")
    currentFrame = 0

    # card = pygame.image.load("Assets\\newCards\Romb10.png")
    while True:
        clock = pygame.time.Clock()
        frame = pil_to_game(get_gif_frame(backgroundImage, currentFrame))
        frame = pygame.transform.scale(frame, (scrInfo.current_w, scrInfo.current_h))
        screen.blit(frame, (0, 0))
        # screen.blit(card, (400, 400))

        currentFrame = (currentFrame + 1) % (backgroundImage.n_frames // 3 - 16)

        if currentFrame == 0:
            break

        pygame.display.flip()
        clock.tick(10)

def loadTitle():
    global screen, scrInfo
    font = pygame.font.Font("Assets\Fonts\Pixeltype.ttf", 300)
    baseSurf = font.render("Minti", True, 'white')
    title = baseSurf.copy()
    titleRect = title.get_rect()
    titleRect.center = (scrInfo.current_w // 2, scrInfo.current_h // 2)

    # outLine = baseSurf.copy()
    # outLineRect = outLine.get_rect()
    # outLineRect.center = (scrInfo.current_w // 2 - 2, 302)

    alpha_surf = pygame.Surface(title.get_size(), pygame.SRCALPHA)
    alpha = 0

    while True:
        clock = pygame.time.Clock()
        title = baseSurf.copy()

        # alpha_surf.fill((0, 0, 0, alpha))
        # outLine.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        alpha_surf.fill((255, 255, 255, alpha))
        title.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # screen.blit(outLine, outLineRect)
        screen.blit(title, titleRect)
        pygame.display.update()

        alpha += 5
        if alpha > 255:
            break

        clock.tick(50)

def playBtnAction():
    if pygame.mouse.get_pressed()[0]:
        SoundsUtil.buttonClickSoundPlay()
        pygame.time.delay(100)
        playAgain = True
        while playAgain:
            test = game.Game(MODE)
            SoundsUtil.shuffleSoundPlay()
            playAgain = test.playGame()
            SoundsUtil.musicUnpause()

def howToPlayBtnAction():
    global gameLoop, BACKGROUND
    pygame.display.flip()
    if pygame.mouse.get_pressed()[0]:
        SoundsUtil.buttonClickSoundPlay()
        f = open("Assets/How_To_Play.txt", "r")
        content = f.read()
        done = False
        pygame.init()
        clock = pygame.time.Clock()
        while not done:

            done = checkIfQuit()

            screen.blit(BACKGROUND, (0, 0))
            backButton = button(position=(50, 25), clr='white', cngclr='#ffcc99', size=(100, 50),
                                text=' <-BACK', font="Assets\Fonts\Pixeltype.ttf", font_size=30)
            backButton.draw(screen)
            if backButton.mouseover():
                if pygame.mouse.get_pressed()[0]:
                    # added buttonClickSound - Ralu
                    SoundsUtil.buttonClickSoundPlay()
                    done = True

            BLUE = pygame.Color('dodgerblue')
            ptext.draw(content, (10, 60), color=BLUE, fontsize = 35, fontname = FONT)  # Recognizes newline characters.
            pygame.display.flip()
            clock.tick(60)
        PHOTO = pygame.image.load("Assets/Images/frameFromGif.jpg")
        PHOTO = pygame.transform.scale(PHOTO, (scrInfo.current_w, scrInfo.current_h))
        screen.blit(PHOTO, (0, 0))
        pygame.display.update()

def optionBtnAction():
    if pygame.mouse.get_pressed()[0]:
        SoundsUtil.buttonClickSoundPlay()
        pygame.init()
        global screen, scrInfo

        global MODE
        done = False
        clock = pygame.time.Clock()
        pygame.display.update()
        while not done:
            background = pygame.image.load('background_play.jpg')
            background = pygame.transform.scale(background, (scrInfo.current_w, scrInfo.current_h))
            screen.blit(background, (0, 0))

            done = checkIfQuit()

            easyButton = button(position=(buttonsX, buttonsY), clr='white', cngclr='#ffcc99', size=(200, 50),
                                text='EASY',
                                font="Assets\Fonts\Pixeltype.ttf", font_size=30)
            advancedButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY), clr='white', cngclr='#ffcc99', size=(200, 50), text='ADVANCED',
                                    font='Assets\Fonts\Pixeltype.ttf', font_size=30)

            backButton = button(position=(50, 25), clr='white', cngclr='#ffcc99', size=(100, 50),
                                text=' <-BACK', font="Assets\Fonts\Pixeltype.ttf", font_size=30)


            easyButton.draw(screen)
            advancedButton.draw(screen)
            backButton.draw(screen)

            if easyButton.mouseover():
                if pygame.mouse.get_pressed()[0]:
                    SoundsUtil.buttonClickSoundPlay()
                    time.sleep(0.5)
                    MODE = 'Easy'

            if advancedButton.mouseover():
                if pygame.mouse.get_pressed()[0]:
                    SoundsUtil.buttonClickSoundPlay()
                    time.sleep(0.5)
                    MODE = 'Advanced'

            if backButton.mouseover():
                if pygame.mouse.get_pressed()[0]:
                    # added buttonClickSound - Ralu
                    SoundsUtil.buttonClickSoundPlay()
                    done = True
            pygame.display.flip()

        PHOTO = pygame.image.load("Assets/Images/frameFromGif.jpg")
        PHOTO = pygame.transform.scale(PHOTO, (scrInfo.current_w, scrInfo.current_h))
        screen.blit(PHOTO, (0, 0))
        pygame.display.update()
        clock.tick(60)


def menu():
    global screen, currentFrame, backgroundImage, scrInfo

    playButton = button(position=(buttonsX, buttonsY), clr='white', cngclr='#ffcc99', size=(200, 50), text='PLAY', font="Assets\Fonts\Pixeltype.ttf", font_size=30)
    optionsButton = button(position=(buttonsX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#ffcc99', size=(200, 50), text='OPTIONS', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
    howToPlayButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY), clr='white', cngclr='#ffcc99', func = howToPlayBtnAction, size=(200, 50), text='HOW TO PLAY', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
    quitButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#ffcc99', size=(200, 50), text='QUIT', font='Assets\Fonts\Pixeltype.ttf', font_size=30)

    playButton.draw(screen)
    optionsButton.draw(screen)
    howToPlayButton.draw(screen)
    quitButton.draw(screen)

    playButton.mouseover()
    optionsButton.mouseover()
    howToPlayButton.mouseover()

    if quitButton.mouseover():
        quitBtnAction()

    if howToPlayButton.mouseover():
        howToPlayBtnAction()

    if playButton.mouseover():
        playBtnAction()

    if optionsButton.mouseover():
        optionBtnAction()

def quitBtnAction():
    global gameLoop
    if pygame.mouse.get_pressed()[0]:
        gameLoop = False

def checkIfQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            return True

##############################################################
pygame.init()
SoundsUtil.musicPlay()
# Create game screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)

bgColor = '#251513'
gameLoop = True
scrInfo = pygame.display.Info()
scrWidth = scrInfo.current_w
scrHeight = scrInfo.current_h
buttonsX = scrWidth // 4
buttonsY = scrHeight // 4
incrementButtonY = scrHeight // 6
incrementButtonX = scrWidth // 6

screen.fill(bgColor)
loadBackground()
loadTitle()
buttonDisplay = True
BACKGROUND = pygame.image.load("Assets/Images/poker.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND,(scrInfo.current_w, scrInfo.current_h))

while gameLoop:
    gameLoop = not checkIfQuit()
    menu()
    pygame.display.update()

# BEFORE QUITTING THE GAME: - Ralu

# -> play buttonClickSound
SoundsUtil.buttonClickSoundPlay()
# -> add 100 ms delay
pygame.time.delay(100)
# -> then play quitSound
SoundsUtil.musicStop()
SoundsUtil.quitSoundPlay()
# -> fadeout BG music
pygame.mixer.music.fadeout(500)
# -> add 1500 ms delay until quitting game
pygame.time.delay(1300)


pygame.quit()