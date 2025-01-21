## Find Minimum Time to Finish All Jobs

**Problem Link:** https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description

**Problem Statement:**
- Given an array of integers `jobs` where each integer represents the time it takes to complete a job, and an integer `k` which represents the number of workers, return the minimum time it takes to finish all jobs.
- Each worker can only work on one job at a time, and once a worker starts a job, they must finish it before starting a new job.
- The input array `jobs` will have at least one element and at most 10^5 elements.
- The input integer `k` will be between 1 and 10^5.

**Expected Output Format:**
- The function should return the minimum time it takes to finish all jobs.

**Key Requirements and Edge Cases to Consider:**
- The function should handle cases where the number of workers is less than or equal to the number of jobs.
- The function should handle cases where the number of workers is greater than the number of jobs.
- The function should handle cases where all jobs have the same time requirement.
- The function should handle cases where the time requirements of the jobs are in descending order.
- The function should handle cases where the time requirements of the jobs are in ascending order.

**Example Test Cases with Explanations:**
- If `jobs = [3, 2, 3]` and `k = 3`, the function should return `3` because each worker can work on one job at a time, and the maximum time it takes to finish a job is `3`.
- If `jobs = [1, 2, 4, 7, 8]` and `k = 2`, the function should return `15` because the two workers can work on the two longest jobs (`7` and `8`) in parallel, and then work on the remaining jobs (`1`, `2`, and `4`) in parallel.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves generating all possible combinations of jobs and workers, and calculating the time it takes to finish all jobs for each combination.
- The approach uses a recursive function to generate all possible combinations, and a priority queue to keep track of the worker who will finish their job the earliest.
- The time complexity of this approach is high because it generates all possible combinations of jobs and workers, which can be very large.

```cpp
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size();
        vector<int> workers(k, 0);
        return dfs(jobs, workers, 0, n, k);
    }
    
    int dfs(vector<int>& jobs, vector<int>& workers, int index, int n, int k) {
        if (index == n) {
            int maxTime = 0;
            for (int i = 0; i < k; i++) {
                maxTime = max(maxTime, workers[i]);
            }
            return maxTime;
        }
        
        int minTime = INT_MAX;
        for (int i = 0; i < k; i++) {
            if (workers[i] + jobs[index] < minTime) {
                workers[i] += jobs[index];
                minTime = min(minTime, dfs(jobs, workers, index + 1, n, k));
                workers[i] -= jobs[index];
            }
        }
        return minTime;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, where $n$ is the number of jobs and $k$ is the number of workers. This is because the function generates all possible combinations of jobs and workers.
> - **Space Complexity:** $O(n + k)$, where $n$ is the number of jobs and $k$ is the number of workers. This is because the function uses a recursive call stack and a priority queue to keep track of the worker who will finish their job the earliest.
> - **Why these complexities occur:** The high time complexity occurs because the function generates all possible combinations of jobs and workers, which can be very large. The space complexity occurs because the function uses a recursive call stack and a priority queue to keep track of the worker who will finish their job the earliest.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a binary search algorithm to find the minimum time it takes to finish all jobs.
- The approach uses a helper function to check if it is possible to finish all jobs within a given time limit.
- The time complexity of this approach is much lower than the brute force approach because it uses a binary search algorithm to find the minimum time.

```cpp
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int low = *max_element(jobs.begin(), jobs.end());
        int high = accumulate(jobs.begin(), jobs.end(), 0);
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canFinish(jobs, k, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    
    bool canFinish(vector<int>& jobs, int k, int time) {
        int count = 0;
        int sum = 0;
        for (int i = 0; i < jobs.size(); i++) {
            if (sum + jobs[i] > time) {
                count++;
                sum = jobs[i];
            } else {
                sum += jobs[i];
            }
        }
        return count < k;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of jobs and $m$ is the sum of all job times. This is because the function uses a binary search algorithm to find the minimum time.
> - **Space Complexity:** $O(1)$, because the function only uses a constant amount of space to store the low and high values.
> - **Optimality proof:** The binary search algorithm is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity. The helper function `canFinish` is also optimal because it uses a single pass through the jobs array to check if it is possible to finish all jobs within a given time limit.

---

### Final Notes

**Learning Points:**
- The importance of using a binary search algorithm to find the minimum time it takes to finish all jobs.
- The use of a helper function to check if it is possible to finish all jobs within a given time limit.
- The optimization of the time complexity by reducing the search space by half at each step.

**Mistakes to Avoid:**
- Using a brute force approach that generates all possible combinations of jobs and workers.
- Not using a binary search algorithm to find the minimum time it takes to finish all jobs.
- Not optimizing the time complexity by reducing the search space by half at each step.