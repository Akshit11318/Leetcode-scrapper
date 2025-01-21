## Total Cost to Hire K Workers
**Problem Link:** https://leetcode.com/problems/total-cost-to-hire-k-workers/description

**Problem Statement:**
- Input format and constraints: Given a list of `quality` and `wage` arrays representing the quality and wage of each worker, and an integer `K` representing the number of workers to hire, find the total cost to hire `K` workers.
- Expected output format: The minimum cost to hire `K` workers.
- Key requirements and edge cases to consider: The cost of hiring a worker is calculated as `wage[i] * (quality[j] / quality[i])`, where `i` is the worker being hired and `j` is the worker with the highest quality among the hired workers.
- Example test cases with explanations:
  - Example 1: `quality = [10,20,5]`, `wage = [70,50,30]`, `K = 2`, the minimum cost is `105.0`.
  - Example 2: `quality = [1,1,1]`, `wage = [70,68,38]`, `K = 2`, the minimum cost is `106.0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of hiring `K` workers and calculate the total cost for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `K` workers from the given list of workers.
  2. For each combination, calculate the total cost by iterating over the workers and calculating the cost of hiring each worker based on the worker with the highest quality in the combination.
  3. Keep track of the minimum total cost found among all combinations.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions, but it is inefficient due to its high time complexity.

```cpp
#include <vector>
#include <algorithm>

double mincostToHireWorkers(std::vector<int>& quality, std::vector<int>& wage, int K) {
    int n = quality.size();
    std::vector<std::pair<int, int>> workers;
    for (int i = 0; i < n; i++) {
        workers.emplace_back(quality[i], wage[i]);
    }

    double minCost = 1e9;
    std::sort(workers.begin(), workers.end(), [](const auto& a, const auto& b) {
        return (double)a.second / a.first < (double)b.second / b.first;
    });

    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) != K) continue;
        double totalCost = 0;
        int maxQuality = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) continue;
            totalCost += (double)workers[i].second * (double)maxQuality / (double)workers[i].first;
            maxQuality = std::max(maxQuality, workers[i].first);
        }
        minCost = std::min(minCost, totalCost);
    }

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of workers.
> - **Space Complexity:** $O(n)$, for storing the workers.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of hiring `K` workers, resulting in a high time complexity. The space complexity is due to the storage of the workers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to keep track of the workers with the highest quality and calculate the total cost based on the ratio of wage to quality.
- Detailed breakdown of the approach:
  1. Create a vector of pairs to store the ratio of wage to quality for each worker.
  2. Sort the vector based on the ratio.
  3. Use a priority queue to keep track of the workers with the highest quality.
  4. Iterate over the sorted vector and calculate the total cost based on the ratio and the quality of the workers in the priority queue.
- Proof of optimality: This approach has a time complexity of $O(n \log n)$, which is optimal for this problem.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

double mincostToHireWorkers(std::vector<int>& quality, std::vector<int>& wage, int K) {
    int n = quality.size();
    std::vector<std::pair<double, int>> workers;
    for (int i = 0; i < n; i++) {
        workers.emplace_back((double)wage[i] / quality[i], quality[i]);
    }

    std::sort(workers.begin(), workers.end());
    std::priority_queue<int> pq;
    double minCost = 1e9;
    double totalQuality = 0;

    for (auto& worker : workers) {
        pq.push(worker.second);
        totalQuality += worker.second;
        if (pq.size() > K) {
            totalQuality -= pq.top();
            pq.pop();
        }
        if (pq.size() == K) {
            minCost = std::min(minCost, totalQuality * worker.first);
        }
    }

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of workers.
> - **Space Complexity:** $O(n)$, for storing the workers and the priority queue.
> - **Optimality proof:** This approach has a time complexity of $O(n \log n)$, which is optimal for this problem. The priority queue ensures that the workers with the highest quality are always considered, resulting in the minimum total cost.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, sorting, and iteration.
- Problem-solving patterns identified: Using a priority queue to keep track of the workers with the highest quality and calculating the total cost based on the ratio of wage to quality.
- Optimization techniques learned: Using a priority queue to reduce the time complexity from $O(2^n \cdot n)$ to $O(n \log n)$.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the workers based on the ratio of wage to quality, not using a priority queue to keep track of the workers with the highest quality.
- Edge cases to watch for: When the number of workers is equal to `K`, the total cost is calculated based on the ratio of the worker with the highest quality.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it produces the correct output.