# class Button:
#     def __init__(self, img, x, y, def_color, hover_color, font, txt):
#         self.bgImage = img
#         self.posX = x
#         self.posY = y
#         self.bgRect = self.bgImage.get_rect(center=(self.posX, self.posY))
#         self.defColor = def_color
#         self.hoverColor = hover_color
#         self.font = font
#         self.txt = txt
#         self.txtImage = self.font.render(self.txt, True, self.defColor)
#         self.txtRect = self.txtImage.get_rect(center=(self.posX, self.posY))
#
#     def is_hovered(self, pos):
#         return pos[0] in range(self.bgRect.left, self.bgRect.right) and pos[1] in range(self.bgRect.top, self.bgRect.bottom)
#
#     def change_bg_color(self, pos):
#         if self.is_hovered(pos):
#             self.txtImage = self.font.render(self.txt, True, self.hoverColor)
#         else:
#             self.txtImage = self.font.render(self.txt, True, self.defColor)
#
#     def update_btn(self, screen):
#         screen.blit(self.bgImage, self.bgRect)
#         screen.blit(self.txtImage, self.txtRect)

import pygame

class button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):
        self.clr    = clr
        self.size   = size
        self.func   = func
        self.surf   = pygame.Surface(size)
        self.rect   = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])


        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

    def call_back(self, *args):
        if self.func:
            return self.func(*args)

class text:
    def __init__(self, msg, position, clr=[100, 100, 100], font="Segoe Print", font_size=15, mid=False):
        self.position = position
        self.font = pygame.font.SysFont(font, font_size)
        self.txt_surf = self.font.render(msg, 1, clr)

        if len(clr) == 4:
            self.txt_surf.set_alpha(clr[3])

        if mid:
            self.position = self.txt_surf.get_rect(center=position)


    def draw(self, screen):
        screen.blit(self.txt_surf, self.position)




# call back functions
def fn1():
    print('Start Game')
def fn2():
    print('How to play')


if __name__ == '__main__':
    pygame.init()
    screen_size = (1000, 500)
    size        = 10
    clr         = [255, 0, 255]
    bg          = (255, 255, 0)
    font_size   = 15
    font        = pygame.font.Font(None, font_size)
    clock       = pygame.time.Clock()

    screen    = pygame.display.set_mode(screen_size)
    screen.fill(bg)

    button1 = button(position=(255, 250), size=(200, 100), clr=(220, 220, 220), cngclr=(255, 0, 0), func=fn1, text='Start')
    button2 = button((725, 250), (200, 100), (220, 220, 220), (255, 0, 0), fn2, 'How to play')

    button_list = [button1, button2]

    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    crash = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in button_list:
                        if b.rect.collidepoint(pos):
                            b.call_back()

        for b in button_list:
            b.draw(screen)

        pygame.display.update()
        clock.tick(60)

