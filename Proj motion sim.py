import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle, t_max, dt):
    g = 9.81
    angle_rad = np.radians(angle)
    t = np.arange(0, t_max, dt)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    range_of_projectile = 0
    max_height = 0

    for i in range(1, len(t)):
        x[i] = v0 * np.cos(angle_rad) * t[i]
        y[i] = v0 * np.sin(angle_rad) * t[i] - 0.5 * g * t[i]**2

        if y[i] < 0:
            range_of_projectile = x[i]
            break

        if y[i] > max_height:
            max_height = y[i]

    return t, x, y, range_of_projectile, max_height

def plot_trajectory(t, x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Projectile Path")
    plt.title("Projectile Motion")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("Welcome to the Projectile Motion Simulator!")
    try:
        v0 = float(input("Enter the initial velocity (m/s): "))
        angle = float(input("Enter the launch angle (degrees): "))
        t_max = 2 * (v0 * np.sin(np.radians(angle)) / 9.81)  # Calculate time of flight
        dt = float(input("Enter the time step for the simulation (seconds): "))

        print("\nSimulating projectile motion... Please wait!")
        t, x, y, range_of_projectile, max_height = projectile_motion(v0, angle, t_max, dt)

        plot_trajectory(t, x, y)

        print(f"\nRange of the projectile: {range_of_projectile:.2f} meters")
        print(f"Maximum height reached: {max_height:.2f} meters")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
