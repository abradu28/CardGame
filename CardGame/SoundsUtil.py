import pygame


pygame.init()

# SOUNDS

def buttonClickSoundPlay():
    buttonClickSound.play()
def cardClickSoundPlay():
    cardClickSound.play()
def shuffleSoundPlay():
    shuffleSound.play()
def quitSoundPlay():
    quitSound.play()
def loseSoundPlay():
    loseSound.play()
def winSoundPlay():
    winSound.play()

buttonClickSound = pygame.mixer.Sound('Assets/Sounds/buttonClickSound.wav')
cardClickSound = pygame.mixer.Sound('Assets/Sounds/cardFlipSound.wav')
shuffleSound = pygame.mixer.Sound('Assets/Sounds/shuffleSound.wav')
quitSound = pygame.mixer.Sound('Assets/Sounds/quitSound.wav')
winSound = pygame.mixer.Sound('Assets/Sounds/winSound.wav')
loseSound = pygame.mixer.Sound('Assets/Sounds/loseSound.mp3')

buttonClickSound.set_volume(0.1)
cardClickSound.set_volume(0.15)
shuffleSound.set_volume(0.15)
quitSound.set_volume(0.03)
winSound.set_volume(0.1)
loseSound.set_volume(0.15)

# MUSIC

def musicPlay():
    pygame.mixer.music.play(-1)
def musicPause():
    pygame.mixer.music.pause()
def musicUnpause():
    pygame.mixer.music.unpause()
def musicStop():
    pygame.mixer.music.fadeout(20)

music =  pygame.mixer.music.load('Assets/Sounds/bgMusic.mp3')
pygame.mixer.music.set_volume(0.05)
