## Count the Number of Good Subarrays

**Problem Link:** https://leetcode.com/problems/count-the-number-of-good-subarrays/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5` and `1 <= k <= 10^5`.
- Expected output format: The number of good subarrays.
- Key requirements: A good subarray is defined as a subarray where the number of distinct elements is less than or equal to `k`.
- Edge cases: Consider empty arrays, arrays with a single element, and arrays with duplicate elements.
- Example test cases:
  - `nums = [1, 2, 1, 2, 3], k = 2`: The good subarrays are `[1]`, `[2]`, `[1]`, `[2]`, `[1, 2]`, `[2, 1]`, `[1, 2, 1]`, `[2, 1, 2]`. The answer is 7.
  - `nums = [1, 2, 1, 3], k = 2`: The good subarrays are `[1]`, `[2]`, `[1]`, `[1, 2]`, `[2, 1]`, `[1, 2, 1]`. The answer is 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subarrays and check each one for the number of distinct elements.
- Step-by-step breakdown:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, count the number of distinct elements.
  3. If the number of distinct elements is less than or equal to `k`, increment the count of good subarrays.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int countGoodSubarrays(std::vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            std::unordered_set<int> distinct;
            for (int x = i; x <= j; x++) {
                distinct.insert(nums[x]);
            }
            if (distinct.size() <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`, because we are generating all possible subarrays and counting distinct elements for each.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements of `nums` in the `distinct` set.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves generating all possible subarrays, which results in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a sliding window approach with an unordered map to keep track of the frequency of each element in the current window.
- Detailed breakdown:
  1. Initialize an unordered map `freq` to store the frequency of each element in the current window.
  2. Initialize variables `left` and `right` to represent the boundaries of the window.
  3. Initialize a variable `count` to store the number of good subarrays.
  4. Iterate over `nums` with the `right` pointer, expanding the window to the right.
  5. For each element, increment its frequency in `freq`.
  6. While the number of distinct elements in `freq` exceeds `k`, shrink the window from the left by decrementing the frequency of the element at the `left` index and incrementing `left`.
  7. For each position of the `right` pointer, the number of good subarrays ending at that position is `right - left + 1`, so add this to `count`.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int countGoodSubarrays(std::vector<int>& nums, int k) {
    int count = 0;
    std::unordered_map<int, int> freq;
    int left = 0;
    for (int right = 0; right < nums.size(); right++) {
        freq[nums[right]]++;
        while (freq.size() > k) {
            freq[nums[left]]--;
            if (freq[nums[left]] == 0) {
                freq.erase(nums[left]);
            }
            left++;
        }
        count += right - left + 1;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we are iterating over `nums` once with the `right` pointer and potentially once with the `left` pointer.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements of `nums` in the `freq` map.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `nums` and uses a sliding window to efficiently track the number of distinct elements in the current window.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window, unordered map.
- Problem-solving patterns identified: Using a sliding window to track the number of distinct elements in a subarray.
- Optimization techniques learned: Reducing the time complexity from cubic to linear by using a sliding window approach.

**Mistakes to Avoid:**
- Common implementation errors: Failing to increment or decrement frequencies correctly, not checking for the existence of an element in the map before erasing it.
- Edge cases to watch for: Empty arrays, arrays with a single element, arrays with duplicate elements.
- Performance pitfalls: Using a brute force approach that generates all possible subarrays, resulting in a cubic time complexity.