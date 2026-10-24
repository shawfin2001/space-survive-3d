from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# ============================================================
# CAMERA
# ============================================================

camera_pos = (0, 650, 600)

fovY = 120
GRID_LENGTH = 1000
WORLD_LIMIT = 900


# ============================================================
# GAME VARIABLES
# ============================================================

# ---------------- PLAYER ----------------

player_x = 0
player_y = 0
player_z = 25

player_speed = 6

# Direction vector of spaceship
# Initially facing +Y direction
player_dx = 0.0
player_dy = 1.0

# Visual rotation angle
player_angle = 0


# ---------------- GAME ----------------

score = 0
lives = 3
bombs = 0
level = 1

game_over = False


# ---------------- CHEAT ----------------

cheat_mode = False


# ---------------- CAMERA ----------------

# 0 = Third person
# 1 = First person

camera_mode = 0


# ============================================================
# BULLETS
# ============================================================

# [x, y, z, dx, dy]

bullets = []


# ============================================================
# ASTEROIDS
# ============================================================

# [x, y, z, size, speed, health, type, rotation]

asteroids = []


# ============================================================
# POWER UPS
# ============================================================

# [x, y, z, type, rotation]

powerups = []


# ============================================================
# EXPLOSIONS
# ============================================================

# [x, y, z, size, life]

explosions = []

bomb_effect = 0


# ============================================================
# PLAYER STATUS
# ============================================================

shield_active = False
shield_timer = 0


rapid_fire = False
rapid_fire_timer = 0
triple_fire = False
triple_fire_timer = 0

flash_timer = 0


# ============================================================
# GAME COUNTERS
# ============================================================

frame_count = 0

spawn_counter = 0
powerup_counter = 0


# ============================================================
# OPENGL QUADRIC
# ============================================================

quadric = None


# ============================================================
# RANDOM NUMBER SYSTEM
# ============================================================

random_seed = 423


def pseudo_random():

    global random_seed

    random_seed = (random_seed * 37 + 17) % 10000

    return random_seed / 10000.0


# ============================================================
# TEXT
# ============================================================

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):

    glColor3f(1, 1, 1)

    glMatrixMode(GL_PROJECTION)

    glPushMatrix()

    glLoadIdentity()

    gluOrtho2D(
        0,
        1000,
        0,
        800
    )

    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()

    glLoadIdentity()

    glRasterPos2f(x, y)

    for ch in text:

        glutBitmapCharacter(
            font,
            ord(ch)
        )

    glPopMatrix()

    glMatrixMode(GL_PROJECTION)

    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)


# ============================================================
# SPACESHIP
# ============================================================

