## Count Pairs Whose Sum is Less Than Target

**Problem Link:** https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description

**Problem Statement:**
- Given an array of integers `nums` and a target `target`, return the number of pairs of integers in the array whose sum is less than `target`.
- Input format: `nums` is a list of integers, and `target` is an integer.
- Constraints: $1 \leq \text{length of nums} \leq 10^5$, $1 \leq \text{each element of nums} \leq 10^9$, $1 \leq \text{target} \leq 10^{18}$.
- Expected output: The number of pairs of integers whose sum is less than `target`.
- Key requirements: The solution should handle large inputs efficiently.
- Edge cases: When `nums` is empty or contains a single element, or when `target` is less than the minimum element in `nums`.

Example test cases:
- `nums = [1, 2, 3, 4, 5], target = 7` should return `6` because the pairs whose sum is less than `7` are `(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4)`.
- `nums = [1], target = 1` should return `0` because there are no pairs whose sum is less than `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use a nested loop to generate all possible pairs of integers from the array and check if their sum is less than the target.
- Step-by-step breakdown:
  1. Initialize a counter variable `count` to store the number of pairs whose sum is less than the target.
  2. Use two nested loops to generate all possible pairs of integers from the array.
  3. For each pair, check if the sum is less than the target.
  4. If the sum is less than the target, increment the counter.

```cpp
int countPairs(vector<int>& nums, long long target) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] < target) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`, because we are using two nested loops to generate all possible pairs.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the counter variable.
> - **Why these complexities occur:** The time complexity is quadratic because we are generating all possible pairs, and the space complexity is constant because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a two-pointer technique to efficiently count the number of pairs whose sum is less than the target.
- Step-by-step breakdown:
  1. Sort the array in ascending order.
  2. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
  3. Initialize a counter variable `count` to store the number of pairs whose sum is less than the target.
  4. Use a loop to move the `right` pointer to the left until the sum of the elements at the `left` and `right` pointers is less than the target.
  5. For each position of the `right` pointer, increment the counter by the number of elements to the left of the `right` pointer that have a sum less than the target with the element at the `right` pointer.

```cpp
int countPairs(vector<int>& nums, long long target) {
    sort(nums.begin(), nums.end());
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int left = 0, right = i;
        while (left < right) {
            if (nums[left] + nums[right] < target) {
                count += right - left;
                break;
            }
            right--;
        }
    }
    return count;
}
```

However, this solution is still not optimal because it has a time complexity of $O(n^2)$ due to the nested loop.

A more optimal solution would be to use a binary search approach to find the number of elements that have a sum less than the target with each element.

```cpp
int countPairs(vector<int>& nums, long long target) {
    sort(nums.begin(), nums.end());
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int left = 0, right = i;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] + nums[i] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        count += right + 1;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of `nums`, because we are using a binary search approach to find the number of elements that have a sum less than the target with each element.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the counter variable.
> - **Optimality proof:** This solution is optimal because we are using a binary search approach to find the number of elements that have a sum less than the target with each element, which reduces the time complexity from $O(n^2)$ to $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- The importance of sorting the array to enable efficient searching and counting.
- The use of binary search to find the number of elements that have a sum less than the target with each element.
- The trade-off between time and space complexity in different solutions.

**Mistakes to Avoid:**
- Not sorting the array before using a two-pointer technique or binary search.
- Not using a binary search approach to find the number of elements that have a sum less than the target with each element.
- Not considering the time and space complexity of different solutions.