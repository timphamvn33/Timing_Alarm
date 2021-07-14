import pygame
import time
import math
pygame.init()
screen =pygame.display.set_mode((500, 600))
pygame.display.set_caption("Countdown")
GREY = (169,169,169)
AQUA=(0,255,255)   
BLACK = (0, 0, 0)
RED = (255, 0, 0)
font=pygame.font.SysFont('sans', 50)
font1 = pygame.font.SysFont('sans', 100)     
b1= font.render('+', True, BLACK)
b2= font.render('-', True, BLACK)
b3= font.render('Min', True, BLACK)
b4= font.render('Sec', True, BLACK)
b5= font.render('Start', True, BLACK)
b6= font.render('Reset', True, BLACK)
clock = pygame.time.Clock()
mins =0
secs=0
total=0
total_secs=0
start=False
running = True
while running:
	clock.tick(60)
	screen.fill(GREY)
	mouse_x, mouse_y=pygame.mouse.get_pos()
	# draw the rects 
	pygame.draw.rect(screen, AQUA, (100, 50, 50, 50))
	pygame.draw.rect(screen, AQUA, (100, 130, 50, 50))
	pygame.draw.rect(screen, AQUA, (350, 50, 50, 50))
	pygame.draw.rect(screen, AQUA, (350, 130, 50, 50))
	pygame.draw.rect(screen, AQUA, (50, 200, 170, 50))
	pygame.draw.rect(screen, AQUA, (280, 200, 170, 50))
	pygame.draw.rect(screen, BLACK, (45, 495, 410, 60))
	pygame.draw.rect(screen, AQUA, (50, 500, 400, 50))
	# draw MIN
	screen.blit(b3, (10, 45))
	screen.blit(b3, (420, 45))
	#draw sec
	screen.blit(b4, (10, 125))
	screen.blit(b4, (420, 125))
	#draw plus
	screen.blit(b1, (110, 45))
	screen.blit(b1, (110, 125))
	#draw minus
	screen.blit(b2, (365, 45 ))
	screen.blit(b2, (365, 125))
	# draw Start, reset
	screen.blit(b5, (90, 200))
	screen.blit(b6, (300, 200))
	#draw circle
	pygame.draw.circle(screen, BLACK, (250, 380), 100)
	pygame.draw.circle(screen, AQUA, (250, 380), 98)
	pygame.draw.circle(screen, BLACK, (250, 380), 5)
 
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				if (100<mouse_x<150) and (50<mouse_y<100): # plus minutes
				   total_secs+=60 
				   total=total_secs
				if (100<mouse_x<150) and (130<mouse_y<180): #plus second
				   total_secs+=1
				   total=total_secs
				if (350<mouse_x<400) and (50<mouse_y<100): # minus minutes
				   total_secs-=60
				   total=total_secs  
				if (350<mouse_x<400) and (130<mouse_y<180): # minus seconds 
				   total_secs-=1
				   total=total_secs
				if (50<mouse_x<220) and (200<mouse_y<250): # start button
				   start=True
				   total=total_secs 
				if (280<mouse_x<450) and (200<mouse_y<250): #reset button
				   total_secs=0         

		#write again for start
		if start:
		  if total_secs>0:
		  	
		  	total_secs-=1
		  	time.sleep(1)
		  else:
		  	
		  	start=False

		#draw the current time
		mins=total_secs//60
		secs=total_secs-(mins*60)
		text_time=font1.render(str(mins)+ ':' + str(secs), True, RED)
		screen.blit(text_time, (180,50))
		#draw sec stick run
		x_sec=250+90*math.sin(6*secs*math.pi/180)
		y_sec=380-90*math.cos(6*secs*math.pi/180)
		pygame.draw.line(screen, RED, (250,380), (int(x_sec), int(y_sec)))
		#draw minute stick run
		x_min=250+50*math.sin(6*mins*math.pi/180)
		y_min=380-50*math.cos(6*mins*math.pi/180)
		pygame.draw.line(screen, BLACK, (250,380), (int(x_min), int(y_min)))

		#draw red rect  decline floowing the time
		if total!=0:
			pygame.draw.rect(screen, RED, (50, 500, int(400*(total_secs/total)), 50))
		pygame.display.flip()
pygame.quit()			