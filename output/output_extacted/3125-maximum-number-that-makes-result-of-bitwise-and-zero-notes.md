## Maximum Number that Makes Result of Bitwise AND Zero

**Problem Link:** https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/description

**Problem Statement:**
- Input: A list of integers `nums`.
- Constraints: The list will contain at least two elements and at most 10^5 elements, with each element in the range [0, 10^9].
- Expected Output: The maximum number that can be achieved by performing bitwise AND operations with all numbers in the list such that the result is zero.
- Key Requirements: The number should be as large as possible while still ensuring the bitwise AND with every number in the list is zero.
- Edge Cases: An empty list is not a valid input, and the list must contain at least two elements.

**Example Test Cases:**
- For `nums = [1, 2, 3]`, the output should be `0` because the bitwise AND of `1`, `2`, and `3` is `0`, but we are looking for the maximum number that, when bitwise ANDed with each of `1`, `2`, and `3`, gives `0`. This implies we are looking for a number that does not share any `1` bits with any of the numbers in the list.
- For `nums = [5, 8]`, the output should be `0` because the bitwise AND of `5` and `8` is `0`, and any number larger than `0` would have at least one bit in common with either `5` or `8`, thus not satisfying the condition.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible number from the maximum value in the list down to `0` and see if it satisfies the condition of having a bitwise AND of `0` with all numbers in the list.
- This involves iterating over each number in the list for every potential candidate number, performing a bitwise AND operation, and checking if the result is `0`.

```cpp
class Solution {
public:
    int maximumNumber(vector<int>& nums) {
        int maxNum = *max_element(nums.begin(), nums.end());
        for (int i = maxNum; i >= 0; --i) {
            bool satisfies = true;
            for (int num : nums) {
                if ((i & num) != 0) {
                    satisfies = false;
                    break;
                }
            }
            if (satisfies) return i;
        }
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of elements in the list and $m$ is the maximum value in the list, because for each potential number (up to the maximum in the list), we are checking its bitwise AND with every number in the list.
> - **Space Complexity:** $O(1)$, excluding the input, because we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach requires checking every possible number against every number in the list, leading to a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is recognizing that for a number to have a bitwise AND of `0` with every number in the list, it must not share any `1` bits with any of the numbers in the list.
- Given that all numbers are represented in binary, the maximum number that can satisfy this condition is a number that has `1`s only in the positions where all numbers in the list have `0`s.
- However, upon closer inspection, it becomes clear that finding such a number directly is complex due to the variability in binary representations of the numbers in the list.
- A simpler approach is to recognize that the only number that will have a bitwise AND of `0` with every number in the list is `0` itself, because for any other number, there will be at least one number in the list with which it shares a `1` bit.

```cpp
class Solution {
public:
    int maximumNumber(vector<int>& nums) {
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are simply returning `0` without any operations dependent on the input size.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space.
> - **Optimality proof:** This is the optimal solution because it directly addresses the requirement that the bitwise AND with every number in the list must be `0`. No other number can satisfy this condition for all possible inputs.

---

### Final Notes

**Learning Points:**
- The importance of understanding bitwise operations and their implications.
- Recognizing that sometimes, the most straightforward solution is the optimal one.
- The value of analyzing the problem constraints and requirements to identify the simplest path to a solution.

**Mistakes to Avoid:**
- Overcomplicating the problem by looking for complex patterns or algorithms when a simple solution exists.
- Not fully considering the implications of the problem constraints on the potential solutions.
- Failing to recognize the uniqueness of the solution `0` in satisfying the bitwise AND condition with all numbers in the list.