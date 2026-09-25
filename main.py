import tkinter as tk
import math
import random

# Global dimensions (will be dynamically updated to fit your screen)
W = 1280
H = 720
cinematic_y = 70
ch = 580
gy = 570
by = 570
girl_x = 900
boy_x = -100

STATE_WAIT = 0
STATE_WALK = 1
STATE_KNEEL = 2
STATE_HUG = 3
STATE_LOVE = 4

current_state = STATE_WAIT
timer = 0

clouds = []
leaves = []
dialogues = []
hearts = []
birds = []
boy_skeleton_ids = {}

def init_dimensions():
    global W, H, cinematic_y, ch, gy, by, girl_x
    root.update_idletasks()
    
    w_curr = canvas.winfo_width()
    h_curr = canvas.winfo_height()
    
    if w_curr > 100:
        W = w_curr
        H = h_curr
        
    cinematic_y = H * 0.1
    ch = H * 0.8
    gy = cinematic_y + ch - (H * 0.12)
    by = gy
    girl_x = W * 0.75

def create_scene():
    canvas.create_rectangle(0, cinematic_y, W*2, cinematic_y+ch, fill="#87CEEB", outline="")

    # Sun & Glow
    canvas.create_oval(W*0.15, cinematic_y+50, W*0.15+150, cinematic_y+200, fill="#FFC107", outline="#FFEB3B", width=4)
    canvas.create_oval(W*0.15-20, cinematic_y+30, W*0.15+170, cinematic_y+220, fill="", outline="#FFF9C4", width=12, stipple="gray50")

    # Mountains
    canvas.create_polygon(-100, gy, W*0.2, gy-150, W*0.45, gy, fill="#81C784", outline="", smooth=True)
    canvas.create_polygon(W*0.3, gy, W*0.55, gy-180, W*0.8, gy, fill="#66BB6A", outline="", smooth=True)
    canvas.create_polygon(W*0.6, gy, W*0.85, gy-120, W*1.5, gy, fill="#4CAF50", outline="", smooth=True)

    # Clouds
    for _ in range(8):
        cx, cy = random.randint(0, int(W)), random.randint(int(cinematic_y+20), int(cinematic_y+150))
        cw, ch_c = random.randint(80, 150), random.randint(40, 70)
        c1 = canvas.create_oval(cx, cy, cx+cw, cy+ch_c, fill="#FFFFFF", outline="")
        c2 = canvas.create_oval(cx+cw*0.3, cy-ch_c*0.4, cx+cw*0.8, cy+ch_c*0.7, fill="#FFFFFF", outline="")
        clouds.extend([c1, c2])

    # Birds
    for _ in range(6):
        bx, b_y = random.randint(0, int(W)), random.randint(int(cinematic_y+50), int(cinematic_y+180))
        bird = canvas.create_text(bx, b_y, text="v", font=("Helvetica", 12, "bold"), fill="#2C3E50")
        birds.append([bird, random.uniform(1.2, 2.0)])

    # Ground & Grass
    canvas.create_rectangle(0, gy, W*2, H*2, fill="#558B2F", outline="")
    canvas.create_rectangle(0, gy+30, W*2, H*2, fill="#33691E", outline="")

    for _ in range(60):
        fx, fy = random.randint(0, int(W)), random.randint(int(gy+10), int(cinematic_y+ch-10))
        canvas.create_oval(fx, fy, fx+6, fy+6, fill=random.choice(["#E91E63", "#9C27B0", "#FFFFFF", "#FFEB3B", "#FF9800"]), outline="")

    # Eiffel Tower
    ex = W * 0.25
    canvas.create_polygon(ex-70, gy, ex-35, gy, ex-25, gy-70, ex-50, gy-70, fill="#2C3E50", outline="#1A252F", width=2)
    canvas.create_polygon(ex+70, gy, ex+35, gy, ex+25, gy-70, ex+50, gy-70, fill="#2C3E50", outline="#1A252F", width=2)
    canvas.create_arc(ex-40, gy-35, ex+40, gy+35, start=0, extent=180, style=tk.ARC, outline="#1A252F", width=6)
    canvas.create_rectangle(ex-55, gy-70, ex+55, gy-80, fill="#111111")
    canvas.create_polygon(ex-45, gy-80, ex+45, gy-80, ex+25, gy-180, ex-25, gy-180, fill="#2C3E50", outline="#1A252F", width=2)
    canvas.create_line(ex-40, gy-80, ex+25, gy-180, fill="#1A252F", width=2)
    canvas.create_line(ex+40, gy-80, ex-25, gy-180, fill="#1A252F", width=2)
    canvas.create_line(ex-35, gy-130, ex+35, gy-130, fill="#1A252F", width=3)
    canvas.create_rectangle(ex-35, gy-180, ex+35, gy-188, fill="#111111")
    canvas.create_polygon(ex-20, gy-188, ex+20, gy-188, ex+5, gy-320, ex-5, gy-320, fill="#2C3E50", outline="#1A252F", width=2)
    canvas.create_line(ex-20, gy-188, ex+5, gy-320, fill="#1A252F", width=2)
    canvas.create_line(ex+20, gy-188, ex-5, gy-320, fill="#1A252F", width=2)
    canvas.create_rectangle(ex-10, gy-320, ex+10, gy-328, fill="#111111")
    canvas.create_line(ex, gy-328, ex, gy-380, fill="#1A252F", width=4)

    # Spring Tree
    tx = W * 0.85
    canvas.create_polygon(tx-30, gy, tx+30, gy, tx+15, gy-320, tx-15, gy-320, fill="#4E342E", smooth=True)
    canvas.create_line(tx-15, gy, tx-8, gy-320, fill="#3E2723", width=3)
    canvas.create_line(tx+10, gy, tx+5, gy-320, fill="#3E2723", width=3)
    canvas.create_polygon(tx-8, gy-180, tx-80, gy-290, tx-70, gy-300, tx, gy-200, fill="#4E342E")
    canvas.create_polygon(tx+8, gy-150, tx+90, gy-260, tx+80, gy-270, tx, gy-170, fill="#4E342E")

    colors = ["#E67E22", "#D35400", "#E74C3C", "#F39C12", "#CA6F1E", "#FF5722"]
    for _ in range(90):
        cx = random.randint(int(tx-140), int(tx+140))
        cy = random.randint(int(gy-380), int(gy-220))
        r = random.randint(25, 55)
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=random.choice(colors), outline="")

    # Girl (Neeharika)
    global g_frock_back, g_frock_front, g_hair_back, g_hair_front
    global g_arm_l, g_sleeve_l, g_hand_l, g_shadow

    g_shadow = canvas.create_oval(girl_x-35, gy-8, girl_x+35, gy+8, fill="#33691E", outline="")
    
    canvas.create_oval(girl_x-16, gy-10, girl_x-2, gy+2, fill="#880E4F")
    canvas.create_oval(girl_x+2, gy-10, girl_x+16, gy+2, fill="#880E4F")
    canvas.create_line(girl_x-9, gy-40, girl_x-9, gy-5, width=6, fill="#FFD180")
    canvas.create_line(girl_x+9, gy-40, girl_x+9, gy-5, width=6, fill="#FFD180")
    
    g_hair_back = canvas.create_polygon(girl_x-20, gy-140, girl_x+20, gy-140, girl_x+30, gy-60, girl_x-30, gy-60, fill="#3E2723", smooth=True)
    g_frock_back = canvas.create_polygon(girl_x-15, gy-70, girl_x+15, gy-70, girl_x+40, gy-15, girl_x-40, gy-15, fill="#C2185B", smooth=True)
    g_frock_front = canvas.create_polygon(girl_x-15, gy-70, girl_x+15, gy-70, girl_x+30, gy-20, girl_x-30, gy-20, fill="#F06292", smooth=True)
    
    canvas.create_polygon(girl_x-13, gy-110, girl_x+13, gy-110, girl_x+15, gy-70, girl_x-15, gy-70, fill="#E91E63")
    canvas.create_rectangle(girl_x-14, gy-73, girl_x+14, gy-67, fill="#FCE4EC", outline="")
    canvas.create_rectangle(girl_x-4, gy-120, girl_x+4, gy-110, fill="#FFD180", outline="")
    canvas.create_oval(girl_x-16, gy-145, girl_x+16, gy-110, fill="#FFD180", outline="")
    
    g_hair_front = canvas.create_polygon(girl_x-17, gy-147, girl_x+17, gy-147, girl_x+22, gy-125, girl_x-22, gy-125, fill="#271510", smooth=True)
    
    g_arm_l = canvas.create_line(girl_x, gy-105, girl_x-15, gy-60, width=6, fill="#FFD180", capstyle=tk.ROUND)
    g_sleeve_l = canvas.create_line(girl_x, gy-105, girl_x-8, gy-85, width=8, fill="#E91E63", capstyle=tk.ROUND)
    g_hand_l = canvas.create_oval(girl_x-20, gy-63, girl_x-10, gy-53, fill="#FFD180", outline="")

    for _ in range(25):
        spawn_leaf()

