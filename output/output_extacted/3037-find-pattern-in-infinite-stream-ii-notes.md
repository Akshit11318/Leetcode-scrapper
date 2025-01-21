## Find Pattern in Infinite Stream II

**Problem Link:** https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/description

**Problem Statement:**
- Input format: A binary string `stream` of length `n` and an integer `k`.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= 10^5`, `stream` consists only of `0`s and `1`s.
- Expected output format: Return the minimum window size `k` for which there exists a repeating pattern of length `k` in the infinite stream `stream`.
- Key requirements and edge cases to consider: 
    - If no repeating pattern of length `k` exists, return `-1`.
    - The pattern must be a substring of `stream`.
    - The pattern must repeat infinitely in the infinite stream.
- Example test cases with explanations: 
    - For `stream = "0110"`, `k = 2`, the output should be `2` because the pattern `"01"` repeats infinitely.
    - For `stream = "1011"`, `k = 4`, the output should be `-1` because no pattern of length `4` repeats infinitely.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every substring of length `k` in `stream` and see if it repeats infinitely in the infinite stream.
- Step-by-step breakdown of the solution:
    1. Generate all substrings of length `k` from `stream`.
    2. For each substring, check if it repeats infinitely in the infinite stream by comparing it with the corresponding substring in the next `k` characters, and so on.
    3. If a repeating pattern is found, return `k`.
- Why this approach comes to mind first: It is the most straightforward way to check for a repeating pattern.

```cpp
int findPattern(string stream, int k) {
    int n = stream.size();
    for (int i = 0; i <= n - k; i++) {
        string pattern = stream.substr(i, k);
        bool isRepeating = true;
        for (int j = i + k; j < n; j += k) {
            for (int p = 0; p < k; p++) {
                if (stream[(j + p) % n] != pattern[p]) {
                    isRepeating = false;
                    break;
                }
            }
            if (!isRepeating) break;
        }
        if (isRepeating) return k;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$ because for each substring of length `k`, we are potentially checking `n/k` substrings of length `k`.
> - **Space Complexity:** $O(k)$ for storing the pattern.
> - **Why these complexities occur:** The nested loops cause the high time complexity, and the space complexity is due to storing the pattern.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every substring, we can use the KMP (Knuth-Morris-Pratt) algorithm to efficiently check for a repeating pattern.
- Detailed breakdown of the approach:
    1. Preprocess the `stream` to build the KMP lookup table.
    2. Use the KMP algorithm to check if the pattern repeats infinitely in the infinite stream.
- Proof of optimality: The KMP algorithm has a linear time complexity, making it the most efficient way to check for a repeating pattern.

```cpp
vector<int> computeLPS(string pattern) {
    int m = pattern.size();
    vector<int> lps(m);
    int length = 0;
    lps[0] = 0;
    int i = 1;
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

int findPattern(string stream, int k) {
    int n = stream.size();
    for (int i = 0; i <= n - k; i++) {
        string pattern = stream.substr(i, k);
        vector<int> lps = computeLPS(pattern);
        bool isRepeating = true;
        int j = k;
        int patternIndex = 0;
        while (j < n) {
            if (stream[j] == pattern[patternIndex]) {
                patternIndex++;
                j++;
                if (patternIndex == k) {
                    patternIndex = lps[patternIndex - 1];
                }
            } else {
                if (patternIndex != 0) {
                    patternIndex = lps[patternIndex - 1];
                } else {
                    isRepeating = false;
                    break;
                }
            }
        }
        if (isRepeating) return k;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ because we are using the KMP algorithm to check for a repeating pattern.
> - **Space Complexity:** $O(k)$ for storing the pattern and the KMP lookup table.
> - **Optimality proof:** The KMP algorithm has a linear time complexity, making it the most efficient way to check for a repeating pattern.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: KMP algorithm, string matching, and pattern recognition.
- Problem-solving patterns identified: Using preprocessing to improve efficiency and applying algorithms to solve complex problems.
- Optimization techniques learned: Using the KMP algorithm to reduce time complexity.
- Similar problems to practice: String matching, pattern recognition, and text processing problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the KMP algorithm or not handling edge cases properly.
- Edge cases to watch for: Empty strings, strings with only one character, and patterns that do not repeat infinitely.
- Performance pitfalls: Not using the KMP algorithm or using a naive approach with high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution is correct and efficient.