import time

def wait(delay_ms):
    end_time = time.perf_counter() + (delay_ms / 1000.0)
    while time.perf_counter() < end_time:
        pass  # Busy-wait for the specified delay

def bubble_sort(arr, delay_ms):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Visualize the sorting step
            print(arr)
            wait(delay_ms)  # Wait for the specified delay
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
data = [3, 2, 1, 5, 4]
delay = int(input("Enter delay in milliseconds: "))

print("Starting bubble sort...")
bubble_sort(data, delay)
print("Sorted array:", data)
