import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def key_handler(key):
    print (key)
    if simplegui.KEY_MAP['up'] == key:
        print("Du hast Up geklickt !")

    if simplegui.KEY_MAP['up'] == key:
        print("B geklickt du hast")

frame = simplegui.create_frame('Keyboard handling', 100, 100)
frame.set_keydown_handler(key_handler)
frame.start()