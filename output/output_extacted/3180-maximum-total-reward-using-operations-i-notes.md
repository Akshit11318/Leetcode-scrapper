## Maximum Total Reward Using Operations I

**Problem Link:** https://leetcode.com/problems/maximum-total-reward-using-operations-i/description

**Problem Statement:**
- Given an array of integers `nums` and two operations: 
    1. Multiply the current number by 2.
    2. Increment the current number by 1.
- The goal is to maximize the total reward, which is the sum of the numbers after performing the operations.
- The constraint is that the operations can only be performed on the current number.
- The input format is an array of integers `nums`, and the output format is the maximum total reward that can be achieved.
- Key requirements and edge cases to consider include:
    - Handling arrays of varying lengths.
    - Considering the impact of the operations on the total reward.
- Example test cases with explanations:
    - For the input `[1, 2, 3]`, the maximum total reward is `12`, achieved by multiplying each number by 2 and then incrementing each number by 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of operations for each number in the array and calculate the total reward for each combination.
- The step-by-step breakdown of the solution involves:
    1. Generating all possible combinations of operations for each number.
    2. Calculating the total reward for each combination.
    3. Keeping track of the maximum total reward found.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTotalReward(std::vector<int>& nums) {
    int maxReward = 0;
    int n = nums.size();
    
    // Generate all possible combinations of operations
    for (int i = 0; i < (1 << n); i++) {
        int reward = 0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                // Multiply the current number by 2
                reward += nums[j] * 2;
            } else {
                // Increment the current number by 1
                reward += nums[j] + 1;
            }
        }
        maxReward = std::max(maxReward, reward);
    }
    
    return maxReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible combinations of operations, which is $2^n$, and for each combination, we calculate the total reward, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum total reward and the current reward.
> - **Why these complexities occur:** The time complexity is high because we try all possible combinations of operations, which grows exponentially with the length of the input array. The space complexity is low because we only need to keep track of a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can use a greedy approach to maximize the total reward.
- The detailed breakdown of the approach involves:
    1. Sorting the input array in descending order.
    2. Multiplying the largest numbers by 2 to maximize the total reward.
    3. Incrementing the remaining numbers by 1 to further increase the total reward.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTotalReward(std::vector<int>& nums) {
    std::sort(nums.rbegin(), nums.rend());
    int maxReward = 0;
    int n = nums.size();
    
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            // Multiply the current number by 2
            maxReward += nums[i] * 2;
        } else {
            // Increment the current number by 1
            maxReward += nums[i] + 1;
        }
    }
    
    return maxReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we sort the input array, which takes $O(n \log n)$ time, and then iterate through the sorted array to calculate the total reward, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum total reward.
> - **Optimality proof:** This approach is optimal because it maximizes the total reward by multiplying the largest numbers by 2 and incrementing the remaining numbers by 1. This greedy approach ensures that we get the maximum possible total reward.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy approach, sorting.
- Problem-solving patterns identified: maximizing the total reward by multiplying the largest numbers by 2 and incrementing the remaining numbers by 1.
- Optimization techniques learned: using a greedy approach to solve the problem efficiently.
- Similar problems to practice: other problems that involve maximizing a total reward or score using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: not sorting the input array correctly, not handling edge cases properly.
- Edge cases to watch for: empty input array, input array with a single element.
- Performance pitfalls: using an inefficient algorithm that has a high time complexity.
- Testing considerations: testing the solution with different input arrays, including edge cases and large input arrays.