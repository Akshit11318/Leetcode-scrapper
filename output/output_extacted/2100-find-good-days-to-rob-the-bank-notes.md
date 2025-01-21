## Find Good Days to Rob the Bank
**Problem Link:** https://leetcode.com/problems/find-good-days-to-rob-the-bank/description

**Problem Statement:**
- Input: An array `security` of length `n` representing the security level of each day and an integer `time`.
- Expected output: A list of indices representing the good days to rob the bank.
- Key requirements and edge cases to consider:
  - A day `i` is considered good if the security level of day `i` is greater than or equal to the security level of day `i - time` and day `i + time`.
  - The security level is compared using a sliding window of size `2 * time + 1`.
- Example test cases with explanations:
  - Example 1: `security = [1,1,1,1,1], time = 3`, the output should be `[2, 3]`.
  - Example 2: `security = [1,2,3,4,5,6], time = 2`, the output should be `[2, 3]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each day and compare its security level with the security levels of the previous and next `time` days.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the good days.
  2. Iterate over each day in the security array.
  3. For each day, compare its security level with the security levels of the previous and next `time` days.
  4. If the security level of the current day is greater than or equal to the security levels of the previous and next `time` days, add the day to the list of good days.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it directly checks each day against the given conditions.

```cpp
vector<int> goodDaysToRobBank(vector<int>& security, int time) {
    vector<int> goodDays;
    for (int i = time; i < security.size() - time; i++) {
        bool isGoodDay = true;
        for (int j = 1; j <= time; j++) {
            if (security[i] < security[i - j] || security[i] < security[i + j]) {
                isGoodDay = false;
                break;
            }
        }
        if (isGoodDay) {
            goodDays.push_back(i);
        }
    }
    return goodDays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot time)$, where $n$ is the length of the security array, because for each day, we are comparing its security level with the security levels of the previous and next `time` days.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the security array, because in the worst case, all days could be good days.
> - **Why these complexities occur:** The brute force approach involves nested loops, which lead to the quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to store the number of days with increasing security levels and another prefix sum array to store the number of days with decreasing security levels.
- Detailed breakdown of the approach:
  1. Initialize two prefix sum arrays, one for increasing security levels and one for decreasing security levels.
  2. Iterate over the security array and update the prefix sum arrays.
  3. Iterate over the security array again and check if the current day is a good day by comparing its security level with the security levels of the previous and next `time` days using the prefix sum arrays.
- Proof of optimality: This approach has a linear time complexity, which is the best possible time complexity for this problem.

```cpp
vector<int> goodDaysToRobBank(vector<int>& security, int time) {
    vector<int> goodDays;
    int n = security.size();
    vector<int> increasing(n, 0), decreasing(n, 0);
    for (int i = 1; i < n; i++) {
        increasing[i] = (security[i] >= security[i - 1]) ? increasing[i - 1] + 1 : 0;
        decreasing[i] = (security[i] <= security[i - 1]) ? decreasing[i - 1] + 1 : 0;
    }
    for (int i = time; i < n - time; i++) {
        if (increasing[i] >= time && decreasing[i] >= time) {
            goodDays.push_back(i);
        }
    }
    return goodDays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the security array, because we are iterating over the security array twice.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the security array, because we are using two prefix sum arrays.
> - **Optimality proof:** This approach has a linear time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays, linear time complexity.
- Problem-solving patterns identified: Using prefix sum arrays to store information about the security levels.
- Optimization techniques learned: Reducing the time complexity from quadratic to linear.
- Similar problems to practice: Problems involving prefix sum arrays and linear time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the prefix sum arrays correctly.
- Edge cases to watch for: Not handling the case where `time` is 0.
- Performance pitfalls: Not using prefix sum arrays, which can lead to a quadratic time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.