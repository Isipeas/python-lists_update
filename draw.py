import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def draw_circle(canvas):
    canvas.draw_circle([20, 10], 40, 12, 'Green')
    canvas.draw_circle([10, 10], 30, 12, 'Red')
    canvas.draw_circle([30, 20], 20, 5, 'Blue', 'White')
    canvas.draw_circle([40, 40], 80, 10, 'Yellow', 'Orange')

frame = simplegui.create_frame('Draw on Canvas', 400,400)
frame.set_draw_handler(draw_circle)
frame.start()


