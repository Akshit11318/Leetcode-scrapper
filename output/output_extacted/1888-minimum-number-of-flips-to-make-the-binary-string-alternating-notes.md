## Minimum Number of Flips to Make the Binary String Alternating

**Problem Link:** https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description

**Problem Statement:**
- Input: A binary string `binaryString`.
- Output: The minimum number of flips required to make the binary string alternating.
- Key Requirements: The string must be alternating between '0' and '1'.
- Edge Cases: Empty string, single character string, strings of even and odd lengths.

**Example Test Cases:**
- Input: `binaryString = "111000"` 
  Output: `2`
  Explanation: Flip the first and third bits to get the string "101010", which is alternating.

- Input: `binaryString = "010"`
  Output: `0`
  Explanation: The string is already alternating.

- Input: `binaryString = "1111"`
  Output: `2`
  Explanation: Flip two bits to make the string alternating.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible combinations of flips.
- For each bit in the string, we can either flip it or not, resulting in $2^n$ possible combinations for a string of length $n$.
- We then check each combination to see if the resulting string is alternating.

```cpp
int minFlips(string binaryString) {
    int n = binaryString.size();
    int minFlips = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        string flippedString = binaryString;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                flippedString[i] = flippedString[i] == '0' ? '1' : '0';
            }
        }
        if (isAlternating(flippedString)) {
            int flips = __builtin_popcount(mask);
            minFlips = min(minFlips, flips);
        }
    }
    return minFlips;
}

bool isAlternating(string s) {
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == s[i - 1]) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the binary string. This is because we generate all possible combinations of flips ($2^n$) and for each combination, we check if the resulting string is alternating, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the flipped string.
> - **Why these complexities occur:** The brute force approach checks all possible combinations of flips, leading to exponential time complexity. The space complexity is linear because we need to store the flipped string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to consider two possibilities for the first bit: '0' or '1'. 
- For each possibility, we then check the rest of the string and count the number of flips required to make it alternating.
- We choose the possibility that requires fewer flips.

```cpp
int minFlips(string binaryString) {
    int n = binaryString.size();
    int flipsStartingWith0 = 0;
    int flipsStartingWith1 = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            if (binaryString[i] != '0') flipsStartingWith0++;
            if (binaryString[i] != '1') flipsStartingWith1++;
        } else {
            if (binaryString[i] != '1') flipsStartingWith0++;
            if (binaryString[i] != '0') flipsStartingWith1++;
        }
    }
    return min(flipsStartingWith0, flipsStartingWith1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the binary string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the flip counts.
> - **Optimality proof:** This approach is optimal because it considers all possible alternating patterns (starting with '0' or '1') and chooses the one that requires the fewest flips. It does so in linear time, which is the best possible time complexity for this problem because we must at least read the input string.

---

### Final Notes

**Learning Points:**
- The importance of considering all possible patterns when solving string problems.
- How to optimize a brute force approach by reducing the number of possibilities to consider.
- The use of bit manipulation to solve problems involving binary strings.

**Mistakes to Avoid:**
- Not considering all possible patterns, leading to incorrect results.
- Using a brute force approach when a more efficient solution is possible.
- Not optimizing the solution for time and space complexity.