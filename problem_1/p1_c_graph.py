import time
import matplotlib.pyplot as plt
import random

# Import functions from your modules
from p1_b import stable_matching_1b
from p1_c import stable_matching_1c

# Helper function to generate random preference files
def generate_pref_file(n, filename):
    with open(filename, 'w') as f:
        f.write(f"{n}\n")
        doctors = list(range(n))
        hospitals = list(range(n))
        # Write doctor preferences
        for _ in range(n):
            random.shuffle(hospitals)
            f.write(' '.join(map(str, hospitals)) + '\n')
        # Write hospital preferences
        for _ in range(n):
            random.shuffle(doctors)
            f.write(' '.join(map(str, doctors)) + '\n')

# Test sizes
sizes = [10, 50, 100, 200, 300, 400, 500]
times_1b = []
times_1c = []

for n in sizes:
    filename = f"prefs_{n}.txt"
    generate_pref_file(n, filename)

    # Time 1b
    start = time.time()
    stable_matching_1b(filename)
    times_1b.append(time.time() - start)

    # Time 1c
    start = time.time()
    stable_matching_1c(filename)
    times_1c.append(time.time() - start)

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(sizes, times_1b, marker='o', label='stable_matching_1b')
plt.plot(sizes, times_1c, marker='s', label='stable_matching_1c')
plt.xlabel('Number of doctors/hospitals (n)')
plt.ylabel('Execution time (seconds)')
plt.title('Empirical Performance Comparison: 1b vs 1c')
plt.legend()
plt.grid(True)
plt.show()
