## Number of Unique Good Subsequences

**Problem Link:** https://leetcode.com/problems/number-of-unique-good-subsequences/description

**Problem Statement:**
- Input: a binary string `binaryString` of length `n`.
- Constraints: `1 <= n <= 10^5`.
- Expected Output: the number of unique good subsequences of `binaryString`.
- Key Requirements: A good subsequence is a subsequence that has at least one `0` and at least one `1`, or it has at least one `0` if the string contains no `1`.
- Example Test Cases:
  - Input: `binaryString = "001"`. Output: `6`.
  - Input: `binaryString = "11"`. Output: `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and count those that meet the criteria.
- Step-by-step breakdown:
  1. Generate all possible subsequences of the input string.
  2. For each subsequence, check if it contains at least one `0` and one `1`, or if it contains at least one `0` and the original string contains no `1`.
  3. Count the number of subsequences that meet the criteria.

```cpp
int countUniqueGoodSubsequences(string binaryString) {
    int n = binaryString.length();
    unordered_set<string> uniqueSubsequences;
    
    for (int mask = 1; mask < (1 << n); mask++) {
        string subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence += binaryString[i];
            }
        }
        bool hasZero = false, hasOne = false;
        for (char c : subsequence) {
            if (c == '0') hasZero = true;
            else hasOne = true;
        }
        if ((hasZero && hasOne) || (hasZero && binaryString.find('1') == string::npos)) {
            uniqueSubsequences.insert(subsequence);
        }
    }
    
    return uniqueSubsequences.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and for each subsequence, we check its validity (which takes $O(n)$ time).
> - **Space Complexity:** $O(2^n \cdot n)$, as in the worst case, we might store all possible subsequences in the `uniqueSubsequences` set.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences and checking each one, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to efficiently count the number of unique good subsequences.
- Detailed breakdown:
  1. Initialize variables to keep track of the count of subsequences ending with `0` and `1`, and the count of subsequences with at least one `0` and one `1`.
  2. Iterate through the input string. For each character:
    - If the character is `0`, update the count of subsequences ending with `0`.
    - If the character is `1`, update the count of subsequences ending with `1` and the count of subsequences with at least one `0` and one `1`.
  3. The final count of unique good subsequences is the sum of the count of subsequences with at least one `0` and one `1`, and the count of subsequences with at least one `0` if the string contains no `1`.

```cpp
int countUniqueGoodSubsequences(string binaryString) {
    int n = binaryString.length();
    long long hasZero = 0, hasOne = 0, hasBoth = 0;
    
    for (int i = 0; i < n; i++) {
        if (binaryString[i] == '0') {
            hasZero = (hasZero << 1) + 1;
            if (hasOne > 0) {
                hasBoth = (hasBoth << 1) + 1;
            }
        } else {
            hasOne = (hasOne << 1) + 1;
            if (hasZero > 0) {
                hasBoth = (hasBoth << 1) + 1;
            }
        }
    }
    
    if (hasOne == 0) {
        return hasZero;
    } else {
        return hasZero + hasOne - hasBoth;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we make a single pass through the input string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counts.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string, and it uses a constant amount of space. This is the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, bit manipulation.
- Problem-solving patterns identified: using dynamic programming to efficiently count the number of unique subsequences.
- Optimization techniques learned: reducing the time and space complexity of the brute force approach by using dynamic programming.
- Similar problems to practice: other problems involving dynamic programming and bit manipulation.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables correctly, not handling edge cases properly.
- Edge cases to watch for: empty input string, input string containing only `0`s or only `1`s.
- Performance pitfalls: using the brute force approach for large input strings.
- Testing considerations: testing the function with different input strings, including edge cases.