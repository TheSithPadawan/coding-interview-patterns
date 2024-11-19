import time
import threading
from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor

class Task:
    def __init__(self, runnable, run_time):
        # runnable is a function that will be executed by a thread
        self.runnable = runnable
        self.run_time = run_time

    def __lt__(self, other):
        return self.run_time < other.run_time


class DelayBlockingQueue:
    """
    这个queue应该是多线程safe的
    """
    def __init__(self):
        # priority queue is threadsafe
        self.pq = PriorityQueue()
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def add(self, runnable, delay_time):
        run_time = time.time() + delay_time / 1000  # Convert ms to seconds
        new_task = Task(runnable, run_time)
        with self.condition:
            self.pq.put(new_task)
            if self.pq.queue[0] == new_task:
                self.condition.notify()

    def take(self):
        # so using condition variable here also adds the notify mechanism, which is more efficient
        with self.condition:
            while True:
                if self.pq.empty():
                    self.condition.wait()
                else:
                    wait_time = self.pq.queue[0].run_time - time.time()
                    if wait_time <= 0:
                        return self.pq.get()
                    else:
                        self.condition.wait(timeout=wait_time)

class DelayScheduleMonitor:
    """
    No thread pool - directly managing threads:
    this approach can lead to higher overhead compared to using a thread pool since it spawns a new thread for every task.
    Therefore we use threadpool for that
    """
    def __init__(self):
        self.delay_queue = DelayBlockingQueue()
        self.executor = ThreadPoolExecutor(max_workers=30)

    def schedule(self, runnable, delay_time):
        self.delay_queue.add(runnable, delay_time)

    def start(self):
        print('Time is:', time.strftime('%X'))
        def worker():
            while True:
                try:
                    task = self.delay_queue.take()
                    self.executor.submit(task.runnable)
                except Exception as ex:
                    print('encountered exception', ex, 'aborting')
                    break

        threading.Thread(target=worker, daemon=True).start()


# Example Usage
def example_task():
    print(f"Task executed at {time.strftime('%X')}")

if __name__ == "__main__":
    scheduler = DelayScheduleMonitor()
    scheduler.start()

    # Schedule tasks with varying delays
    scheduler.schedule(example_task, 5000)  # 5-second delay
    scheduler.schedule(example_task, 2000)  # 2-second delay
    scheduler.schedule(example_task, 7000)  # 7-second delay

    time.sleep(10)  # Wait for tasks to complete
    print("Main thread exiting")
