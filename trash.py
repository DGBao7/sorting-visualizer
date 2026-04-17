import time

start = time.time()
for _ in range(1000):
    pass
print("time.time:", time.time() - start)

start = time.perf_counter()
for _ in range(1000):
    pass
print("perf_counter:", time.perf_counter() - start)