## Maximum Running Time of N Computers
**Problem Link:** https://leetcode.com/problems/maximum-running-time-of-n-computers/description

**Problem Statement:**
- Input format and constraints: Given an array `batteries` of length `n` representing the battery life of each computer and a `threshold` value, find the maximum running time of `n` computers.
- Expected output format: The maximum running time should be returned as an integer.
- Key requirements and edge cases to consider: The running time cannot exceed the minimum battery life of all computers. The threshold value is used to determine the maximum running time.
- Example test cases with explanations: For example, if `batteries = [3,3,3,1,2]` and `threshold = 4`, the maximum running time is 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible running times from 1 to the minimum battery life and check if it's possible to keep all computers running for that time.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum battery life to the smallest value in the `batteries` array.
  2. Iterate over all possible running times from 1 to the minimum battery life.
  3. For each running time, check if the total battery life of all computers is greater than or equal to the running time multiplied by the `threshold`.
  4. If it is, update the maximum running time.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible solutions.

```cpp
int maxRunningTime(vector<int>& batteries, int threshold) {
    int minBattery = INT_MAX;
    for (int battery : batteries) {
        minBattery = min(minBattery, battery);
    }

    int maxTime = 0;
    for (int time = 1; time <= minBattery; time++) {
        long long totalBattery = 0;
        for (int battery : batteries) {
            totalBattery += battery;
        }
        if (totalBattery >= time * threshold) {
            maxTime = time;
        }
    }
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot minBattery)$, where $n$ is the number of computers and $minBattery$ is the minimum battery life.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is due to the constant space used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the maximum running time.
- Detailed breakdown of the approach:
  1. Initialize the minimum and maximum running times to 0 and the minimum battery life, respectively.
  2. Perform a binary search between the minimum and maximum running times.
  3. For each mid running time, check if the total battery life of all computers is greater than or equal to the running time multiplied by the `threshold`.
  4. If it is, update the minimum running time to the mid running time plus 1.
  5. Otherwise, update the maximum running time to the mid running time.
- Proof of optimality: The binary search approach ensures that we find the maximum running time in the minimum number of iterations.

```cpp
int maxRunningTime(vector<int>& batteries, int threshold) {
    long long totalBattery = 0;
    for (int battery : batteries) {
        totalBattery += battery;
    }

    int left = 0;
    int right = *min_element(batteries.begin(), batteries.end());
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        if (totalBattery >= mid * threshold) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + log(minBattery))$, where $n$ is the number of computers and $minBattery$ is the minimum battery life.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The binary search approach ensures that we find the maximum running time in the minimum number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, optimization.
- Problem-solving patterns identified: Using binary search to find the maximum running time.
- Optimization techniques learned: Reducing the time complexity from $O(n \cdot minBattery)$ to $O(n + log(minBattery))$.
- Similar problems to practice: Other optimization problems that can be solved using binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the edge cases, not using the correct data type for the total battery life.
- Edge cases to watch for: The minimum battery life, the threshold value.
- Performance pitfalls: Using a brute force approach instead of a binary search approach.
- Testing considerations: Testing the function with different inputs, including edge cases.