def render_player():

    global player_x
    global player_y
    global player_z
    global player_angle

    glPushMatrix()

    # ========================================================
    # POSITION + ROTATION
    # ========================================================

    glTranslatef(
        player_x,
        player_y,
        player_z
    )

    glRotatef(
        player_angle,
        0,
        0,
        1
    )


    # ========================================================
    # MAIN CENTRAL BODY
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.75,
        0.90,
        1.00
    )

    glScalef(
        1.25,
        3.2,
        0.55
    )

    glutSolidCube(30)

    glPopMatrix()


    # ========================================================
    # FRONT NOSE
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.95,
        0.98,
        1.00
    )

    glTranslatef(
        0,
        55,
        0
    )

    glScalef(
        0.65,
        1.2,
        0.45
    )

    glutSolidCube(30)

    glPopMatrix()


    # ========================================================
    # UPPER BODY
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.55,
        0.80,
        1.00
    )

    glTranslatef(
        0,
        5,
        17
    )

    glScalef(
        0.9,
        1.8,
        0.35
    )

    glutSolidCube(30)

    glPopMatrix()


    # ========================================================
    # COCKPIT
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.00,
        0.95,
        1.00
    )

    glTranslatef(
        0,
        25,
        23
    )

    glScalef(
        0.75,
        1.25,
        0.5
    )

    gluSphere(
        quadric,
        20,
        12,
        12
    )

    glPopMatrix()


    # ========================================================
    # LEFT MAIN WING
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.30,
        0.45,
        0.75
    )

    glTranslatef(
        -40,
        5,
        0
    )

    glRotatef(
        -8,
        0,
        0,
        1
    )

    glScalef(
        2.2,
        1.8,
        0.25
    )

    glutSolidCube(30)

    glPopMatrix()


    # ========================================================
    # RIGHT MAIN WING
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.30,
        0.45,
        0.75
    )

    glTranslatef(
        40,
        5,
        0
    )

    glRotatef(
        8,
        0,
        0,
        1
    )

    glScalef(
        2.2,
        1.8,
        0.25
    )

    glutSolidCube(30)

    glPopMatrix()


    # ========================================================
    # LEFT WING TIP
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.40,
        0.65,
        1.00
    )

    glTranslatef(
        -62,
        -10,
        3
    )

    glRotatef(
        -20,
        0,
        0,
        1
    )

    glScalef(
        0.8,
        1.5,
        0.3
    )

    glutSolidCube(25)

    glPopMatrix()


    # ========================================================
    # RIGHT WING TIP
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.40,
        0.65,
        1.00
    )

    glTranslatef(
        62,
        -10,
        3
    )

    glRotatef(
        20,
        0,
        0,
        1
    )

    glScalef(
        0.8,
        1.5,
        0.3
    )

    glutSolidCube(25)

    glPopMatrix()


    # ========================================================
    # LEFT ENGINE
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.45,
        0.55,
        0.70
    )

    glTranslatef(
        -22,
        -38,
        0
    )

    glRotatef(
        90,
        1,
        0,
        0
    )

    gluCylinder(
        quadric,
        10,
        7,
        28,
        12,
        12
    )

    glPopMatrix()


    # ========================================================
    # RIGHT ENGINE
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.45,
        0.55,
        0.70
    )

    glTranslatef(
        22,
        -38,
        0
    )

    glRotatef(
        90,
        1,
        0,
        0
    )

    gluCylinder(
        quadric,
        10,
        7,
        28,
        12,
        12
    )

    glPopMatrix()


    # ========================================================
    # LEFT ENGINE EXHAUST
    # ========================================================

    glPushMatrix()

    glColor3f(
        1.0,
        0.35,
        0.05
    )

    glTranslatef(
        -22,
        -67,
        0
    )

    glRotatef(
        90,
        1,
        0,
        0
    )

    gluCylinder(
        quadric,
        7,
        2,
        25,
        10,
        10
    )

    glPopMatrix()


    # ========================================================
    # RIGHT ENGINE EXHAUST
    # ========================================================

    glPushMatrix()

    glColor3f(
        1.0,
        0.35,
        0.05
    )

    glTranslatef(
        22,
        -67,
        0
    )

    glRotatef(
        90,
        1,
        0,
        0
    )

    gluCylinder(
        quadric,
        7,
        2,
        25,
        10,
        10
    )

    glPopMatrix()


    # ========================================================
    # LEFT SIDE ENGINE POD
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.30,
        0.50,
        0.80
    )

    glTranslatef(
        -25,
        -5,
        -8
    )

    glScalef(
        0.5,
        1.8,
        0.5
    )

    glutSolidCube(25)

    glPopMatrix()


    # ========================================================
    # RIGHT SIDE ENGINE POD
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.30,
        0.50,
        0.80
    )

    glTranslatef(
        25,
        -5,
        -8
    )

    glScalef(
        0.5,
        1.8,
        0.5
    )

    glutSolidCube(25)

    glPopMatrix()


    # ========================================================
    # LEFT FIN
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.55,
        0.75,
        1.00
    )

    glTranslatef(
        -20,
        -5,
        22
    )

    glRotatef(
        -15,
        0,
        1,
        0
    )

    glScalef(
        0.3,
        1.3,
        1.2
    )

    glutSolidCube(20)

    glPopMatrix()


    # ========================================================
    # RIGHT FIN
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.55,
        0.75,
        1.00
    )

    glTranslatef(
        20,
        -5,
        22
    )

    glRotatef(
        15,
        0,
        1,
        0
    )

    glScalef(
        0.3,
        1.3,
        1.2
    )

    glutSolidCube(20)

    glPopMatrix()


    # ========================================================
    # CENTER ENERGY CORE
    # ========================================================

    glPushMatrix()

    glColor3f(
        0.10,
        1.00,
        1.00
    )

    glTranslatef(
        0,
        -5,
        18
    )

    gluSphere(
        quadric,
        8,
        10,
        10
    )

    glPopMatrix()


    # ========================================================
    # SHIELD
    # ========================================================

    if shield_active:

        glPushMatrix()

        glColor3f(
            0.1,
            0.8,
            1.0
        )

        glScalef(
            1.7,
            1.7,
            1.3
        )

        gluSphere(
            quadric,
            50,
            15,
            15
        )

        glPopMatrix()


    glPopMatrix()


# ============================================================
# ASTEROID
# ============================================================

def render_asteroid(a):

    x = a[0]
    y = a[1]
    z = a[2]

    size = a[3]

    asteroid_type = a[6]

    rotation = a[7]


    glPushMatrix()

    glTranslatef(
        x,
        y,
        z
    )

    # Rotation animation

    glRotatef(
        rotation,
        1,
        1,
        0
    )


    # Different asteroid types

    if asteroid_type == 0:

        glColor3f(
            0.70,
            0.70,
            0.72
        )

    elif asteroid_type == 1:

        glColor3f(
            0.95,
            0.35,
            0.12
        )

    else:

        glColor3f(
            0.65,
            0.30,
            0.85
        )


    # Main asteroid

    glPushMatrix()

    glScalef(
        1.0,
        0.75 + (size % 3) * 0.15,
        1.15
    )

    gluSphere(
        quadric,
        size,
        10,
        10
    )

    glPopMatrix()


    # Extra rock section

    glPushMatrix()

    glColor3f(
        0.60,
        0.60,
        0.65
    )

    glTranslatef(
        size * 0.4,
        size * 0.2,
        size * 0.3
    )

    glScalef(
        0.5,
        0.7,
        0.4
    )

    glutSolidCube(size)

    glPopMatrix()


    glPopMatrix()


# ============================================================
# BULLET
# ============================================================

