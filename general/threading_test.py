import threading
import time


def fibonacci(n):
    if n <= 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def multi_thread():
    threads = []
    start_time = time.time()
    for i in range(2):
        thread = threading.Thread(target=fibonacci, args=(20,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"taken time here is :{end_time - start_time}")


multi_thread()
