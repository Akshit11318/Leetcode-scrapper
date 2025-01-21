## Sum of Subsequence Widths
**Problem Link:** https://leetcode.com/problems/sum-of-subsequence-widths/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 20`, `1 <= nums[i] <= 10^9`.
- Expected Output: The sum of the widths of all possible subsequences of `nums`.
- Key Requirements: Calculate the sum of the widths of all possible subsequences, where the width of a subsequence is the difference between the maximum and minimum elements in the subsequence.
- Edge Cases: Handle cases where the input array is empty or contains a single element.

**Example Test Cases:**
- Input: `nums = [2,1,3]`
  Output: `6`
  Explanation: The possible subsequences are `[2]`, `[1]`, `[3]`, `[2,1]`, `[2,3]`, `[1,3]`, `[2,1,3]`. The sum of their widths is `(2-2) + (1-1) + (3-3) + (2-1) + (3-2) + (3-1) + (3-1) = 0 + 0 + 0 + 1 + 1 + 2 + 2 = 6`.
- Input: `nums = [2]`
  Output: `0`
  Explanation: The only possible subsequence is `[2]`, and its width is `0`.

---

### Brute Force Approach

**Explanation:**
- Generate all possible subsequences of the input array.
- For each subsequence, calculate its width by finding the difference between the maximum and minimum elements.
- Sum up the widths of all subsequences.

```cpp
#include <vector>
#include <algorithm>

int sumSubseqWidths(std::vector<int>& nums) {
    int n = nums.size();
    int sum = 0;
    for (int mask = 1; mask < (1 << n); ++mask) {
        int maxVal = INT_MIN, minVal = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                maxVal = std::max(maxVal, nums[i]);
                minVal = std::min(minVal, nums[i]);
            }
        }
        sum += (maxVal - minVal);
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and for each subsequence, we find the maximum and minimum elements (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and the current subsequence.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the linear space complexity comes from the need to store the current subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- Sort the input array in ascending order.
- For each element in the sorted array, calculate its contribution to the sum of subsequence widths by considering all possible subsequences that contain this element.
- Use the fact that the contribution of each element to the sum of subsequence widths is proportional to its value and its position in the sorted array.

```cpp
#include <vector>
#include <algorithm>

int sumSubseqWidths(std::vector<int>& nums) {
    int n = nums.size();
    std::sort(nums.begin(), nums.end());
    long long sum = 0;
    long long p2 = 1;
    for (int i = 0; i < n; ++i) {
        sum += (p2 - 1) * (nums[n-1-i] - nums[i]);
        p2 *= 2;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we sort the input array (which takes $O(n \log n)$ time) and then make a single pass over the sorted array (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and the current element.
> - **Optimality proof:** This approach is optimal because it avoids generating all possible subsequences, which would take exponential time. Instead, it uses the fact that the contribution of each element to the sum of subsequence widths can be calculated in linear time.

---

### Final Notes

**Learning Points:**
- The importance of sorting the input array to simplify the calculation of subsequence widths.
- The use of the fact that the contribution of each element to the sum of subsequence widths is proportional to its value and its position in the sorted array.
- The avoidance of generating all possible subsequences to reduce the time complexity.

**Mistakes to Avoid:**
- Generating all possible subsequences, which would take exponential time.
- Failing to sort the input array, which would make it difficult to calculate the contribution of each element to the sum of subsequence widths.
- Not using the fact that the contribution of each element to the sum of subsequence widths is proportional to its value and its position in the sorted array, which would make the calculation more complex.