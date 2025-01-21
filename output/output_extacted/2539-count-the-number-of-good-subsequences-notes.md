## Count the Number of Good Subsequences
**Problem Link:** https://leetcode.com/problems/count-the-number-of-good-subsequences/description

**Problem Statement:**
- Input format and constraints: Given a string `binaryString` consisting only of characters `0` and `1`, find the number of good subsequences. A subsequence is considered good if it contains at least one `0` and at least one `1`.
- Expected output format: The total count of good subsequences.
- Key requirements and edge cases to consider: Handling strings with all `0`s or all `1`s, empty strings, and strings with varying lengths.
- Example test cases with explanations:
  - For the string `"001"`, there are `6` good subsequences: `"01"`, `"001"`, `"01"`, `"01"`, `"01"`, and `"01"`.
  - For the string `"110"`, there are `6` good subsequences: `"11"`, `"10"`, `"11"`, `"11"`, `"10"`, and `"11"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the given string and then filter out those that contain at least one `0` and one `1`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input string.
  2. For each subsequence, check if it contains at least one `0` and one `1`.
  3. If it does, increment the count of good subsequences.
- Why this approach comes to mind first: It's straightforward and ensures all possible subsequences are considered.

```cpp
int countGoodSubsequences(string binaryString) {
    int n = binaryString.length();
    int count = 0;
    for (int mask = 1; mask < (1 << n); ++mask) {
        string subsequence = "";
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                subsequence += binaryString[i];
            }
        }
        bool hasZero = false, hasOne = false;
        for (char c : subsequence) {
            if (c == '0') hasZero = true;
            if (c == '1') hasOne = true;
        }
        if (hasZero && hasOne) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate $2^n$ subsequences and for each, we potentially scan its length.
> - **Space Complexity:** $O(n)$, for storing the subsequence.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible subsequences, and the linear space complexity is for storing the current subsequence being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that a good subsequence must have at least one `0` and one `1`. Thus, instead of generating all subsequences, we can use dynamic programming to count the number of subsequences ending at each position that contain at least one `0` and one `1`.
- Detailed breakdown of the approach:
  1. Initialize arrays to keep track of the number of subsequences ending at each position that contain at least one `0` and one `1`.
  2. Iterate through the string, updating these counts based on whether the current character is `0` or `1`.
- Proof of optimality: This approach avoids generating unnecessary subsequences and directly counts the good ones, reducing time complexity significantly.

```cpp
int countGoodSubsequences(string binaryString) {
    int n = binaryString.length();
    long long count0 = 0, count1 = 0, count01 = 0;
    for (char c : binaryString) {
        if (c == '0') {
            count0 = count0 * 2 + 1;
        } else {
            count1 = count1 * 2 + 1;
        }
        if (c == '0') {
            count01 = count01 * 2 + count1;
        } else {
            count01 = count01 * 2 + count0;
        }
    }
    return count01;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, as we make a single pass through the string.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store our counts.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of good subsequences without generating all possible subsequences, thus minimizing the time complexity to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for counting subsequences efficiently.
- Problem-solving patterns identified: Recognizing the need to avoid brute force enumeration and instead use combinatorial or dynamic programming techniques.
- Optimization techniques learned: Using arrays to keep track of counts and updating them iteratively to avoid redundant calculations.
- Similar problems to practice: Other subsequence counting problems, such as those involving specific patterns or constraints.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing or updating dynamic programming arrays.
- Edge cases to watch for: Handling empty strings or strings with all `0`s or all `1`s.
- Performance pitfalls: Failing to recognize the exponential time complexity of brute force approaches for subsequence problems.
- Testing considerations: Ensuring to test with a variety of input lengths and patterns to catch any implementation errors.