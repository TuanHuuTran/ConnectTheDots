import pygame
from sprite import *

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (22, 72, 99)
        self.stage_number = stage_number
        #self.board = self.create_game(stage_number)
        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        self.clock = pygame.time.Clock()
        self.init_all_sprites()
        self.button_list = []
        self.init_all_buttons()

    def init_all_buttons(self):        
        self.button_list.append(Button(100, 650, "resources/images/home_btn_pink.png", "Home", 75, 75))
        self.button_list.append(Button(225, 650, "resources/images/reset_btn.png", "Reset", 75, 75))
    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(Sprite(0, 0, "resources/images/background.jpg", self.width, self.height))
        self.sprite_list.add(Sprite(50, 50, "resources/images/green_box.png", 300, 250))
        self.sprite_list.add(Sprite(75, 325, "resources/images/pink_box.png", 250, 75))
        self.sprite_list.add(Sprite(75, 425, "resources/images/pink_box.png", 250, 75))
        self.sprite_list.add(Sprite(75, 525, "resources/images/pink_box.png", 250, 75))
        
    def get_setting_config(self, setting_option):
        width = 1200
        height = 800
        board_width = 500
        board_height = 500

        if(setting_option == 1):
            pass
        elif(setting_option == 2):
            pass
        elif(setting_option == 3):
            pass

        return width, height, board_width, board_height

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y
    
    def create_game(self, stage_number):
        pass

    def save_score(self, file_path):
        pass

    def get_score(self, file_path):
        pass

    def event(self):
        #check if user press the exit button on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit(0)

    def update(self):
        pass
    
    def draw_board(self):
        pass

    def draw(self):
        self.screen.fill(self.background_color)
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()