def render_bullet(b):

    x = b[0]
    y = b[1]
    z = b[2]

    dx = b[3]
    dy = b[4]


    glPushMatrix()

    glTranslatef(
        x,
        y,
        z
    )


    # Rotate bullet according to direction

    if dx > 0.1 and dy >= -0.1:

        glRotatef(
            90,
            0,
            0,
            1
        )

    elif dx < -0.1 and dy >= -0.1:

        glRotatef(
            -90,
            0,
            0,
            1
        )

    elif dy < -0.1:

        glRotatef(
            180,
            0,
            0,
            1
        )


    glColor3f(
        1,
        1,
        0
    )

    glScalef(
        0.5,
        1.5,
        0.5
    )

    glutSolidCube(10)

    glPopMatrix()


# ============================================================
# POWER UP
# ============================================================

def render_powerup(p):

    x = p[0]
    y = p[1]
    z = p[2]

    power_type = p[3]
    rotation = p[4]
    bob = p[5]

    glPushMatrix()

    # Floating / bobbing movement
    glTranslatef(
        x,
        y,
        z + bob
    )

    # Main rotation
    glRotatef(
        rotation,
        0,
        0,
        1
    )


    # ========================================================
    # OUTER ROTATING ENERGY STRUCTURE
    # ========================================================

    glPushMatrix()

    glRotatef(
        rotation * 2,
        1,
        0,
        0
    )

    if power_type == 0:

        glColor3f(
            0.1,
            0.8,
            1.0
        )

    elif power_type == 1:

        glColor3f(
            0.2,
            1.0,
            0.2
        )

    else:

        glColor3f(
            1.0,
            0.6,
            0.1
        )


    glScalef(
        1.5,
        1.5,
        0.25
    )

    glutSolidCube(35)

    glPopMatrix()


    # ========================================================
    # MAIN POWER CRYSTAL
    # ========================================================

    glPushMatrix()

    if power_type == 0:

        # Shield
        glColor3f(
            0.05,
            0.65,
            1.0
        )

    elif power_type == 1:

        # Health
        glColor3f(
            0.1,
            0.9,
            0.15
        )

    else:

        # Rapid fire
        glColor3f(
            1.0,
            0.45,
            0.05
        )


    # Crystal shape

    glScalef(
        0.8,
        0.8,
        1.3
    )

    gluSphere(
        quadric,
        22,
        8,
        8
    )

    glPopMatrix()


    # ========================================================
    # BRIGHT INNER ENERGY CORE
    # ========================================================

    glPushMatrix()

    glColor3f(
        1.0,
        1.0,
        1.0
    )

    glScalef(
        0.35,
        0.35,
        0.35
    )

    gluSphere(
        quadric,
        22,
        8,
        8
    )

    glPopMatrix()


    # ========================================================
    # TOP CRYSTAL
    # ========================================================

    glPushMatrix()

    glTranslatef(
        0,
        0,
        28
    )

    if power_type == 0:

        glColor3f(
            0.3,
            0.9,
            1.0
        )

    elif power_type == 1:

        glColor3f(
            0.4,
            1.0,
            0.4
        )

    else:

        glColor3f(
            1.0,
            0.8,
            0.2
        )


    glScalef(
        0.45,
        0.45,
        0.8
    )

    glutSolidCube(18)

    glPopMatrix()


    # ========================================================
    # LEFT ENERGY NODE
    # ========================================================

    glPushMatrix()

    glTranslatef(
        -25,
        0,
        0
    )

    gluSphere(
        quadric,
        7,
        8,
        8
    )

    glPopMatrix()


    # ========================================================
    # RIGHT ENERGY NODE
    # ========================================================

    glPushMatrix()

    glTranslatef(
        25,
        0,
        0
    )

    gluSphere(
        quadric,
        7,
        8,
        8
    )

    glPopMatrix()


    # ========================================================
    # BOTTOM ENERGY NODE
    # ========================================================

    glPushMatrix()

    glTranslatef(
        0,
        0,
        -25
    )

    gluSphere(
        quadric,
        7,
        8,
        8
    )

    glPopMatrix()


    glPopMatrix()
# ============================================================
# EXPLOSION
# ============================================================

def render_explosion(e):

    x = e[0]
    y = e[1]
    z = e[2]

    size = e[3]


    glPushMatrix()

    glTranslatef(
        x,
        y,
        z
    )

    glColor3f(
        1.0,
        0.4,
        0.0
    )

    gluSphere(
        quadric,
        size,
        10,
        10
    )

    glPopMatrix()


# ============================================================
# SPACE ENVIRONMENT
# ============================================================

def render_space_environment():

    # --------------------------------------------------------
    # Deep-space background: stars only, no floor and no grid
    # --------------------------------------------------------

    glPointSize(2.5)

    glBegin(GL_POINTS)

    glColor3f(0.9, 0.95, 1.0)

    # Deterministic star field. These are generated from simple
    # arithmetic so no external graphics resources are needed.
    for i in range(140):

        x = ((i * 97) % 1200) - 600
        y = ((i * 173) % 1200) - 600
        z = 80 + ((i * 61) % 420)

        glVertex3f(x, y, z)

    glEnd()


    # A few larger distant stars

    glPointSize(5)

    glBegin(GL_POINTS)

    glColor3f(1.0, 1.0, 1.0)

    for i in range(12):

        x = ((i * 211) % 1100) - 550
        y = ((i * 137) % 1100) - 550
        z = 140 + ((i * 83) % 300)

        glVertex3f(x, y, z)

    glEnd()


    # --------------------------------------------------------
    # Distant blue planet
    # --------------------------------------------------------

    glPushMatrix()

    glTranslatef(-480, 430, 220)

    glColor3f(0.08, 0.18, 0.55)

    gluSphere(
        quadric,
        70,
        18,
        18
    )

    glPopMatrix()


    # --------------------------------------------------------
    # Small distant moon
    # --------------------------------------------------------

    glPushMatrix()

    glTranslatef(-390, 350, 250)

    glColor3f(0.35, 0.38, 0.48)

    gluSphere(
        quadric,
        22,
        12,
        12
    )

    glPopMatrix()



