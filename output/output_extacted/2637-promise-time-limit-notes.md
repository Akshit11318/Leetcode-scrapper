## Promise Time Limit

**Problem Link:** https://leetcode.com/problems/promise-time-limit/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` and two arrays `time` and `probability` of length `n` as input. The `time` array contains the time limits for each promise, and the `probability` array contains the probabilities of each promise being kept.
- Expected output format: The problem requires finding the maximum expected time limit for the promises.
- Key requirements and edge cases to consider: The time limits and probabilities must be non-negative, and the probabilities must sum up to 1.
- Example test cases with explanations: For example, if `time = [1, 2, 3]` and `probability = [0.5, 0.3, 0.2]`, the maximum expected time limit is `1 * 0.5 + 2 * 0.3 + 3 * 0.2 = 1.7`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the expected time limit by multiplying each time limit with its corresponding probability and summing them up.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum expected time limit.
  2. Iterate over the `time` and `probability` arrays.
  3. For each pair of time limit and probability, multiply them together and add the result to the maximum expected time limit.
- Why this approach comes to mind first: This approach is straightforward and directly calculates the expected time limit.

```cpp
double maxExpectedTimeLimit(vector<int>& time, vector<double>& probability) {
    double maxExpectedTime = 0.0;
    for (int i = 0; i < time.size(); i++) {
        maxExpectedTime += time[i] * probability[i];
    }
    return maxExpectedTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of promises. This is because we iterate over the `time` and `probability` arrays once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum expected time limit.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each promise, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we must iterate over the `time` and `probability` arrays to calculate the expected time limit.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the maximum expected time limit.
  2. Iterate over the `time` and `probability` arrays.
  3. For each pair of time limit and probability, multiply them together and add the result to the maximum expected time limit.
- Proof of optimality: This approach is optimal because we must examine each promise to calculate the expected time limit, and we perform a constant amount of work for each promise.
- Why further optimization is impossible: Further optimization is impossible because we must iterate over the `time` and `probability` arrays to calculate the expected time limit, and we perform a constant amount of work for each promise.

```cpp
double maxExpectedTimeLimit(vector<int>& time, vector<double>& probability) {
    double maxExpectedTime = 0.0;
    for (int i = 0; i < time.size(); i++) {
        maxExpectedTime += time[i] * probability[i];
    }
    return maxExpectedTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of promises. This is because we iterate over the `time` and `probability` arrays once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum expected time limit.
> - **Optimality proof:** This approach is optimal because we must examine each promise to calculate the expected time limit, and we perform a constant amount of work for each promise.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of expected value, which is a fundamental concept in probability theory.
- Problem-solving patterns identified: The problem requires iterating over the `time` and `probability` arrays to calculate the expected time limit, which is a common pattern in problems involving expected values.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the brute force approach, as the optimal solution is the same as the brute force approach.
- Similar problems to practice: Other problems involving expected values, such as calculating the expected value of a random variable or finding the maximum expected value of a set of outcomes.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the maximum expected time limit to 0.0, which can cause incorrect results.
- Edge cases to watch for: The problem requires checking for edge cases such as empty input arrays or probabilities that do not sum up to 1.
- Performance pitfalls: The problem does not have any performance pitfalls beyond the brute force approach, as the optimal solution is the same as the brute force approach.
- Testing considerations: The problem requires testing for different input scenarios, including edge cases and large input sizes.