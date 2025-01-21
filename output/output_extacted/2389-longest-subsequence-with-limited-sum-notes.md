## Longest Subsequence with Limited Sum

**Problem Link:** https://leetcode.com/problems/longest-subsequence-with-limited-sum/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= k <= 10^9`.
- Expected output: The length of the longest subsequence of `nums` with a sum less than or equal to `k`.
- Key requirements: The subsequence must be non-decreasing and its sum must not exceed `k`.
- Edge cases: Empty input array, `k` is 0, or all elements in `nums` are greater than `k`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subsequences of `nums` and check if their sum is less than or equal to `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums`.
  2. For each subsequence, calculate its sum.
  3. Check if the sum is less than or equal to `k` and if the subsequence is non-decreasing.
  4. Keep track of the longest subsequence that meets these conditions.

```cpp
#include <vector>
#include <algorithm>

int longestSubsequence(std::vector<int>& nums, int k) {
    int n = nums.size();
    int max_length = 0;

    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        std::vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }

        // Check if the subsequence is non-decreasing and its sum is less than or equal to k
        if (std::is_sorted(subsequence.begin(), subsequence.end())) {
            int sum = 0;
            for (int num : subsequence) {
                sum += num;
            }
            if (sum <= k) {
                max_length = std::max(max_length, (int)subsequence.size());
            }
        }
    }

    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot \log n)$, where $n$ is the length of `nums`. This is because we generate all possible subsequences, which takes $O(2^n)$ time, and for each subsequence, we check if it is non-decreasing, which takes $O(n \cdot \log n)$ time using the `std::is_sorted` function.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we need to store the current subsequence.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subsequences, which results in an exponential time complexity. The `std::is_sorted` function also adds to the time complexity because it uses a sorting algorithm internally.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a two-pointer technique to efficiently find the longest non-decreasing subsequence with a sum less than or equal to `k`.
- Detailed breakdown of the approach:
  1. Sort the `nums` array in non-decreasing order.
  2. Initialize two pointers, `left` and `right`, to the beginning of the `nums` array.
  3. Initialize a variable `sum` to 0, which will store the sum of the current subsequence.
  4. Move the `right` pointer to the right and add the current element to `sum` until `sum` exceeds `k`.
  5. Move the `left` pointer to the right and subtract the current element from `sum` until `sum` is less than or equal to `k`.
  6. Keep track of the maximum length of the subsequence seen so far.

```cpp
#include <vector>
#include <algorithm>

int longestSubsequence(std::vector<int>& nums, int k) {
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    int max_length = 0;
    int sum = 0;
    int left = 0;

    for (int right = 0; right < n; right++) {
        sum += nums[right];

        while (sum > k) {
            sum -= nums[left];
            left++;
        }

        max_length = std::max(max_length, right - left + 1);
    }

    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the length of `nums`. This is because we sort the `nums` array, which takes $O(n \cdot \log n)$ time, and then we use a two-pointer technique, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, where $n$ is the length of `nums`. This is because we only use a constant amount of space to store the `left`, `right`, `sum`, and `max_length` variables.
> - **Optimality proof:** This approach is optimal because it uses a two-pointer technique, which is the most efficient way to find the longest non-decreasing subsequence with a sum less than or equal to `k`. The sorting step is also necessary to ensure that the subsequence is non-decreasing.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting, and subsequence problems.
- Problem-solving patterns identified: Using a two-pointer technique to efficiently find the longest non-decreasing subsequence with a sum less than or equal to `k`.
- Optimization techniques learned: Avoiding unnecessary computations by using a two-pointer technique and sorting the input array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array or `k` being 0.
- Edge cases to watch for: Empty input array, `k` is 0, or all elements in `nums` are greater than `k`.
- Performance pitfalls: Using an inefficient algorithm, such as generating all possible subsequences, which results in an exponential time complexity.