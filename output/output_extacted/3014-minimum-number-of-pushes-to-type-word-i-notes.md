## Minimum Number of Pushes to Type Word I
**Problem Link:** https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description

**Problem Statement:**
- Input format and constraints: The input is a string `word`. The length of the string will be in the range $[1, 10^5]$.
- Expected output format: The minimum number of pushes required to type the word.
- Key requirements and edge cases to consider: The `i` key is broken and can only be pressed once, and the string will only contain lowercase letters.
- Example test cases with explanations:
    - For the input `"hello"`, the output should be `0` because there is no `i` in the string.
    - For the input `"iii"`, the output should be `1` because the `i` key can only be pressed once.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach would be to count the number of `i`s in the string.
- Step-by-step breakdown of the solution: 
    1. Initialize a counter to store the number of `i`s.
    2. Iterate over each character in the string.
    3. If the character is `i`, increment the counter.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
int minPushes(string word) {
    int count = 0;
    for (char c : word) {
        if (c == 'i') {
            count++;
        }
    }
    return max(0, count - 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are iterating over each character in the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counter.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the string once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because it is already quite efficient.
- Detailed breakdown of the approach: 
    1. Initialize a counter to store the number of `i`s.
    2. Iterate over each character in the string.
    3. If the character is `i`, increment the counter.
- Proof of optimality: This solution is optimal because it has a linear time complexity and uses a constant amount of space.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input string once, which already takes linear time.

```cpp
int minPushes(string word) {
    int count = 0;
    for (char c : word) {
        if (c == 'i') {
            count++;
        }
    }
    return max(0, count - 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are iterating over each character in the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counter.
> - **Optimality proof:** This solution is optimal because it has a linear time complexity and uses a constant amount of space, and further optimization is impossible because we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear iteration, constant space usage.
- Problem-solving patterns identified: Counting characters in a string.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Other string manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string.
- Edge cases to watch for: An empty string, a string with only one `i`.
- Performance pitfalls: Using data structures that scale with the input size, such as vectors or maps.
- Testing considerations: Test with strings of different lengths, including empty strings and strings with only one `i`.