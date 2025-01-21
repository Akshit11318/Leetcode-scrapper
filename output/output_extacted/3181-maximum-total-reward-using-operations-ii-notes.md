## Maximum Total Reward Using Operations II
**Problem Link:** https://leetcode.com/problems/maximum-total-reward-using-operations-ii/description

**Problem Statement:**
- Input format and constraints: Given an array `rewards` of size `n`, where `n` is a positive integer, and two integers `timeLimit` and `k`, find the maximum total reward that can be obtained using operations II, where in one operation, you can remove the smallest or the largest element from the array.
- Expected output format: The maximum total reward.
- Key requirements and edge cases to consider: The array `rewards` is not sorted, and the operations can be performed in any order. The time limit `timeLimit` and the number of operations `k` are given as inputs.
- Example test cases with explanations: For example, given `rewards = [1, 2, 3, 4, 5]`, `timeLimit = 3`, and `k = 2`, the maximum total reward is `9`, which can be obtained by removing the smallest and largest elements from the array.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of removing the smallest and largest elements from the array.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of removing `k` elements from the array.
  2. For each combination, calculate the total reward by summing up the remaining elements in the array.
  3. Keep track of the maximum total reward obtained.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible combinations and find the maximum total reward.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTotalReward(std::vector<int>& rewards, int timeLimit, int k) {
    int n = rewards.size();
    int maxReward = 0;
    std::sort(rewards.begin(), rewards.end());
    for (int i = 0; i <= k; i++) {
        for (int j = 0; j <= k - i; j++) {
            int left = i;
            int right = j;
            int totalReward = 0;
            for (int index = left; index < n - right; index++) {
                totalReward += rewards[index];
            }
            maxReward = std::max(maxReward, totalReward);
        }
    }
    return maxReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the array `rewards`, and $k$ is the number of operations. This is because we are generating all possible combinations of removing `k` elements from the array and calculating the total reward for each combination.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array `rewards`. This is because we are only using a constant amount of space to store the maximum total reward and other variables.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to generate all possible combinations of removing `k` elements from the array. The space complexity occurs because we are only using a constant amount of space to store the maximum total reward and other variables.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to find the maximum total reward.
- Detailed breakdown of the approach:
  1. Sort the array `rewards` in ascending order.
  2. Initialize two pointers, `left` and `right`, to the beginning of the array.
  3. Initialize the maximum total reward to negative infinity.
  4. Iterate over the array using the `right` pointer.
  5. For each position of the `right` pointer, calculate the total reward by summing up the elements in the window `[left, right]`.
  6. Update the maximum total reward if the current total reward is greater.
  7. Move the `left` pointer to the right to reduce the window size and increase the total reward.
- Proof of optimality: The sliding window approach ensures that we consider all possible combinations of removing `k` elements from the array and find the maximum total reward.
- Why further optimization is impossible: The sliding window approach has a time complexity of $O(n \cdot k)$, which is optimal because we need to consider all possible combinations of removing `k` elements from the array.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTotalReward(std::vector<int>& rewards, int timeLimit, int k) {
    int n = rewards.size();
    int maxReward = 0;
    std::sort(rewards.begin(), rewards.end());
    for (int left = 0; left <= k; left++) {
        int totalReward = 0;
        for (int right = left; right < n; right++) {
            totalReward += rewards[right];
            if (right - left + 1 > k) {
                totalReward -= rewards[left];
                left++;
            }
            if (right - left + 1 == k + 1) {
                maxReward = std::max(maxReward, totalReward);
            }
        }
    }
    return maxReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the array `rewards`, and $k$ is the number of operations. This is because we are using a sliding window approach to find the maximum total reward.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array `rewards`. This is because we are only using a constant amount of space to store the maximum total reward and other variables.
> - **Optimality proof:** The sliding window approach ensures that we consider all possible combinations of removing `k` elements from the array and find the maximum total reward.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, sorting, and iteration.
- Problem-solving patterns identified: Using a sliding window approach to find the maximum total reward.
- Optimization techniques learned: Reducing the time complexity by using a sliding window approach.
- Similar problems to practice: Maximum subarray sum, minimum window subarray, and other sliding window problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases, and not using a sliding window approach.
- Edge cases to watch for: Empty array, `k` greater than `n`, and `timeLimit` less than `k`.
- Performance pitfalls: Using a brute force approach, not optimizing the solution, and not using a sliding window approach.
- Testing considerations: Testing with different inputs, edge cases, and boundary conditions.