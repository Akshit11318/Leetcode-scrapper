## Missing Element in Sorted Array
**Problem Link:** https://leetcode.com/problems/missing-element-in-sorted-array/description

**Problem Statement:**
- Input: A sorted array `nums` of distinct integers and an integer `k`.
- Constraints: $1 \leq \text{length of } nums \leq 10^5$, $1 \leq k \leq 10^5$.
- Expected Output: Find the `k`-th missing number in the sorted array.
- Key Requirements: The array is sorted and contains distinct integers.
- Edge Cases: The array may be empty, or `k` may be larger than the number of missing elements.

**Example Test Cases:**
- Input: `nums = [4, 7, 9, 10], k = 3`
  Output: `8`
  Explanation: The missing numbers are `[5, 6, 8]`, so the third missing number is `8`.
- Input: `nums = [4, 7, 9, 10], k = 2`
  Output: `6`
  Explanation: The missing numbers are `[5, 6, 8]`, so the second missing number is `6`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and find all missing numbers.
- We can do this by comparing each number with its index, considering the first number as a starting point.
- If the difference between the current number and the expected number (based on the index) is greater than 1, we know there are missing numbers.

```cpp
#include <vector>
using namespace std;

int findKthMissingPositive(vector<int>& nums, int k) {
    // Initialize variables to keep track of the current number and the count of missing numbers
    int current = 1;
    int missingCount = 0;
    
    // Iterate through the array
    for (int i = 0; i < nums.size(); i++) {
        // While the current number is less than the current element in the array
        while (current < nums[i]) {
            // Increment the missing count
            missingCount++;
            // If the missing count equals k, return the current number
            if (missingCount == k) {
                return current;
            }
            // Increment the current number
            current++;
        }
        // If the current number equals the current element in the array, increment the current number
        if (current == nums[i]) {
            current++;
        }
    }
    
    // If we have not found k missing numbers yet, continue from the last element in the array
    while (missingCount < k) {
        missingCount++;
        if (missingCount == k) {
            return current;
        }
        current++;
    }
    
    // This line should not be reached
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the length of the array and $k$ is the given integer.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the array once and potentially iterate up to $k$ times after that. The space complexity is constant because we only use a fixed amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search approach to find the `k`-th missing number.
- We can define a function that calculates the number of missing numbers up to a given index.
- We then use binary search to find the index where the `k`-th missing number would be.

```cpp
#include <vector>
using namespace std;

int findKthMissingPositive(vector<int>& nums, int k) {
    int left = 1;
    int right = nums.size() + nums.back();
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        int missingCount = mid - 1 - (lower_bound(nums.begin(), nums.end(), mid) - nums.begin());
        
        if (missingCount < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + \log n)$, where $n$ is the length of the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because we use binary search to find the `k`-th missing number, which reduces the search space significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, iteration through arrays.
- Problem-solving patterns identified: finding missing numbers in a sorted array.
- Optimization techniques learned: using binary search to reduce the search space.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: empty array, `k` larger than the number of missing elements.
- Performance pitfalls: using a brute force approach for large inputs.