# ============================================================
# SPAWN ASTEROID
# ============================================================

def spawn_asteroid():

    side = int(
        pseudo_random() * 4
    )

    size_choice = pseudo_random()


    # Small asteroid

    if size_choice < 0.35:

        size = 18

        speed = 0.15

        health = 1

        asteroid_type = 1


    # Medium asteroid

    elif size_choice < 0.75:

        size = 30

        speed = 0.09

        health = 2

        asteroid_type = 0


    # Large asteroid

    else:

        size = 50

        speed = 0.07

        health = 4

        asteroid_type = 2


    # Spawn from four boundaries

    if side == 0:

        x = -950

        y = (
            pseudo_random() * 1100
        ) - 550


    elif side == 1:

        x = 950

        y = (
            pseudo_random() * 1100
        ) - 550


    elif side == 2:

        x = (
            pseudo_random() * 1100
        ) - 550

        y = -950


    else:

        x = (
            pseudo_random() * 1100
        ) - 550

        y = 950


    z = size

    rotation = (
        pseudo_random() * 360
    )


    asteroids.append([
        x,
        y,
        z,
        size,
        speed,
        health,
        asteroid_type,
        rotation
    ])


# ============================================================
# SPAWN POWER UP
# ============================================================

def spawn_powerup():

    x = (
        pseudo_random() * 1000
    ) - 500

    y = (
        pseudo_random() * 1000
    ) - 500


    power_type = int(
        pseudo_random() * 3
    )


    powerups.append([
        x,
        y,
        30,
        power_type,
        0,
        0
    ])


# ============================================================
# MOVE PLAYER
# ============================================================

def move_player(dx, dy):

    global player_x
    global player_y


    player_x += dx

    player_y += dy


    # Boundary restriction

    if player_x > WORLD_LIMIT:

        player_x = WORLD_LIMIT


    if player_x < -WORLD_LIMIT:

        player_x = -WORLD_LIMIT


    if player_y > WORLD_LIMIT:

        player_y = WORLD_LIMIT


    if player_y < -WORLD_LIMIT:

        player_y = -WORLD_LIMIT


# ============================================================
# ROTATE PLAYER
# ============================================================

def rotate_player(direction):

    global player_angle

    global player_dx
    global player_dy


    # 5 degree rotation
    #
    # Instead of importing another library,
    # fixed values are used for 5 degrees.

    cos5 = 0.9961947

    sin5 = 0.0871557


    old_dx = player_dx

    old_dy = player_dy


    if direction > 0:

        # Rotate counter-clockwise

        player_dx = (
            old_dx * cos5
            -
            old_dy * sin5
        )

        player_dy = (
            old_dx * sin5
            +
            old_dy * cos5
        )

        player_angle += 5


    else:

        # Rotate clockwise

        player_dx = (
            old_dx * cos5
            +
            old_dy * sin5
        )

        player_dy = (
            -old_dx * sin5
            +
            old_dy * cos5
        )

        player_angle -= 5


    # Keep angle between 0 and 360

    if player_angle >= 360:

        player_angle -= 360


    if player_angle < 0:

        player_angle += 360


# ============================================================
# SHOOT
# ============================================================

def shoot():

    global player_dx
    global player_dy


    # Bullet starts slightly in front of spaceship

    bullet_x = (
        player_x
        +
        player_dx * 35
    )

    bullet_y = (
        player_y
        +
        player_dy * 35
    )

    bullet_z = player_z


    # Bullet speed

    bullet_speed = 15


    if triple_fire:
        # Center bullet
        bullets.append([
            bullet_x, bullet_y, bullet_z,
            player_dx * bullet_speed, player_dy * bullet_speed
        ])

        # Two side bullets using simple fixed-angle rotation (10 degrees)
        cos10 = 0.9848078
        sin10 = 0.1736482

        left_dx = player_dx * cos10 - player_dy * sin10
        left_dy = player_dx * sin10 + player_dy * cos10

        right_dx = player_dx * cos10 + player_dy * sin10
        right_dy = -player_dx * sin10 + player_dy * cos10

        bullets.append([
            bullet_x, bullet_y, bullet_z,
            left_dx * bullet_speed, left_dy * bullet_speed
        ])

        bullets.append([
            bullet_x, bullet_y, bullet_z,
            right_dx * bullet_speed, right_dy * bullet_speed
        ])
    else:
        bullets.append([
            bullet_x, bullet_y, bullet_z,
            player_dx * bullet_speed, player_dy * bullet_speed
        ])