def draw_cinematic_bars():
    # Cinematic black bars overlay to force a perfect 16:9 widescreen movie look
    canvas.create_rectangle(0, 0, W*2, cinematic_y, fill="#000000", outline="")
    canvas.create_rectangle(0, cinematic_y+ch, W*2, H*2, fill="#000000", outline="")

def draw_boy_skeleton():
    global boy_skeleton_ids
    x, y = boy_x, by
    boy_skeleton_ids['shadow'] = canvas.create_oval(x-35, y-8, x+35, y+8, fill="#33691E", outline="")
    boy_skeleton_ids['head'] = canvas.create_oval(x-14, y-140, x+14, y-110, fill="#FFD180", outline="")
    boy_skeleton_ids['hair'] = canvas.create_polygon(x-16, y-142, x+16, y-142, x+18, y-125, x-18, y-125, x-18, y-135, fill="#111111", smooth=True)
    boy_skeleton_ids['neck'] = canvas.create_rectangle(x-5, y-115, x+5, y-105, fill="#FFD180", outline="")
    boy_skeleton_ids['shirt'] = canvas.create_polygon(x-5, y-105, x+5, y-105, x+3, y-45, x-3, y-45, fill="#ECF0F1")
    boy_skeleton_ids['jacket'] = canvas.create_polygon(x-16, y-105, x+16, y-105, x+14, y-45, x-14, y-45, fill="#2980B9")
    boy_skeleton_ids['leg_l'] = canvas.create_line(x-6, y-45, x-6, y-5, width=12, fill="#2C3E50", capstyle=tk.ROUND)
    boy_skeleton_ids['leg_r'] = canvas.create_line(x+6, y-45, x+6, y-5, width=12, fill="#2C3E50", capstyle=tk.ROUND)
    boy_skeleton_ids['shoe_l'] = canvas.create_oval(x-14, y-12, x+2, y, fill="#212F3D")
    boy_skeleton_ids['shoe_r'] = canvas.create_oval(x-2, y-12, x+14, y, fill="#212F3D")
    boy_skeleton_ids['arm_l'] = canvas.create_line(x-16, y-100, x-16, y-50, width=10, fill="#2980B9", capstyle=tk.ROUND)
    boy_skeleton_ids['arm_r'] = canvas.create_line(x+16, y-100, x+16, y-50, width=10, fill="#2980B9", capstyle=tk.ROUND)
    boy_skeleton_ids['hand_l'] = canvas.create_oval(x-21, y-58, x-11, y-48, fill="#FFD180", outline="")
    boy_skeleton_ids['hand_r'] = canvas.create_oval(x+11, y-58, x+21, y-48, fill="#FFD180", outline="")
    boy_skeleton_ids['box'] = canvas.create_rectangle(x, y, x, y, fill="#C0392B", outline="#922B21", state="hidden")
    boy_skeleton_ids['diamond'] = canvas.create_polygon(0, 0, 0, 0, fill="#E0F7FA", outline="#00BCD4", state="hidden")

