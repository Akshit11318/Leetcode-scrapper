## Maximum Number of Tasks You Can Assign
**Problem Link:** https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description

**Problem Statement:**
- Input: Two arrays `tasks` and `workers`, where `tasks[i]` is the minimum requirement to complete the `i-th` task and `workers[j]` is the skill of the `j-th` worker.
- Constraints: Both arrays are non-empty and have the same length.
- Expected output: The maximum number of tasks that can be assigned to workers.
- Key requirements: A task can be assigned to a worker if the worker's skill is greater than or equal to the task's requirement.
- Edge cases: If no tasks can be assigned, return 0.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible assignment of tasks to workers.
- For each task, we find a worker with sufficient skill and assign the task to that worker.
- We continue this process until no more tasks can be assigned.

```cpp
class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int n = tasks.size();
        int maxTasks = 0;
        
        // Generate all possible subsets of tasks
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> subset;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.push_back(tasks[i]);
                }
            }
            
            // Check if the subset can be assigned to workers
            if (canAssign(subset, workers, pills, strength)) {
                maxTasks = max(maxTasks, (int)subset.size());
            }
        }
        
        return maxTasks;
    }
    
    bool canAssign(vector<int>& subset, vector<int>& workers, int pills, int strength) {
        int n = subset.size();
        sort(subset.begin(), subset.end(), greater<int>());
        sort(workers.begin(), workers.end(), greater<int>());
        
        for (int i = 0; i < n; i++) {
            if (workers[i] < subset[i]) {
                if (pills == 0) {
                    return false;
                }
                pills--;
                i--; // Try to assign the task to the next worker
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \log n)$, where $n$ is the number of tasks. The reason is that we generate all possible subsets of tasks, and for each subset, we sort the tasks and workers, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tasks. The reason is that we need to store the subset of tasks.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because we generate all possible subsets of tasks. The sorting operation contributes to the $O(n \log n)$ factor.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use binary search to find the maximum number of tasks that can be assigned.
- We use two pointers, `low` and `high`, to represent the range of possible assignments.
- We calculate the midpoint `mid` and check if we can assign `mid` tasks to workers.
- If we can, we update `low` to `mid + 1`. Otherwise, we update `high` to `mid - 1`.

```cpp
class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int n = tasks.size();
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        
        int low = 0;
        int high = n;
        
        while (low < high) {
            int mid = (low + high + 1) / 2;
            
            if (canAssign(mid, tasks, workers, pills, strength)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        
        return low;
    }
    
    bool canAssign(int k, vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int j = workers.size() - 1;
        int pillUsed = 0;
        
        for (int i = k - 1; i >= 0; i--) {
            if (workers[j] < tasks[i]) {
                if (pillUsed == pills) {
                    return false;
                }
                pillUsed++;
                j--;
            } else {
                j--;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. The reason is that we use binary search to find the maximum number of tasks, and for each iteration, we check if we can assign `mid` tasks to workers, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, where $n$ is the number of tasks. The reason is that we only use a constant amount of space to store the pointers and variables.
> - **Optimality proof:** The optimal approach is optimal because we use binary search to find the maximum number of tasks, which reduces the search space from $O(2^n)$ to $O(\log n)$. The `canAssign` function checks if we can assign `mid` tasks to workers in $O(n)$ time, which is the best possible time complexity for this problem.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is binary search, which is used to find the maximum number of tasks that can be assigned.
- The problem-solving pattern identified is to use a `canAssign` function to check if we can assign a certain number of tasks to workers.
- The optimization technique learned is to use binary search to reduce the search space from $O(2^n)$ to $O(\log n)$.

**Mistakes to Avoid:**
- A common implementation error is to forget to update the `low` and `high` pointers correctly in the binary search loop.
- An edge case to watch for is when the number of tasks is 0, in which case we should return 0.
- A performance pitfall is to use a brute force approach, which has an exponential time complexity.