# ============================================================
# CHEAT AUTO AIM
# ============================================================

def cheat_shoot():

    global player_dx
    global player_dy
    global player_angle

    if len(asteroids) == 0:
        return

    # --------------------------------------------------------
    # Find nearest asteroid
    # --------------------------------------------------------

    nearest = None
    nearest_distance = 999999999

    for a in asteroids:

        dx = a[0] - player_x
        dy = a[1] - player_y

        distance = dx * dx + dy * dy

        if distance < nearest_distance:

            nearest_distance = distance
            nearest = a

    if nearest is None:
        return


    # --------------------------------------------------------
    # Direction toward asteroid
    # --------------------------------------------------------

    dx = nearest[0] - player_x
    dy = nearest[1] - player_y

    distance = (dx * dx + dy * dy) ** 0.5

    if distance <= 0:
        return

    target_dx = dx / distance
    target_dy = dy / distance


    # --------------------------------------------------------
    # Smoothly rotate toward asteroid
    # --------------------------------------------------------

    # Cross product tells us which direction to turn

    cross = (
        player_dx * target_dy
        -
        player_dy * target_dx
    )


    # 5 degree rotation

    cos5 = 0.9961947
    sin5 = 0.0871557


    if cross > 0.02:

        # Rotate left

        old_dx = player_dx
        old_dy = player_dy

        player_dx = (
            old_dx * cos5
            -
            old_dy * sin5
        )

        player_dy = (
            old_dx * sin5
            +
            old_dy * cos5
        )

        player_angle += 5


    elif cross < -0.02:

        # Rotate right

        old_dx = player_dx
        old_dy = player_dy

        player_dx = (
            old_dx * cos5
            +
            old_dy * sin5
        )

        player_dy = (
            -old_dx * sin5
            +
            old_dy * cos5
        )

        player_angle -= 5


    # Keep angle between 0 and 360

    if player_angle >= 360:

        player_angle -= 360

    if player_angle < 0:

        player_angle += 360


    # --------------------------------------------------------
    # Fire only when approximately facing the asteroid
    # --------------------------------------------------------

    dot = (
        player_dx * target_dx
        +
        player_dy * target_dy
    )

    if dot > 0.98:

        bullets.append([
            player_x + player_dx * 35,
            player_y + player_dy * 35,
            player_z,
            player_dx * 15,
            player_dy * 15
        ])

# ============================================================
# BULLET COLLISION
# ============================================================

def check_bullet_collision():

    global score
    global bombs


    bullets_to_remove = []

    asteroids_to_remove = []


    for bi in range(
        len(bullets)
    ):

        if bi in bullets_to_remove:

            continue


        b = bullets[bi]


        for ai in range(
            len(asteroids)
        ):

            if ai in asteroids_to_remove:

                continue


            a = asteroids[ai]


            dx = (
                b[0] - a[0]
            )

            dy = (
                b[1] - a[1]
            )


            distance = (
                dx * dx
                +
                dy * dy
            )


            collision_distance = (
                a[3] + 10
            ) ** 2


            if distance < collision_distance:

                a[5] -= 1

                bullets_to_remove.append(
                    bi
                )


                if a[5] <= 0:

                    score += 10


                    # Bomb every 100 points

                    if score % 100 == 0:

                        bombs += 1


                    explosions.append([
                        a[0],
                        a[1],
                        a[2],
                        10,
                        15
                    ])


                    # Large asteroid splits

                    if a[3] >= 45:

                        for k in range(2):

                            new_x = (
                                a[0]
                                +
                                (k * 40)
                                -
                                20
                            )

                            new_y = (
                                a[1]
                                +
                                (k * 30)
                                -
                                15
                            )


                            asteroids.append([
                                new_x,
                                new_y,
                                25,
                                18,
                                1.2,
                                1,
                                1,
                                0
                            ])


                    asteroids_to_remove.append(
                        ai
                    )


                break


    # Remove bullets

    for i in range(
        len(bullets) - 1,
        -1,
        -1
    ):

        if i in bullets_to_remove:

            bullets.pop(i)


    # Remove asteroids

    for i in range(
        len(asteroids) - 1,
        -1,
        -1
    ):

        if i in asteroids_to_remove:

            asteroids.pop(i)


# ============================================================
# PLAYER / ASTEROID COLLISION
# ============================================================

def check_player_collision():

    global lives

    global shield_active
    global shield_timer

    global flash_timer


    for i in range(
        len(asteroids) - 1,
        -1,
        -1
    ):

        a = asteroids[i]


        dx = (
            player_x - a[0]
        )

        dy = (
            player_y - a[1]
        )


        distance = (
            dx * dx
            +
            dy * dy
        )


        collision_distance = (
            35 + a[3]
        ) ** 2


        if distance < collision_distance:


            # Shield absorbs damage

            if shield_active:

                shield_active = False

                shield_timer = 0


            # Cheat makes player invincible

            elif cheat_mode:

                pass


            else:

                lives -= 1

                flash_timer = 20


            explosions.append([
                a[0],
                a[1],
                a[2],
                15,
                15
            ])


            asteroids.pop(i)


            if lives <= 0:

                set_game_over()


# ============================================================
# POWER UP COLLISION
# ============================================================

