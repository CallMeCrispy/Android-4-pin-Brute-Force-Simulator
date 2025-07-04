import time
import random
import pyfiglet

# Display ASCII banner
banner = pyfiglet.figlet_format("Android Simulator")
print(banner)

# Ask user to start or cancel
choice = input("Do you want to start the Android brute-force simulation? (y/n): ").strip().lower()
if choice != 'y':
    print("Simulation canceled.")
    exit()

# SIMULATED correct PIN (unknown to attacker)
correct_pin = str(random.randint(0, 9999)).zfill(4)

def simulate_android_bruteforce():
    print("\nSimulating Android PIN brute-force...")
    time.sleep(1)
    print("Trying to unlock device...")
    time.sleep(1)

    attempts = 0
    start_time = time.time()

    try:
        for pin in range(10000):
            guess = str(pin).zfill(4)
            print(f"[*] Attempting PIN: {guess}")
            time.sleep(0.01)
            attempts += 1

            if guess == correct_pin:
                elapsed = time.time() - start_time
                print(f"\nDevice unlocked with PIN: {guess}")
                print(f"Total attempts: {attempts}")
                print(f"Time taken: {elapsed:.2f} seconds")
                return
    except KeyboardInterrupt:
        print("\nBrute-force interrupted by user.")
        print(f"Attempts made: {attempts}")
        return

    print("\nFailed to unlock after 10,000 attempts.")

# Run the simulation
simulate_android_bruteforce()
