
import pygame
from random import randint


# -----There are two ways to create objects in pygame ------ 

#   First 
# rect1 = pygame.Surface((widthsize, heightsize))
# rect1_rect = rect1.get_rect()
# screen.blit(rect1, (x_coor, y_coor))

# Second
# rect1 = pygame.Rect(x_coor, y_coor, widthsize, heightsize)
# pygame.draw.rect(screen, color, rect1)




# object
class Object:
    def __init__(self, x, y, width, height, speed = 1, center = False, does_image_exist = False, imagefile_name = None):
        self.width = width
        self.height = height
        self.does_image_exist = does_image_exist
        self.x_speed = randint(speed - 5, speed + 5)
        self.y_speed = randint(speed - 5, speed + 5)

        if does_image_exist:
            self.image = pygame.image.load(imagefile_name)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            if center:
                self.rect.center = x,y

        elif does_image_exist == False:
            self.rect = pygame.Rect(x, y, self.width, self.height)
            if center:
                self.rect.center = x,y
        self.random_move = (randint(0,2),randint(0,2))
        self.flag = False
    
    def key_movement(self,speed = 1,arrowkey = False):
        keys = pygame.key.get_pressed()
        self.speed = speed
        if arrowkey == False:
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed
        
        elif arrowkey == True:
        
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed


    def draw_on_screen(self, screen,x,y, color = (0, 255, 0)):
        self.rect.x = x
        self.rect.y= y
        if self.does_image_exist == False:
            pygame.draw.rect(screen, color, self.rect)
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def transform_image(self,scale_width,scale_height):
        self.image = pygame.transform.scale(self.image,(self.rect.width * scale_width, self.rect.height * scale_height))
    
    def rotate_image(self,angle):
        if self.flag == False:
            self.flag = True
            self.image = pygame.transform.rotate(self.image,angle)

        
        
    def automactic_movement(self,screenwidth,screenheight):
        """this implements object movement like a ball within the screen"""
        
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.top <= 0 or self.rect.bottom >= screenheight:
            self.y_speed *= -1
        if self.rect.left <= 0 or self.rect.right>= screenwidth :
            self.x_speed *= -1
    
    
    def limit_movement(self, xleft, xright, ytop, ybottom):
        """this limits object's movement""" 
        
        if self.rect.x <= xleft:
            self.rect.x = xleft
        if self.rect.x >= xright - self.rect.width:
            self.rect.x = xright - self.rect.width
        if self.rect.y <= ytop:
            self.rect.y = ytop
        if self.rect.y >= ybottom - self.rect.height:
            self.rect.y = ybottom - self.rect.height
        
    def location_reset(self,screenwidth, screenheight):
        self.rect.center = screenwidth / 2, screenheight / 2
    
    def disappear(self,screen):
        self.rect.x = -200
        self.rect.y = -200
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    def update_position(self,x,y):
        self.rect.x = x
        self.rect.y = y

        





if __name__ == "__main__":
    pass