def check_powerup_collision():

    global shield_active
    global shield_timer

    global lives

    global rapid_fire
    global rapid_fire_timer


    for i in range(
        len(powerups) - 1,
        -1,
        -1
    ):

        p = powerups[i]


        dx = (
            player_x - p[0]
        )

        dy = (
            player_y - p[1]
        )


        distance = (
            dx * dx
            +
            dy * dy
        )


        if distance < 45 * 45:


            # Shield

            if p[3] == 0:

                shield_active = True

                # Shield lasts for 5 seconds at approximately 60 FPS
                shield_timer = 300


            # Health

            elif p[3] == 1:

                if lives < 3:

                    lives += 1


            # Rapid fire

            else:

                rapid_fire = True

                rapid_fire_timer = 600


            powerups.pop(i)

            # Immediately replace the collected power-up
            # so that 4 power-ups remain available.
            if len(powerups) < 4:

                spawn_powerup()


# ============================================================
# BOMB
# ============================================================

def use_bomb():

    global bombs

    global bomb_effect

    global score


    if bombs <= 0:

        return


    bombs -= 1

    bomb_effect = 30


    # Destroy all asteroids

    for a in asteroids:

        explosions.append([
            a[0],
            a[1],
            a[2],
            20,
            20
        ])

        score += 5


    asteroids.clear()


# ============================================================
# GAME OVER
# ============================================================

def set_game_over():

    global game_over

    game_over = True


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global player_x
    global player_y

    global player_dx
    global player_dy

    global player_angle

    global score
    global lives
    global bombs
    global level

    global game_over

    global shield_active
    global shield_timer

    global rapid_fire
    global rapid_fire_timer
    global triple_fire
    global triple_fire_timer

    global bomb_effect

    global frame_count
    global spawn_counter
    global powerup_counter


    player_x = 0

    player_y = 0


    # Initial facing direction

    player_dx = 0.0

    player_dy = 1.0

    player_angle = 0


    score = 0

    lives = 3

    bombs = 0

    level = 1


    game_over = False


    shield_active = False

    shield_timer = 0


    rapid_fire = False

    rapid_fire_timer = 0


    bomb_effect = 0


    frame_count = 0

    spawn_counter = 0

    powerup_counter = 0


    bullets.clear()

    asteroids.clear()

    powerups.clear()

    explosions.clear()


    # Initial asteroids - keep Level 1 open and manageable

    for i in range(3):

        spawn_asteroid()


    # Keep exactly 4 power-ups available at the start

    for i in range(4):

        spawn_powerup()


# ============================================================
# UPDATE BULLETS
# ============================================================

def update_bullets():

    for i in range(
        len(bullets) - 1,
        -1,
        -1
    ):

        b = bullets[i]


        b[0] += b[3]

        b[1] += b[4]


        if (
            b[0] > 1100
            or
            b[0] < -1100
            or
            b[1] > 1100
            or
            b[1] < -1100
        ):

            bullets.pop(i)


# ============================================================
# UPDATE ASTEROIDS
# ============================================================

def update_asteroids():

    for a in asteroids:

        dx = (
            player_x - a[0]
        )

        dy = (
            player_y - a[1]
        )


        distance_squared = (
            dx * dx
            +
            dy * dy
        )


        if distance_squared > 0:

            distance = (
                distance_squared ** 0.5
            )


            a[0] += (
                dx /
                distance
            ) * a[4]


            a[1] += (
                dy /
                distance
            ) * a[4]


        # Rotation

        a[7] += 1.5


        if a[7] >= 360:

            a[7] -= 360


# ============================================================
# UPDATE POWER UPS
# ============================================================

def update_powerups():

    for p in powerups:

        # Rotation
        p[4] += 2

        if p[4] >= 360:
            p[4] -= 360


        # Floating / bobbing
        p[5] += 0.08

        if p[5] > 6.28:
            p[5] -= 6.28


        # Use a simple wave approximation
        # to move the stone up and down

        if p[5] < 3.14:

            p[2] = 30 + (p[5] / 3.14) * 20

        else:

            p[2] = 50 - (
                (p[5] - 3.14) / 3.14
            ) * 20


# ============================================================
# UPDATE EXPLOSIONS
# ============================================================

def update_explosions():

    for i in range(
        len(explosions) - 1,
        -1,
        -1
    ):

        e = explosions[i]


        e[3] += 3

        e[4] -= 1


        if e[4] <= 0:

            explosions.pop(i)


# ============================================================
# UPDATE DIFFICULTY
# ============================================================

def update_difficulty():

    global level


    new_level = (
        1
        +
        frame_count // 1800
    )


    if new_level > 10:

        new_level = 10


    level = new_level


# ============================================================
# KEYBOARD
# ============================================================

