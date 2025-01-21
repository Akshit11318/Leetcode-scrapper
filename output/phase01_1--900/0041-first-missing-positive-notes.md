## First Missing Positive
**Problem Link:** https://leetcode.com/problems/first-missing-positive/description

**Problem Statement:**
- Input format: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`.
- Expected output format: The smallest positive integer that does not appear in `nums`.
- Key requirements and edge cases to consider: Handling zeros, negatives, duplicates, and the array being empty or containing a single element.
- Example test cases with explanations:
  - `nums = [1, 2, 0]`, expected output: `3`.
  - `nums = [3, 4, -1, 1]`, expected output: `2`.
  - `nums = [7, 8, 9, 11, 12]`, expected output: `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible positive integers starting from 1 and check if each one exists in the array.
- Step-by-step breakdown of the solution:
  1. Create a set from the array for efficient lookups.
  2. Iterate from 1 upwards, checking if each number exists in the set.
  3. Return the first number that does not exist in the set.
- Why this approach comes to mind first: It directly addresses the problem statement without requiring additional insights.

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int i = 1;
        while (numSet.count(i)) {
            i++;
        }
        return i;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the first missing positive integer. The set creation takes $O(n)$, and the while loop in the worst case iterates up to $m$, which is bounded by $n$ in this problem context because we are looking for the first missing positive integer.
> - **Space Complexity:** $O(n)$, for storing all elements of `nums` in the set.
> - **Why these complexities occur:** The set allows for constant time lookups, but its creation and the subsequent linear search for the first missing positive integer dictate the overall time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize the given array itself as extra space to mark the presence of numbers, thus avoiding additional space complexity.
- Detailed breakdown of the approach:
  1. Iterate through the array, for each number $i$ in the range $[1, n]$, use it as an index to mark its presence by negating the value at index $i-1$.
  2. A second pass through the array to find the first index $i$ which has a positive value at $i-1$, indicating $i$ is the first missing positive integer.
- Proof of optimality: This approach achieves $O(n)$ time complexity and $O(1)$ space complexity (not counting the input array), making it optimal for this problem.
- Why further optimization is impossible: We must at least read the input once, leading to a lower bound of $O(n)$ for time complexity.

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (1 <= nums[i] && nums[i] <= n && nums[nums[i] - 1] > 0) {
                swap(nums[nums[i] - 1], nums[i]);
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }
        return n + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as each element is potentially swapped once, and we make two passes through the array.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space.
> - **Optimality proof:** The approach minimizes both time and space complexities by leveraging the input array for marking presence and using a single pass for each necessary operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, swapping elements to mark presence, and two-pass algorithms.
- Problem-solving patterns identified: Utilizing the problem constraints to minimize space complexity and focusing on the specific requirements (first missing positive integer) to optimize the solution.
- Optimization techniques learned: Reducing space complexity by using the input array as extra space and minimizing the number of passes through the data.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like an empty array or not checking for the existence of numbers within the bounds of the array.
- Edge cases to watch for: Arrays containing only zeros, negatives, or duplicates, and ensuring the solution handles these correctly.
- Performance pitfalls: Using data structures that lead to higher time or space complexities than necessary.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.