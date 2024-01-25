import pyglet

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

window = pyglet.window.Window()
window.set_fullscreen(True)

label = pyglet.text.Label('Hello, world',
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center',
                          color = ALLY_COLOR
                        )
label2 = pyglet.text.Label('Hello, world',
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x=window.width//2, y=window.height//2,
                          height = -36,
                          anchor_x='center', anchor_y='center',
                          color = ENEMY_COLOR
                        )

ball = pyglet.shapes.Circle(100,100,3,color=ALLY_COLOR)


@window.event
def on_draw():
    window.clear()
    label.draw()
    label2.draw()
    ball.draw()

def update(dt):
    label2.x = label2.x + 1
    label2.draw()

def cc(dt):
    if label2.color == ENEMY_COLOR :
        label2.color = ALLY_COLOR
    else :
        label2.color = ENEMY_COLOR
    label2.draw()

pyglet.clock.schedule_interval(update, 1/60)
pyglet.clock.schedule_interval(cc, 1.0)
pyglet.app.run()
