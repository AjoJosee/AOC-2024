import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Read input from file
with open("advent14.txt", "r") as file:
    lines = file.readlines()

# Constants for grid size
WIDE = 101
TALL = 103
#not working properly
# Parsing robot data from input
robots = []
for robot in lines:
    sides = robot.split(" ")
    left_side = sides[0]
    right_side = sides[1]
    left_sides = left_side.split(",")
    Px = int(left_sides[0].split("=")[-1])
    Py = int(left_sides[1])
    right_sides = right_side.split(",")
    Vx = int(right_sides[0].split("=")[-1])
    Vy = int(right_sides[1].strip())
    robots.append([Px, Py, Vx, Vy])

# Create figure for animation
fig, ax = plt.subplots(figsize=(10, 10))
grid = [[0] * WIDE for _ in range(TALL)]
im = ax.imshow(grid, cmap='viridis', vmin=0, vmax=1)

# Control variables
is_paused = False
speed = 1  # Initial speed in milliseconds
current_frame = 0

def update(second):
    """Updates the grid for the given second."""
    global is_paused, current_frame

    if is_paused:
        return [im]  # Skip update if paused

    current_frame = second  # Track current frame

    final_grid = [[0] * WIDE for _ in range(TALL)]
    for Px, Py, Vx, Vy in robots:
        new_Px = (Px + Vx * second) % WIDE
        new_Py = (Py + Vy * second) % TALL
        final_grid[new_Py][new_Px] = 1  # Mark robot position on grid

    im.set_array(final_grid)
    ax.set_title(f'Time Step: {second}')
    return [im]

def on_key_press(event):
    """Handles keyboard input for animation controls."""
    global is_paused, speed, current_frame, ani

    if event.key == ' ':
        # Toggle pause/resume
        is_paused = not is_paused
        print("Paused" if is_paused else "Resumed")

    elif event.key == '+':
        # Increase animation speed
        speed = max(50, speed - 50)
        ani.event_source.interval = speed
        print(f"Speed increased: {speed} ms/frame")

    elif event.key == '-':
        # Decrease animation speed
        speed += 50
        ani.event_source.interval = speed
        print(f"Speed decreased: {speed} ms/frame")

    elif event.key == 'left':
        # Step back one frame
        if current_frame > 0:
            current_frame -= 1
            update(current_frame)
            plt.draw()
        print(f"Stepped back to frame {current_frame}")

    elif event.key == 'right':
        # Step forward one frame
        if current_frame < num_seconds - 1:
            current_frame += 1
            update(current_frame)
            plt.draw()
        print(f"Stepped forward to frame {current_frame}")

# Attach key event to figure
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Number of frames (simulation seconds)
num_seconds = 10000  # Adjust for your needs

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_seconds, interval=speed, blit=False)

# For manual control during the animation, use plt.pause(0.01) for interactive updates.
plt.show()
