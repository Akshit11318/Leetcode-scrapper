## Longest Square Streak in an Array

**Problem Link:** https://leetcode.com/problems/longest-square-streak-in-an-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `1 <= nums[i] <= 10^9`.
- Expected Output: The length of the longest streak of consecutive square numbers in the array.
- Key Requirements: Identify sequences of square numbers in the array and determine the longest streak.

**Example Test Cases:**
- For `nums = [4, 3, 6, 16, 8, 9]`, the longest square streak is `[4, 16, 9]`, so the output is `3`.
- For `nums = [2, 3, 5, 6, 7]`, there is no square streak, so the output is `1`.

---

### Brute Force Approach

**Explanation:**
- Start by checking every possible sequence of numbers in the array to see if they form a sequence of consecutive square numbers.
- For each sequence, verify if each number is a square number and if the next number in the sequence is the next square number.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

int longestSquareStreak(std::vector<int>& nums) {
    if (nums.size() == 0) return 0;
    
    int maxStreak = 1;
    for (int i = 0; i < nums.size(); i++) {
        int streak = 1;
        int prevSquare = nums[i];
        for (int j = i + 1; j < nums.size(); j++) {
            double sqrt = std::sqrt(nums[j]);
            if (sqrt == std::floor(sqrt) && sqrt * sqrt == nums[j] && sqrt == std::sqrt(prevSquare) + 1) {
                streak++;
                prevSquare = nums[j];
            }
        }
        maxStreak = std::max(maxStreak, streak);
    }
    
    if (maxStreak == 1) {
        for (int num : nums) {
            if (std::sqrt(num) != std::floor(std::sqrt(num))) {
                return 1;
            }
        }
    }
    
    return maxStreak;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially scan the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store variables.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity. The space complexity is constant because we do not use any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- To optimize, we can use a `set` to store the numbers in the array for efficient lookup. Then, for each number, we check if it's a square and if the next square number is in the set.
- We keep track of the longest streak found so far.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <cmath>

int longestSquareStreak(std::vector<int>& nums) {
    if (nums.size() == 0) return 0;
    
    std::set<int> numSet(nums.begin(), nums.end());
    int maxStreak = 1;
    
    for (int num : numSet) {
        if (std::sqrt(num) != std::floor(std::sqrt(num))) continue;
        
        int streak = 1;
        int current = num;
        while (numSet.find(current + (std::sqrt(current) + 1) * (std::sqrt(current) + 1)) != numSet.end()) {
            streak++;
            current = (std::sqrt(current) + 1) * (std::sqrt(current) + 1);
        }
        
        if (streak > 1) maxStreak = std::max(maxStreak, streak);
    }
    
    if (maxStreak == 1) {
        for (int num : nums) {
            if (std::sqrt(num) == std::floor(std::sqrt(num))) {
                return 1;
            }
        }
    }
    
    return maxStreak;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of elements in the array and $m$ is the maximum number of iterations in the while loop for any number. However, since the while loop is dependent on the value of the numbers and not directly on $n$, we can consider this as an optimization over the brute force approach.
> - **Space Complexity:** $O(n)$, for storing the numbers in the set.
> - **Optimality proof:** This approach is more efficient because it avoids unnecessary comparisons by directly checking for the presence of the next square number in the set, reducing the time complexity significantly for large inputs.

---

### Final Notes

**Learning Points:**
- The importance of using efficient data structures like `set` for lookup operations.
- How to approach problems involving sequences and streaks in arrays.
- Optimization techniques such as reducing the number of comparisons and using mathematical properties (like square numbers) to simplify the problem.

**Mistakes to Avoid:**
- Not considering the mathematical properties of the problem, leading to inefficient solutions.
- Not optimizing the solution by reducing unnecessary comparisons or using more efficient data structures.
- Not handling edge cases properly, such as empty arrays or arrays with no square numbers.