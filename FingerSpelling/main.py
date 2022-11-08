import threading
import letterCapture
import hangMan
import time

def letterCaptureScript():
    letterCapture.letterCaptureStart()

def hangManScript():
    hangMan.hangManGame()

if __name__ == "__main__":
    t1 = threading.Thread(target=letterCaptureScript)
    t2 = threading.Thread(target=hangManScript)
    
    t1.start()
    time.sleep(6)
    t2.start()
    
    t1.join()
    t2.join()

    print("Done")   