## Minimum Deletions to Make String Balanced
**Problem Link:** https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description

**Problem Statement:**
- Input: A string `s` containing only characters 'L' and 'R'.
- Constraints: `1 <= s.length <= 10^5`.
- Expected Output: The minimum number of deletions to make the string balanced, where a string is balanced if it has an equal number of 'L' and 'R' characters.
- Key Requirements: Find the minimum number of deletions required.
- Edge Cases: An empty string, a string with only one type of character, or a string with an odd length.

**Example Test Cases:**
- Input: `s = "LLRR"`; Output: `0`. The string is already balanced.
- Input: `s = "RLLLLRRRLR"`; Output: `3`. To balance the string, we can delete 3 'L' characters.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to consider all possible combinations of deletions to find the minimum required to balance the string.
- Step-by-step breakdown:
  1. Count the total number of 'L' and 'R' characters in the string.
  2. Calculate the difference between the counts of 'L' and 'R' characters.
  3. Since we need an equal number of 'L' and 'R' characters for the string to be balanced, the minimum number of deletions required would be half of the absolute difference between the counts of 'L' and 'R' characters.

```cpp
int minimumDeletions(string s) {
    int countL = 0, countR = 0;
    for (char c : s) {
        if (c == 'L') countL++;
        else countR++;
    }
    return abs(countL - countR) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate through the string once to count 'L' and 'R' characters.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts of 'L' and 'R' characters.
> - **Why these complexities occur:** The brute force approach is straightforward and only requires a single pass through the string, leading to linear time complexity. The space complexity is constant because we only need a fixed amount of space to store the counts, regardless of the string's length.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is the same as in the brute force approach: calculate the difference between the counts of 'L' and 'R' characters and return half of the absolute difference.
- Detailed breakdown: The optimal approach does not differ significantly from the brute force in this case because the problem's nature requires counting the characters, which is inherently linear in the string's length.
- Proof of optimality: Since we must at least read the input string once to determine the counts of 'L' and 'R', the time complexity cannot be better than $O(n)$, making the current approach optimal.

```cpp
int minimumDeletions(string s) {
    int countL = 0, countR = 0;
    for (char c : s) {
        if (c == 'L') countL++;
        else countR++;
    }
    return abs(countL - countR) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, as we must iterate through the string to count 'L' and 'R' characters.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts.
> - **Optimality proof:** This approach is optimal because it achieves the minimum time complexity required to solve the problem, which is reading the input string once.

---

### Final Notes
**Learning Points:**
- The importance of understanding the problem constraints and requirements.
- The need to consider the minimum operations required to achieve the desired outcome.
- The role of counting characters in string problems.

**Mistakes to Avoid:**
- Not considering edge cases, such as an empty string or a string with only one type of character.
- Overcomplicating the solution by considering unnecessary operations.
- Not optimizing the solution for space complexity.

**Similar Problems to Practice:**
- Other string manipulation problems that require character counting or balancing.
- Problems that involve finding the minimum number of operations to achieve a certain state.
- Problems that require considering edge cases and optimizing for both time and space complexity.