## Count the Repetitions

**Problem Link:** [https://leetcode.com/problems/count-the-repetitions/description](https://leetcode.com/problems/count-the-repetitions/description)

**Problem Statement:**
- Input format: `string` `s1` and `s2`, and an integer `n`.
- Constraints: `s1` and `s2` are non-empty strings, and `n` is a positive integer.
- Expected output format: The number of repetitions of `s1` in `s2` repeated `n` times.
- Key requirements and edge cases to consider: Handling cases where `s1` is longer than `s2`, and optimizing the solution for large values of `n`.
- Example test cases with explanations:
  - Example 1: `s1 = "abacaba", s2 = "abacabaabacaba", n = 2`. Output: `2`.
  - Example 2: `s1 = "nac", s2 = "nac", n = 1`. Output: `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Repeat `s2` `n` times and count the occurrences of `s1`.
- Step-by-step breakdown of the solution:
  1. Repeat `s2` `n` times to form a new string `s2_repeated`.
  2. Initialize a counter to store the number of repetitions of `s1`.
  3. Iterate over `s2_repeated` with a sliding window of size `s1.length()`.
  4. For each window, check if the substring matches `s1`.
  5. If it matches, increment the counter.
- Why this approach comes to mind first: It directly addresses the problem statement by repeating `s2` and counting occurrences of `s1`.

```cpp
string s1, s2;
int n;
int countRepetitions(string s1, string s2, int n) {
    string s2_repeated = "";
    for (int i = 0; i < n; i++) {
        s2_repeated += s2;
    }
    int count = 0;
    for (int i = 0; i <= s2_repeated.length() - s1.length(); i++) {
        if (s2_repeated.substr(i, s1.length()) == s1) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot s2.length() \cdot s1.length())$, where `n` is the number of repetitions and `s1.length()` and `s2.length()` are the lengths of `s1` and `s2` respectively.
> - **Space Complexity:** $O(n \cdot s2.length())$ for storing the repeated string `s2_repeated`.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is due to the repeated string `s2_repeated`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `KMP` (Knuth-Morris-Pratt) algorithm to efficiently count the occurrences of `s1` in `s2_repeated`.
- Detailed breakdown of the approach:
  1. Implement the `KMP` algorithm to build a lookup table for `s1`.
  2. Repeat `s2` `n` times and iterate over the repeated string using the `KMP` algorithm.
  3. Count the occurrences of `s1` using the `KMP` algorithm.
- Proof of optimality: The `KMP` algorithm has a time complexity of $O(s1.length() + s2_repeated.length())$, which is optimal for this problem.
- Why further optimization is impossible: The `KMP` algorithm is already optimal for string matching, and further optimization would require a different algorithm or data structure.

```cpp
int countRepetitions(string s1, string s2, int n) {
    vector<int> lps(s1.length());
    int j = 0;
    for (int i = 1; i < s1.length(); i++) {
        while (j > 0 && s1[i] != s1[j]) {
            j = lps[j - 1];
        }
        if (s1[i] == s1[j]) {
            j++;
        }
        lps[i] = j;
    }
    string s2_repeated = "";
    for (int i = 0; i < n; i++) {
        s2_repeated += s2;
    }
    int count = 0;
    j = 0;
    for (int i = 0; i < s2_repeated.length(); i++) {
        while (j > 0 && s2_repeated[i] != s1[j]) {
            j = lps[j - 1];
        }
        if (s2_repeated[i] == s1[j]) {
            j++;
        }
        if (j == s1.length()) {
            count++;
            j = lps[j - 1];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(s1.length() + n \cdot s2.length())$, where `n` is the number of repetitions and `s1.length()` and `s2.length()` are the lengths of `s1` and `s2` respectively.
> - **Space Complexity:** $O(s1.length() + n \cdot s2.length())$ for storing the repeated string `s2_repeated` and the lookup table.
> - **Optimality proof:** The `KMP` algorithm is optimal for string matching, and the repeated string `s2_repeated` is necessary to count the occurrences of `s1`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `KMP` algorithm, string matching, and repetition counting.
- Problem-solving patterns identified: Using a lookup table to optimize string matching.
- Optimization techniques learned: Using the `KMP` algorithm to reduce the time complexity.
- Similar problems to practice: Other string matching and repetition counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the `KMP` algorithm or the lookup table.
- Edge cases to watch for: Handling cases where `s1` is longer than `s2`, and optimizing the solution for large values of `n`.
- Performance pitfalls: Using a naive approach with a high time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.