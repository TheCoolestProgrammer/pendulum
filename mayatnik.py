import pygame
import random

                   #         #
     #####        #           #          ####
#####     ##       #         #         ##    ####
##          #       ###   ###         #        ##
#                      ###                      #
##                      #                      ##
###                    ###                    ###
######                #####                 #####
############       ###########       ############
#################################################


# this programm is summulator of chaotic pendulum


#################################################
############       ###########       ############
######                #####                 #####
###                    ###                    ###
##                      #                      ##
#                      ###                      #
##          #       ###   ###         #        ##
#####     ##       #         #         ##    ####
     #####        #           #          ####
                   #         #



 #######                                #######
##      ##                            ##      ##
###                                          ###
#####              settings             ########
###########                        #############
################              ##################

len_circles= 3

randome_mode = False # DANGER: BAGS

max_random_value_speed = 15

min_random_value_speed = 2

max_random_value_radius = 100

min_random_value_radius = 20

radiuses =[96, 45, 88]


speeds=[7, 9, 2]

fps = 30

screen_width, screen_height = 800, 800

line_depth = 1

################################################
### ######################################## ###
##    #############        ###############    ##
#          ########        ##########          #
             ####            ####
                ##          ##
                  #        #

# some combinations:
# [15,14,12] [3,99,14]
# [25,9,23] [3,99,14]
# [96, 45, 88] [7, 9, 2]

running = True
pygame.init()
pygame.display.set_caption('pendulum')

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


circles = []

class circle():
    def __init__(self, x=0 ,y = 0,speed=1,radius=70):
        self.radius = radius
        if not x:
            self.center_x = screen_width//2
            self.center_y= screen_height//2
        else:
            self.center_x = x
            self.center_y = y

        self.speed = speed

        self.pos_x = self.center_x - self.radius
        self.min_x = self.pos_x
        self.max_x = self.center_x + self.radius
        self.difference = -self.radius
        self.mode = 1
    def update(self):
        self.pos_x = self.center_x+self.difference
        self.min_x = self.center_x-self.radius
        self.max_x = self.center_x+self.radius
        if self.mode == 1:
            self.pos_y = ((self.radius ** 2) - (self.difference ** 2)) ** 0.5 +self.center_y
            pygame.draw.line(screen, (0, 255, 255), (self.center_x, self.center_y), (self.pos_x, self.pos_y))
        else:
            self.pos_y = self.center_y -( ((self.radius ** 2) - (self.difference) ** 2) ** 0.5)
            pygame.draw.line(screen, (0, 255, 255), (self.center_x,self.center_y), (self.pos_x, self.pos_y))
        if self.mode == 1:
            if self.pos_x +self.speed/2< self.max_x:                                   #<------------------------
                if self.max_x- self.difference-self.center_x <2*self.speed:            #| this shit was made for make traectory smoother
                    self.pos_x += self.speed/4                                         #| if u don`t want it delete 95th string and delete
                    self.difference += self.speed/4                                    #| "/2" and "/4" from strings 94,96,97 and repeat it all on strings 107-113
                else:
                    self.pos_x += self.speed
                    self.difference +=self.speed

            else:
                self.mode = 2
                # self.pos_x -= 2
        elif self.mode == 2:

            if self.pos_x-self.speed/2 > self.min_x:
                if self.max_x - self.difference - self.center_x < 2 * self.speed:
                    self.pos_x -= self.speed/4
                    self.difference -= self.speed/4
                else:
                    self.pos_x -= self.speed
                    self.difference -= self.speed
            else:
                self.mode = 1
                # self.pos_x += 2

if randome_mode:
    radiuses=[]
    speeds=[]

    speed = random.randint(min_random_value_speed, max_random_value_speed)
    radius = random.randint(min_random_value_radius, max_random_value_radius)
    speeds.append(speed)
    radiuses.append(radius)
    circle1 = circle(0,0,speed,radius)
    circles.append(circle1)
    circles[0].update()
else:
    circle1 = circle(0,0,speeds[0],radiuses[0])
    circles.append(circle1)
    circles[0].update()
for i in range(len_circles-1):
    x= circles[i].pos_x
    y= circles[i].pos_y
    if randome_mode:
        speed = random.randint(min_random_value_speed,max_random_value_speed)
        radius = random.randint(min_random_value_radius,max_random_value_radius)
        speeds.append(speed)
        radiuses.append(radius)
    else:
        speed = speeds[i+1]
        radius = radiuses[i+1]
    circle2 = circle(x,y,speed,radius)
    circles.append(circle2)
    circles[i+1].update()
if randome_mode:
    print("__________________your parameters___________________")
    print("speeds=",speeds)
    print("radiuses=",radiuses)
    print("you can save these parameters if you like picture")
    print("____________________________________________________")
points = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    circle1.update()
    for i in range(1,len(circles)):
        circles[i].center_x=circles[i-1].pos_x
        circles[i].center_y=circles[i-1].pos_y
        circles[i].update()
    points.append([circles[-1].pos_x, circles[-1].pos_y])
    for i in range(1,len(points)):
        pygame.draw.line(screen,(0,255,0),(points[i-1][0],points[i-1][1]),(points[i][0],points[i][1]),line_depth)
    pygame.display.update((0, 0, screen_width, screen_height))
    clock.tick(fps)
    pygame.display.set_caption(str(clock.get_fps()))