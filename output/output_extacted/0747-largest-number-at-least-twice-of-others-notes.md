## Largest Number At Least Twice Of Others

**Problem Link:** https://leetcode.com/problems/largest-number-at-least-twice-of-others/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `2 <= nums.length <= 50`, `1 <= nums[i] <= 100`.
- Expected Output: The index of the largest number that is at least twice as large as every other number in the array. If no such number exists, return `-1`.
- Key Requirements:
  - The number at the returned index must be at least twice as large as every other number in the array.
  - If there are multiple such numbers, return the index of the first occurrence.
- Edge Cases:
  - If the array contains only one element, return `0`.
  - If the array contains two elements and one is at least twice as large as the other, return the index of the larger number.
- Example Test Cases:
  - Input: `nums = [3,6,1,0]`, Output: `1` (Explanation: 6 is the largest number, and for every other number in the array, 6 is at least twice as large. More formally, for every `x` in the array, `6 >= 2*x`.)
  - Input: `nums = [1,2,3,4]`, Output: `-1` (Explanation: There is no number that is at least twice as large as every other number.)

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every number in the array to see if it is at least twice as large as every other number.
- This approach involves iterating over the array and for each number, checking every other number to see if the condition is met.

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            bool isDominant = true;
            for (int j = 0; j < n; j++) {
                if (i != j && nums[i] < 2 * nums[j]) {
                    isDominant = false;
                    break;
                }
            }
            if (isDominant) {
                return i;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially check every other element.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the index and the boolean flag.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the use of a fixed amount of space results in constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to find the maximum number and the second maximum number in a single pass through the array.
- Then, check if the maximum number is at least twice as large as the second maximum number. If it is, return the index of the maximum number.

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int maxNum = INT_MIN, secondMaxNum = INT_MIN;
        int maxIndex = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > maxNum) {
                secondMaxNum = maxNum;
                maxNum = nums[i];
                maxIndex = i;
            } else if (nums[i] > secondMaxNum) {
                secondMaxNum = nums[i];
            }
        }
        return maxNum >= 2 * secondMaxNum ? maxIndex : -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number, the second maximum number, and their indices.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once to find the maximum and second maximum numbers. The space complexity is optimal because we only use a constant amount of space.