## Number of Students Doing Homework at a Given Time

**Problem Link:** https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description

**Problem Statement:**
- Input format: `startTime` and `endTime` arrays, each representing the start and end times of homework for a student, and a `queryTime` representing the time at which we want to find the number of students doing homework.
- Constraints: The input arrays `startTime` and `endTime` have the same length, and all times are in the range $[1, 1000]$.
- Expected output format: The number of students doing homework at the given `queryTime`.
- Key requirements and edge cases to consider: Handling cases where the query time is exactly equal to a start or end time, ensuring correct counting when a student's homework period spans the query time.
- Example test cases with explanations:
  - Example 1: `startTime = [1,2,3]`, `endTime = [3,2,7]`, `queryTime = 4`. Expected output: 1.
  - Example 2: `startTime = [4]`, `endTime = [4]`, `queryTime = 4`. Expected output: 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each student's homework period and check if the `queryTime` falls within that period.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable `count` to 0.
  2. Iterate through each student's homework period using a loop.
  3. For each period, check if `queryTime` is greater than or equal to `startTime` and less than or equal to `endTime`.
  4. If the condition is met, increment the `count` variable.
  5. After iterating through all periods, return the `count` as the number of students doing homework at the `queryTime`.

```cpp
int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
    int count = 0;
    for (int i = 0; i < startTime.size(); i++) {
        if (queryTime >= startTime[i] && queryTime <= endTime[i]) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of students. This is because we are iterating through each student's homework period once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count variable, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear because we perform a single pass through the input arrays, and the space complexity is constant because we only use a fixed amount of space to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in the same manner as the brute force approach, as it already has a linear time complexity which is optimal for this problem. The brute force approach is already optimal because we must at least look at each student's homework period once to determine if they are doing homework at the query time.
- Detailed breakdown of the approach: Same as the brute force approach, as it is already optimal.
- Proof of optimality: Since we must examine each student's homework period at least once, the optimal time complexity is $O(n)$, where $n$ is the number of students. The brute force approach achieves this, making it the optimal solution.

```cpp
int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
    int count = 0;
    for (int i = 0; i < startTime.size(); i++) {
        if (queryTime >= startTime[i] && queryTime <= endTime[i]) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of students. This is because we are iterating through each student's homework period once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count variable, regardless of the input size.
> - **Optimality proof:** The time complexity is linear because we perform a single pass through the input arrays, and the space complexity is constant because we only use a fixed amount of space to store the count. This is optimal because we must at least look at each student's homework period once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, conditional counting.
- Problem-solving patterns identified: Iterating through data to find matches based on conditions.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent need to examine each piece of data at least once.
- Similar problems to practice: Other problems involving scanning through data to find matches or counts based on given conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the count variable, incorrect conditional statements.
- Edge cases to watch for: Handling cases where the query time is exactly equal to a start or end time.
- Performance pitfalls: Unnecessary iterations or nested loops that could increase time complexity.
- Testing considerations: Ensure to test with a variety of input sizes and edge cases to validate the solution's correctness and performance.