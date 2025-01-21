## Minimum Right Shifts to Sort the Array
**Problem Link:** https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The array `nums` will have at least one element and at most $10^5$ elements. Each element in `nums` will be between $1$ and $10^9$.
- Expected Output: The minimum number of right shifts required to sort the array in ascending order.
- Key Requirements: The array should be sorted in ascending order after applying the minimum number of right shifts.
- Edge Cases: If the array is already sorted, the output should be $0$. If the array has only one element, the output should be $0$.

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible right shifts and checking if the array is sorted after each shift.
- We can generate all possible right shifts of the array and check if each shifted array is sorted.
- This approach comes to mind first because it is straightforward and simple to implement.

```cpp
class Solution {
public:
    int minRightShiftsToSort(vector<int>& nums) {
        int n = nums.size();
        int minShifts = n;
        for (int shifts = 0; shifts < n; shifts++) {
            vector<int> shiftedNums = nums;
            // Apply right shift
            for (int i = 0; i < shifts; i++) {
                int temp = shiftedNums.back();
                shiftedNums.pop_back();
                shiftedNums.insert(shiftedNums.begin(), temp);
            }
            // Check if the shifted array is sorted
            bool isSorted = true;
            for (int i = 1; i < n; i++) {
                if (shiftedNums[i] < shiftedNums[i - 1]) {
                    isSorted = false;
                    break;
                }
            }
            if (isSorted) {
                minShifts = min(minShifts, shifts);
            }
        }
        return minShifts;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are generating all possible right shifts of the array and checking if each shifted array is sorted.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are creating a new array for each possible right shift.
> - **Why these complexities occur:** The brute force approach involves trying all possible right shifts, which results in a time complexity of $O(n^2)$. The space complexity is $O(n)$ because we are creating a new array for each possible right shift.

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to find the minimum number of right shifts required to move the smallest element to the beginning of the array.
- We can use a single pass through the array to find the index of the smallest element.
- We can then calculate the minimum number of right shifts required to move the smallest element to the beginning of the array.

```cpp
class Solution {
public:
    int minRightShiftsToSort(vector<int>& nums) {
        int n = nums.size();
        int minIndex = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }
        int minShifts = minIndex;
        for (int i = minIndex + 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) {
                return -1; // Array cannot be sorted by right shifts
            }
        }
        return minShifts;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are making a single pass through the array to find the index of the smallest element.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the array. This is because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This is the optimal solution because we are making a single pass through the array to find the index of the smallest element, and then calculating the minimum number of right shifts required to move the smallest element to the beginning of the array.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of a single pass through the array to find the index of the smallest element.
- The problem-solving pattern identified in this problem is to find the minimum number of right shifts required to move the smallest element to the beginning of the array.
- The optimization technique learned in this problem is to use a single pass through the array to find the index of the smallest element, rather than trying all possible right shifts.

**Mistakes to Avoid:**
- A common implementation error is to try all possible right shifts, which results in a time complexity of $O(n^2)$.
- An edge case to watch for is when the array is already sorted, in which case the output should be $0$.
- A performance pitfall is to use extra space that scales with the input size, which can result in a space complexity of $O(n)$.