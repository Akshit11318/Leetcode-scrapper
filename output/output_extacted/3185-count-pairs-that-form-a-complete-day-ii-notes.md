## Count Pairs That Form a Complete Day II

**Problem Link:** https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/description

**Problem Statement:**
- Input: An array of integers `nums` where each integer represents the time of day in 24-hour format, with the hour and minute concatenated.
- Constraints: `1 <= nums.length <= 10^5`, `100 <= nums[i] <= 9999`.
- Expected output: The number of pairs that form a complete day, where a pair consists of two times `a` and `b` such that `a + b` equals 24 hours in the format `HHMM`.
- Key requirements: Each element in the input array must be unique.
- Example test cases:
  - Input: `nums = [555, 901, 845, 120, 1032]`
  - Output: `2`
  - Explanation: The pairs `(555, 845)` and `(120, 1032)` form a complete day.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each time in the array, compare it with every other time to check if their sum equals 24 hours.
- Step-by-step breakdown:
  1. Iterate through each time in the array.
  2. For each time, iterate through the rest of the times in the array.
  3. Check if the sum of the current time and the compared time equals 24 hours.
  4. If a match is found, increment the count of pairs.

```cpp
int countCompleteDays(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if ((nums[i] / 100 + nums[j] / 100) == 24 && (nums[i] % 100 + nums[j] % 100) == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of times in the input array. This is because we have two nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of pairs.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only keeping track of the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of comparing each time with every other time, we can use a `unordered_map` to store the times we've seen so far and their counts.
- Detailed breakdown:
  1. Create an `unordered_map` to store the times as keys and their counts as values.
  2. Iterate through the array of times.
  3. For each time, calculate its complement (the time that would make a complete day when added to it).
  4. Check if the complement is already in the map. If it is, increment the count of pairs by the count of the complement.
  5. Insert or update the current time in the map.

```cpp
int countCompleteDays(vector<int>& nums) {
    unordered_map<int, int> timeCount;
    int count = 0;
    for (int time : nums) {
        int hour = time / 100, minute = time % 100;
        int complementHour = 24 - hour, complementMinute = 0 - minute;
        if (complementMinute < 0) {
            complementHour--;
            complementMinute += 60;
        }
        int complement = complementHour * 100 + complementMinute;
        if (timeCount.find(complement) != timeCount.end()) {
            count += timeCount[complement];
        }
        timeCount[time]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of times in the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every time in the map.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is also optimal because we need to store the counts of the times to calculate the pairs efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using a map to store counts of elements for efficient lookup and calculation of pairs.
- Problem-solving patterns: Identifying the need to find pairs that satisfy a certain condition and using a data structure to facilitate this.
- Optimization techniques: Reducing the time complexity from quadratic to linear by avoiding nested loops and using a map for efficient lookup.
- Similar problems to practice: Other problems involving finding pairs or calculating counts efficiently, such as two-sum problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the complement of a time or failing to update the count of pairs correctly.
- Edge cases to watch for: Handling times that are exactly on the hour (e.g., 1200) and ensuring the complement calculation handles wrap-around correctly.
- Performance pitfalls: Using nested loops or other inefficient algorithms that lead to high time complexity.
- Testing considerations: Ensuring the solution works correctly for a variety of inputs, including edge cases and large datasets.