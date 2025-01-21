## Maximum Fruits Harvested After At Most K Steps

**Problem Link:** https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description

**Problem Statement:**
- Input format and constraints: Given a `fruits` array representing the fruits at each position and an integer `k`, find the maximum number of fruits that can be harvested after at most `k` steps.
- Expected output format: The maximum number of fruits that can be harvested.
- Key requirements and edge cases to consider: The fruits array can be empty, and the value of `k` can be 0 or greater than the length of the fruits array.
- Example test cases with explanations:
  - `fruits = [1, 2, 3], k = 3` should return `3` because we can harvest all fruits in 3 steps.
  - `fruits = [1, 2, 3], k = 1` should return `1` because we can only harvest one fruit in 1 step.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible combinations of harvesting fruits and check if we can harvest them within `k` steps.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of fruits harvested.
  2. Generate all possible combinations of harvesting fruits.
  3. For each combination, calculate the number of steps required to harvest the fruits.
  4. If the number of steps is less than or equal to `k`, update the maximum number of fruits harvested.
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations and check if they meet the condition.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxTotalFruits(std::vector<std::vector<int>>& fruits, int k) {
        int maxFruits = 0;
        for (int i = 0; i < fruits.size(); i++) {
            int currentFruits = 0;
            int steps = 0;
            for (int j = i; j < fruits.size(); j++) {
                currentFruits += fruits[j][1];
                steps += fruits[j][0] - fruits[i][0];
                if (steps > k) break;
                maxFruits = std::max(maxFruits, currentFruits);
            }
        }
        return maxFruits;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of fruits, because we have two nested loops to generate all combinations.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum number of fruits harvested.
> - **Why these complexities occur:** The time complexity is quadratic because we have two nested loops, and the space complexity is constant because we only use a few variables to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to find the maximum number of fruits that can be harvested within `k` steps.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the fruits array.
  2. Initialize a variable to store the maximum number of fruits harvested.
  3. Move the `right` pointer to the right and add the fruits at the `right` position to the current total.
  4. If the distance between the `left` and `right` pointers is greater than `k`, move the `left` pointer to the right until the distance is less than or equal to `k`.
  5. Update the maximum number of fruits harvested.
- Proof of optimality: This approach is optimal because it only considers the fruits that can be harvested within `k` steps, and it does so in a single pass through the fruits array.

```cpp
class Solution {
public:
    int maxTotalFruits(std::vector<std::vector<int>>& fruits, int k) {
        int maxFruits = 0;
        int left = 0;
        int currentFruits = 0;
        for (int right = 0; right < fruits.size(); right++) {
            currentFruits += fruits[right][1];
            while (fruits[right][0] - fruits[left][0] > k) {
                currentFruits -= fruits[left][1];
                left++;
            }
            maxFruits = std::max(maxFruits, currentFruits);
        }
        return maxFruits;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of fruits, because we only need to make a single pass through the fruits array.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum number of fruits harvested.
> - **Optimality proof:** This approach is optimal because it only considers the fruits that can be harvested within `k` steps, and it does so in a single pass through the fruits array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, two-pointer technique.
- Problem-solving patterns identified: Using a sliding window to find the maximum number of elements that meet a certain condition.
- Optimization techniques learned: Reducing the time complexity from quadratic to linear by using a single pass through the fruits array.
- Similar problems to practice: Other problems that involve finding the maximum number of elements that meet a certain condition, such as the maximum subarray problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the edge cases, such as an empty fruits array or a value of `k` that is 0 or greater than the length of the fruits array.
- Edge cases to watch for: The fruits array can be empty, and the value of `k` can be 0 or greater than the length of the fruits array.
- Performance pitfalls: Using a quadratic time complexity approach when a linear time complexity approach is possible.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.