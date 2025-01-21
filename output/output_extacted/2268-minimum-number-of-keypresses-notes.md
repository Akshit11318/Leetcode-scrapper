## Minimum Number of Keypresses
**Problem Link:** https://leetcode.com/problems/minimum-number-of-keypresses/description

**Problem Statement:**
- Input: A string `s` consisting of lowercase letters.
- Output: The minimum number of keypresses to type `s` using the given rules.
- Rules:
  - For each character, you can either press the key once or hold the key to type the same character multiple times.
  - If a character is repeated three or more times, it's more efficient to hold the key.
- Key requirements and edge cases:
  - `1 <= s.length <= 10^5`
  - `s` consists only of lowercase letters.

### Brute Force Approach
**Explanation:**
- The brute force approach involves iterating over the string `s` and checking each character to see if it's repeated.
- We can use a simple loop to count the occurrences of each character and calculate the minimum number of keypresses.

```cpp
int minKeypresses(string s) {
    int result = 0;
    for (int i = 0; i < s.length();) {
        int count = 0;
        while (i + count < s.length() && s[i] == s[i + count]) {
            count++;
        }
        if (count == 2) {
            result += 2;
        } else if (count > 2) {
            result += count - (count / 3) + 1;
        } else {
            result++;
        }
        i += count;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we're iterating over the string once.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the result and the count of repeated characters.
> - **Why these complexities occur:** The time complexity is linear because we're scanning the string once, and the space complexity is constant because we're not using any data structures that scale with the input size.

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is actually the same as the brute force approach, as we need to scan the entire string to count the occurrences of each character.
- However, we can make some minor optimizations to the code to improve readability and performance.

```cpp
int minKeypresses(string s) {
    int result = 0;
    int i = 0;
    while (i < s.length()) {
        int count = 1;
        while (i + 1 < s.length() && s[i] == s[i + 1]) {
            i++;
            count++;
        }
        result += (count < 3) ? count : count - (count / 3) + 1;
        i++;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the result and the count of repeated characters.
> - **Optimality proof:** This is the optimal solution because we need to scan the entire string to count the occurrences of each character, and we're doing so in a single pass.

### Final Notes
**Learning Points:**
- The importance of scanning the input data at least once to gather information.
- How to calculate the minimum number of keypresses based on the count of repeated characters.
- The trade-off between code readability and performance optimization.

**Mistakes to Avoid:**
- Not handling edge cases, such as an empty input string.
- Not using a clear and efficient algorithm to count the occurrences of each character.
- Not optimizing the code for performance and readability.