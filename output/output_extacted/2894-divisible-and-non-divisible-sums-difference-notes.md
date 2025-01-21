## Divisible and Non-Divisible Sums Difference
**Problem Link:** https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= k <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected output format: The difference between the sum of all numbers in `nums` that are divisible by `k` and the sum of all numbers in `nums` that are not divisible by `k`.
- Key requirements and edge cases to consider: Handle cases where the input array is empty or contains only one element, and ensure the solution works for large inputs.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4]` and `k = 3`, the sum of divisible numbers is `3` and the sum of non-divisible numbers is `1 + 2 + 4 = 7`, so the difference is `7 - 3 = 4`.
  - For `nums = [4, 7, 9, 6, 9, 5]` and `k = 5`, the sum of divisible numbers is `5 + 10 = 15` and the sum of non-divisible numbers is `4 + 7 + 9 + 6 + 9 = 35`, so the difference is `35 - 15 = 20`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array, check each number's divisibility by `k`, and accumulate the sums of divisible and non-divisible numbers separately.
- Step-by-step breakdown of the solution:
  1. Initialize two sums, `divisibleSum` and `nonDivisibleSum`, to zero.
  2. Iterate through each number `num` in the array `nums`.
  3. For each `num`, check if it is divisible by `k` by using the modulo operator (`num % k == 0`).
  4. If `num` is divisible by `k`, add it to `divisibleSum`; otherwise, add it to `nonDivisibleSum`.
  5. After iterating through all numbers, calculate the difference between `nonDivisibleSum` and `divisibleSum`.
- Why this approach comes to mind first: It directly implements the problem statement's requirements without considering optimization.

```cpp
int divisibleAndNonDivisibleSumsDifference(vector<int>& nums, int k) {
    int divisibleSum = 0;
    int nonDivisibleSum = 0;
    for (int num : nums) {
        if (num % k == 0) {
            divisibleSum += num;
        } else {
            nonDivisibleSum += num;
        }
    }
    return nonDivisibleSum - divisibleSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we iterate through the array once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the sums, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the input array, and the space complexity is constant because we only use a fixed amount of space to store the sums.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity because we must examine each element at least once to determine its divisibility by `k`.
- Detailed breakdown of the approach: The optimal approach remains the same as the brute force approach since it already has the best possible time complexity for this problem.
- Proof of optimality: Any algorithm solving this problem must at least read the input, which requires $O(n)$ time. Thus, the brute force approach is optimal.
- Why further optimization is impossible: We cannot improve upon the time complexity because we must check each number's divisibility, which inherently requires a linear scan of the input.

```cpp
int divisibleAndNonDivisibleSumsDifference(vector<int>& nums, int k) {
    int divisibleSum = 0;
    int nonDivisibleSum = 0;
    for (int num : nums) {
        if (num % k == 0) {
            divisibleSum += num;
        } else {
            nonDivisibleSum += num;
        }
    }
    return nonDivisibleSum - divisibleSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** The algorithm is optimal because it achieves the best possible time complexity for the problem by only requiring a single pass through the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and accumulation of sums.
- Problem-solving patterns identified: Direct implementation of problem requirements often leads to an optimal or near-optimal solution.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent requirements of the problem.
- Similar problems to practice: Problems involving iteration and conditional checks, such as finding the maximum or minimum in an array, or problems that require accumulating sums based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, incorrect use of the modulo operator, or not handling edge cases like an empty input array.
- Edge cases to watch for: Empty input array, array with a single element, or when all elements are divisible or non-divisible by `k`.
- Performance pitfalls: Attempting to optimize beyond the optimal solution, which can lead to overcomplicating the code without achieving better performance.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution works as expected.