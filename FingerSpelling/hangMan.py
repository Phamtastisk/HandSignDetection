import pygame as pg
pg.init()
import letterCapture
import random 

def hangManGame():
    letterCount = 0
    clock = pg.time.Clock()
    # use a (r, g, b) tuple for color
    yellow = (0, 0, 0)
    # create the basic window/screen and a title/caption
    # default is a black background
    screen = pg.display.set_mode((800, 800))
    pg.display.set_caption("Text adventures with Pygame")
    # pick a font you have and set its size
    myfont = pg.font.SysFont("Comic Sans MS", 30)

    wordsArr = ["Netto", "Pepsi", "Tesla"]

    selectedWord = random.choice(wordsArr)
    print(selectedWord)
    progress = ""
    picture_hint = pg.image.load(selectedWord + ".png")
    i = 0
    for i in range(len(selectedWord)):
        progress = progress + " _ "
        i = i+1    
    # apply it to text on a label
    label = myfont.render(progress,False, yellow)
    #Button picture
    new_wordPic = pg.image.load('btnNewWord.png')
    # event loop
    running = True
    while running:
        for event in pg.event.get():
            # exit conditions --> windows titlebar x click
            screen.fill((202,228,241))
            screen.blit(new_wordPic,(10,10))
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                match selectedWord:
                    case "Netto":
                        #print()
                        if letterCapture.letterIndex == "N" and letterCount == 0:
                            label = myfont.render("N _ _ _ _", False, yellow) 
                            letterCount = 1
                        if letterCapture.letterIndex == "E" and letterCount == 1:
                            label = myfont.render("N E _ _ _", False, yellow) 
                            letterCount = 2
                        if letterCapture.letterIndex == "T" and letterCount == 2:
                            label = myfont.render("N E T _ _", False, yellow)
                            letterCount = 3
                        if letterCapture.letterIndex == "T" and letterCount == 3:
                            label = myfont.render("N E T T _", False, yellow)
                            letterCount = 4
                        if letterCapture.letterIndex == "O"  and letterCount == 4:
                            label = myfont.render("N E T T O", False, yellow)
                            
                    case "Pepsi":
                        #print()
                        if letterCapture.letterIndex == "P" and letterCount == 0:
                            label = myfont.render("P _ _ _ _", False, yellow) 
                            letterCount = 1
                        if letterCapture.letterIndex == "E" and letterCount == 1:
                            label = myfont.render("P E _ _ _", False, yellow) 
                            letterCount = 2
                        if letterCapture.letterIndex == "P" and letterCount == 2:
                            label = myfont.render("P E P _ _", False, yellow)
                            letterCount = 3
                        if letterCapture.letterIndex == "S" and letterCount == 3:
                            label = myfont.render("P E P S _", False, yellow)
                            letterCount = 4
                        if letterCapture.letterIndex == "I"  and letterCount == 4:
                            label = myfont.render("P E P S I", False, yellow)
                            
                    case "Tesla":
                        #print()
                        if letterCapture.letterIndex == "T" and letterCount == 0:
                            label = myfont.render("T _ _ _ _", False, yellow) 
                            letterCount = 1
                        if letterCapture.letterIndex == "E" and letterCount == 1:
                            label = myfont.render("T E _ _ _", False, yellow) 
                            letterCount = 2
                        if letterCapture.letterIndex == "S" and letterCount == 2:
                            label = myfont.render("T E S _ _", False, yellow)
                            letterCount = 3
                        if letterCapture.letterIndex == "L" and letterCount == 3:
                            label = myfont.render("T E S L _", False, yellow)
                            letterCount = 4
                        if letterCapture.letterIndex == "A"  and letterCount == 4:
                            label = myfont.render("T E S L A", False, yellow)
                        
                    case _:
                        ""
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Clicked")
                x, y = event.pos
                #print("X ")
                #print(x)
                #print("Y")
                #print(y)
                if new_wordPic.get_rect().collidepoint(x, y):
                    print("Give me a new word!")

                    letterCount = 0
                    #Select a new random word
                    selectedWord = random.choice(wordsArr)
                    progress = ""
                    picture_hint = pg.image.load(selectedWord + ".png")
                    i = 0
                    for i in range(len(selectedWord)):
                        progress = progress + " _ "
                        i = i+1    
                    # apply it to text on a label
                    label = myfont.render(progress,False, yellow)

        window_center = screen.get_rect().center
        screen.blit(label, label.get_rect(center = window_center))
        screen.blit(picture_hint, (150, 10))
        pg.display.update()
        clock.tick(100)
    pg.quit()


        