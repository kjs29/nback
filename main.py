import sys, time, pygame
from object import Object
from random import randint

pygame.init()

# Create screen
screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("N-Back")

##### Settings #####
# icon
icon = pygame.image.load("img/n.png")
pygame.display.set_icon(icon)
  
# color
color = {"black" : (0, 0, 0), "white" : (255, 255, 255), "green" : (0, 255, 0),
         "grey" : (175,173,169), "red" : (255,0,0), "light green" : (144,238, 144),
         "sky blue" : (50,130,230), "light red" : (255,127,127), "light green" : (144,238,144),
         "blue" : (0,0,255), "purple" : (201,71,245), "dark grey" : (120,120,120)
        }

# FPS
fps_clock = pygame.time.Clock()
fps = 60

# Count down timer
countdown = 4
last_count = pygame.time.get_ticks()
last_count2 = pygame.time.get_ticks()
start_count = time.time()

# current N-back
current_nback = 2

#font
font15 = pygame.font.Font("font/gameplay.ttf", 15)
font20 = pygame.font.Font("font/gameplay.ttf", 20)
font55 = pygame.font.Font("font/gameplay.ttf", 55)
font30_clear = pygame.font.Font("font/KGPrimaryPenmanship.ttf",30)

# Questions (numbers)
lst = []
lst_rendered_contents = []
lst_rect = []
lst_answer = []
lst_rendered_contents_2 = []

number_of_questions = 4

# Background

# Main menu
bg2 = pygame.image.load("img/bg2.png")
bg3 = pygame.image.load("img/bg3.png")
bg4 = pygame.image.load("img/bg4.png")
bg8 = pygame.image.load("img/bg8.png")
scroll2 = 0
scroll3 = 0
scroll4 = 0
bg2_width = bg2.get_width()
bg3_width = bg3.get_width()
bg4_width = bg4.get_width()

# Game screen
gamebg = pygame.image.load("img/bgspace.png")
scroll5 = 0
gamebg_width = gamebg.get_width()

def update_screen(screen, color):
    screen.fill(color)  

# Sound channels
main_sound_channel = pygame.mixer.Channel(0)
game_sound_channel = pygame.mixer.Channel(1)
score_sound_channel = pygame.mixer.Channel(2)
pause_sound_channel = pygame.mixer.Channel(3)


################################## Game Control ###################################

# Random number generator control
random_number_control = False

# Ultimate control - to exit the game
run = True

# Main Menu

# Main Menu control - to exit the main menu
main = True

# How to play menu control - to exit the how to play menu
howtoplay = False
time_reset = 0

# Credit menu control - to exit the credit menu
credit = False

# Options menu control - to exit the options menu
options = False

# Gameplay screen
game = False
gamepaused = 0

# Score screen
score = False
score_update_control = False


# Sound control

# Game screen
main_background_sound_flag = False
number_appear_sound_flag = False
count_down_sound_flag = False
game_start_sound_flag = False
game_background_sound_flag = False
clock_tick_sound_flag = False

# Game Paused screen
paused_sound_flag =  False

# Score screen
score_sound_flag = False

# Background sound flag/ 1 = yes, 0 = no
backgroundsound = 1


percentage_control = False

#################################################################################



def regenerate_numbers():
    global lst, number_of_questions, random_number_control, lst_rect, lst_rendered_contents,lst_answer, lst_user_answer, low_number, med_number, high_number
    if low_number == True:
        number_of_questions = current_nback * 2
    elif med_number == True:
        number_of_questions = current_nback * 4
    elif high_number == True:
        number_of_questions = current_nback * 6

    if random_number_control == False:
        random_number_control = True
        font = pygame.font.Font("font/gameplay.ttf", 164)
        for i in range(number_of_questions):
            lst.append(randint(1, 9))
            each_content_1 = font.render(str(lst[i]), True, color["white"])
            each_rect_1 = each_content_1.get_rect()
            lst_rendered_contents.append(each_content_1)
            lst_rect.append(each_rect_1)
        # answer list

        lst_answer = []
        for i in range(len(lst)):
            if i >= current_nback:
                if lst[i] == lst[i - current_nback]:
                    lst_answer.append("O")
                else:
                    lst_answer.append("X")
        #print(f"answer : {lst_answer}")

        # user answer list
        lst_user_answer = [" " for _ in range(len(lst_answer))]
        # make each element invisible
        for each in lst_rect:
            each.x = -200
            each.y = -200


def play_sound(filename = None, volume = 1, loop = False, channel = -1):
    if channel == -1 and backgroundsound == 1:
        sound = pygame.mixer.Sound(filename)
        if volume != 1:
            sound.set_volume(volume)
        if loop:
            sound.play(-1)
        else:
            sound.play()
    # menu screen background music
    elif channel == 0:
        score_sound_channel.pause()
        game_sound_channel.pause()
        pause_sound_channel.pause()
        main_sound_channel.play(pygame.mixer.Sound("sound/moment.mp3"),-1,fade_ms = 500)
    # game screen background music
    elif channel == 1:
        main_sound_channel.pause()
        pause_sound_channel.pause()
        game_sound_channel.play(pygame.mixer.Sound("sound/game_loop_background_edited.wav"),-1,fade_ms=500)
    # score screen background music
    elif channel == 2:
        game_sound_channel.pause()
        pause_sound_channel.pause()
        score_sound_channel.set_volume(0.5)
        score_sound_channel.play(pygame.mixer.Sound("sound/gamescore.wav"),-1)
    # pause screen background music
    elif channel == 3:
        game_sound_channel.pause()
        main_sound_channel.pause()
        pause_sound_channel.play(pygame.mixer.Sound("sound/tobu_colors.mp3"),-1,fade_ms=500)

def reset_all_sound_flags():
    global main_background_sound_flag, number_appear_sound_flag, count_down_sound_flag, game_start_sound_flag, game_background_sound_flag, clock_tick_sound_flag,score_sound_flag,paused_sound_flag
    main_background_sound_flag = False
    number_appear_sound_flag = False
    count_down_sound_flag = False
    game_start_sound_flag = False
    game_background_sound_flag = False
    clock_tick_sound_flag =False
    score_sound_flag = False
    paused_sound_flag = False

def mute_background_sound_flags():
    global main_sound_channel, game_sound_channel, score_sound_channel, pause_sound_channel
    main_sound_channel.set_volume(0)
    game_sound_channel.set_volume(0)
    score_sound_channel.set_volume(0)
    pause_sound_channel.set_volume(0)


def resume_background_sound_flags():
    global main_sound_channel, game_sound_channel, score_sound_channel, pause_sound_channel
    main_sound_channel.set_volume(1)
    game_sound_channel.set_volume(1)
    score_sound_channel.set_volume(0.5)
    pause_sound_channel.set_volume(1)



def multiline_text(screen,size,text,color,coor,linespace= 10):
    text_list = text.splitlines()
    for i,e in enumerate(text_list):
        font = pygame.font.Font("font/KGPrimaryPenmanship.ttf",size)
        message_content = font.render(e,True,color)
        message_content_rect = message_content.get_rect()
        message_content_rect.center = coor[0], coor[1] + size*i + (i*linespace)
        screen.blit(message_content,message_content_rect)

def show_text(screen,text,coor,color,size):
    font = pygame.font.Font("font/KGPrimaryPenmanship.ttf",size)
    content = font.render(text,True,color)
    content_rect = content.get_rect()
    content_rect.center = coor[0],coor[1]
    screen.blit(content,content_rect)