def update_boy_skeleton(new_x, new_y, state_anim, frame_timer):
    x, y = new_x, new_y
    canvas.coords(boy_skeleton_ids['shadow'], x-35, y-8, x+35, y+8)
    h_y = y - 125
    canvas.coords(boy_skeleton_ids['head'], x-14, h_y-15, x+14, h_y+15)
    canvas.coords(boy_skeleton_ids['hair'], x-16, h_y-17, x+16, h_y-17, x+18, h_y, x-18, h_y, x-18, h_y-10)
    canvas.coords(boy_skeleton_ids['neck'], x-5, y-115, x+5, y-105)
    canvas.coords(boy_skeleton_ids['shirt'], x-5, y-105, x+5, y-105, x+3, y-45, x-3, y-45)
    canvas.coords(boy_skeleton_ids['jacket'], x-16, y-105, x+16, y-105, x+14, y-45, x-14, y-45)
    
    stride, arm_swing = 0, 0
    if state_anim == STATE_WALK:
        stride = math.sin(frame_timer * 0.4) * 20
        arm_swing = math.sin(frame_timer * 0.4) * 15
        canvas.coords(boy_skeleton_ids['leg_l'], x-6, y-45, x-6+stride, y-5)
        canvas.coords(boy_skeleton_ids['shoe_l'], x-6+stride-8, y-10, x-6+stride+8, y+2)
        canvas.coords(boy_skeleton_ids['leg_r'], x+6, y-45, x+6-stride, y-5)
        canvas.coords(boy_skeleton_ids['shoe_r'], x+6-stride-8, y-10, x+6-stride+8, y+2)
        canvas.coords(boy_skeleton_ids['arm_l'], x-16, y-100, x-16-arm_swing, y-55)
        canvas.coords(boy_skeleton_ids['hand_l'], x-16-arm_swing-5, y-60, x-16-arm_swing+5, y-50)
        canvas.coords(boy_skeleton_ids['arm_r'], x+16, y-100, x+16+arm_swing, y-55)
        canvas.coords(boy_skeleton_ids['hand_r'], x+16+arm_swing-5, y-60, x+16+arm_swing+5, y-50)
        canvas.itemconfig(boy_skeleton_ids['box'], state="hidden")
        canvas.itemconfig(boy_skeleton_ids['diamond'], state="hidden")
    elif state_anim == STATE_KNEEL:
        canvas.coords(boy_skeleton_ids['leg_l'], x-6, y-45, x+20, y-45, x+20, y-5)
        canvas.coords(boy_skeleton_ids['shoe_l'], x+12, y-10, x+28, y+2)
        canvas.coords(boy_skeleton_ids['leg_r'], x+6, y-45, x-15, y-5, x-35, y-5)
        canvas.coords(boy_skeleton_ids['shoe_r'], x-43, y-10, x-27, y+2)
        
        canvas.coords(boy_skeleton_ids['arm_l'], x-16, y-100, x-10, y-60)
        canvas.coords(boy_skeleton_ids['hand_l'], x-15, y-65, x-5, y-55)
        
        canvas.coords(boy_skeleton_ids['arm_r'], x+16, y-100, x+30, y-85, x+45, y-100)
        canvas.coords(boy_skeleton_ids['hand_r'], x+40, y-105, x+50, y-95)
        
        canvas.coords(boy_skeleton_ids['box'], x+42, y-103, x+50, y-95)
        canvas.coords(boy_skeleton_ids['diamond'], x+44, y-103, x+48, y-103, x+46, y-108)
        canvas.itemconfig(boy_skeleton_ids['box'], state="normal")
        canvas.itemconfig(boy_skeleton_ids['diamond'], state="normal")
    elif state_anim == STATE_HUG or state_anim == STATE_LOVE:
        canvas.coords(boy_skeleton_ids['leg_l'], x-6, y-45, x-6, y-5)
        canvas.coords(boy_skeleton_ids['shoe_l'], x-14, y-12, x+2, y)
        canvas.coords(boy_skeleton_ids['leg_r'], x+6, y-45, x+6, y-5)
        canvas.coords(boy_skeleton_ids['shoe_r'], x-2, y-12, x+14, y)
        
        canvas.coords(boy_skeleton_ids['arm_l'], x-16, y-100, x+5, y-90)
        canvas.coords(boy_skeleton_ids['hand_l'], x, y-95, x+10, y-85)
        canvas.coords(boy_skeleton_ids['arm_r'], x+16, y-100, x+30, y-80, x+5, y-70)
        canvas.coords(boy_skeleton_ids['hand_r'], x, y-75, x+10, y-65)
        canvas.itemconfig(boy_skeleton_ids['box'], state="hidden")
        canvas.itemconfig(boy_skeleton_ids['diamond'], state="hidden")
    else: 
        canvas.coords(boy_skeleton_ids['leg_l'], x-6, y-45, x-6, y-5)
        canvas.coords(boy_skeleton_ids['shoe_l'], x-14, y-12, x+2, y)
        canvas.coords(boy_skeleton_ids['leg_r'], x+6, y-45, x+6, y-5)
        canvas.coords(boy_skeleton_ids['shoe_r'], x-2, y-12, x+14, y)
        canvas.coords(boy_skeleton_ids['arm_l'], x-16, y-100, x-16, y-55)
        canvas.coords(boy_skeleton_ids['hand_l'], x-21, y-60, x-11, y-50)
        canvas.coords(boy_skeleton_ids['arm_r'], x+16, y-100, x+16, y-55)
        canvas.coords(boy_skeleton_ids['hand_r'], x+11, y-60, x+21, y-50)
        canvas.itemconfig(boy_skeleton_ids['box'], state="hidden")
        canvas.itemconfig(boy_skeleton_ids['diamond'], state="hidden")

