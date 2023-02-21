import pygame
import tkinter as tk
from tkinter import *
import os


root = tk.Tk()

embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left

buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)


root.update() # Required to prevent x-server error from preventing the code from running
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
# os.environ['SDL_VIDEODRIVER'] = 'windib' # <- This is for Windows support

screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color('white'))

pygame.display.init()
pygame.display.flip()


def draw():
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('black'), (250,250), 125)
    pygame.display.flip()

def clear():
    screen.fill(pygame.Color('white'))
    pygame.display.flip()

def write():
    screen.fill(pygame.Color('white'))
    pygame.font.init()
    text = entry1.get()
    font = pygame.font.SysFont('quicksandmedium',25, bold=1)
    displaytext = font.render(text, 1, pygame.Color('black'))
    screen.blit(displaytext, (250-displaytext.get_width()//2,250-displaytext.get_height()//2))
    pygame.display.flip()


# Controls to interact with PyGame window.
button1 = Button(buttonwin,text = 'Draw',  command=draw)
button1.pack(side=TOP)
button2 = Button(buttonwin,text = 'Clear', command=clear)
button2.pack(side=BOTTOM)
entry1 = Entry(buttonwin)
entry1.pack(side=BOTTOM)
button3 = Button(buttonwin,text = 'Write', command=write)
button3.pack(side=BOTTOM)

root.update()

while True:
    pygame.display.flip()
    root.update()