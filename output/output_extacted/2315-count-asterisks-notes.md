## Count Asterisks
**Problem Link:** https://leetcode.com/problems/count-asterisks/description

**Problem Statement:**
- Input: A string `s` containing `|` and `*`.
- Constraints: `1 <= s.length <= 100`, `s[i]` is either `|` or `*`.
- Expected Output: The number of asterisks between every pair of adjacent bars, inclusive.
- Key Requirements: Count asterisks between adjacent bars.
- Edge Cases: No bars, one bar, multiple bars with varying asterisks between them.

**Example Test Cases:**
- `s = "l|*e*et|*c**o|*de|"`, Output: `2`
- `s = "iamprogrammer"` , Output: `0`
- `s = "*|*|*"`, Output: `2`

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the string to find `|` characters and then counting the asterisks between them.
- This approach involves maintaining a count of asterisks between each pair of bars.

```cpp
int countAsterisks(string s) {
    int count = 0;
    bool inBar = false;
    int asteriskCount = 0;
    
    for (char c : s) {
        if (c == '|') {
            if (inBar) {
                count += asteriskCount;
                asteriskCount = 0;
            }
            inBar = !inBar;
        } else if (c == '*' && inBar) {
            asteriskCount++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through the string once.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through the string once. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that we only need to count asterisks when we are between two bars. 
- We maintain a flag `inBar` to track whether we are currently between two bars.

```cpp
int countAsterisks(string s) {
    int count = 0;
    bool inBar = false;
    
    for (char c : s) {
        if (c == '|') {
            inBar = !inBar;
        } else if (c == '*' && inBar) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through the string once.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store our variables.
> - **Optimality proof:** This is optimal because we must at least read the input string once to count the asterisks, and we do this in a single pass. The space complexity is also optimal since we only use a constant amount of space.

### Final Notes
**Learning Points:**
- Key algorithmic concept: Iterating through a string and maintaining flags to track the current state.
- Problem-solving pattern: Using a boolean flag to track whether we are currently between two bars.
- Optimization technique: Only incrementing the count when we encounter an asterisk and are between two bars.

**Mistakes to Avoid:**
- Not resetting the `inBar` flag correctly when encountering a `|` character.
- Not checking if we are between two bars before incrementing the count for an asterisk.
- Using more space than necessary by storing unnecessary information.