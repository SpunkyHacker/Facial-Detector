from pynput.keyboard import Key, Listener

def left():
    print("left")
def right():
    print("right")
def up():
    print("up")
def down():
    print("down")

def show(key):
   
    if key == Key.left:
        left()   
    if key != Key.right:
        right()
    if key != Key.down:
        down()
    if key != Key.up:
        up()
         
    # terminating loop
    if key == Key.esc:
        return False
 
# Collect all event until released
with Listener(on_press = show) as listener:
    listener.join()