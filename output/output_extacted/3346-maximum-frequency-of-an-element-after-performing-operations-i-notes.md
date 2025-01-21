## Maximum Frequency of an Element After Performing Operations I
**Problem Link:** https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Output: The maximum frequency of an element in `nums` after performing the given operations.
- Key requirements:
  - For each operation, we can either increment the smallest element in `nums` or decrement the largest element in `nums`.
  - We can perform at most `k` operations.
- Edge cases:
  - If `nums` is empty, return 0.
  - If `k` is 0, return the frequency of the most frequent element in `nums`.

**Example Test Cases:**
- `nums = [1, 2, 4], k = 5`
  - We can increment the smallest element (1) 5 times to get [6, 2, 4], then decrement the largest element (4) to get [6, 2, 3].
  - The maximum frequency of an element is 1.
- `nums = [1, 2, 4], k = 0`
  - The maximum frequency of an element is 1.

---

### Brute Force Approach
**Explanation:**
- Try all possible combinations of incrementing the smallest element and decrementing the largest element.
- For each combination, calculate the frequency of each element and keep track of the maximum frequency.
- This approach comes to mind first because it exhaustively checks all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int maxFrequency(vector<int>& nums, int k) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int maxFreq = 0;
    for (int i = 0; i < n; i++) {
        int freq = 0;
        for (int j = i; j < n; j++) {
            int sum = 0;
            for (int l = i; l <= j; l++) {
                sum += nums[l];
            }
            int expectedSum = (j - i + 1) * nums[j];
            if (sum + k >= expectedSum) {
                freq = j - i + 1;
            }
        }
        maxFreq = max(maxFreq, freq);
    }
    return maxFreq;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `nums`. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum frequency and other variables.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all possible combinations of operations, resulting in a cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- We can use a sliding window approach to efficiently calculate the maximum frequency of an element.
- We maintain a window of elements and try to expand it to the right by incrementing the smallest element or decrementing the largest element.
- We use a prefix sum array to efficiently calculate the sum of elements within the window.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxFrequency(vector<int>& nums, int k) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int maxFreq = 0;
    int windowSum = 0;
    int left = 0;
    for (int right = 0; right < n; right++) {
        windowSum += nums[right];
        while (windowSum + k < (right - left + 1) * nums[right]) {
            windowSum -= nums[left];
            left++;
        }
        maxFreq = max(maxFreq, right - left + 1);
    }
    return maxFreq;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of `nums`. This is because we sort the array and then use a sliding window approach.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum frequency and other variables.
> - **Optimality proof:** This approach is optimal because it efficiently calculates the maximum frequency of an element by expanding a window of elements and trying to include as many elements as possible within the window.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, prefix sum array.
- Problem-solving patterns identified: using a window to efficiently calculate the maximum frequency of an element.
- Optimization techniques learned: using a prefix sum array to efficiently calculate the sum of elements within the window.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the window sum when expanding the window.
- Edge cases to watch for: handling the case where `nums` is empty or `k` is 0.
- Performance pitfalls: using a brute force approach that has a high time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.