from time import time

def compute_average(n):
    """Performs n appends to an empty list and return average time elapsed"""
    data = []
    start = time()
    for k in range(n):
        data.insert(k, None)
    end = time()
    return (end - start) / n

# Testing
if __name__ == "__main__":
    temp = [100, 1000, 10000, 100000]
    for i in range(len(temp)):
        print(compute_average(temp[i]))