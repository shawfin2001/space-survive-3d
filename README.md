# Space Survive 3D 🚀

**Space Survive 3D** is a 3D space shooter game developed using Python and OpenGL. Control a spaceship, destroy incoming asteroids, collect power-ups, and survive as the difficulty increases.

## 🎮 Features

- **3D Graphics:** A space environment with stars, a distant planet, a moon, asteroids, and a detailed spaceship.
- **Spaceship Movement:** Move forward, backward, left, and right, and rotate to aim at targets.
- **Asteroid Combat:** Shoot asteroids, destroy them, and earn points. Larger asteroids require more hits and split into smaller asteroids when destroyed.
- **Multiple Levels:** The difficulty increases over time, with more asteroids appearing as you progress.
- **Power-Ups:** Collect shield, health, and rapid-fire power-ups to improve your chances of survival.
- **Bomb System:** Use bombs to destroy all asteroids currently in the arena.
- **Camera Modes:** Switch between first-person and third-person views.
- **Cheat Mode:** Enable automatic targeting and firing to help fight asteroids.
- **Game HUD:** Monitor your score, lives, level, bombs, and active status indicators.
- **Restart Option:** Start a new game after losing all your lives.

## 🛠️ Technologies Used

- **Python**
- **PyOpenGL** — OpenGL bindings for Python
- **OpenGL GLU** — Graphics utility functions
- **GLUT / FreeGLUT** — Window management and keyboard/mouse input

## 📋 Requirements

- Python 3
- PyOpenGL
- A working GLUT implementation, such as FreeGLUT
- A computer with graphics support for OpenGL

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/space-survive-3d.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd space-survive-3d
```

### 3. Install Python dependencies

```bash
python -m pip install PyOpenGL PyOpenGL_accelerate
```

Make sure a compatible GLUT or FreeGLUT runtime is installed and available on your system.

### 4. Run the game

```bash
python projectcse423.py
```

A game window should open, allowing you to control the spaceship and play.

## 🕹️ Controls

| Key / Input | Action |
|---|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Q` | Move left |
| `E` | Move right |
| Left Mouse Button | Shoot bullets |
| Right Mouse Button | Switch camera mode |
| `Spacebar` | Use a bomb |
| `C` | Toggle cheat mode |
| `R` | Restart the game |

**Camera adjustment:** Use the arrow keys to adjust the camera position.

## 🎯 Objective

Destroy asteroids to earn points, collect power-ups, and avoid collisions. Manage your lives and bombs carefully as the game becomes more challenging. Your goal is to survive for as long as possible while achieving the highest score you can.

## 📂 Project Structure

```text
space-survive-3d/
├── README.md
└── projectcse423.py
```

- `projectcse423.py` — Contains the game logic, rendering functions, controls, collision detection, power-ups, camera handling, and main game loop.
- `README.md` — Project overview, installation instructions, and gameplay documentation.

## 🚀 Future Improvements

- Add sound effects and background music.
- Introduce additional asteroid types and power-ups.
- Add a high-score leaderboard and persistent score storage.
- Improve visual effects, lighting, and textures.
- Add more game modes and difficulty settings.

## 👨‍💻 Author

Developed as a Python and OpenGL game project.

---

If you enjoyed this project, consider giving the repository a ⭐ on GitHub!
