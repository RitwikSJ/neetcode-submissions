class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        priority = [[task, freq[task]] for task in freq]
        priority.sort(key=lambda x: x[1], reverse=True)
        print(priority)

        wait_times = {}
        unique_tasks_remaining = len(priority)
        priority_index = 0
        time = 0
        checked_items = 0

        while unique_tasks_remaining:
            print(time, wait_times, priority_index)
            if priority[priority_index][0] in wait_times and checked_items < unique_tasks_remaining:
                priority_index += 1
                if priority_index == unique_tasks_remaining:
                    priority_index = 0
                checked_items += 1
            elif priority[priority_index][0] in wait_times and checked_items == unique_tasks_remaining:
                time += 1
                for task in list(wait_times.keys()):
                    if wait_times[task] == 1:
                        wait_times.pop(task)
                    else:
                        wait_times[task] -= 1
                priority_index = 0
            else:
                print(priority[priority_index][0])
                priority[priority_index][1] -= 1

                for task in list(wait_times.keys()):
                    if wait_times[task] == 1:
                        wait_times.pop(task)
                    else:
                        wait_times[task] -= 1

                if priority[priority_index][1] == 0:
                    if priority[priority_index][0] in wait_times:
                        wait_times.pop(priority[priority_index][0])
                    priority.pop(priority_index)
                    unique_tasks_remaining -= 1
                else:  
                    wait_times[priority[priority_index][0]] = n

                priority_index = 0
                checked_items = 0
                time += 1
        
        return time



        
