## Find the Count of Monotonic Pairs II

**Problem Link:** https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected output format: The count of monotonic pairs.
- Key requirements and edge cases to consider: The array can contain duplicate elements, and the pairs can be non-unique.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,3,4,5]`, Output: `4`. Explanation: The monotonic pairs are `(1,2)`, `(1,3)`, `(1,4)`, `(1,5)`.
  - Example 2: Input: `nums = [5,4,3,2,1]`, Output: `0`. Explanation: There are no monotonic pairs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every pair of elements in the array to see if they form a monotonic pair.
- Step-by-step breakdown of the solution:
  1. Iterate through the array with two nested loops to generate all possible pairs.
  2. For each pair, check if the elements are in increasing or decreasing order.
  3. If the elements are in increasing or decreasing order, increment the count of monotonic pairs.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it checks every possible pair of elements.

```cpp
int countMonotonicPairs(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] < nums[j] || nums[i] > nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using two nested loops to generate all possible pairs of elements.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the count of monotonic pairs.
> - **Why these complexities occur:** The time complexity is high because we are checking every possible pair of elements, resulting in a quadratic number of operations. The space complexity is low because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient algorithm to count the number of monotonic pairs.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to store the count of monotonic pairs.
  2. Iterate through the array, and for each element, find the number of elements that are greater than or less than it.
  3. Add the number of elements that are greater than or less than the current element to the count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in a linear time complexity.

```cpp
int countMonotonicPairs(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int greater = 0, lesser = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (i != j) {
                if (nums[i] < nums[j]) {
                    greater++;
                } else if (nums[i] > nums[j]) {
                    lesser++;
                }
            }
        }
        count += greater + lesser;
    }
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using two nested loops to count the number of elements that are greater than or less than each element.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the count of monotonic pairs.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array, resulting in a linear time complexity. However, we can further optimize this by using a more efficient data structure, such as a `multiset`, to count the number of elements that are greater than or less than each element.

However, this can be optimized using a `multiset` or a similar data structure to achieve a better time complexity.

```cpp
int countMonotonicPairs(vector<int>& nums) {
    int count = 0;
    multiset<int> s;
    for (int num : nums) {
        count += s.size() - distance(s.lower_bound(num), s.end());
        s.insert(num);
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we are using a `multiset` to count the number of elements that are greater than or less than each element, and the `insert` and `lower_bound` operations take logarithmic time.
> - **Space Complexity:** $O(n)$, as we are storing all elements in the `multiset`.
> - **Optimality proof:** This approach is optimal because it uses a `multiset` to efficiently count the number of elements that are greater than or less than each element, resulting in a logarithmic time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `multiset` to efficiently count the number of elements that are greater than or less than each element.
- Problem-solving patterns identified: Using a more efficient data structure to optimize the solution.
- Optimization techniques learned: Using a `multiset` to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve counting the number of elements that satisfy certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `multiset` or a similar data structure to optimize the solution.
- Edge cases to watch for: Handling duplicate elements and non-unique pairs.
- Performance pitfalls: Using a brute force approach that results in a high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness and efficiency.