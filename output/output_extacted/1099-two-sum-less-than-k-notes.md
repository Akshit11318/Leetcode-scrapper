## Two Sum Less Than K
**Problem Link:** https://leetcode.com/problems/two-sum-less-than-k/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: The length of `nums` is between 1 and 1000, and `k` is between 1 and 1000.
- Expected output format: The maximum sum of two numbers in `nums` that is less than `k`.
- Key requirements and edge cases to consider: The input array can contain duplicate numbers, and the output should be the maximum sum that is less than `k`, not just any sum.
- Example test cases with explanations:
  - `nums = [34,23,1,24,75,33,54,8], k = 60` should return `58` because `24 + 34 = 58` is the maximum sum less than `60`.
  - `nums = [10,20,30], k = 15` should return `-1` because there is no pair of numbers that sums to less than `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum sum of two numbers that is less than `k`, we can compare every pair of numbers in the array and keep track of the maximum sum that meets the condition.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_sum` to a value that is less than any possible sum (e.g., `-1`).
  2. Iterate over each pair of numbers in the array using nested loops.
  3. For each pair, calculate the sum and check if it is less than `k`.
  4. If the sum is less than `k` and greater than the current `max_sum`, update `max_sum`.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible pairs and checking their sums against the condition.

```cpp
int twoSumLessThanK(vector<int>& nums, int k) {
    int max_sum = -1;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int sum = nums[i] + nums[j];
            if (sum < k && sum > max_sum) {
                max_sum = sum;
            }
        }
    }
    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because we are using nested loops to compare each pair of numbers.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the `max_sum` variable.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loops, and the space complexity is constant because we are not using any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sorting the array allows us to find the maximum sum more efficiently by maintaining two pointers, one at the start and one at the end of the array, and moving them based on the sum of the values at these pointers.
- Detailed breakdown of the approach:
  1. Sort the array in ascending order.
  2. Initialize two pointers, `left` at the start of the array and `right` at the end.
  3. Initialize `max_sum` to `-1`.
  4. Loop until `left` is greater than `right`.
  5. Calculate the sum of the values at the `left` and `right` pointers.
  6. If the sum is less than `k` and greater than the current `max_sum`, update `max_sum`.
  7. If the sum is less than `k`, move the `left` pointer to the right to try to increase the sum. Otherwise, move the `right` pointer to the left to decrease the sum.
- Proof of optimality: This approach ensures that we consider all possible pairs of numbers in a way that maximizes the sum while being less than `k`, and it does so in a time-efficient manner by only iterating through the array once after sorting.

```cpp
int twoSumLessThanK(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int max_sum = -1;
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum < k) {
            max_sum = max(max_sum, sum);
            left++;
        } else {
            right--;
        }
    }
    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array, because sorting the array takes $O(n \log n)$ time and the subsequent while loop takes $O(n)$ time.
> - **Space Complexity:** $O(1)$ if the sorting algorithm used is in-place, otherwise $O(n)$ for sorting algorithms that require extra space.
> - **Optimality proof:** This approach is optimal because it ensures that we find the maximum sum less than `k` in the most efficient way possible, taking advantage of the sorted array to minimize the number of comparisons needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two-pointer technique.
- Problem-solving patterns identified: Using sorting to simplify the problem, applying the two-pointer technique to find the maximum sum efficiently.
- Optimization techniques learned: Taking advantage of the properties of a sorted array to reduce the number of comparisons needed.
- Similar problems to practice: Other problems involving finding maximum or minimum sums, or applying the two-pointer technique in different contexts.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (e.g., an empty array), not initializing variables correctly.
- Edge cases to watch for: Arrays with duplicate numbers, arrays with negative numbers, `k` being less than the smallest possible sum.
- Performance pitfalls: Using a brute force approach for large inputs, not considering the time complexity of the sorting algorithm used.
- Testing considerations: Testing with arrays of different sizes, testing with different values of `k`, testing edge cases.