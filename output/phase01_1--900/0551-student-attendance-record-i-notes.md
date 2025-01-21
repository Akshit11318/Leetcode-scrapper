## Student Attendance Record I

**Problem Link:** https://leetcode.com/problems/student-attendance-record-i/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` representing the attendance record of a student, where each character is either 'A', 'L', or 'P'. The length of the string is between 1 and 1000.
- Expected output format: Return `true` if the student could be rewarded, and `false` otherwise.
- Key requirements and edge cases to consider: A student could be rewarded if they have less than 2 absences and less than 3 consecutive late arrivals.
- Example test cases with explanations:
  - Input: `s = "PPALLP"` Output: `True`
  - Input: `s = "PPALLL"` Output: `False`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check for each possible scenario where a student could be rewarded, we need to count the number of absences and the maximum number of consecutive late arrivals.
- Step-by-step breakdown of the solution:
  1. Initialize counters for absences and late arrivals.
  2. Iterate over the string to count absences and late arrivals.
  3. Use a separate counter to track consecutive late arrivals.
  4. Update the maximum number of consecutive late arrivals as we iterate.
- Why this approach comes to mind first: It's straightforward to count the required metrics and compare them against the reward criteria.

```cpp
bool checkRecord(string s) {
    int absences = 0;
    int lateArrivals = 0;
    int consecutiveLate = 0;
    int maxConsecutiveLate = 0;

    for (char c : s) {
        if (c == 'A') {
            absences++;
            consecutiveLate = 0; // Reset consecutive late counter
        } else if (c == 'L') {
            lateArrivals++;
            consecutiveLate++;
            maxConsecutiveLate = max(maxConsecutiveLate, consecutiveLate);
        } else {
            consecutiveLate = 0; // Reset consecutive late counter
        }
    }

    return absences < 2 && maxConsecutiveLate < 3;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we make a single pass through the input string.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store our counters, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the string once. The space complexity is constant because our counters do not grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach applies here. However, we can simplify the solution by directly returning `false` as soon as we encounter more than one absence or three consecutive late arrivals, thus avoiding unnecessary iterations.
- Detailed breakdown of the approach:
  1. Initialize counters for absences and consecutive late arrivals.
  2. Iterate over the string, updating counters and checking the reward criteria.
  3. If the criteria are not met at any point, immediately return `false`.
- Proof of optimality: This approach is optimal because it still only requires a single pass through the input string and uses constant space, but it potentially reduces the number of iterations needed by exiting early when the reward criteria are not met.

```cpp
bool checkRecord(string s) {
    int absences = 0;
    int consecutiveLate = 0;

    for (char c : s) {
        if (c == 'A') {
            absences++;
            if (absences > 1) return false; // More than one absence
            consecutiveLate = 0; // Reset consecutive late counter
        } else if (c == 'L') {
            consecutiveLate++;
            if (consecutiveLate > 2) return false; // More than two consecutive late arrivals
        } else {
            consecutiveLate = 0; // Reset consecutive late counter
        }
    }

    return true; // If we've made it this far, the student could be rewarded
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because in the worst case, we still need to iterate over the entire string.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store our counters.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is also optimal because we cannot use less than constant space to store the necessary information.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and optimization through early returns.
- Problem-solving patterns identified: Counting and comparing against a set of criteria.
- Optimization techniques learned: Early returns to reduce unnecessary iterations.
- Similar problems to practice: Other string manipulation and pattern recognition problems.

**Mistakes to Avoid:**
- Common implementation errors: Failing to reset counters when necessary (e.g., when encountering a 'P' after an 'L').
- Edge cases to watch for: Handling strings with varying lengths and compositions.
- Performance pitfalls: Unnecessary iterations or using more space than necessary.
- Testing considerations: Ensure to test with a variety of input strings, including edge cases like very short or very long strings, and strings that just barely meet or fail the reward criteria.