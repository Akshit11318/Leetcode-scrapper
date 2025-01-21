## Minimum Moves to Equal Array Elements II

**Problem Link:** https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description

**Problem Statement:**
- Input: A non-empty integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`.
- Expected Output: The minimum number of moves required to make all array elements equal.
- Key requirements: Find the median of the array and calculate the total moves required to make all elements equal to the median.
- Example test cases:
  - Input: `nums = [1,2,3]`
    - Output: `2`
    - Explanation: Move one step from 1 to 2, and one step from 3 to 2.
  - Input: `nums = [1,10,2,9]`
    - Output: `16`
    - Explanation: Move one step from 1 to 2, 8 steps from 10 to 2, one step from 2 to 2, and 6 steps from 9 to 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the total moves required for each possible target value in the array.
- Step-by-step breakdown:
  1. Iterate over each possible target value in the array.
  2. For each target value, calculate the total moves required to make all elements equal to the target value.
  3. Keep track of the minimum total moves required.

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        int minMoves = INT_MAX;
        
        for (int i = 0; i < n; i++) {
            int totalMoves = 0;
            for (int j = 0; j < n; j++) {
                totalMoves += abs(nums[j] - nums[i]);
            }
            minMoves = min(minMoves, totalMoves);
        }
        
        return minMoves;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have a nested loop structure, where for each element, we calculate the total moves required.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum total moves.
> - **Why these complexities occur:** The brute force approach involves iterating over each possible target value and calculating the total moves required, resulting in a quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to find the median of the array, as the median is the value that minimizes the sum of absolute differences with all other values.
- Detailed breakdown:
  1. Sort the array in ascending order.
  2. If the array has an odd length, the median is the middle element. If the array has an even length, the median can be either of the two middle elements, as the problem allows for integer values.
  3. Calculate the total moves required to make all elements equal to the median.

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int median = nums[n / 2];
        
        int totalMoves = 0;
        for (int num : nums) {
            totalMoves += abs(num - median);
        }
        
        return totalMoves;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we sort the array, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total moves and the median.
> - **Optimality proof:** The optimal solution involves finding the median of the array, which is the value that minimizes the sum of absolute differences with all other values. This is because the median is the value that has the minimum sum of absolute deviations, which is a well-known property in statistics.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of the median to minimize the sum of absolute differences.
- The problem-solving pattern identified is to find the optimal value that minimizes the total moves required.
- The optimization technique learned is to use the median instead of iterating over all possible target values.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach, which can result in a quadratic time complexity.
- An edge case to watch for is when the array has an even length, as the median can be either of the two middle elements.
- A performance pitfall is to use an inefficient sorting algorithm, which can result in a higher time complexity.