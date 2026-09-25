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
