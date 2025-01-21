## Find the Distinct Difference Array
**Problem Link:** https://leetcode.com/problems/find-the-distinct-difference-array/description

**Problem Statement:**
- Given a 0-indexed integer array `nums`, return an array `diff` where `diff[i]` is the count of distinct elements in `nums` that are **smaller** than `nums[i]`.
- Input constraints: `1 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^5`.
- Expected output format: An array of integers representing the distinct difference array.
- Key requirements and edge cases:
  - The array `nums` contains distinct integers.
  - The array `diff` should be of the same length as `nums`.
  - For each `nums[i]`, count the distinct elements in `nums` that are smaller than `nums[i]`.
- Example test cases:
  - Input: `nums = [1, 2, 3, 4, 5]`
    - Output: `[0, 1, 2, 3, 4]`
    - Explanation: For each element in `nums`, the distinct elements smaller than it are counted.
  - Input: `nums = [5, 4, 3, 2, 1]`
    - Output: `[4, 3, 2, 1, 0]`
    - Explanation: Similarly, for each element, count the distinct elements smaller than it.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each element in `nums`, iterate through all previous elements to count the distinct smaller elements.
- Step-by-step breakdown:
  1. Initialize an empty array `diff` of the same length as `nums`.
  2. For each element `nums[i]`, initialize a set to store unique smaller elements.
  3. Iterate from the first element to `nums[i-1]`, adding each smaller element to the set.
  4. The size of the set is the count of distinct smaller elements for `nums[i]`, which is then added to `diff`.
- Why this approach comes to mind first: It directly addresses the requirement by comparing each element with all its predecessors.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> distinctDifferenceArray(std::vector<int>& nums) {
    std::vector<int> diff(nums.size());
    for (int i = 0; i < nums.size(); i++) {
        std::unordered_set<int> smaller;
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                smaller.insert(nums[j]);
            }
        }
        diff[i] = smaller.size();
    }
    return diff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each of the $n$ elements, we potentially iterate through all previous elements.
> - **Space Complexity:** $O(n)$ for storing the result and the set of smaller elements for each iteration.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, and the use of a set for each element contributes to the linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a `std::set` to keep track of all elements seen so far, and for each new element, calculate the difference by finding the number of elements in the set that are smaller than the current element.
- Detailed breakdown:
  1. Initialize an empty set `seen` and an empty vector `diff` of the same length as `nums`.
  2. For each element `nums[i]`, insert it into the `seen` set.
  3. To find the count of distinct smaller elements for `nums[i]`, iterate through the `seen` set and count elements smaller than `nums[i]`.
  4. However, a more efficient approach is to use the property of `std::set` and its iterators to directly count the number of elements smaller than `nums[i]`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and utilizes the efficient insertion and search operations provided by the `std::set`.

```cpp
#include <iostream>
#include <vector>
#include <set>

std::vector<int> distinctDifferenceArray(std::vector<int>& nums) {
    std::vector<int> diff(nums.size());
    std::set<int> seen;
    for (int i = 0; i < nums.size(); i++) {
        auto it = seen.lower_bound(nums[i]);
        diff[i] = std::distance(seen.begin(), it);
        seen.insert(nums[i]);
    }
    return diff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the insertion and search operations in the `std::set`.
> - **Space Complexity:** $O(n)$ for storing the set and the result vector.
> - **Optimality proof:** The use of a `std::set` allows for efficient counting of smaller elements, making this approach optimal in terms of time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Utilizing `std::set` for efficient insertion and search operations.
- Understanding how to calculate the count of elements smaller than a given element in a set.
- Recognizing the importance of optimizing the algorithm to reduce time complexity.

**Mistakes to Avoid:**
- Not considering the use of data structures like sets for efficient operations.
- Failing to optimize the algorithm, leading to high time complexity.
- Not properly handling edge cases, such as an empty input array.