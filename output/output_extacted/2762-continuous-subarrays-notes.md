## Continuous Subarrays
**Problem Link:** https://leetcode.com/problems/continuous-subarrays/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, `1 <= k <= 10^9`.
- Expected Output: The number of continuous subarrays where every element is greater than `k`.
- Key Requirements: Count all subarrays that meet the condition, including single-element subarrays.
- Edge Cases: Empty array, array with all elements less than or equal to `k`, array with all elements greater than `k`.

**Example Test Cases:**
- `nums = [1, 2, 3, 4, 5], k = 3`, Expected Output: 6 (subarrays are [4], [5], [4, 5], [5], [4, 5], [5]).
- `nums = [1, 2, 3, 4, 5], k = 5`, Expected Output: 1 (only subarray [5] meets the condition).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over all possible subarrays of the given array.
- For each subarray, check if every element is greater than `k`.
- Count all subarrays that meet this condition.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            bool valid = true;
            for (int x = i; x <= j; x++) {
                if (nums[x] <= k) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because for each of the $n$ starting indices, we potentially iterate over the remaining $n$ elements, and for each subarray, we check its validity by iterating over its elements again.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The nested loops over the array and the subarray validation check lead to the cubic time complexity. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a sliding window approach, maintaining a window of elements greater than `k`.
- We start with an empty window and expand it to the right as long as the elements are greater than `k`.
- Whenever we encounter an element less than or equal to `k`, we slide the window to the right of this element.
- The number of subarrays ending at each position within the window can be calculated based on the window's size.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > k) {
            int windowSize = 1;
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] > k) {
                    windowSize++;
                } else {
                    break;
                }
            }
            // Calculate the number of subarrays in the window
            count += (windowSize * (windowSize + 1)) / 2;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we make a single pass through the array, and the inner loop does not exceed the total number of elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array, and it correctly counts all valid subarrays without redundant computations.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique in array problems.
- How to calculate the number of subarrays within a given window.
- The trade-off between brute force and optimal solutions in terms of complexity.

**Mistakes to Avoid:**
- Not considering the sliding window approach for array problems.
- Incorrectly calculating the number of subarrays within a window.
- Not optimizing the solution for large inputs.

**Similar Problems to Practice:**
- Other array problems involving subarrays, such as finding the maximum sum subarray or the longest subarray with a certain property.