# buttons
class Button:
    def __init__(self, font_name, size, x, y, color, text, center = False, image = False, imagefile_name = None):
        self.click_sound = pygame.mixer.Sound("sound/click.wav")
        self.image = image
        if image == False:
            self.font_name = font_name
            self.color = color
            self.text = text
            self.size = size
            self.font_kind = pygame.font.Font(self.font_name, size)
            self.content = self.font_kind.render(self.text,True, self.color)
            self.rect = self.content.get_rect()
        else:
            self.image = pygame.image.load(imagefile_name)
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #if I want to make it centered automatically
        if center == True:
            self.rect.center = x, y
        self.clicked = False
        self.hand = False
        self.move = 100


    def draw_text(self, screen):
        if self.image == False:
            screen.blit(self.content, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image,(self.rect.x, self.rect.y))

    def hovered(self,change_color, change_size, change_back_color = color["white"], change_back_size = 32,handshape = True, size_reset = False, x = 0, y = 0):
        active = False
        self.mouse_position = pygame.mouse.get_pos()
        
        # as we increase or dicrease the size of the text, the actual rect size doesn't change. 
        # so hovering over it is not applied accordingly. To prevent, I created this function.
        # if True, the changed text is still clickable - suitable for when increasing the size of the text.
        # if False, the changed text is not clickable - suitable for when decreasing the size of the text.
        if size_reset == True:
            self.rect = self.content.get_rect()
            self.rect.x = x
            self.rect.y = y
            
        
        if self.rect.collidepoint(self.mouse_position) and self.hand == False:
            self.hand = True
            #print("hovered")
            if handshape:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if self.image == False:
                self.color = change_color
                self.size = change_size
                self.font_kind = pygame.font.Font(self.font_name, self.size)
                self.content = self.font_kind.render(self.text, True, self.color)
            active = True

        elif self.rect.collidepoint(self.mouse_position) == False and self.hand == True:
            self.hand = False
            #print("hovered2")
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if self.image == False:
                self.color = change_back_color
                self.size = change_back_size
                self.font_kind = pygame.font.Font(self.font_name, self.size)
                self.content = self.font_kind.render(self.text, True, self.color)
          
        return active
        

    def check_click(self):
        self.mouse_position = pygame.mouse.get_pos()
        active = False
        if self.rect.collidepoint(self.mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                active = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False

        return active

    def left_right_movement(self):
        global run, game, gamepaused

        self.left_key_pressed = False
        self.right_key_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #print("left key pressed")
                    self.left_key_pressed = True
                    return self.left_key_pressed
                if event.key == pygame.K_RIGHT:
                    #print("right key pressed")
                    self.right_key_pressed = True
                    return self.right_key_pressed
                if event.key == pygame.K_ESCAPE and game == True and gamepaused == 0:
                    gamepaused = 1



    def key_movement(self):
        global main,run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    #print("up key pressed")
                    self.rect.y -= self.move
                    self.click_sound.play()
                if event.key == pygame.K_DOWN:
                    #print("down key pressed")
                    self.rect.y += self.move
                    self.click_sound.play()
                if event.key == pygame.K_RETURN:
                    #print("Enter key pressed")
                    return True
                if event.key == pygame.K_BACKSPACE:
                    #print("Backspace key pressed")
                    self.click_sound.play()
                if main == True:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.move = 0
                if event.key == pygame.K_DOWN:
                    self.move = 0
        
            self.move = 100

    def disappear(self):
        self.rect.center = -2000, -2000
    
    def update_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

"""From here is instantiations and calling functions """

# sound mute
main_sound_button = Button("font/8bitwonder.ttf", 15, 740, 10, color["white"], "Mute sound", False, True, "img/backgroundsound1.png")
main_sound_button_off = Button("font/8bitwonder.ttf", 15, -200, 10, color["white"], "Mute sound", False, True, "img/backgroundsound0.png")

# press backspace text
press_backspace_text = "Press backspace to\nreturn to the main menu"

# Main Menu buttons
main_mainmenu_button = Button("font/8bitwonder.ttf", 84, screenwidth / 2, 100, color['white'], "N back", True)
main_start_button = Button("font/8bitwonder.ttf", 32, screenwidth / 2, 220, color['white'], "start", True)
main_howtoplay_button = Button("font/8bitwonder.ttf", 32, screenwidth / 2, 320, color['white'], "how to play", True)
main_credit_button = Button("font/8bitwonder.ttf", 32, screenwidth / 2, 420, color['white'], "credits", True)
main_options_button = Button("font/8bitwonder.ttf", 32, screenwidth / 2, 520, color["white"], "options", True)
main_exit_button = Button("font/8bitwonder.ttf", 32, screenwidth / 2, 620, color['white'], "exit", True)

# Main Menu key scroll X
main_x_button = Button("font/8bitwonder.ttf", 24, screenwidth / 2 - 200, 0, color['white'], "*", False)

# How to play buttons
howtoplay_title_button = Button("font/8bitwonder.ttf", 32, 250, 220, color['white'], "How to play")
howtoplay_back_button = Button("font/8bitwonder.ttf", 42, 250, 520, color['white'], "Back")
texts = {"Let's learn 2 back": [screenwidth / 2, 240],
         "A new number is displayed\nEvery 5 seconds":[screenwidth / 2, 210],
         5:[650,380],
         7:[screenwidth / 2, 450],
         "2 back" : [140, 165]
        }
lst_texts = list(texts)
howtoplay_title_button.rect.center = screenwidth / 2, screenheight / 2 - 300
howtoplay_back_button.rect.center = screenwidth / 2, screenheight / 2 + 300
lst_practice_answer = [" "," "]

# Credit Menu buttons
credit_title_button = Button("font/8bitwonder.ttf", 42, 250, 220, color['white'], "Creator")
credit_made_by_button = Button("font/8bitwonder.ttf", 64, 250, 320, color['white'], "Jinsung Kim")
credit_back_button = Button("font/8bitwonder.ttf", 42, 250, 520, color['white'], "Back")
credit_email = "jsk.jinsung@gmail.com"
credit_title_button.rect.center = screenwidth / 2, screenheight / 2 - 200
credit_made_by_button.rect.center = screenwidth / 2, screenheight / 2 - 100
credit_back_button.rect.center = screenwidth / 2, screenheight / 2 + 200

# Option menu buttons
options_title_button = Button("font/8bitwonder.ttf", 42, screenwidth / 2, screenheight / 2 - 300, color["white"], "Options", True)
options_n_back_text = Button("font/gameplay.ttf", 32, 150, 250, color["white"], "# n", True)
options_number_of_questions_text1 = Button("font/8bitwonder.ttf", 20, 150, 400, color["white"], "number", True)
options_number_of_questions_text2 = Button("font/8bitwonder.ttf", 20, 150, 430, color["white"], "of", True)
options_number_of_questions_text3 = Button("font/8bitwonder.ttf", 20, 150, 460, color["white"], "questions", True)
options_2back = Button("font/8bitwonder.ttf", 32, 360, 250, color["white"], "2", True)
options_3back = Button("font/8bitwonder.ttf", 32, 440, 250, color["white"], "3", True)
options_4back = Button("font/8bitwonder.ttf", 32, 520, 250, color["white"], "4", True)
options_5back = Button("font/8bitwonder.ttf", 32, 600, 250, color["white"], "5", True)
options_6back = Button("font/8bitwonder.ttf", 32, 680, 250, color["white"], "6", True)
options_low_number_of_questions = Button("font/8bitwonder.ttf", 20, 350, 430, color["white"], "Low", True)
options_med_number_of_questions = Button("font/8bitwonder.ttf", 20, 530, 430, color["white"], "Med", True)
options_high_number_of_questions = Button("font/8bitwonder.ttf", 20, 710, 430, color["white"], "High", True)
options_back_button = Button("font/8bitwonder.ttf", 42, 250, 520, color["white"], "Back")
options_back_button.rect.center = screenwidth / 2, screenheight / 2 + 200

# some underline that indicates where the cursor is
options_key = Object(5, 5, 32, 3, 1, True, False)
options_key.rect.center = 357, 280
low_number = True
med_number = False
high_number = False


# Gamescreen

########################## Buttons & objects in Game screen#############################

# paused screen
pause_text = "Paused"
press_esc_to_pause_text = "<Esc> : pause"
press_right_to_o_text = "<Right key> : 'O'" 
press_left_to_x_text = "<Left key> : 'X' " 
pause_button = Button("font/8bitwonder.ttf", 15, screenwidth / 2, 365, color["black"], " ", True, True, "img/pause.png")
main_menu_text = Button("font/gameplay.ttf", 30, screenwidth / 2, 540, color["white"], "Main Menu", True)
press_esc_text = Button("font/KGPrimaryPenmanship.ttf", 50, screenwidth / 2, 470, color["white"], "Press <ESC> to continue", True)
quit_text = Button("font/gameplay.ttf", 30, screenwidth / 2, 600, color["white"], "Quit", True)
paused_sound_button = Button("font/8bitwonder.ttf", 15, 600, 170, color["white"], "Mute sound", False, True, "img/backgroundsound1.png")

# current n-back status
current_nback_text_font = pygame.font.Font("font/gameplay.ttf", 20)
current_nback_text_content = current_nback_text_font.render(str(current_nback) + " Back", True, color["white"])

# start, finish, car, dashboard images
earth_image = Object(110, 90, 50, 50, 1, False, True, "img/earth.png")
space_station_image = Object(640, 78, 50, 50, 1, False, True, "img/spacestation.png")
rocket_image = Object(110, 80, 50, 50, 1, center = False, does_image_exist = True, imagefile_name = "img/rocket.png")
odometer_image = Object(screenwidth / 2, 600, 100, 100, 1, True, True, "img/speedometer.png")
screen_image = Object(screenwidth / 2, 600, 100, 100, 1, True, True, "img/tablet.png")

# countdown before start
countdown_before_start = -4
countdown_before_start_font = pygame.font.Font("font/gameplay.ttf", 130)
countdown_before_start_content = countdown_before_start_font.render(str(countdown_before_start), True, color["white"])
countdown_before_start_content_rect = countdown_before_start_content.get_rect()
countdown_before_start_content_rect.x = screenwidth / 2 - 40
countdown_before_start_content_rect.y = screenheight / 2 - 60
rocket_x_position = 110

# how many seconds last during one number
seconds_each_number = 5
counter = 0

# counter for countdown before next number
counter_for_next_number = 5
counter_for_next_number_font = pygame.font.Font("font/gameplay.ttf",25)
counter_for_next_number_content = counter_for_next_number_font.render(str(counter_for_next_number), True, color["white"])
counter_for_next_number_content_rect = counter_for_next_number_content.get_rect()
counter_for_next_number_content_rect.x = -200
counter_for_next_number_content_rect.y = -200

# O, X button
o_button = Button(None, 13, 524, 530, color["white"], "1", True, True, "img/o.png")
x_button = Button(None, 13, 284, 530, color["white"], "1", True, True, "img/x.png")
frame_around_o_x_buttons = pygame.Surface((140, 140))
frame_around_o_x_buttons_rect = frame_around_o_x_buttons.get_rect()
frame_around_o_x_buttons_rect.center = -200, -200

#########################################################################################


# score screen

rectangle_outside = pygame.rect.Rect(50, 40, 700, 700)
result_text = Button("font/8bitwonder.ttf", 55, screenwidth / 2, 100, color["white"], "Result", True)
n_back_text = Button("font/gameplay.ttf", 20, 165, 200, color["white"], "n-back", True)
questions = Button("font/gameplay.ttf", 20, 165, 270, color["white"], "questions", True)
correct_answers = Button("font/gameplay.ttf", 20, 165, 410, color["white"], "correct answer", True)
user_answers = Button("font/gameplay.ttf", 20, 165, 540, color["white"], "your answer", True)
result_percentage_text = Button("font/gameplay.ttf", 20, 165, 645, color["white"], "Score", True)
go_back_to_main_menu_button = Button("font/gameplay.ttf", 20, 190, 692, color["white"], "Press enter key to go to Main menu")
number_of_correct_questions = 0
n_back_answer = Button("font/gameplay.ttf", 20, 520, 200, color["white"], str(current_nback), True)

def update_score():
    global lst_rendered_contents_2, score_update_control
    if score_update_control == False:
        score_update_control = True
        for each_n in lst:
            each_number_font = pygame.font.Font("font/gameplay.ttf", 20)
            each_number_content = each_number_font.render(str(each_n), True, color["white"])
            lst_rendered_contents_2.append(each_number_content)

while run:
    update_screen(screen, color["sky blue"])

    # Main Menu screen
    if main == True:
        if main_background_sound_flag == False:
            main_background_sound_flag = True
            play_sound(channel=0)
        for i in range(3):
            screen.blit(bg2, (bg2_width * i + scroll2, 0))
            screen.blit(bg3, (bg3_width * i + scroll3, 0))
            screen.blit(bg4, (bg4_width * i + scroll4, 0))
        scroll2 -= 0.5
        scroll3 -= 1
        scroll4 -= 2
        if abs(scroll2) > bg2_width:
            scroll2 = 0
        if abs(scroll3) > bg3_width:
            scroll3 = 0
        if abs(scroll4) > bg4_width:
            scroll4 = 0
        screen.blit(bg8, (0, 150))
        main_sound_button.draw_text(screen)
        if main_sound_button.check_click():
            if backgroundsound == 1:
                backgroundsound = 0
                mute_background_sound_flags()
            elif backgroundsound == 0:
                backgroundsound = 1
                resume_background_sound_flags()
        if backgroundsound == 0:
            main_sound_button.image = pygame.image.load("img/backgroundsound0.png")
        elif backgroundsound == 1:
            main_sound_button.image = pygame.image.load("img/backgroundsound1.png")
        if howtoplay == True:
            """texts = {"Let's learn 2 back": [screenwidth/2,240],
                     "A new number is displayed\nEvery 5 seconds":[screenwidth/2,210],
                     5:[650,380],
                     7:[screenwidth/2,450],
                     "2 back" : [140,165]
                    }"""
            #print(pygame.mouse.get_pos())
            current_time = time.time()
            if time_reset == 0:
                time_reset = 1
            if time_reset == 1:
                if current_time - start_count > 0:
                    bubble = pygame.Surface((600,200), pygame.SRCALPHA)
                    bubble.fill((255, 255, 255, 100))
                    screen.blit(bubble, (100, 145))
                if current_time - start_count > 1:
                    show_text(screen, lst_texts[0], texts["Let's learn 2 back"], color["white"], 50)
                if current_time - start_count > 3:
                    texts["Let's learn 2 back"] = [2000, 2000]
                if current_time - start_count > 3.2:
                    multiline_text(screen, 50, lst_texts[1], color["white"], texts["A new number is displayed\nEvery 5 seconds"], 15)
                    show_text(screen, lst_texts[4], texts["2 back"], color["sky blue"], 25)
                if time.time() - start_count > 5.4:
                    show_text(screen, str(lst_texts[3]), texts[7], color["green"], 200)
                if time.time() - start_count > 5.9:
                    show_text(screen, str(lst_texts[2]), texts[5], color["purple"], 45)
                if time.time() - start_count > 7.4:
                    lst_texts[2] = 4
                if time.time() - start_count > 8.4:
                    lst_texts[2] = 3
                if time.time() - start_count > 9.4:
                    lst_texts[2] = 2
                if time.time() - start_count > 10.4:
                    lst_texts[2] = 1
                if time.time() - start_count > 11.4:
                    lst_texts[2] = 5
                    lst_texts[3] = 9
                if time.time() - start_count > 13:
                    lst_texts[1] = "The number just\nchanged to 9"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 210
                if time.time() - start_count > 16:
                    lst_texts[1] = "Do you remember\nthe last number?"
                if time.time() - start_count > 19:
                    lst_texts[1] = "Good job!\nYes, it was the number 7"
                if time.time() - start_count > 22:
                    lst_texts[1] = "The last number would be \nN = 1 back number"
                if time.time() - start_count > 25:
                    lst_texts[1] = "Let me give you \nanother number"
                if time.time() - start_count > 28:
                    lst_texts[1] = "Remember \nthe last two numbers"
                if time.time() - start_count > 31:
                    lst_texts[1] = "3"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 240
                if time.time() - start_count > 32:
                    lst_texts[1] = "2"
                if time.time() - start_count > 33:
                    lst_texts[1] = "1"
                if time.time() - start_count > 34:
                    lst_texts[1] = " "
                    lst_texts[2] = 5
                    lst_texts[3] = 7
                    o_button.rect.y = 530
                    x_button.rect.y = 530
                    o_button.draw_text(screen)
                    x_button.draw_text(screen)
                if time.time() - start_count > 35 + 1:
                    lst_texts[2] = 4
                if time.time() - start_count > 35 + 2:
                    lst_texts[2] = 3
                if time.time() - start_count > 35 + 3:
                    lst_texts[2] = 2
                if time.time() - start_count > 35 + 4:
                    lst_texts[2] = 1
                if time.time() - start_count > 35 + 5:
                    lst_texts[1] = "What was the last number?"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 240
                if time.time() - start_count > 35 + 7:
                    lst_texts[1] = "Yes, it was the number 9"
                if time.time() - start_count > 35 + 9:      
                    lst_texts[1] = "What about\nthe second last number?(N = 2)\n(the first number)"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                if time.time() - start_count > 35 + 13:      
                    lst_texts[1] = "It was the number 7\nwhich is the same as\nthe current number 7"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                if time.time() - start_count > 35 + 18:      
                    lst_texts[1] = "You might have noticed\nthese two buttons :\n'O' and 'X'"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                if 35 + 19.2 < time.time() - start_count < 35 + 19.5:
                    pygame.draw.rect(screen, color["light red"], (200, 515, 410, 160), 4)  
                if 35 + 19.8 < time.time() - start_count < 35 + 22:
                    pygame.draw.rect(screen, color["light red"], (200, 515, 410, 160), 4)
                if time.time() - start_count > 35 + 22:
                    lst_texts[1] = "Click 'O' if the second last number\nis the same as the current number\n"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 195
                if time.time() - start_count > 59.3:
                    lst_texts[1] = "Click 'O' if the second last number\nis the same as the current number\nThe previous numbers : 7  9"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                if time.time() - start_count > 59.5:
                    if o_button.check_click():
                        #print("o clicked")
                        lst_practice_answer[0] = "O"
                        #print(lst_practice_answer)
                    elif x_button.check_click():
                        #print("x clicked")
                        lst_practice_answer[0] = "X"
                        #print(lst_practice_answer)
                    if lst_practice_answer[0] == "O":
                        lst_texts[1] = "Correct\n\nThe previous numbers : 7  9"
                        texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                        frame_around_o_x_buttons_rect.center = 524, 594
                        pygame.draw.rect(screen, color["light green"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
                        start_count = time.time()
                        time_reset = 2
                    elif lst_practice_answer[0] == "X":
                        lst_texts[1] = "The answer is wrong but it's okay\nThe current number is 7\nThe second last number was also 7"
                        texts["A new number is displayed\nEvery 5 seconds"][1] = 185
                        frame_around_o_x_buttons_rect.center = 284, 594
                        pygame.draw.rect(screen, color["light red"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
            
            elif time_reset == 2:
                bubble = pygame.Surface((600, 200), pygame.SRCALPHA)
                bubble.fill((255, 255, 255, 100))
                screen.blit(bubble, (100, 145))
                multiline_text(screen, 50, lst_texts[1], color["white"], texts["A new number is displayed\nEvery 5 seconds"], 15)
                show_text(screen, str(lst_texts[3]), texts[7], color["green"], 200)
                show_text(screen, str(lst_texts[2]), texts[5], color["purple"], 45)
                show_text(screen, lst_texts[4], texts["2 back"], color["sky blue"], 25)
                #print(time.time() - start_count)
                if time.time() - start_count > 1:
                    lst_texts[1] = "3"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 240
                if time.time() - start_count > 2:
                    lst_texts[1] = "2"
                if time.time() - start_count > 3:
                    lst_texts[1] = "1"
                if time.time() - start_count > 4:
                    lst_texts[1] = " "
                    lst_texts[2] = 5
                    lst_texts[3] = 8
                    o_button.rect.y = 530
                    x_button.rect.y = 530
                    o_button.draw_text(screen)
                    x_button.draw_text(screen)
                if time.time() - start_count > 4.01:
                    if o_button.check_click():
                        lst_practice_answer[1] = "O"
                    elif x_button.check_click():
                        lst_practice_answer[1] = "X"
                    if lst_practice_answer[1] == "O":
                        lst_texts[1] = "Wrong answer"
                        frame_around_o_x_buttons_rect.center = 524, 594
                        pygame.draw.rect(screen, color["light green"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
                    elif lst_practice_answer[1] == "X":
                        lst_texts[1] = "Correct answer"
                        frame_around_o_x_buttons_rect.center = 284, 594
                        pygame.draw.rect(screen, color["light red"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
                if time.time() - start_count > 5:
                    lst_texts[2] = 4
                    lst_texts[1] = "Choose 'O' or 'X'\nThe previous numbers : 7  9  7"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 210
                if time.time() - start_count > 6:
                    lst_texts[2] = 3
                if time.time() - start_count > 7:
                    lst_texts[2] = 2
                if time.time() - start_count > 8:
                    lst_texts[2] = 1
                if time.time() - start_count > 9:
                    lst_texts[1] = "The correct answer is 'X'\nnumbers : 7  9  7  8\nCorrect answer : O  X"
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 190
                if time.time() - start_count > 18:
                    texts["A new number is displayed\nEvery 5 seconds"][1] = 240
                    lst_texts[1] = "Now let's play the game!"
                if time.time() - start_count > 27:
                    time_reset = 1
                    lst_practice_answer = [" ", " "]
                    lst_texts[1] = "A new number is displayed\nEvery 5 seconds"
                    lst_texts[2] = 5
                    lst_texts[3] = 7
                    texts["A new number is displayed\nEvery 5 seconds"] = [screenwidth/2,210]
                    texts["Let's learn 2 back"] = [screenwidth/2,240]
                    if time_reset == 1:
                        start_count = time.time()
            howtoplay_title_button.draw_text(screen)
            howtoplay_back_button.draw_text(screen)
            howtoplay_title_button.hovered(color['green'], 32, color['white'], 32, handshape = False)
            howtoplay_back_button.hovered(color['green'], 42, color['white'], 42, False)
            if howtoplay_back_button.check_click():
                play_sound("sound/back.wav")
                lst_practice_answer = [" ", " "]
                lst_texts[1] = "A new number is displayed\nEvery 5 seconds"
                lst_texts[2] = 5
                lst_texts[3] = 7
                texts["A new number is displayed\nEvery 5 seconds"] = [screenwidth / 2, 210]
                texts["Let's learn 2 back"] = [screenwidth / 2, 240]
                time_reset = 1
                if time_reset == 1:
                    start_count = time.time()
                o_button.rect.y = 475
                x_button.rect.y = 475
                # game control - howtoplay menu exit

                howtoplay = False
                # I set this because if I sound/ the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        #print("backspace key pressed")
                        main_x_button.content = main_x_button.font_kind.render(main_x_button.text, True, color['white'])
                        play_sound("sound/back.wav")
                        lst_practice_answer = [" ", " "]
                        lst_texts[1] = "A new number is displayed\nEvery 5 seconds"
                        lst_texts[2] = 5
                        lst_texts[3] = 7
                        texts["A new number is displayed\nEvery 5 seconds"] = [screenwidth / 2, 210]
                        texts["Let's learn 2 back"] = [screenwidth / 2, 230]
                        time_reset = 1
                        if time_reset == 1:
                            start_count = time.time()
                        o_button.rect.y = 475
                        x_button.rect.y = 475
                        howtoplay = False
            multiline_text(screen, 25, press_backspace_text, color["dark grey"], (screenwidth / 2, 750), 1)                
        elif credit == True:
            credit_title_button.draw_text(screen)
            credit_made_by_button.draw_text(screen)
            show_text(screen, credit_email, (screenwidth / 2, 375), color["white"], 45)
            credit_back_button.draw_text(screen)
            credit_title_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_title_button.rect.x, y = credit_title_button.rect.y)
            credit_made_by_button.hovered(color['green'], 64, color['white'], 64, False, x = credit_made_by_button.rect.x, y = credit_made_by_button.rect.y)
            credit_back_button.hovered(color['green'], 42, color['white'], 42, False, x = credit_back_button.rect.x, y = credit_back_button.rect.y)
            multiline_text(screen, 25, press_backspace_text,color["white"], (screenwidth / 2, 650), 1)

            if credit_back_button.check_click():
                play_sound("sound/back.wav")
                #print("back button clicked")
                credit = False
                # I set this because if I sound/ the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        #print("backspace key pressed")
                        credit = False
                        play_sound("sound/back.wav")
        
        elif options == True:
            #print(pygame.mouse.get_pos())
            pygame.draw.rect(screen, color["white"], options_key)
            options_title_button.draw_text(screen)
            options_back_button.draw_text(screen)
            options_n_back_text.draw_text(screen)
            options_number_of_questions_text1.draw_text(screen)
            options_number_of_questions_text2.draw_text(screen)
            options_number_of_questions_text3.draw_text(screen)
            options_2back.draw_text(screen)
            options_3back.draw_text(screen)
            options_4back.draw_text(screen)
            options_5back.draw_text(screen)
            options_6back.draw_text(screen)
            options_low_number_of_questions.draw_text(screen)
            options_med_number_of_questions.draw_text(screen)
            options_high_number_of_questions.draw_text(screen)
            options_2back.hovered(color["white"], 32, color["white"], 32, True)
            options_3back.hovered(color["white"], 32, color["white"], 32, True)
            options_4back.hovered(color["white"], 32, color["white"], 32, True)
            options_5back.hovered(color["white"], 32, color["white"], 32, True)
            options_6back.hovered(color["white"], 32, color["white"], 32, True)
            options_low_number_of_questions.hovered(color["white"], 20, color["white"], 20, True)
            options_med_number_of_questions.hovered(color["white"], 20, color["white"], 20, True)
            options_high_number_of_questions.hovered(color["white"], 20, color["white"], 20, True)
            multiline_text(screen,25,press_backspace_text, color["white"], (screenwidth / 2, 644), 1)

            if options_2back.check_click():
                current_nback = 2
                # print(f"number_of_questions:{number_of_questions}")
                # print(f"current n_back : {current_nback}")
                # print(f"low_number:{low_number}\nmed_number:{med_number}\nhigh_number:{high_number}") 
                play_sound("sound/sci.wav")
            if options_3back.check_click():
                current_nback = 3
                play_sound("sound/sci.wav")
            if options_4back.check_click():
                current_nback = 4
                play_sound("sound/sci.wav")
            if options_5back.check_click():
                current_nback = 5
                play_sound("sound/sci.wav")
            if options_6back.check_click():
                current_nback = 6
                play_sound("sound/sci.wav")
            if current_nback == 2:
                options_2back.content = options_2back.font_kind.render("2", True, color["green"])
                options_3back.content = options_3back.font_kind.render("3", True, color["white"])
                options_4back.content = options_4back.font_kind.render("4", True, color["white"])
                options_5back.content = options_5back.font_kind.render("5", True, color["white"])
                options_6back.content = options_6back.font_kind.render("6", True, color["white"])
            elif current_nback == 3:
                options_2back.content = options_2back.font_kind.render("2", True, color["white"])
                options_3back.content = options_3back.font_kind.render("3", True, color["green"])
                options_4back.content = options_4back.font_kind.render("4", True, color["white"])
                options_5back.content = options_5back.font_kind.render("5", True, color["white"])
                options_6back.content = options_6back.font_kind.render("6", True, color["white"])
            elif current_nback == 4:
                options_2back.content = options_2back.font_kind.render("2", True, color["white"])
                options_3back.content = options_3back.font_kind.render("3", True, color["white"])
                options_4back.content = options_4back.font_kind.render("4", True, color["green"])
                options_5back.content = options_5back.font_kind.render("5", True, color["white"])
                options_6back.content = options_6back.font_kind.render("6", True, color["white"])
            elif current_nback == 5:
                options_2back.content = options_2back.font_kind.render("2", True, color["white"])
                options_3back.content = options_3back.font_kind.render("3", True, color["white"])
                options_4back.content = options_4back.font_kind.render("4", True, color["white"])
                options_5back.content = options_5back.font_kind.render("5", True, color["green"])
                options_6back.content = options_6back.font_kind.render("6", True, color["white"])
            elif current_nback == 6:
                options_2back.content = options_2back.font_kind.render("2", True, color["white"])
                options_3back.content = options_3back.font_kind.render("3", True, color["white"])
                options_4back.content = options_4back.font_kind.render("4", True, color["white"])
                options_5back.content = options_5back.font_kind.render("5", True, color["white"])
                options_6back.content = options_6back.font_kind.render("6", True, color["green"])
            if options_low_number_of_questions.check_click():
                low_number = True
                med_number = False
                high_number = False
                play_sound("sound/clicks.wav")
            elif options_med_number_of_questions.check_click():
                low_number = False
                med_number = True
                high_number = False
                play_sound("sound/clicks.wav")
            elif options_high_number_of_questions.check_click():
                low_number = False
                med_number = False
                high_number = True
                play_sound("sound/clicks.wav")

            #print(pygame.mouse.get_pos())
            options_back_button.hovered(color["green"], options_back_button.size, color["white"], options_back_button.size, handshape = False)
            if options_back_button.check_click():
                options = False
                play_sound("sound/back.wav")
                # I set this because if I sound/ the back button, it also clicks exit button in main menu
                pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        #print("backspace key pressed")
                        options = False
                        play_sound("sound/back.wav")
                    if event.key == pygame.K_LEFT:
                        play_sound("sound/menuclick.wav")
                        if options_key.rect.y < 300:
                            options_key.rect.x -= 80
                        else:
                            options_key.rect.x -= 180
                    if event.key == pygame.K_RIGHT:
                        play_sound("sound/menuclick.wav")
                        if options_key.rect.y < 300:
                            options_key.rect.x += 80
                        else:
                            options_key.rect.x += 180
                    if event.key == pygame.K_UP:
                        play_sound("sound/menuclick.wav")
                        options_key.rect.y -= 180
                        options_key.rect.width = 32
                        if 450 < options_key.rect.x < 500:
                            options_key.rect.x = 500
                            options_key.rect.y = 280
                    if event.key == pygame.K_DOWN:
                        play_sound("sound/menuclick.wav")
                        if options_key.rect.y < 300:
                            options_key.rect.y += 180
                        options_key.rect.width = 64
                        options_key.rect.x = 315

                    if event.key == pygame.K_RETURN:
                        if 260 < options_key.rect.y < 300:
                            play_sound("sound/sci.wav")
                            if 340 < options_key.rect.x < 380:
                                current_nback = 2
                            if 390 < options_key.rect.x < 460:
                                current_nback = 3  
                            if 480 < options_key.rect.x < 540:
                                current_nback = 4
                            if 550 < options_key.rect.x < 620:
                                current_nback = 5
                            if 640 < options_key.rect.x < 700:
                                current_nback = 6
                        if 455 < options_key.rect.y < 475:
                            play_sound("sound/clicks.wav")
                            if 305 < options_key.rect.x < 325:
                                low_number = True
                                med_number = False
                                high_number = False
                            if 485 < options_key.rect.x < 505:
                                low_number = False
                                med_number = True                  
                                high_number = False
                            if 665 < options_key.rect.x < 685:
                                low_number = False
                                med_number = False
                                high_number = True
            if options_key.rect.y < 360:
                if options_key.rect.x <= 341:
                    options_key.rect.x = 341
                if options_key.rect.x >= 660:
                    options_key.rect.x = 660
                if options_key.rect.y <= 280:
                    options_key.rect.y = 280
            elif 450 < options_key.rect.y < 470:
                if options_key.rect.x <= 315:
                    options_key.rect.x = 315
                if options_key.rect.x >=675:
                    options_key.rect.x = 675
                if options_key.rect.y >= 460:
                    options_key.rect.y = 460
            if low_number:
                med_number = False
                high_number = False
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low", True, color["green"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med", True, color["white"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high", True, color["white"])
            elif med_number:
                low_number = False
                high_number = False
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low", True, color["white"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med", True, color["green"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high", True, color["white"])
            elif high_number:
                low_number = False
                med_number = False
                options_low_number_of_questions.content = options_low_number_of_questions.font_kind.render("low", True, color["white"])
                options_med_number_of_questions.content = options_med_number_of_questions.font_kind.render("med", True, color["white"])
                options_high_number_of_questions.content = options_high_number_of_questions.font_kind.render("high", True, color["green"])
        else:
            main_mainmenu_button.draw_text(screen)
            main_start_button.draw_text(screen)
            main_howtoplay_button.draw_text(screen)
            main_credit_button.draw_text(screen)
            main_options_button.draw_text(screen)
            main_exit_button.draw_text(screen)
            main_x_button.draw_text(screen)
            main_start_button.hovered(color['green'], 32, color['white'], 32, True)
            main_howtoplay_button.hovered(color['green'], 32, color['white'], 32, False)
            main_credit_button.hovered(color['green'], 32, color['white'], 32, False)
            main_options_button.hovered(color["green"], 32, color["white"], 32, False)
            main_exit_button.hovered(color["dark grey"], 32, color['white'], 32, True)
            

            if main_start_button.check_click():
                play_sound("sound/gamestart.ogg")
                #print("start menu clicked")
                game = True
                main = False
            if main_credit_button.check_click():
                play_sound("sound/entersound.wav")
                #print("credit menu clicked")
                credit = True
            if main_howtoplay_button.check_click():
                play_sound("sound/entersound.wav")
                #print("how to play menu clicked")
                start_count = time.time()
                howtoplay = True
            if main_options_button.check_click():
                play_sound("sound/entersound.wav")
                #print("options menu clicked")
                options = True
            if main_exit_button.check_click():
                run = False
            if main_x_button.key_movement(): 
                if main_x_button.rect.y < 250:
                    #print("START!!!")
                    game = True
                    main = False
                    play_sound("sound/gamestart.ogg")
                elif main_x_button.rect.y < 350:
                    #print("HOW TO PLAY pressed")
                    start_count = time.time()
                    howtoplay = True
                    play_sound("sound/entersound.wav")
                elif main_x_button.rect.y < 450:
                    #print("CREDIT pressed")
                    credit = True
                    play_sound("sound/entersound.wav")
                elif main_x_button.rect.y < 550:
                    #print("Option pressed")
                    options = True
                    play_sound("sound/entersound.wav")
                elif main_x_button.rect.y < 650:
                    #print("EXIT pressed")
                    run = False
            if main_x_button.rect.y < 208:
                main_x_button.rect.y = 208
            if main_x_button.rect.y < 250:
                main_x_button.rect.x = 284
            if 290 < main_x_button.rect.y <350:
                main_x_button.rect.x = 195
            if 390 < main_x_button.rect.y < 450:
                main_x_button.rect.x = 262
            if 490 < main_x_button.rect.y < 550:
                main_x_button.rect.x = 261
            if 590 < main_x_button.rect.y < 650:
                main_x_button.rect.x = 310
            if main_x_button.rect.y > 608:
                main_x_button.rect.y = 608
    
    # Game screen
    elif game == True:
        if gamepaused == 1:
            #print(pygame.mouse.get_pos())
            if paused_sound_flag == False and backgroundsound == 1:
                paused_sound_flag = True
                play_sound("sound/menuclick.wav")
                play_sound(channel = 3)
            screen.blit(gamebg, (0, 0))
            pygame.draw.rect(screen, color["white"], pygame.rect.Rect(150, 150, 500, 500), 4, 15)
            #show_text(screen,pause_text,(screenwidth/2,220), color["white"],90)
            paused_message = font55.render(pause_text, True, color["white"])
            paused_message_rect = paused_message.get_rect()
            paused_message_rect.center = screenwidth / 2, 220
            screen.blit(paused_message, paused_message_rect)
            pause_button.draw_text(screen)
            press_esc_text.draw_text(screen)
            quit_text.draw_text(screen)
            main_menu_text.draw_text(screen)
            paused_sound_button.draw_text(screen)
            if paused_sound_button.check_click():
                if backgroundsound == 1:
                    backgroundsound = 0
                    mute_background_sound_flags()
                    #paused_sound_button.image = pygame.image.load("img/backgroundsound0.png")
                elif backgroundsound == 0:
                    #paused_sound_button.image = pygame.image.load("img/backgroundsound1.png")
                    backgroundsound = 1
                    resume_background_sound_flags()
            if backgroundsound == 0:
                paused_sound_button.image = pygame.image.load("img/backgroundsound0.png")
            elif backgroundsound == 1:
                paused_sound_button.image = pygame.image.load("img/backgroundsound1.png")
            pause_button.hovered(None, None)
            press_esc_text.hovered(color["green"], 50, color["white"], 50)
            main_menu_text.hovered(color["green"], 30, color["white"], 30)
            quit_text.hovered(color["grey"], 30, color["white"], 30)
            if pause_button.check_click() or press_esc_text.check_click():
                paused_sound_flag = False
                game_background_sound_flag = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                gamepaused = 0
            if main_menu_text.check_click():
                #screen.fill(color["black"])
                last_count = 0
                current_count = 0
                countdown_before_start = -4
                percentage_control = False
                rocket_image.rect.x = 110
                rocket_image.rect.y = 80
                countdown_before_start_content_rect.x = screenwidth / 2 - 40
                countdown_before_start_content_rect.y = screenwidth / 2 - 60
                number_of_correct_questions = 0
                lst_rendered_contents = []
                lst = []
                lst_rendered_contents_2 = []
                lst_answer = []
                lst_user_answer = []
                random_number_control = False
                rocket_image.flag = False
                rocket_x_position = 110
                paused_sound_flag = False
                game_background_sound_flag = False
                game_start_sound_flag = False
                count_down_sound_flag = False
                number_appear_sound_flag = False
                clock_tick_sound_flag = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                gamepaused = 0
                main = True
                score = False
                pygame.time.delay(100)
            if quit_text.check_click():
                run = False

        else:
            #print(pygame.mouse.get_pos())
            if main_background_sound_flag and backgroundsound == 1:
                main_background_sound_flag = False
                main_sound_channel.fadeout(500)
            update_screen(screen,color["black"])
            screen.blit(gamebg, (0, 0))
            odometer_image.transform_image(1.2, 1)
            odometer_image.draw_on_screen(screen, 92, 660)
            screen_image.transform_image(1.3, 1.5)
            screen_image.draw_on_screen(screen, 68, -80)
            regenerate_numbers()
            current_nback_text_content = current_nback_text_font.render(str(current_nback) + " Back", True, color["white"])
            screen.blit(current_nback_text_content,(610, 243))
            earth_image.draw_on_screen(screen, 100, 82)
            space_station_image.draw_on_screen(screen, 640, 78)
            rocket_image.draw_on_screen(screen,rocket_image.rect.x, rocket_image.rect.y)
            o_button.rect.y = 475
            x_button.rect.y = 475
            show_text(screen,press_esc_to_pause_text, (70, 20), color["white"], 25)
            show_text(screen,press_right_to_o_text, (80, 40), color["white"], 25)
            show_text(screen,press_left_to_x_text, (80, 60), color["white"], 25)
            # blit images from lst_rendered_contents onto screen
            for i in range(len(lst_rendered_contents)):
                screen.blit(lst_rendered_contents[i], lst_rect[i])

            # every 0.2 second - before start
            current_count = pygame.time.get_ticks()
            #print(f"current_count - last_count : {current_count} - {last_count}")
            
            if current_count - last_count > 200:
                countdown_before_start += 0.2
                last_count = current_count
                countdown_before_start_content = countdown_before_start_font.render(str(countdown_before_start), True, color["white"])
                quotient = int(countdown_before_start) // 5
                rem = int(countdown_before_start) % 5
                
                if int(countdown_before_start) < 0:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    countdown_before_start_content = countdown_before_start_font.render(str(int(-countdown_before_start)), True, color["white"])
                    if int(countdown_before_start) == -3:
                        if count_down_sound_flag == False:
                            count_down_sound_flag = True
                            play_sound("sound/countdown.wav")

                elif int(countdown_before_start) == 0 :
                    countdown_before_start_content = countdown_before_start_font.render(str("Start!"), True, color["white"])
                    countdown_before_start_content_rect.x = screenwidth / 2 - 260
                    if game_start_sound_flag == False:
                        game_start_sound_flag = True
                        play_sound("sound/countdown_start.wav")

                if 0 < countdown_before_start < len(lst_rect) * 5 :
                    countdown_before_start_content_rect.center = -200, -200
                    lst_rect[quotient - 1].center = -200, -200
                    counter_for_next_number_content_rect.x = 680
                    counter_for_next_number_content_rect.y = 20
                    rocket_x_position += 495 / 25 / number_of_questions
                    rocket_image.rect.x = rocket_x_position

                    # every 5 second car moves
                    # if round(countdown_before_start,2) % 5 == 0.0:
                    #     rocket_image_rect.x += 500/number_of_questions

                    # this makes number disappear for a short time
                    if quotient * 5 + 4.78 < countdown_before_start:
                        lst_rect[quotient].center = -200, -200
                    else:
                        lst_rect[quotient].center = screenwidth / 2 + 8, screenheight / 2 - 45

                # show counter before the next number shows up - used remainder
                if 0 <= countdown_before_start < number_of_questions * 5 :
                    if game_background_sound_flag == False:
                        game_background_sound_flag = True
                        play_sound(channel = 1)
                    if rem == 0:
                        if number_appear_sound_flag == False:
                            number_appear_sound_flag = True
                            play_sound("sound/number_appear_edited.mp3")
                        counter_for_next_number_content = counter_for_next_number_font.render(" ", True, color["white"])
                    if rem == 1:
                        counter_for_next_number_content = counter_for_next_number_font.render(" ", True, color["white"])
                        number_appear_sound_flag = False
                    if rem == 2:
                        counter_for_next_number_content = counter_for_next_number_font.render("3", True, color["white"])
                        if clock_tick_sound_flag == False:
                            clock_tick_sound_flag = True
                            play_sound("sound/clock_tick.wav")
                    if rem == 3:
                        clock_tick_sound_flag = False
                        counter_for_next_number_content = counter_for_next_number_font.render("2", True, color["white"])
                    if rem == 4:
                        counter_for_next_number_content = counter_for_next_number_font.render("1", True, color["white"])
                elif round(countdown_before_start, 2) >= number_of_questions * 5:
                    counter_for_next_number_content = counter_for_next_number_font.render(" ", True, color["white"])

            if 5 * current_nback <= round(countdown_before_start, 2) < 5 * number_of_questions:
                o_button.draw_text(screen)
                x_button.draw_text(screen)
                o_button.hovered(None, 12)
                x_button.hovered(None, 12)

                # I tried to implement left key for 'X', and right key for 'O' but it didn't let me
                # so I am just using only x button to determine left key pressed or right key pressed.
                x_button.left_right_movement()

                if o_button.check_click() or x_button.right_key_pressed:
                    #print(f"quotient - 2 : {quotient-current_nback}")
                    lst_user_answer[quotient-current_nback] = "O"
                    #print(lst_user_answer)
                    #print("o clicked")
                    #print(f"current number:{lst[quotient]}")
                    #print(f"current_nback-back number:{lst[quotient - current_nback]}")
                    play_sound("sound/mouseclick.wav")
                    #if lst[quotient] == lst[quotient - current_nback]:
                        #print("correct choice!")
                    #else:
                        #print("wrong choice!")
                if x_button.check_click() or x_button.left_key_pressed:
                    lst_user_answer[quotient-current_nback] = "X"
                    #print(lst_user_answer)
                    #print("x clicked")
                    #print(f"current number:{lst[quotient]}")
                    #print(f"current_nback-back number:{lst[quotient - current_nback]}")
                    play_sound("sound/mouseclick.wav")
                    #if lst[quotient] != lst[quotient - current_nback]:
                        #print("correct choice!")
                    #else:
                        #print("wrong choice!")
        
                if lst_user_answer[quotient-current_nback] == "O":
                    frame_around_o_x_buttons_rect.center = 524, 539
                    pygame.draw.rect(screen, color["light green"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
                elif lst_user_answer[quotient-current_nback] == "X":
                    frame_around_o_x_buttons_rect.center = 284, 539
                    pygame.draw.rect(screen, color["light red"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
                elif lst_user_answer[quotient-current_nback] == " ":
                    frame_around_o_x_buttons_rect.center = -200, -200
                    pygame.draw.rect(screen, color["white"], frame_around_o_x_buttons_rect, 3, border_radius = 15)
            
            if round(countdown_before_start, 2) > number_of_questions * 5:
                reset_all_sound_flags()
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                score = True
                game = False
            
            screen.blit(counter_for_next_number_content, (counter_for_next_number_content_rect.x, counter_for_next_number_content_rect.y))
            screen.blit(countdown_before_start_content, (countdown_before_start_content_rect.x, countdown_before_start_content_rect.y))
            #pygame.draw.rect(screen,color["white"],frame_around_o_x_buttons_rect,3,border_radius = 15)
            first = quotient + 1
            progress = font20.render(str(quotient + 1) + " / " + str(number_of_questions), True, color["white"])
            screen.blit(progress, (110, 243))
        
    elif score == True:
        game = False
        screen.fill(color["black"])
        if score_sound_flag == False and backgroundsound == 1:
            score_sound_flag = True
            play_sound(channel = 2)
        
        # this allows to reset the previous score and update_position new result
        update_score()
        pygame.draw.rect(screen, color["white"], rectangle_outside, 3)
        pygame.draw.line(screen,color["white"], (100, 150), (700, 150), 2)
        pygame.draw.line(screen,color["white"], (280, 185), (280, 680), 2)
        earth_image.draw_on_screen(screen, 100, 82)
        space_station_image.draw_on_screen(screen, 640, 78)
        rocket_image.rotate_image(90)
        rocket_image.draw_on_screen(screen, 600, rocket_image.rect.y)
        screen.blit(result_text.content, result_text.rect)
        n_back_text.draw_text(screen)
        questions.draw_text(screen)
        correct_answers.draw_text(screen)
        user_answers.draw_text(screen)
        n_back_answer.draw_text(screen)
        n_back_answer.content = n_back_answer.font_kind.render(str(current_nback), True, color["white"])
        result_percentage_text.draw_text(screen)
        go_back_to_main_menu_button.draw_text(screen)
        go_back_to_main_menu_button.hovered(color['green'], 20, color['white'], 20, handshape = True)

        # questions 
        if len(lst_rendered_contents_2) <= 10:
            for index, each in enumerate(lst_rendered_contents_2):
                screen.blit(each, ((280 + (470 * (index + 1) / (len(lst_rendered_contents_2) + 1))), 255))
        elif 10 < len(lst_rendered_contents_2) <= 30:
            for index, each in enumerate(lst_rendered_contents_2):
                if index <= 9:
                    screen.blit(each, ((280 + (470 * (index + 1) / (11))), 255))
                if 9 < index <= 19:
                    screen.blit(each, ((280 + (470 * (index % 10 + 1) / (11))), 255 + 40))
                if 19 < index:
                    screen.blit(each, ((280 + (470 * (index % 10 + 1) / (11))), 255 + 80))
        elif 30 < len(lst_rendered_contents_2):            
            long_lst = []
            for each in lst:
                font15 = pygame.font.Font("font/gameplay.ttf",15)
                each_content = font15.render(str(each), True, color["white"])
                long_lst.append(each_content)
            for i, e in enumerate(long_lst):
                if i <= 9:
                    screen.blit(e, ((280 + (470 * (i + 1) / (11))), 247))
                if 9 < i <= 19:
                    screen.blit(e, ((280 + (470 * (i % 10 + 1) / (11))), 247 + 30))
                if 19 < i <= 29:
                    screen.blit(e, ((280 + (470 * (i % 10 + 1) / (11))), 247 + 60))
                if 29 < i:
                    screen.blit(e, ((280 + (470 * (i % 10 + 1) / (11))), 247 + 90))

        # correct answer 
        if len(lst_answer) <= 10:
            for index, each in enumerate(lst_answer):
                answer_font = pygame.font.Font("font/gameplay.ttf", 20)
                answer_content = answer_font.render(str(each), True, color["white"])
                screen.blit(answer_content, ((280 + (470 * (index + 1) / (len(lst_answer) + 1))), 395))
        elif 10 < len(lst_answer):
            for index, each in enumerate(lst_answer):
                answer_font = pygame.font.Font("font/gameplay.ttf", 20)
                answer_content = answer_font.render(str(each), True, color["white"])
                if index <= 9:
                    screen.blit(answer_content, ((280 + (470 * (index + 1) / (11))), 395))
                if 9 < index <= 19:
                    screen.blit(answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 395 + 40))
                if 19 < index:
                    screen.blit(answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 395 + 80))

        # user answer
        if len(lst_user_answer) <= 10:
            for index, each in enumerate(lst_user_answer):
                user_answer_font = pygame.font.Font("font/gameplay.ttf", 20)
                if each == " ":
                    each = "n/a"
                    user_answer_font = pygame.font.Font("font/gameplay.ttf", 10)
                user_answer_content = user_answer_font.render(str(each), True, color["white"])
                screen.blit(user_answer_content,((280 + (470 * (index + 1) / (len(lst_user_answer) + 1))), 530))
        elif len(lst_user_answer) > 10:
            for index, each in enumerate(lst_user_answer):
                user_answer_font = pygame.font.Font("font/gameplay.ttf", 20)
                if each == " ":
                    each = "n/a"
                    user_answer_font = pygame.font.Font("font/gameplay.ttf", 10)
                user_answer_content = user_answer_font.render(str(each), True, color["white"])
                if index <= 9:
                    screen.blit(user_answer_content, ((280 + (470 * (index + 1) / (11))), 530))
                if 9 < index <= 19:
                    screen.blit(user_answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 530 + 40))
                if 19 < index:
                    screen.blit(user_answer_content, ((280 + (470 * (index % 10 + 1) / (11))), 530 + 80))
        if percentage_control == False:
            percentage_control = True
            for i in range(len(lst_answer)):
                if lst_answer[i] == lst_user_answer[i]:
                    number_of_correct_questions += 1
            percentage = number_of_correct_questions / len(lst_answer) * 100
            print("\n################## Report ##################")
            print(f"{current_nback}-back / {number_of_questions} numbers\nQuestions, Correct answers, User answers :\n")
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    print(f"|{lst[i]}", end ="")
                else:
                    print(f"|{lst[i]}", end="|\n")
            print(" "*2*current_nback,end= "")
            for i in range(len(lst_answer)):
                if i != len(lst_answer) - 1:
                    print(f"|{lst_answer[i]}", end ="")
                else:
                    print(f"|{lst_answer[i]}", end="|\n")
            print(" "*2*current_nback,end= "")
            for i in range(len(lst_user_answer)):
                if i != len(lst_user_answer) - 1:
                    print(f"|{lst_user_answer[i]}", end ="")
                else:
                    print(f"|{lst_user_answer[i]}", end="|")
            print(f"\n\nScore : {round(percentage,2)} %")
            print("############################################")
        percentage_font = pygame.font.Font("font/gamecube.ttf", 20)
        percentage_message = percentage_font.render(str(round(percentage, 2)) + " %", True, color["white"])
        if percentage >= 80:
            percentage_message = percentage_font.render(str(round(percentage,2)) + " %", True, color["green"])
        elif percentage <= 40:
            percentage_message = percentage_font.render(str(round(percentage,2)) + " %", True, color["red"])
        percentage_message_rect = percentage_message.get_rect()
        percentage_message_rect.center = 525, 645
        screen.blit(percentage_message,percentage_message_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    last_count = 0
                    current_count = 0
                    countdown_before_start = -4
                    score_update_control = False
                    percentage_control = False
                    rocket_image.rect.x = 110
                    rocket_image.rect.y = 80
                    countdown_before_start_content_rect.x = screenwidth / 2 - 40
                    countdown_before_start_content_rect.y = screenwidth / 2 - 60
                    number_of_correct_questions = 0
                    for i in range(len(lst_rendered_contents)):
                        lst_rendered_contents.pop(0)
                        lst.pop(0)
                        lst_rendered_contents_2.pop(0)
                    for i in range(len(lst_answer)):
                        lst_answer.pop(0)
                        lst_user_answer.pop(0)
                    random_number_control = False
                    screen.fill(color["black"])
                    rocket_image.flag = False
                    rocket_image.rotate_image(270)
                    rocket_image.flag = False
                    rocket_x_position = 110
                    main = True
                    score = False
        if go_back_to_main_menu_button.check_click():
            last_count = 0
            current_count = 0
            countdown_before_start = -4
            score_update_control = False
            percentage_control = False
            rocket_image.rect.x = 110
            rocket_image.rect.y = 80
            countdown_before_start_content_rect.x = screenwidth / 2 - 40
            countdown_before_start_content_rect.y = screenwidth / 2 - 60
            number_of_correct_questions = 0
            for i in range(len(lst_rendered_contents)):
                lst_rendered_contents.pop(0)
                lst.pop(0)
                lst_rendered_contents_2.pop(0)
            for i in range(len(lst_answer)):
                lst_answer.pop(0)
                lst_user_answer.pop(0)
            random_number_control = False
            screen.fill(color["black"])
            rocket_image.flag = False
            rocket_image.rotate_image(270)
            rocket_image.flag = False
            rocket_x_position = 110
            main = True
            score = False
        
    if backgroundsound == 0:
        mute_background_sound_flags()
    elif backgroundsound == 1:
        resume_background_sound_flags()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if game == True and event.key == pygame.K_ESCAPE and gamepaused == 0:
                gamepaused = 1
            elif game == True and event.key == pygame.K_ESCAPE and gamepaused == 1:
                paused_sound_flag = False
                pause_sound_channel.fadeout(500)
                game_background_sound_flag = False
                gamepaused = 0

    pygame.display.update()
    fps_clock.tick(fps)

sys.exit()
