## Minimum Cost to Hire K Workers
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description

**Problem Statement:**
- Input: An array of quality `quality` and an array of wage `wage` for each worker, and an integer `k` representing the number of workers to hire.
- Output: The minimum cost to hire `k` workers.
- Key requirements: Each worker's quality and wage are given. The cost to hire a worker is determined by their wage and the quality of the workers hired so far.
- Example test cases:
  - Input: `quality = [10,20,5]`, `wage = [70,50,30]`, `k = 2`
  - Output: `105.0`
  - Explanation: We can hire the worker with quality 10 for 70 dollars, and the worker with quality 5 for 30 dollars, for a total cost of 100 dollars. However, we need to hire 2 workers, so we also hire the worker with quality 20 for 50 dollars, for a total cost of 100 + (20/10) * 70 = 105 dollars.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the cost of hiring each possible combination of `k` workers and find the minimum cost.
- We can use a recursive function to generate all possible combinations of workers and calculate the cost for each combination.
- However, this approach is not efficient because it has a high time complexity due to the recursive function calls.

```cpp
#include <vector>
#include <algorithm>

double mincostToHireWorkers(std::vector<int>& quality, std::vector<int>& wage, int k) {
    int n = quality.size();
    std::vector<int> indices(n);
    for (int i = 0; i < n; i++) {
        indices[i] = i;
    }
    double minCost = std::numeric_limits<double>::max();
    std::sort(indices.begin(), indices.end(), [&quality, &wage](int a, int b) {
        return (wage[a] * 1.0 / quality[a]) < (wage[b] * 1.0 / quality[b]);
    });
    for (int i = 0; i < (1 << n); i++) {
        int count = 0;
        double totalQuality = 0.0;
        double totalCost = 0.0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                count++;
                totalQuality += quality[indices[j]];
                totalCost += wage[indices[j]];
            }
        }
        if (count == k) {
            double cost = totalCost;
            minCost = std::min(minCost, cost);
        }
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of workers, due to the recursive function calls.
> - **Space Complexity:** $O(n)$, where $n$ is the number of workers, due to the recursive function calls.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of workers, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- We can use a priority queue to keep track of the workers with the highest quality-to-wage ratio.
- We calculate the cost of hiring each worker based on their quality and the quality of the workers already hired.
- We use a heap to keep track of the workers with the highest cost and remove the worker with the highest cost when the number of workers exceeds `k`.
- This approach ensures that we always hire the workers with the lowest cost.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

double mincostToHireWorkers(std::vector<int>& quality, std::vector<int>& wage, int k) {
    int n = quality.size();
    std::vector<std::pair<double, int>> workers(n);
    for (int i = 0; i < n; i++) {
        workers[i] = {(wage[i] * 1.0 / quality[i]), quality[i]};
    }
    std::sort(workers.begin(), workers.end());
    double minCost = std::numeric_limits<double>::max();
    std::priority_queue<int> pq;
    double totalQuality = 0.0;
    for (int i = 0; i < n; i++) {
        pq.push(workers[i].second);
        totalQuality += workers[i].second;
        if (pq.size() > k) {
            totalQuality -= pq.top();
            pq.pop();
        }
        if (pq.size() == k) {
            minCost = std::min(minCost, workers[i].first * totalQuality);
        }
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of workers, due to the sorting and priority queue operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of workers, due to the priority queue and sorting.
> - **Optimality proof:** This approach ensures that we always hire the workers with the lowest cost by using a priority queue to keep track of the workers with the highest quality-to-wage ratio.

---

### Final Notes

**Learning Points:**
- The importance of using data structures like priority queues to solve problems efficiently.
- The need to consider the quality-to-wage ratio when hiring workers.
- The use of sorting and priority queues to solve problems involving ratios and costs.

**Mistakes to Avoid:**
- Using brute force approaches for problems with large inputs.
- Not considering the quality-to-wage ratio when hiring workers.
- Not using data structures like priority queues to solve problems efficiently.