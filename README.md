# Cinematic Tkinter Birthday Animation 🎬🎂

A beautiful, full-screen 2D animated scene built entirely from scratch using Python's standard `tkinter` library. No external game engines or heavy graphics libraries are required. 

This project demonstrates how to use the Tkinter Canvas to create procedural environments, custom skeletal animations, and state-machine-based storytelling.

## ✨ Features

* **Cinematic Widescreen:** Automatically scales to fit your screen with forced 16:9 cinematic letterboxing.
* **Procedural Environment:** Clouds, birds, and falling autumn leaves are generated and animated dynamically using mathematical functions (`math.sin` for natural wave motions).
* **Custom Skeletal Animation:** The character animations (walking, kneeling, hugging) are achieved by updating coordinates of vector-based "bones" and shapes frame-by-frame.
* **Particle System:** Floating heart particles and fading dialogue bubbles.
* **State Machine Logic:** The scene flows through multiple distinct states seamlessly (`WAIT` -> `WALK` -> `KNEEL` -> `HUG` -> `LOVE`).

## 🚀 Getting Started

### Prerequisites
All you need is Python 3 installed on your system. The project uses standard libraries exclusively:
* `tkinter` (Usually comes pre-installed with Python)
* `math`
* `random`

### Running the Animation
1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/tkinter-cinematic-birthday.git](https://github.com/yourusername/tkinter-cinematic-birthday.git)

2. Navigate to the project directory:
   ```bash
   cd tkinter-cinematic-birthday

3. Run the script:
   ```bash
   python main.py
   
Note on Exiting: The animation runs in borderless full-screen mode. To exit the application, press Alt + F4 (Windows/Linux) or Cmd + Q (Mac).

### 🛠️ Customization Guide
You can easily modify the source code to personalize the animation for someone else:
Change the Text: Look for the spawn_dialogue calls in the STATE_KNEEL and STATE_LOVE blocks to change "Happy Birthday" or "I love you".
Adjust Colors: The environment colors (sky, grass, characters) are defined via standard hex codes (e.g., #87CEEB for the sky).
Modify Timing: The pacing of the animation is controlled by the timer variable thresholds in the animate() function.

### 🎨 Make It Your Own
Want to surprise someone? You can easily tweak the code to make it personal:
The Message: Search the code for "Happy Birthday" and "I love you" to change what the characters say.
The Colors: Change the girl's dress or the boy's jacket by tweaking the hex codes (e.g., #F06292 for pink).
The Scenery: Adjust the spawn_leaf or spawn_heart functions to change how the particles behave.

### 📂 Code Architecture overview
create_scene(): Renders the static/procedural background elements (mountains, Eiffel tower, trees).
draw_boy_skeleton() & update_boy_skeleton(): Handles the coordinate math for character joints during different states.
animate(): The core game loop running at ~30 FPS via Tkinter's .after() method, handling particle cleanup and state transitions.

### 👨‍💻 AUTHOR
Anurag Bora
GitHub: @anuragsbora