def keyboardListener(key, x, y):

    global cheat_mode


    # --------------------------------------------------------
    # Restart
    # --------------------------------------------------------

    if key == b'r':

        reset_game()

        return


    # --------------------------------------------------------
    # Cheat mode
    # --------------------------------------------------------

    if key == b'c':

        cheat_mode = not cheat_mode

        return


    if game_over:

        return


    # --------------------------------------------------------
    # FORWARD
    # --------------------------------------------------------

    if key == b'w':

        move_player(
            player_dx * player_speed,
            player_dy * player_speed
        )


    # --------------------------------------------------------
    # BACKWARD
    # --------------------------------------------------------

    elif key == b's':

        move_player(
            -player_dx * player_speed,
            -player_dy * player_speed
        )


    # --------------------------------------------------------
    # ROTATE LEFT
    # --------------------------------------------------------

    elif key == b'a':

        rotate_player(1)


    # --------------------------------------------------------
    # ROTATE RIGHT
    # --------------------------------------------------------

    elif key == b'd':

        rotate_player(-1)


    # --------------------------------------------------------
    # MOVE LEFT
    # --------------------------------------------------------

    elif key == b'q':
    # Move LEFT
      move_player(
        -player_dy * player_speed,
        player_dx * player_speed
    )

    elif key == b'e':
    # Move RIGHT
      move_player(
        player_dy * player_speed,
        -player_dx * player_speed
    )

    # --------------------------------------------------------
    # BOMB
    # --------------------------------------------------------

    elif key == b' ':

        use_bomb()


# ============================================================
# SPECIAL KEY
# ============================================================

def specialKeyListener(key, x, y):

    global camera_pos


    x_pos, y_pos, z_pos = camera_pos


    if key == GLUT_KEY_LEFT:

        x_pos -= 10


    elif key == GLUT_KEY_RIGHT:

        x_pos += 10


    elif key == GLUT_KEY_UP:

        z_pos += 10


    elif key == GLUT_KEY_DOWN:

        z_pos -= 10


    camera_pos = (
        x_pos,
        y_pos,
        z_pos
    )


# ============================================================
# MOUSE
# ============================================================

def mouseListener(button, state, x, y):

    global camera_mode


    if state != GLUT_DOWN:

        return


    # --------------------------------------------------------
    # LEFT CLICK = SHOOT
    # --------------------------------------------------------

    if button == GLUT_LEFT_BUTTON:

        if not game_over:

            shoot()


    # --------------------------------------------------------
    # RIGHT CLICK = CAMERA
    # --------------------------------------------------------

    elif button == GLUT_RIGHT_BUTTON:

        camera_mode = 1 - camera_mode


# ============================================================
# CAMERA
# ============================================================

