from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024 # TUK_GROUND.png의 크기
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

run = load_image('char_run.png')
idle = load_image('char_idle.png')

def handle_events():
    global running, x, y, dir, dir2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                is_idle = False
            elif event.key == SDLK_LEFT:
                dir -= 1
                is_idle = False
            elif event.key == SDLK_UP:
                dir2 += 1
                is_idle = False
            elif event.key == SDLK_DOWN:
                dir2 -= 1
                is_idle = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1

running = True
is_idle = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2 # 캐릭터는 맵 중앙에 생성
frame = 0
dir = 0 # dir이 0일때 정지
dir2 = 0

while running:
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dir != 0 or dir2 != 0:  # run 상태
        is_idle = False
        run.clip_draw(frame * 120, 0, 100, 100, x, y, 200, 200)
    else:  # idle 상태
        is_idle = True
        idle.clip_draw(frame * 120, 0, 100, 100, x, y, 200, 200)

    if x < 0: # x축 아래로 이동하려 할 때 0이 유지되도록 함
        x = 0
    elif x > TUK_WIDTH: # x축 위로 이동하려 할 때 TUK_WIDT이 유지되도록 함
        x = TUK_WIDTH
    if y < 0: # y축 아래로 이동하려 할 때 0이 유지되도록 함
        y = 0
    elif y > TUK_HEIGHT: # x축 아래로 이동하려 할 때 TUK_HEIGHT이 유지되도록 함
        y = TUK_HEIGHT


    update_canvas()
    handle_events()
    frame = (frame + 1) % 10 # 캐릭터 애니메이션 이미지가 10장
    x += dir * 5 # 5씩 이동
    y += dir2 * 5 # 5씩 이동
    delay(0.05)

close_canvas()