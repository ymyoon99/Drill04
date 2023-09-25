from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

run = load_image('char_run.png')
idle = load_image('char_idle.png')

def handle_events():

close_canvas()