def setupCamera():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(
        90,
        1000 / 800,
        0.1,
        1500
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    # ========================================================
    # THIRD PERSON CAMERA
    # ========================================================

    if camera_mode == 0:

        gluLookAt(
            player_x - player_dx * 550,
            player_y - player_dy * 550,
            320,

            player_x,
            player_y,
            0,

            0,
            0,
            1
        )


    # ========================================================
    # FIRST PERSON CAMERA
    # ========================================================

    else:

        # Camera is placed slightly in front of the cockpit
        eye_x = player_x + player_dx * 15
        eye_y = player_y + player_dy * 15
        eye_z = player_z + 25

        # Look far ahead in the direction of the spaceship
        look_x = player_x + player_dx * 500
        look_y = player_y + player_dy * 500
        look_z = player_z + 25

        gluLookAt(
            eye_x,
            eye_y,
            eye_z,

            look_x,
            look_y,
            look_z,

            0,
            0,
            1
        )


# ============================================================
# UPDATE GAME
# ============================================================

def update_game():

    global frame_count

    global spawn_counter
    global powerup_counter

    global shield_timer
    global shield_active

    global rapid_fire_timer
    global rapid_fire

    global flash_timer
    global bomb_effect


    if game_over:

        return


    frame_count += 1


    # --------------------------------------------------------
    # Difficulty
    # --------------------------------------------------------

    update_difficulty()


    # --------------------------------------------------------
    # Bullets
    # --------------------------------------------------------

    update_bullets()


    # --------------------------------------------------------
    # Asteroids
    # --------------------------------------------------------

    update_asteroids()


    # --------------------------------------------------------
    # Power ups
    # --------------------------------------------------------

    update_powerups()


    # --------------------------------------------------------
    # Explosions
    # --------------------------------------------------------

    update_explosions()


    # --------------------------------------------------------
    # Spawn asteroids
    # --------------------------------------------------------

    spawn_counter += 1


    # Keep the early game open. The asteroid count increases slowly
    # with the level instead of filling the arena immediately.
    if level == 1:
        spawn_limit = 330
        max_asteroids = 4
    elif level == 2:
        spawn_limit = 270
        max_asteroids = 5
    elif level == 3:
        spawn_limit = 220
        max_asteroids = 6
    else:
        spawn_limit = 190
        max_asteroids = 7 + (level - 4)

    if max_asteroids > 9:
        max_asteroids = 9

    if spawn_counter >= spawn_limit:

        spawn_counter = 0

        if len(asteroids) < max_asteroids:
            spawn_asteroid()


    # --------------------------------------------------------
    # Power-ups
    # --------------------------------------------------------

    # Keep up to 4 power-ups available in the arena.
    # A collected power-up is immediately replaced by another one.

    if len(powerups) < 4:

        spawn_powerup()


    # --------------------------------------------------------
    # Shield timer
    # --------------------------------------------------------

    if shield_active:

        shield_timer -= 1


        if shield_timer <= 0:

            shield_active = False


    # --------------------------------------------------------
    # Rapid fire timer
    # --------------------------------------------------------

    if rapid_fire:

        rapid_fire_timer -= 1


        if rapid_fire_timer <= 0:

            rapid_fire = False


    # --------------------------------------------------------
    # Cheat auto aim
    # --------------------------------------------------------

    if cheat_mode:

        if frame_count % 3 == 0:

            cheat_shoot()


    # --------------------------------------------------------
    # Collisions
    # --------------------------------------------------------

    check_bullet_collision()

    check_player_collision()

    check_powerup_collision()


    # --------------------------------------------------------
    # Bomb effect
    # --------------------------------------------------------

    if bomb_effect > 0:

        bomb_effect -= 1


    # --------------------------------------------------------
    # Player flash
    # --------------------------------------------------------

    if flash_timer > 0:

        flash_timer -= 1


# ============================================================
# HUD
# ============================================================

def draw_HUD():

    draw_text(
        20,
        760,
        "SPACE SURVIVE 3D"
    )


    draw_text(
        20,
        725,
        "Score: " + str(score)
    )


    draw_text(
        20,
        695,
        "Lives: " + str(lives)
    )


    draw_text(
        20,
        665,
        "Level: " + str(level)
    )


    draw_text(
        20,
        635,
        "Bombs: " + str(bombs)
    )


    if shield_active:

        draw_text(
            20,
            605,
            "Shield: ACTIVE"
        )

    else:

        draw_text(
            20,
            605,
            "Shield: OFF"
        )


    if rapid_fire:

        draw_text(
            20,
            575,
            "Triple Fire: ACTIVE"
        )


    if cheat_mode:

        draw_text(
            20,
            545,
            "CHEAT MODE: ON"
        )


    # Camera status

    if camera_mode == 0:

        draw_text(
            730,
            760,
            "Camera: THIRD PERSON"
        )

    else:

        draw_text(
            730,
            760,
            "Camera: FIRST PERSON"
        )


# ============================================================
# BOMB EFFECT
# ============================================================

def render_bomb_effect():

    if bomb_effect <= 0:

        return


    glPushMatrix()


    glTranslatef(
        player_x,
        player_y,
        player_z
    )


    size = (
        40
        +
        (30 - bomb_effect) * 15
    )


    glColor3f(
        1.0,
        0.3,
        0.0
    )


    gluSphere(
        quadric,
        size,
        15,
        15
    )


    glPopMatrix()


# ============================================================
# DISPLAY
# ============================================================

def showScreen():

    glClear(
        GL_COLOR_BUFFER_BIT
        |
        GL_DEPTH_BUFFER_BIT
    )


    glLoadIdentity()


    glViewport(
        0,
        0,
        1000,
        800
    )


    setupCamera()


    # ========================================================
    # SPACE
    # ========================================================

    render_space_environment()


    # ========================================================
    # OPEN SPACE - no floor/grid
    # ========================================================

    # ========================================================
    # ASTEROIDS
    # ========================================================

    for a in asteroids:

        render_asteroid(a)


    # ========================================================
    # BULLETS
    # ========================================================

    for b in bullets:

        render_bullet(b)


    # ========================================================
    # POWER UPS
    # ========================================================

    for p in powerups:

        render_powerup(p)


    # ========================================================
    # EXPLOSIONS
    # ========================================================

    for e in explosions:

        render_explosion(e)


    # ========================================================
    # BOMB
    # ========================================================

    render_bomb_effect()


    # ========================================================
    # PLAYER
    # ========================================================

    if not game_over:

    # Don't render the spaceship itself in first-person view
      if camera_mode == 0:
          render_player()


    # ========================================================
    # HUD
    # ========================================================

    draw_HUD()


    # ========================================================
    # GAME OVER
    # ========================================================

    if game_over:

        draw_text(
            400,
            430,
            "GAME OVER"
        )


        draw_text(
            360,
            390,
            "Final Score: " + str(score)
        )


        draw_text(
            330,
            350,
            "Press R to Restart"
        )


    # ========================================================
    # CONTROLS
    # ========================================================

    if not game_over:

        draw_text(
            20,
            30,
            "W/S: Forward/Back | A/D: Rotate | Q/E: Left/Right | Mouse: Shoot | SPACE: Bomb"
        )


    glutSwapBuffers()


# ============================================================
# IDLE
# ============================================================

def idle():

    update_game()

    glutPostRedisplay()


# ============================================================
# MAIN
# ============================================================

def main():

    global quadric


    glutInit()


    glutInitDisplayMode(
        GLUT_DOUBLE
        |
        GLUT_RGB
        |
        GLUT_DEPTH
    )


    glutInitWindowSize(
        1000,
        800
    )


    glutInitWindowPosition(
        0,
        0
    )


    wind = glutCreateWindow(
        b"Space Survive 3D"
    )


    # Dark space background


    # Create quadric

    quadric = gluNewQuadric()


    # Initialize game

    reset_game()


    # Register callbacks

    glutDisplayFunc(
        showScreen
    )


    glutKeyboardFunc(
        keyboardListener
    )


    glutSpecialFunc(
        specialKeyListener
    )


    glutMouseFunc(
        mouseListener
    )


    glutIdleFunc(
        idle
    )


    glutMainLoop()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()