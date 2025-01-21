## Teemo Attacking
**Problem Link:** https://leetcode.com/problems/teemo-attacking/description

**Problem Statement:**
- Input: `timeSeries` and `duration` as integers, representing the time series of attacks and the duration of each attack's effect.
- Expected Output: The total time of poisoned durations.
- Key Requirements: Calculate the total time of poisoned durations based on the given time series and duration.
- Example Test Cases:
  - `timeSeries = [1, 4], duration = 2`: The total time of poisoned durations is `4`.
  - `timeSeries = [1, 2], duration = 2`: The total time of poisoned durations is `3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the poisoned duration for each attack and sum them up.
- Step-by-step breakdown:
  1. Initialize a variable `totalTime` to store the total time of poisoned durations.
  2. Iterate over the `timeSeries` array.
  3. For each attack, calculate the poisoned duration and add it to `totalTime`.
  4. Handle overlapping poisoned durations by subtracting the overlapping time from `totalTime`.

```cpp
int findPoisonedDuration(vector<int>& timeSeries, int duration) {
    if (timeSeries.empty()) return 0;
    int totalTime = 0;
    for (int i = 0; i < timeSeries.size(); i++) {
        int poisonedDuration = duration;
        if (i > 0) {
            int overlappingTime = max(0, duration - (timeSeries[i] - timeSeries[i - 1]));
            poisonedDuration -= overlappingTime;
        }
        totalTime += poisonedDuration;
    }
    return totalTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of attacks in the `timeSeries` array. This is because we iterate over the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `totalTime` variable.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the array once. The space complexity is constant because we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can calculate the total time of poisoned durations by summing up the durations of non-overlapping attacks and adding the remaining duration of the last attack.
- Detailed breakdown:
  1. Initialize a variable `totalTime` to store the total time of poisoned durations.
  2. Iterate over the `timeSeries` array.
  3. For each attack, check if it overlaps with the previous attack.
  4. If it doesn't overlap, add the full duration to `totalTime`.
  5. If it overlaps, add the non-overlapping part of the duration to `totalTime`.
  6. After the loop, add the remaining duration of the last attack to `totalTime`.

```cpp
int findPoisonedDuration(vector<int>& timeSeries, int duration) {
    if (timeSeries.empty()) return 0;
    int totalTime = 0;
    for (int i = 0; i < timeSeries.size() - 1; i++) {
        totalTime += min(duration, timeSeries[i + 1] - timeSeries[i]);
    }
    return totalTime + duration;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of attacks in the `timeSeries` array. This is because we iterate over the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `totalTime` variable.
> - **Optimality proof:** This approach is optimal because we only iterate over the array once and use a constant amount of space. We also avoid unnecessary calculations by only adding the non-overlapping parts of the durations to `totalTime`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, conditional statements, and basic arithmetic operations.
- Problem-solving patterns identified: calculating the total time of poisoned durations by summing up non-overlapping durations and adding the remaining duration of the last attack.
- Optimization techniques learned: avoiding unnecessary calculations and using a constant amount of space.

**Mistakes to Avoid:**
- Common implementation errors: incorrect iteration bounds, incorrect conditional statements, and incorrect arithmetic operations.
- Edge cases to watch for: empty input array, single-element input array, and overlapping attacks.
- Performance pitfalls: using unnecessary data structures or algorithms that scale poorly with the input size.
- Testing considerations: test with different input sizes, test with overlapping and non-overlapping attacks, and test with edge cases.