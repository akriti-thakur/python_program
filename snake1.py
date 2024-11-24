import time
import  pygame
import math
import random as random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue=(0,0,255) 
red=(255,0,0)
green = (0, 255, 0)
dis_height=600
dis_width=600

dis=pygame.display.set_mode((dis_height,dis_width))
pygame.display.set_caption("snake game")



block=10
clock=pygame.time.Clock()

font= pygame.font.SysFont(None,40)
def messege(msg,color):
    messe= font.render(msg,True,color)
    dis.blit(messe,[dis_width/2,dis_height/2])
    
def oursnake(block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],block,block])
    
    
def game():
    game_over=False
    game_close= False
    
    x1= dis_width/2
    y1=dis_height/2
    x1_change=0
    y1_change=0
    snake_List = []
    Length_of_snake = 1
    
    foodx=round(random.randrange(0,dis_width-block)/10.0)*10.0
    foody = round(random.randrange(0, dis_width - block) / 10.0)*10.0
    

    while game_over != True:
        while game_close== True:
          
            messege('''you lost! press 
                    Q to quit or c 
                    to play again''',red)
            pygame.display.update()
            
            
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                        
                    if event.key== pygame.K_c:
                        game()
        for event in pygame.event.get():
            print(event)
            if event.type== pygame.QUIT:
                game_over=True
        
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-block
                    y1_change=0
                if event.key==pygame.K_RIGHT:
                    x1_change=block
                    y1_change=0
                if event.key==pygame.K_UP:
                    y1_change=-block
                    x1_change=0
                if event.key==pygame.K_DOWN:
                    y1_change=block
                    x1_change=0
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
        # mouse_x,mouse_y=pygame.mouse.get_pos()
        # angle= math.atan2(mouse_y-y1,mouse_x-x1)
        
        # x1_change=speed* math.cos(angle)
        # y1_change=speed* math.sin(angle)
        if x1 >=dis_width or x1 <0 or y1>= dis_height or y1<0 :
            game_over=True 
        x1 +=x1_change
        y1 += y1_change       
        dis.fill(blue) 
        
        pygame.draw.circle(dis,green,[foodx,foody],block) 
        head=[]
        head.append(x1)
        head.append(y1)
        snake_List.append(head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x== head:
                game_close= True
                
        oursnake(block,snake_List)
  
            

        pygame.display.update()
    
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-block)/10.0)*10.0
            foody = round(random.randrange(0, dis_width - block) / 10.0)*10.0
            print("yummmm")
            Length_of_snake +=1
        clock.tick(10)

    messege("You lost",red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


game()