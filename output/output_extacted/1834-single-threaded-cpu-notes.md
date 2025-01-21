## Single Threaded CPU
**Problem Link:** https://leetcode.com/problems/single-threaded-cpu/description

**Problem Statement:**
- Input format: You are given a 2D integer array `tasks` where `tasks[i] = [enqueueTimei, processingTimei]`.
- Constraints: `1 <= tasks.length <= 10^5`, `1 <= enqueueTimei, processingTimei <= 10^5`.
- Expected output format: Return the order in which the CPU will process the tasks.
- Key requirements and edge cases to consider: Tasks are given as pairs of enqueue time and processing time. The CPU will process the tasks in the order that minimizes the average waiting time.
- Example test cases with explanations: For example, given `tasks = [[0,3],[1,2],[2,1],[6,2]]`, the output should be `[2,3,1,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the tasks based on their enqueue time and then process them one by one.
- Step-by-step breakdown of the solution:
  1. Sort the tasks based on their enqueue time.
  2. Initialize an empty queue to store the tasks that are waiting to be processed.
  3. Iterate over the sorted tasks and add them to the queue.
  4. Dequeue a task from the queue and process it.
  5. Repeat steps 3 and 4 until the queue is empty.
- Why this approach comes to mind first: This approach seems straightforward because it processes the tasks in the order they are enqueued.

```cpp
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct Task {
    int enqueueTime;
    int processingTime;
    int index;
};

struct CompareTasks {
    bool operator()(const Task& a, const Task& b) {
        if (a.enqueueTime == b.enqueueTime) {
            return a.processingTime > b.processingTime;
        }
        return a.enqueueTime > b.enqueueTime;
    }
};

vector<int> getOrder(vector<vector<int>>& tasks) {
    vector<Task> taskList;
    for (int i = 0; i < tasks.size(); i++) {
        Task task;
        task.enqueueTime = tasks[i][0];
        task.processingTime = tasks[i][1];
        task.index = i;
        taskList.push_back(task);
    }

    sort(taskList.begin(), taskList.end(), [](const Task& a, const Task& b) {
        return a.enqueueTime < b.enqueueTime;
    });

    priority_queue<Task, vector<Task>, CompareTasks> pq;
    vector<int> result;
    int currentTime = 0;

    for (int i = 0; i < taskList.size(); i++) {
        while (!pq.empty() && pq.top().enqueueTime <= currentTime) {
            Task task = pq.top();
            pq.pop();
            result.push_back(task.index);
            currentTime += task.processingTime;
        }

        if (taskList[i].enqueueTime > currentTime) {
            currentTime = taskList[i].enqueueTime;
        }

        pq.push(taskList[i]);
    }

    while (!pq.empty()) {
        Task task = pq.top();
        pq.pop();
        result.push_back(task.index);
        currentTime += task.processingTime;
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. This is because we sort the tasks and use a priority queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tasks. This is because we store all tasks in a vector and a priority queue.
> - **Why these complexities occur:** The time complexity occurs because we sort the tasks and use a priority queue, which has a logarithmic time complexity for insertion and deletion operations. The space complexity occurs because we store all tasks in a vector and a priority queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the tasks that are waiting to be processed. The priority queue should be sorted based on the processing time of the tasks. If two tasks have the same processing time, we should process the task that was enqueued first.
- Detailed breakdown of the approach:
  1. Sort the tasks based on their enqueue time.
  2. Initialize an empty priority queue to store the tasks that are waiting to be processed.
  3. Iterate over the sorted tasks and add them to the priority queue.
  4. Dequeue a task from the priority queue and process it.
  5. Repeat steps 3 and 4 until the priority queue is empty.
- Proof of optimality: This approach is optimal because it processes the tasks in the order that minimizes the average waiting time. By using a priority queue, we ensure that the task with the shortest processing time is processed first, which minimizes the waiting time for all tasks.

```cpp
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct Task {
    int enqueueTime;
    int processingTime;
    int index;
};

struct CompareTasks {
    bool operator()(const Task& a, const Task& b) {
        if (a.processingTime == b.processingTime) {
            if (a.enqueueTime == b.enqueueTime) {
                return a.index > b.index;
            }
            return a.enqueueTime > b.enqueueTime;
        }
        return a.processingTime > b.processingTime;
    }
};

vector<int> getOrder(vector<vector<int>>& tasks) {
    vector<Task> taskList;
    for (int i = 0; i < tasks.size(); i++) {
        Task task;
        task.enqueueTime = tasks[i][0];
        task.processingTime = tasks[i][1];
        task.index = i;
        taskList.push_back(task);
    }

    sort(taskList.begin(), taskList.end(), [](const Task& a, const Task& b) {
        return a.enqueueTime < b.enqueueTime;
    });

    priority_queue<Task, vector<Task>, CompareTasks> pq;
    vector<int> result;
    int currentTime = 0;

    int i = 0;
    while (i < taskList.size() || !pq.empty()) {
        while (i < taskList.size() && taskList[i].enqueueTime <= currentTime) {
            pq.push(taskList[i]);
            i++;
        }

        if (pq.empty()) {
            currentTime = taskList[i].enqueueTime;
        } else {
            Task task = pq.top();
            pq.pop();
            result.push_back(task.index);
            currentTime += task.processingTime;
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. This is because we sort the tasks and use a priority queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tasks. This is because we store all tasks in a vector and a priority queue.
> - **Optimality proof:** This approach is optimal because it processes the tasks in the order that minimizes the average waiting time. By using a priority queue, we ensure that the task with the shortest processing time is processed first, which minimizes the waiting time for all tasks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, sorting, and greedy algorithm.
- Problem-solving patterns identified: Using a priority queue to store tasks that are waiting to be processed, and sorting the tasks based on their enqueue time.
- Optimization techniques learned: Using a priority queue to minimize the average waiting time.
- Similar problems to practice: Scheduling problems, such as scheduling tasks on a single machine or multiple machines.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when the priority queue is empty.
- Edge cases to watch for: When the priority queue is empty, and when two tasks have the same processing time.
- Performance pitfalls: Not using a priority queue, which can lead to a higher time complexity.
- Testing considerations: Testing the code with different inputs, such as different task lists and different enqueue times.