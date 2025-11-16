# empirical_tests.py (updated)
import time
import matplotlib.pyplot as plt
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort
import random

def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start

sizes = [1000, 5000, 10000]
input_types = ["Random", "Sorted", "Reverse"]
det_times = []
rand_times = []

for n in sizes:
    arr_random = [random.randint(0, n) for _ in range(n)]
    arr_sorted = sorted(arr_random)
    arr_reverse = list(reversed(arr_sorted))

    for arr, label in zip([arr_random, arr_sorted, arr_reverse], input_types):
        dt = measure_time(quicksort, arr)
        rt = measure_time(randomized_quicksort, arr)
        det_times.append(dt)
        rand_times.append(rt)
        print(f"Size: {n}, Type: {label} | Deterministic: {dt:.6f}s | Randomized: {rt:.6f}s")

# Plot results
plt.figure(figsize=(8,6))
plt.plot(sizes*3, det_times, marker='o', label='Deterministic')
plt.plot(sizes*3, rand_times, marker='o', label='Randomized')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Deterministic vs Randomized Quicksort')
plt.grid(True)
plt.legend()
plt.savefig("../documentation/execution_plot.png")
plt.show()

