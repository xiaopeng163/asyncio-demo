from queue import deque
from print_msg import print_message_periodical

class Task:

    next_id = 0

    def __init__(self, routine):
        self.id = Task.next_id
        Task.next_id += 1
        self.routine = routine


class Scheduler:

    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_task_results = {}
        self.failed_task_errors = {}
    
    def add(self, routine):
        task = Task(routine)
        self.runnable_tasks.append(task)
        return task.id
    
    def run_to_completion(self):
        while len(self.runnable_tasks) !=0:
            task = self.runnable_tasks.popleft()
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:
                print(f'completed with result: {stopped.value}')
                self.completed_task_results[task.id] = stopped.value
            except Exception as e:
                print(f'failed with exception: {e}')
                self.failed_task_errors[task.id] = e
            else:
                assert yielded is None
                self.runnable_tasks.append(task)

if __name__ == "__main__":
    sch = Scheduler()
    sch.add(print_message_periodical(3, 'three'))
    sch.add(print_message_periodical(10, 'ten'))
    sch.run_to_completion()