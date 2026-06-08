import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        priority = [[-freq[task], task] for task in freq]
        heapq.heapify(priority)
        print(priority)
        unique_tasks_remaining = len(priority)

        wait_times = {}
        time = 0
        temp = []
        j = 0

        while unique_tasks_remaining:
            # print(time, wait_times, priority)
            print(j)
            j += 1
            # if j == 11:
            #     break
            if priority and priority[0][1] in wait_times:
                print('h')
                temp.append(heapq.heappop(priority))
            elif not priority:
                print('r')
                time += 1
                for task in list(wait_times.keys()):
                    if wait_times[task] == 1:
                        wait_times.pop(task)
                    else:
                        wait_times[task] -= 1
                priority = temp
                heapq.heapify(priority)
                temp = []
            else:
                print(unique_tasks_remaining, priority, wait_times, j)
                group = heapq.heappop(priority)
                pri_lvl, curr_task = -group[0], group[1]
                pri_lvl -= 1

                for task in list(wait_times.keys()):
                    if wait_times[task] == 1:
                        wait_times.pop(task)
                    else:
                        wait_times[task] -= 1

                if pri_lvl != 0:  
                    wait_times[curr_task] = n
                    temp.append([-pri_lvl, curr_task])
                else:
                    unique_tasks_remaining -= 1
                                
                for i in temp:
                    heapq.heappush(priority, i)
                temp = []
                time += 1
        
        return time



        
