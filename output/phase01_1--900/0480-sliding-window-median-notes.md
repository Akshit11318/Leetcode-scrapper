## Sliding Window Median
**Problem Link:** [https://leetcode.com/problems/sliding-window-median/description](https://leetcode.com/problems/sliding-window-median/description)

**Problem Statement:**
- Input format: `nums` array and `k` size of the sliding window
- Constraints: `1 <= k <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`
- Expected output format: Array of medians for each window
- Key requirements: Calculate the median of each `k`-sized window in the `nums` array
- Example test cases:
  - `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3` should return `[1, -1, -1, 3, 5, 6]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort each window and find the median
- Step-by-step breakdown:
  1. Iterate over the `nums` array with a sliding window of size `k`.
  2. For each window, sort the elements.
  3. Find the median of the sorted window.
- Why this approach comes to mind first: It's straightforward to calculate the median of each window by sorting.

```cpp
#include <vector>
#include <algorithm>

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    vector<double> medians;
    for (int i = 0; i <= nums.size() - k; ++i) {
        vector<int> window(nums.begin() + i, nums.begin() + i + k);
        sort(window.begin(), window.end());
        if (k % 2 == 0) {
            double median = (window[k / 2 - 1] + window[k / 2]) / 2.0;
            medians.push_back(median);
        } else {
            double median = window[k / 2];
            medians.push_back(median);
        }
    }
    return medians;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \log k)$, where $n$ is the size of the `nums` array, due to sorting each window.
> - **Space Complexity:** $O(k)$ for storing each window.
> - **Why these complexities occur:** Sorting each window of size $k$ takes $O(k \log k)$ time, and we do this $n - k + 1$ times.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a balanced binary search tree (BST) like `std::multiset` to maintain the window elements.
- Detailed breakdown:
  1. Initialize two multisets: `lower` and `upper`, to store the lower and upper halves of the window, respectively.
  2. Iterate over the `nums` array and add each element to the appropriate multiset.
  3. Balance the multisets to ensure the size difference is at most 1.
  4. Calculate the median based on the sizes and top elements of the multisets.
- Proof of optimality: This approach allows for $O(\log k)$ time to add or remove an element and calculate the median, leading to an overall time complexity of $O(n \log k)$.

```cpp
#include <vector>
#include <multiset>

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    vector<double> medians;
    multiset<int> window;
    for (int i = 0; i < nums.size(); ++i) {
        window.insert(nums[i]);
        if (i >= k) window.erase(window.find(nums[i - k]));
        if (i >= k - 1) {
            if (k % 2 == 0) {
                auto it = window.begin();
                advance(it, k / 2 - 1);
                double median = (*it + *next(it)) / 2.0;
                medians.push_back(median);
            } else {
                auto it = window.begin();
                advance(it, k / 2);
                double median = *it;
                medians.push_back(median);
            }
        }
    }
    return medians;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the size of the `nums` array, due to inserting and erasing elements from the multiset.
> - **Space Complexity:** $O(k)$ for storing the window elements in the multiset.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by using a balanced BST to maintain the window elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Balanced binary search trees, sliding window technique
- Problem-solving patterns: Maintaining a balanced data structure to minimize time complexity
- Optimization techniques: Using a multiset to efficiently calculate the median
- Similar problems to practice: Other sliding window problems, such as maximum or minimum in a window

**Mistakes to Avoid:**
- Common implementation errors: Failing to balance the multisets, incorrect median calculation
- Edge cases to watch for: Handling even and odd window sizes
- Performance pitfalls: Using an unbalanced data structure or inefficient sorting algorithm
- Testing considerations: Verifying the correctness of the median calculation for various window sizes and input arrays