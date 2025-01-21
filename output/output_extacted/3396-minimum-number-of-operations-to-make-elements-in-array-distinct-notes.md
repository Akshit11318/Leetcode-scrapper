## Minimum Number of Operations to Make Array Elements Distinct
**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`.
- Expected output: The minimum number of operations required to make all elements in the array distinct.
- Key requirements: Each operation involves incrementing an element by 1.
- Edge cases: The array can contain duplicates, and the elements can be in any order.

**Example Test Cases:**
- For `nums = [3,2,1,2,1,7]`, the output is `6` because we can increment the first occurrence of `1` to `2`, the second occurrence of `1` to `3`, and the second occurrence of `2` to `4`, resulting in `[3,2,3,4,7,7]`.
- For `nums = [1,2,3,4,5]`, the output is `0` because all elements are already distinct.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves sorting the array and then iterating through it to find duplicates.
- For each duplicate found, increment the current element until it becomes distinct.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
int minOperations(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int operations = 0;
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] <= nums[i - 1]) {
            operations += nums[i - 1] - nums[i] + 1;
            nums[i] = nums[i - 1] + 1;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$ for the input array, assuming the sorting algorithm used has a constant space complexity.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant because we only use a fixed amount of space to store the input array and the `operations` variable.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a `set` data structure to keep track of the distinct elements encountered so far.
- Iterate through the sorted array, and for each element, check if it is already present in the `set`.
- If it is, increment the element until it becomes distinct and add it to the `set`.
- This approach is optimal because it minimizes the number of operations required to make all elements distinct.

```cpp
int minOperations(vector<int>& nums) {
    set<int> distinct;
    int operations = 0;
    for (int num : nums) {
        if (distinct.find(num) != distinct.end()) {
            int nextDistinct = num + 1;
            while (distinct.find(nextDistinct) != distinct.end()) {
                nextDistinct++;
                operations++;
            }
            distinct.insert(nextDistinct);
            operations++;
        } else {
            distinct.insert(num);
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation and the use of the `set` data structure.
> - **Space Complexity:** $O(n)$ for the `set` data structure, where $n$ is the number of elements in the array.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to make all elements distinct by using a `set` to keep track of the distinct elements encountered so far.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structure (in this case, a `set`) to solve the problem efficiently.
- The need to consider the time and space complexities of the solution.
- The use of sorting to simplify the problem and make it easier to find duplicates.

**Mistakes to Avoid:**
- Not considering the time and space complexities of the solution.
- Not using the right data structure to solve the problem efficiently.
- Not handling edge cases correctly (e.g., an empty array or an array with all distinct elements).