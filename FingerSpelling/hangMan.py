import pygame as pg
pg.init()
import letterCapture
#import pygetwindow as gw

import pyautogui
import time

def hangManGame():
    
    clock = pg.time.Clock()

    # use a (r, g, b) tuple for color
    yellow = (255, 255, 0)

    # create the basic window/screen and a title/caption
    # default is a black background
    screen = pg.display.set_mode((400, 200))
    pg.display.set_caption("Text adventures with Pygame")
    # pick a font you have and set its size
    myfont = pg.font.SysFont("Comic Sans MS", 30)
    # apply it to text on a label
    label = myfont.render("_ _ _ ",False, yellow)

    text = ""
    # event loop
    running = True
    while running:
        for event in pg.event.get():
            # exit conditions --> windows titlebar x click
            screen.fill(0)
            if event.type == pg.QUIT:
                running = False
            
            #print("Hangman Game")
            print(letterCapture.letterIndex)
            
            if letterCapture.letterIndex == "C":
                label = myfont.render("C _ _", False, yellow) 
            if letterCapture.letterIndex == "A":
                label = myfont.render("C A _", False, yellow) 
            if letterCapture.letterIndex == "R":
                label = myfont.render("C A R", False, yellow) 

            #if event.type == pg.KEYDOWN:
            #    if event.key == 99:
            #        label = myfont.render("C _ _ ", False, yellow)
            #    if event.key == 97:
            #        label = myfont.render("C A _ ", False, yellow)
            #    if event.key == 114:
            #        label = myfont.render("C A R ", False, yellow)
                    
            #if letterCapture.letterIndex == "C":
                #label = myfont.render("C _ _ ", False, yellow)
            #if letterCapture.letterIndex == "A":
                #label = myfont.render("C A _ ", False, yellow)
            #if letterCapture.letterIndex == "R":
                #label = myfont.render("C A R ", False, yellow)
            
        window_center = screen.get_rect().center
        screen.blit(label, label.get_rect(center = window_center))
        #pg.display.flip()
        pg.display.update()
        clock.tick(100)
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

    pg.quit()

