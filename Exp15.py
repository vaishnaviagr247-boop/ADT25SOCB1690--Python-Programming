# Assignment No. 15
# Name:vaishnavi Agrahari
# Class:SY-07
# Roll No.:52

# Step 1: Import the required modules
import gc
import tracemalloc
import time

# Step 2: Define a class for creating cyclic objects
class Node:
    def __init__(self):
        self.reference = None

# Step 3: Start memory tracking
tracemalloc.start()

# Step 4: Create objects that refer to each other
def create_cycles(number):
    for i in range(number):
        # Create two objects
        a = Node()
        b = Node()

        # Create a reference cycle
        a.reference = b
        b.reference = a

# Step 5: Create many cyclic objects
create_cycles(10000)

# Step 6: Measure memory before garbage collection
current_before, peak_before = tracemalloc.get_traced_memory()

print("Memory before GC:", round(current_before / 1024, 2), "KB")

# Step 7: Measure garbage collection time
start_time = time.perf_counter()

# Manually run garbage collection
collected = gc.collect()

gc_time = time.perf_counter() - start_time

# Step 8: Measure memory after garbage collection
current_after, peak_after = tracemalloc.get_traced_memory()

# Step 9: Display the results
print("Objects collected:", collected)

print("Memory after GC:", round(current_after / 1024, 2), "KB")

print("Peak traced memory:", round(peak_after / 1024, 2), "KB")

print("GC execution time:", round(gc_time, 6), "seconds")

# Step 10: Stop memory tracking
tracemalloc.stop()