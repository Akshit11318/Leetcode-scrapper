## Number of Changing Keys
**Problem Link:** https://leetcode.com/problems/number-of-changing-keys/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `k`, find the number of changing keys.
- Expected output format: Return the number of changing keys.
- Key requirements and edge cases to consider: The string `s` only contains lowercase English letters and the integer `k` is a positive integer.
- Example test cases with explanations: 
    - Input: `s = "abc", k = 2`
    - Output: `2`
    - Explanation: The first and second keys are changing keys.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each character in the string `s` and check if the current character is different from the previous character.
- Step-by-step breakdown of the solution:
    1. Initialize a variable `count` to store the number of changing keys.
    2. Iterate through each character in the string `s`.
    3. For each character, check if it is different from the previous character.
    4. If the characters are different, increment the `count` variable.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
class Solution {
public:
    int changingKeys(string s, int k) {
        int count = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s[i] != s[i - 1]) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `count` variable.
> - **Why these complexities occur:** The time complexity is linear because we iterate through each character in the string, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can simplify the code and make it more efficient by using a single loop.
- Detailed breakdown of the approach:
    1. Initialize a variable `count` to store the number of changing keys.
    2. Iterate through each character in the string `s` starting from the second character.
    3. For each character, check if it is different from the previous character.
    4. If the characters are different, increment the `count` variable.
- Proof of optimality: This approach is optimal because we only iterate through each character in the string once, and we use a constant amount of space.

```cpp
class Solution {
public:
    int changingKeys(string s, int k) {
        int count = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s[i] != s[i - 1]) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `count` variable.
> - **Optimality proof:** This approach is optimal because we only iterate through each character in the string once, and we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and constant space complexity.
- Problem-solving patterns identified: Simplifying the problem by iterating through each character in the string.
- Optimization techniques learned: Using a single loop to iterate through each character in the string.
- Similar problems to practice: Other problems that involve iterating through a string or array.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `count` variable, not checking for the base case (i.e., an empty string), and not using a constant amount of space.
- Edge cases to watch for: An empty string, a string with a single character, and a string with duplicate characters.
- Performance pitfalls: Using more than one loop to iterate through each character in the string.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.