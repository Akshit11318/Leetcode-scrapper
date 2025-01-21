## Previous Permutation with One Swap
**Problem Link:** https://leetcode.com/problems/previous-permutation-with-one-swap/description

**Problem Statement:**
- Input: A list of distinct integers `nums`.
- Constraints: $1 \leq nums.length \leq 10^5$, $1 \leq nums[i] \leq 10^5$.
- Expected output: The previous permutation of `nums` in lexicographically decreasing order, with the constraint that only one swap operation is allowed. If no such permutation exists, return the input array in reverse order.
- Key requirements: The input array contains distinct integers, and we are looking for the lexicographically largest permutation that is smaller than the input.
- Edge cases: If the input array is already the smallest permutation, return the array in reverse order.

**Example Test Cases:**
- Input: `nums = [1, 2, 3]`
  Output: `[3, 1, 2]`
- Input: `nums = [3, 1, 2]`
  Output: `[3, 2, 1]`
- Input: `nums = [1, 1, 5]`
  Output: `[5, 1, 1]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all permutations of the input array and checking which one is the lexicographically largest permutation that is smaller than the input.
- We can use a recursive function to generate all permutations and then filter out the ones that are not smaller than the input.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> prevPermOpt1(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<std::vector<int>> perms;
    std::vector<int> temp = nums;
    std::sort(temp.begin(), temp.end());
    do {
        perms.push_back(temp);
    } while (std::next_permutation(temp.begin(), temp.end()));

    std::vector<int> result = nums;
    std::reverse(result.begin(), result.end());
    for (const auto& perm : perms) {
        if (perm < nums && perm > result) {
            result = perm;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of elements in the input array. This is because we are generating all permutations of the input array.
> - **Space Complexity:** $O(n!)$, as we need to store all permutations in memory.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input array, which results in exponential time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to find the first pair of elements from the right that are in decreasing order.
- We can then swap the first element with the largest element to its right that is smaller than it.
- This approach ensures that we get the lexicographically largest permutation that is smaller than the input.

```cpp
#include <vector>

std::vector<int> prevPermOpt1(std::vector<int>& nums) {
    int n = nums.size();
    for (int i = n - 2; i >= 0; --i) {
        if (nums[i] > nums[i + 1]) {
            int max_idx = i + 1;
            for (int j = i + 2; j < n; ++j) {
                if (nums[j] < nums[i] && nums[j] > nums[max_idx]) {
                    max_idx = j;
                }
            }
            std::swap(nums[i], nums[max_idx]);
            return nums;
        }
    }
    std::reverse(nums.begin(), nums.end());
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are scanning the array from right to left to find the first pair of elements in decreasing order.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the indices and temporary variables.
> - **Optimality proof:** This approach is optimal because we are only scanning the array once and performing a constant number of operations to find the solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: scanning the array from right to left, finding the first pair of elements in decreasing order, and swapping elements to get the lexicographically largest permutation.
- Problem-solving patterns identified: using a greedy approach to find the optimal solution.
- Optimization techniques learned: reducing the time complexity from exponential to linear by using a more efficient algorithm.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the edge case where the input array is already the smallest permutation.
- Edge cases to watch for: handling the case where the input array is empty or has only one element.
- Performance pitfalls: using an inefficient algorithm that results in exponential time complexity.
- Testing considerations: testing the function with different input arrays to ensure it produces the correct output.