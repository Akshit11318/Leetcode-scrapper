## Kth Smallest Amount with Single Denomination Combination

**Problem Link:** https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description

**Problem Statement:**
- Input format and constraints: Given an integer array `amount` where `amount[i]` is the amount of money that the `i-th` person has, and an integer `k`, return the `k-th` smallest amount that can be achieved by combining the money of any subset of the people.
- Expected output format: The `k-th` smallest amount that can be achieved.
- Key requirements and edge cases to consider: 
  - The input array `amount` can be empty.
  - The value of `k` can be larger than the total number of subsets.
  - The amount of money that each person has can be large.
- Example test cases with explanations:
  - If `amount = [1, 2, 3]` and `k = 3`, the output should be `3` because the subsets are `[1], [2], [3]`, and the third smallest amount is `3`.
  - If `amount = [1, 2, 3]` and `k = 4`, the output should be `4` because the subsets are `[1], [2], [3], [1 + 2], [1 + 3], [2 + 3], [1 + 2 + 3]`, and the fourth smallest amount is `4`.

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible subsets of the input array `amount`, calculate the sum of each subset, and then sort these sums to find the `k-th` smallest amount.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array `amount`.
  2. Calculate the sum of each subset.
  3. Store the sums in a list or array.
  4. Sort the list of sums in ascending order.
  5. Return the `k-th` smallest sum.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int kthSmallestAmount(std::vector<int>& amount, int k) {
    // Generate all possible subsets of the input array amount
    int n = amount.size();
    int totalSubsets = 1 << n; // 2^n
    std::vector<int> subsetSums;

    for (int i = 0; i < totalSubsets; i++) {
        int subsetSum = 0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                subsetSum += amount[j];
            }
        }
        subsetSums.push_back(subsetSum);
    }

    // Sort the list of sums in ascending order
    std::sort(subsetSums.begin(), subsetSums.end());

    // Return the k-th smallest sum
    return subsetSums[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \log 2^n)$, where $n$ is the number of elements in the input array `amount`. The reason is that we generate $2^n$ subsets and sort them, which takes $O(2^n \log 2^n)$ time.
> - **Space Complexity:** $O(2^n)$, where $n$ is the number of elements in the input array `amount`. The reason is that we store the sums of all subsets in a list.
> - **Why these complexities occur:** The brute force approach generates all possible subsets, which leads to exponential time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `priority_queue` to keep track of the smallest amounts.
- Detailed breakdown of the approach:
  1. Initialize a `priority_queue` to store the smallest amounts.
  2. Push the initial amount `0` into the `priority_queue`.
  3. Pop the smallest amount from the `priority_queue` and push it back with each of the amounts in the input array `amount`.
  4. Repeat step 3 until we have popped `k` amounts from the `priority_queue`.
  5. The `k-th` smallest amount is the last amount popped from the `priority_queue`.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

int kthSmallestAmount(std::vector<int>& amount, int k) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    std::unordered_set<int> visited;

    pq.push(0);
    visited.insert(0);

    for (int i = 0; i < k; i++) {
        int currentAmount = pq.top();
        pq.pop();

        for (int a : amount) {
            int nextAmount = currentAmount + a;
            if (visited.find(nextAmount) == visited.end()) {
                pq.push(nextAmount);
                visited.insert(nextAmount);
            }
        }
    }

    return pq.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \log k)$, where $k$ is the input parameter. The reason is that we use a `priority_queue` to keep track of the smallest amounts.
> - **Space Complexity:** $O(k)$, where $k$ is the input parameter. The reason is that we store the smallest amounts in a `priority_queue` and an `unordered_set`.
> - **Optimality proof:** This approach is optimal because we only generate the smallest amounts and keep track of them using a `priority_queue`. This ensures that we find the `k-th` smallest amount in the minimum possible time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `priority_queue` to keep track of the smallest amounts.
- Problem-solving patterns identified: Generating all possible subsets and sorting them is not efficient, but using a `priority_queue` can solve the problem efficiently.
- Optimization techniques learned: Using a `priority_queue` to keep track of the smallest amounts.
- Similar problems to practice: Other problems that involve generating all possible subsets and finding the smallest or largest amount.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `priority_queue` to keep track of the smallest amounts.
- Edge cases to watch for: The input array `amount` can be empty, and the value of `k` can be larger than the total number of subsets.
- Performance pitfalls: Generating all possible subsets and sorting them can lead to exponential time and space complexity.
- Testing considerations: Test the function with different input arrays `amount` and values of `k` to ensure that it works correctly.