## Minimum Number of Changes to Make Binary String Beautiful

**Problem Link:** https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description

**Problem Statement:**
- Input format and constraints: The input is a binary string `s` of length `n`. The goal is to make the string `beautiful`, which means that for every pair of adjacent bits, one must be `0` and the other must be `1`. The string can be modified by changing any number of bits.
- Expected output format: The minimum number of changes required to make the string beautiful.
- Key requirements and edge cases to consider: The input string only contains `0`s and `1`s, and the length of the string is a positive integer.
- Example test cases with explanations: 
    - Input: `s = "110101"`, Output: `1`
    - Input: `s = "10"`, Output: `0`
    - Input: `s = "1111"`, Output: `2`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible binary strings of the same length as the input string, and then check each one to see if it is beautiful and how many changes it would take to transform the input string into it.
- Step-by-step breakdown of the solution: 
    1. Generate all possible binary strings of length `n`.
    2. For each generated string, calculate the number of changes required to transform the input string into it.
    3. Check if the generated string is beautiful.
    4. Keep track of the minimum number of changes required to make the input string beautiful.
- Why this approach comes to mind first: It's a straightforward approach that involves checking all possibilities, which is often the first line of thinking when dealing with combinatorial problems.

```cpp
int makeBeautiful(string s) {
    int n = s.length();
    int minChanges = INT_MAX;
    // Generate all possible binary strings of length n
    for (int mask = 0; mask < (1 << n); mask++) {
        string temp = "";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) temp += '1';
            else temp += '0';
        }
        // Calculate the number of changes required to transform s into temp
        int changes = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != temp[i]) changes++;
        }
        // Check if temp is beautiful
        bool isBeautiful = true;
        for (int i = 0; i < n - 1; i++) {
            if (temp[i] == temp[i + 1]) {
                isBeautiful = false;
                break;
            }
        }
        // Update minChanges if temp is beautiful
        if (isBeautiful) minChanges = min(minChanges, changes);
    }
    return minChanges == INT_MAX ? -1 : minChanges;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we are generating $2^n$ possible binary strings, and for each string, we are performing $O(n)$ operations to calculate the number of changes and check if it's beautiful.
> - **Space Complexity:** $O(n)$, as we need to store the generated binary strings of length $n$.
> - **Why these complexities occur:** The brute force approach involves generating all possible binary strings, which leads to exponential time complexity. The space complexity is linear because we only need to store one binary string at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to realize that we don't need to generate all possible binary strings. Instead, we can observe that a beautiful binary string must alternate between `0`s and `1`s. Therefore, we can simply try two possibilities: starting with `0` and starting with `1`.
- Detailed breakdown of the approach: 
    1. Try starting the beautiful string with `0`.
    2. Calculate the number of changes required to transform the input string into a beautiful string starting with `0`.
    3. Try starting the beautiful string with `1`.
    4. Calculate the number of changes required to transform the input string into a beautiful string starting with `1`.
    5. Return the minimum of the two calculated changes.
- Why further optimization is impossible: This approach is optimal because it only considers the two possible beautiful strings that can be formed, which are the ones starting with `0` and `1`. This is the minimum number of possibilities that need to be considered to find the minimum number of changes.

```cpp
int makeBeautiful(string s) {
    int n = s.length();
    int changesStartWith0 = 0;
    int changesStartWith1 = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0 && s[i] != '0') changesStartWith0++;
        if (i % 2 == 1 && s[i] != '1') changesStartWith0++;
        if (i % 2 == 0 && s[i] != '1') changesStartWith1++;
        if (i % 2 == 1 && s[i] != '0') changesStartWith1++;
    }
    return min(changesStartWith0, changesStartWith1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are iterating over the input string twice to calculate the number of changes for the two possible beautiful strings.
> - **Space Complexity:** $O(1)$, as we only need to store a constant number of variables to keep track of the number of changes.
> - **Optimality proof:** This approach is optimal because it only considers the two possible beautiful strings that can be formed, which are the ones starting with `0` and `1`. This is the minimum number of possibilities that need to be considered to find the minimum number of changes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of observing patterns and reducing the search space to solve problems efficiently.
- Problem-solving patterns identified: The problem follows the pattern of finding the minimum number of changes required to transform one string into another, which is a common problem-solving pattern in string algorithms.
- Optimization techniques learned: The problem demonstrates the technique of reducing the search space by observing patterns and considering only the minimum number of possibilities required to solve the problem.
- Similar problems to practice: Other problems that involve finding the minimum number of changes required to transform one string into another, such as the Levenshtein distance problem.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to consider the two possible beautiful strings that can be formed, which are the ones starting with `0` and `1`.
- Edge cases to watch for: The problem does not have any edge cases that need to be handled separately, as the input string can be of any length and can contain any combination of `0`s and `1`s.
- Performance pitfalls: One performance pitfall is to use a brute force approach that generates all possible binary strings, which can lead to exponential time complexity.
- Testing considerations: The problem should be tested with a variety of input strings, including strings of different lengths and strings that contain different combinations of `0`s and `1`s.