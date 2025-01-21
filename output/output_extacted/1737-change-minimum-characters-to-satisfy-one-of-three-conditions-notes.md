## Change Minimum Characters to Satisfy One of Three Conditions

**Problem Link:** https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description

**Problem Statement:**
- Input: Two strings `s` and `t`, each of length `n`.
- Constraints: `1 <= n <= 1000`, `s` and `t` consist of lowercase English letters.
- Expected Output: The minimum number of operations to make `s` or `t` satisfy one of the three conditions:
  1. All characters are the same.
  2. The characters alternate.
  3. No two adjacent characters are the same.
- Key Requirements:
  - Find the minimum number of operations to satisfy any of the conditions.
- Example Test Cases:
  - `s = "aba", t = "bbb"`: The minimum number of operations is 0 for condition 2 (alternating characters).
  - `s = "abc", t = "cba"`: The minimum number of operations is 2 for condition 3 (no two adjacent characters are the same).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of character changes in both strings to satisfy any of the three conditions.
- For each condition, calculate the number of operations required to transform the string into the desired form.
- Compare the results for both strings and all conditions to find the minimum number of operations.

```cpp
int minOperations(string s, string t) {
    int n = s.size();
    int result = INT_MAX;

    // Check for condition 1: All characters are the same
    for (char c = 'a'; c <= 'z'; c++) {
        int operationsS = 0;
        int operationsT = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != c) operationsS++;
            if (t[i] != c) operationsT++;
        }
        result = min(result, min(operationsS, operationsT));
    }

    // Check for condition 2: The characters alternate
    for (char c1 = 'a'; c1 <= 'z'; c1++) {
        for (char c2 = 'a'; c2 <= 'z'; c2++) {
            int operationsS = 0;
            int operationsT = 0;
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0 && s[i] != c1) operationsS++;
                if (i % 2 == 1 && s[i] != c2) operationsS++;
                if (i % 2 == 0 && t[i] != c1) operationsT++;
                if (i % 2 == 1 && t[i] != c2) operationsT++;
            }
            result = min(result, min(operationsS, operationsT));
        }
    }

    // Check for condition 3: No two adjacent characters are the same
    for (int mask = 0; mask < (1 << n); mask++) {
        int operationsS = 0;
        int operationsT = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) && s[i] != 'a') operationsS++;
            if (!(mask & (1 << i)) && s[i] != 'b') operationsS++;
            if ((mask & (1 << i)) && t[i] != 'a') operationsT++;
            if (!(mask & (1 << i)) && t[i] != 'b') operationsT++;
            if (i > 0 && ((mask & (1 << i)) == (mask & (1 << (i - 1))))) {
                operationsS++;
                operationsT++;
            }
        }
        result = min(result, min(operationsS, operationsT));
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26 \cdot 26 \cdot n + 2^n \cdot n)$, where $n$ is the length of the strings. The first term accounts for checking all possible alternating patterns, and the second term accounts for checking all possible masks for the third condition.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used to store the variables.
> - **Why these complexities occur:** The brute force approach involves checking all possible combinations, leading to exponential time complexity for the third condition.

---

### Optimal Approach (Required)

**Explanation:**
- For condition 1, we only need to check the frequency of each character in both strings and find the character with the maximum frequency in each string. The minimum number of operations is the length of the string minus the maximum frequency.
- For condition 2, we can check all possible pairs of alternating characters and calculate the number of operations required to transform each string into the alternating pattern.
- For condition 3, we can use a greedy approach to construct the string with no two adjacent characters being the same. We start with the first character and then choose the next character to be different from the previous one.

```cpp
int minOperations(string s, string t) {
    int n = s.size();
    int result = INT_MAX;

    // Check for condition 1: All characters are the same
    vector<int> freqS(26, 0);
    vector<int> freqT(26, 0);
    for (char c : s) freqS[c - 'a']++;
    for (char c : t) freqT[c - 'a']++;
    int maxFreqS = 0;
    int maxFreqT = 0;
    for (int i = 0; i < 26; i++) {
        maxFreqS = max(maxFreqS, freqS[i]);
        maxFreqT = max(maxFreqT, freqT[i]);
    }
    result = min(result, min(n - maxFreqS, n - maxFreqT));

    // Check for condition 2: The characters alternate
    for (char c1 = 'a'; c1 <= 'z'; c1++) {
        for (char c2 = 'a'; c2 <= 'z'; c2++) {
            int operationsS = 0;
            int operationsT = 0;
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0 && s[i] != c1) operationsS++;
                if (i % 2 == 1 && s[i] != c2) operationsS++;
                if (i % 2 == 0 && t[i] != c1) operationsT++;
                if (i % 2 == 1 && t[i] != c2) operationsT++;
            }
            result = min(result, min(operationsS, operationsT));
        }
    }

    // Check for condition 3: No two adjacent characters are the same
    int operationsS = 0;
    int operationsT = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) operationsS++;
        if (t[i] == t[i - 1]) operationsT++;
    }
    result = min(result, min(operationsS, operationsT));

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26 \cdot 26 \cdot n + n)$, where $n$ is the length of the strings. The first term accounts for checking all possible alternating patterns, and the second term accounts for checking the third condition.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used to store the variables.
> - **Optimality proof:** The optimal approach checks all possible combinations for the first two conditions and uses a greedy approach for the third condition, ensuring that the minimum number of operations is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: brute force, greedy approach, frequency counting.
- Problem-solving patterns identified: checking all possible combinations, using a greedy approach to construct the optimal solution.
- Optimization techniques learned: reducing the number of combinations to check, using a greedy approach to avoid unnecessary calculations.
- Similar problems to practice: string manipulation, pattern recognition.

**Mistakes to Avoid:**
- Common implementation errors: not checking all possible combinations, not using a greedy approach when applicable.
- Edge cases to watch for: empty strings, strings with a single character.
- Performance pitfalls: using exponential time complexity when a polynomial solution is possible.
- Testing considerations: testing with different input sizes, testing with different patterns.