def spawn_leaf():
    x = random.randint(int(W*0.6), int(W*0.95))
    y = random.randint(int(gy-350), int(gy-150))
    leaf = canvas.create_polygon(x, y, x+9, y+4, x+13, y, x+6, y-6, fill=random.choice(["#E67E22", "#D35400", "#F1C40F"]), outline="", smooth=True)
    leaves.append([leaf, random.uniform(-4, -1.8), random.uniform(2.0, 4.0)])

def spawn_dialogue(x, y, text, size=11):
    txt = canvas.create_text(x, y, text=text, font=("Helvetica", size, "bold"), fill="#E91E63")
    root.update_idletasks()
    bbox = canvas.bbox(txt)
    bubble = canvas.create_oval(bbox[0]-15, bbox[1]-10, bbox[2]+15, bbox[3]+10, fill="#FFFFFF", outline="#F48FB1", width=3)
    canvas.tag_lower(bubble, txt)
    dialogues.append([bubble, txt, 160])

def spawn_heart(x, y):
    h = canvas.create_text(x, y, text="❤", font=("Helvetica", 18), fill="#E91E63")
    hearts.append([h, 80])

def animate():
    global current_state, timer, boy_x
    timer += 1

    for c in clouds:
        canvas.move(c, 0.4, 0)
        if canvas.coords(c)[0] > W:
            canvas.move(c, -W-200, 0)
            
    for b in birds:
        wing_flap = math.sin(timer * 0.4) * 2
        canvas.move(b[0], 1.5, wing_flap)
        if canvas.coords(b[0])[0] > W:
            canvas.coords(b[0], -50, random.randint(int(cinematic_y+50), int(cinematic_y+150)))

    for l in leaves:
        canvas.move(l[0], l[1], l[2])
        coords = canvas.coords(l[0])
        if coords and (coords[1] > gy or coords[0] < -10):
            canvas.delete(l[0])
            leaves.remove(l)
            spawn_leaf()

    wave = math.sin(timer * 0.15) * 12
    canvas.coords(g_frock_front, girl_x-15, gy-70, girl_x+15, gy-70, girl_x+30+wave, gy-20, girl_x-30+wave, gy-20)
    canvas.coords(g_frock_back, girl_x-15, gy-70, girl_x+15, gy-70, girl_x+40+wave, gy-15, girl_x-40+wave, gy-15)
    canvas.coords(g_hair_back, girl_x-20, gy-140, girl_x+20, gy-140, girl_x+30+wave, gy-60, girl_x-30+wave, gy-60)

    for d in reversed(dialogues):
        d[2] -= 1
        if d[2] <= 0:
            canvas.delete(d[0])
            canvas.delete(d[1])
            dialogues.remove(d)

    for h in reversed(hearts):
        canvas.move(h[0], 0, -2.5)
        h[1] -= 1
        if h[1] <= 0:
            canvas.delete(h[0])
            hearts.remove(h)

    if current_state == STATE_WAIT:
        update_boy_skeleton(boy_x, by, STATE_WAIT, 0)
        if timer > 60:
            current_state = STATE_WALK
            timer = 0

    elif current_state == STATE_WALK:
        boy_x += 3
        update_boy_skeleton(boy_x, by, STATE_WALK, timer)
        if boy_x >= girl_x - 90:
            current_state = STATE_KNEEL
            timer = 0

    elif current_state == STATE_KNEEL:
        if timer < 10:
            drop = 30 * (timer / 10)
            update_boy_skeleton(boy_x, by+drop, STATE_WAIT, 0)
        elif timer == 10:
            update_boy_skeleton(boy_x, by+30, STATE_KNEEL, 0)
            spawn_dialogue(W*0.5, cinematic_y+1000, "Happy Birthday", size=11)
        else:
            update_boy_skeleton(boy_x, by+30, STATE_KNEEL, 0)

        if timer > 160:
            current_state = STATE_HUG
            timer = 0

    elif current_state == STATE_HUG:
        if timer < 10:
            update_boy_skeleton(boy_x, by+30, STATE_WAIT, 0)
            boy_x += 2.5
        elif timer < 20:
            drop = 30 - 30 * ((timer-10) / 10)
            update_boy_skeleton(boy_x, by+drop, STATE_WAIT, 0)
            boy_x += 2
        else:
            update_boy_skeleton(boy_x, by, STATE_HUG, 0)
            canvas.coords(g_arm_l, girl_x, gy-105, boy_x-10, gy-100)
            canvas.coords(g_sleeve_l, girl_x, gy-105, boy_x-5, gy-100)
            canvas.coords(g_hand_l, boy_x-15, gy-105, boy_x-5, gy-95)

        if timer > 60:
            current_state = STATE_LOVE
            timer = 0

    elif current_state == STATE_LOVE:
        update_boy_skeleton(boy_x, by, STATE_LOVE, 0)
        if timer == 1:
            spawn_dialogue(boy_x - 70, by - 160, "I love you", size=6)
            spawn_dialogue(girl_x + 70, gy - 160, "Love you too", size=6)
            
        if timer % 12 == 0:
            spawn_heart(girl_x - 15, gy-180)
            
        if timer > 180:
            timer = 0

    root.after(30, animate)

root = tk.Tk()
root.title("Happy Birthday")
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg="#000000", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Correct initialization sequence
init_dimensions()
create_scene()
draw_boy_skeleton()
draw_cinematic_bars()  
update_boy_skeleton(boy_x, by, STATE_WAIT, 0)

root.after(500, animate)
root.mainloop()
