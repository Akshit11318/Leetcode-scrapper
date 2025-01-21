## Maximum Number of Pairs in Array
**Problem Link:** https://leetcode.com/problems/maximum-number-of-pairs-in-array/description

**Problem Statement:**
- Input: An array `nums` of integers and an integer `maxSum`.
- Constraints: `1 <= nums.length <= 3 * 10^5`, `1 <= nums[i] <= 10^5`, `1 <= maxSum <= 10^5`.
- Expected output: The maximum number of pairs that can be formed such that the sum of each pair is less than or equal to `maxSum`.
- Key requirements: The pairs must be formed from the elements of the `nums` array, and each element can be used at most once.
- Edge cases: Handle cases where `nums` is empty, `maxSum` is very small, or `maxSum` is very large.

**Example Test Cases:**
- `nums = [1, 2, 3, 4, 5], maxSum = 7` should return `2` because the pairs `(1, 2)` and `(3, 4)` can be formed.
- `nums = [1, 2, 3, 4, 5], maxSum = 10` should return `2` because the pairs `(1, 5)` and `(2, 4)` can be formed.
- `nums = [1], maxSum = 10` should return `0` because no pairs can be formed.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible pairs of elements from the `nums` array and check if their sum is less than or equal to `maxSum`.
- Step-by-step breakdown:
  1. Generate all possible pairs of elements from the `nums` array.
  2. For each pair, check if the sum is less than or equal to `maxSum`.
  3. If the sum is valid, increment a counter to keep track of the number of valid pairs.
  4. Return the maximum number of valid pairs found.

```cpp
int maxPairs(vector<int>& nums, int maxSum) {
    int n = nums.size();
    int maxPairs = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] <= maxSum) {
                maxPairs++;
                break; // Break the inner loop to avoid counting duplicate pairs
            }
        }
    }
    return maxPairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `nums` array, because we are generating all possible pairs of elements.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the `maxPairs` variable.
> - **Why these complexities occur:** The time complexity is high because we are using nested loops to generate all possible pairs, and the space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach
**Explanation:**
- The key insight is to sort the `nums` array and use two pointers to find the maximum number of pairs.
- Step-by-step breakdown:
  1. Sort the `nums` array in ascending order.
  2. Initialize two pointers, `left` and `right`, to the start and end of the sorted array, respectively.
  3. While `left` is less than `right`, check if the sum of the elements at `left` and `right` is less than or equal to `maxSum`.
  4. If the sum is valid, increment `left` and decrement `right` to find the next pair.
  5. If the sum is not valid, decrement `right` to reduce the sum.
  6. Return the maximum number of valid pairs found.

```cpp
int maxPairs(vector<int>& nums, int maxSum) {
    sort(nums.begin(), nums.end());
    int left = 0, right = nums.size() - 1;
    int maxPairs = 0;
    while (left < right) {
        if (nums[left] + nums[right] <= maxSum) {
            maxPairs++;
            left++;
        } else {
            right--;
        }
    }
    return maxPairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the `nums` array, because we are sorting the array and using a two-pointer technique.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the `maxPairs` variable and the two pointers.
> - **Optimality proof:** This approach is optimal because we are using a two-pointer technique to find the maximum number of pairs, which has a linear time complexity after sorting the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, two-pointer technique, and greedy algorithm.
- Problem-solving patterns identified: using sorting to simplify the problem and finding the maximum number of pairs using a two-pointer technique.
- Optimization techniques learned: reducing the time complexity by using a two-pointer technique instead of generating all possible pairs.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty `nums` array, and not handling duplicate pairs correctly.
- Edge cases to watch for: handling cases where `maxSum` is very small or very large, and handling cases where the `nums` array has duplicate elements.
- Performance pitfalls: using a brute force approach with a high time complexity, and not optimizing the solution using a two-pointer technique.