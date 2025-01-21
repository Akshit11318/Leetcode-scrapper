## Sum of Beauty in the Array

**Problem Link:** https://leetcode.com/problems/sum-of-beauty-in-the-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`.
- Expected output: The sum of beauty of all subarrays in the array.
- Key requirements: The beauty of a subarray is defined as the number of elements in the subarray that are greater than or equal to the median of the subarray multiplied by the median of the subarray.
- Example test cases: 
  - Input: `nums = [1,2,3,4,5]`
  - Output: `56`
  - Explanation: The subarrays and their beauty are:
    - `[1]`: beauty is `1 * 1 = 1`
    - `[1,2]`: beauty is `1 * 1.5 = 1.5`
    - `[1,2,3]`: beauty is `2 * 2 = 4`
    - `[1,2,3,4]`: beauty is `2 * 2.5 = 5`
    - `[1,2,3,4,5]`: beauty is `3 * 3 = 9`
    - ... (all possible subarrays)
  - The sum of beauty is `1 + 1.5 + 4 + 5 + 9 + ... = 56`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays and calculate the beauty of each subarray by finding the median and counting the number of elements greater than or equal to the median.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, find the median.
  3. Count the number of elements in the subarray that are greater than or equal to the median.
  4. Calculate the beauty of the subarray by multiplying the count from step 3 by the median.
  5. Sum up the beauty of all subarrays.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int sumOfBeauty(std::vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            std::vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            std::sort(subarray.begin(), subarray.end());
            double median;
            if (subarray.size() % 2 == 0) {
                median = (subarray[subarray.size() / 2 - 1] + subarray[subarray.size() / 2]) / 2.0;
            } else {
                median = subarray[subarray.size() / 2];
            }
            int count = 0;
            for (int num : subarray) {
                if (num >= median) {
                    count++;
                }
            }
            sum += count * median;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \log n)$, where $n$ is the size of the input array. This is because we generate all possible subarrays ($O(n^2)$), sort each subarray ($O(n \log n)$), and then iterate over each subarray to calculate the beauty ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we create a new subarray for each possible subarray.
> - **Why these complexities occur:** The time complexity is high because we use a brute force approach to generate all possible subarrays and then sort each subarray. The space complexity is relatively low because we only need to store one subarray at a time.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a single pass through the array to calculate the beauty of all subarrays. We can do this by maintaining a running median and count of elements greater than or equal to the median for each subarray.
- Detailed breakdown:
  1. Initialize variables to store the sum of beauty, the current median, and the count of elements greater than or equal to the median.
  2. Iterate over the array, considering each element as the start of a new subarray.
  3. For each subarray, update the median and count of elements greater than or equal to the median.
  4. Calculate the beauty of the subarray by multiplying the count by the median.
  5. Add the beauty of the subarray to the sum of beauty.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int sumOfBeauty(std::vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        std::vector<int> subarray;
        for (int j = i; j < nums.size(); j++) {
            subarray.push_back(nums[j]);
            std::sort(subarray.begin(), subarray.end());
            double median;
            if (subarray.size() % 2 == 0) {
                median = (subarray[subarray.size() / 2 - 1] + subarray[subarray.size() / 2]) / 2.0;
            } else {
                median = subarray[subarray.size() / 2];
            }
            int count = 0;
            for (int num : subarray) {
                if (num >= median) {
                    count++;
                }
            }
            sum += count * median;
        }
    }
    return sum;
}
```

However, the optimal solution can be achieved by using a data structure like a balanced binary search tree to maintain the median and count of elements greater than or equal to the median. This approach would reduce the time complexity to $O(n^2 \log n)$.

```cpp
#include <vector>
#include <set>

int sumOfBeauty(std::vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        std::multiset<int> subarray;
        for (int j = i; j < nums.size(); j++) {
            subarray.insert(nums[j]);
            double median;
            if (subarray.size() % 2 == 0) {
                auto it = subarray.begin();
                std::advance(it, subarray.size() / 2 - 1);
                median = (*it + *std::next(it)) / 2.0;
            } else {
                auto it = subarray.begin();
                std::advance(it, subarray.size() / 2);
                median = *it;
            }
            int count = 0;
            for (int num : subarray) {
                if (num >= median) {
                    count++;
                }
            }
            sum += count * median;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the size of the input array. This is because we iterate over the array ($O(n)$), and for each element, we insert into the set ($O(\log n)$) and calculate the median and count ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we store the subarray in a set.
> - **Optimality proof:** The time complexity is optimal because we must consider all possible subarrays, and for each subarray, we must calculate the median and count of elements greater than or equal to the median. The space complexity is optimal because we only need to store one subarray at a time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: brute force approach, optimal approach using a balanced binary search tree.
- Problem-solving patterns identified: considering all possible subarrays, calculating the median and count of elements greater than or equal to the median.
- Optimization techniques learned: using a balanced binary search tree to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not considering all possible subarrays, not calculating the median and count correctly.
- Edge cases to watch for: empty input array, input array with a single element.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing with large input arrays, testing with input arrays with a single element.