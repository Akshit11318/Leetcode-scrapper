## Number of Substrings with Only 1s

**Problem Link:** https://leetcode.com/problems/number-of-substrings-with-only-1s/description

**Problem Statement:**
- Input: A binary string `s` consisting of `0`s and `1`s.
- Constraints: The length of the string `s` is in the range `[1, 10^5]`.
- Expected Output: The number of substrings in `s` that consist entirely of `1`s.
- Key Requirements:
  - A substring is a contiguous segment of characters within a string.
  - We need to count all possible substrings that contain only `1`s.
- Example Test Cases:
  - Input: `s = "0110111"`
    - Output: `9`
    - Explanation: The substrings with only `1`s are `"1"`, `"11"`, `"111"`, `"1"`, `"11"`, `"1"`, `"1"`, `"11"`, `"1"`.
  - Input: `s = "101"`
    - Output: `2`
    - Explanation: The substrings with only `1`s are `"1"`, `"1"`.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: The most straightforward way to solve this problem is to generate all possible substrings of the given string `s` and then check each substring to see if it consists entirely of `1`s.
- Step-by-Step Breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if it consists entirely of `1`s.
  3. Count the number of substrings that meet the condition.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            bool allOnes = true;
            for (char c : substr) {
                if (c != '1') {
                    allOnes = false;
                    break;
                }
            }
            if (allOnes) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because for each of the $n$ starting positions, we consider up to $n$ ending positions, and for each substring, we potentially iterate through its characters again to check for all `1`s.
> - **Space Complexity:** $O(n)$, primarily due to the creation of substrings.
> - **Why these complexities occur:** The nested loops for generating substrings and checking each character within those substrings lead to the high time complexity. The space complexity is due to the temporary storage needed for the substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of generating all substrings and checking them, we can iterate through the string and keep track of the current sequence of `1`s. Whenever we encounter a `0`, we reset the sequence. For each sequence of `1`s, we can calculate the number of substrings that can be formed from it using the formula for the sum of an arithmetic series: $1 + 2 + ... + n = \frac{n(n + 1)}{2}$, where $n$ is the length of the sequence of `1`s.
- Detailed Breakdown:
  1. Initialize a counter for the total number of substrings with only `1`s.
  2. Iterate through the string, keeping track of the current sequence length of `1`s.
  3. When a `0` is encountered, calculate the number of substrings that can be formed from the current sequence of `1`s and add it to the total count. Then, reset the sequence length.
  4. After iterating through the entire string, perform the calculation one last time for the last sequence of `1`s if it exists.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    int seqLen = 0;
    for (char c : s) {
        if (c == '1') {
            seqLen++;
        } else {
            if (seqLen > 0) {
                count += (seqLen * (seqLen + 1)) / 2;
                seqLen = 0;
            }
        }
    }
    // Handle the last sequence of '1's
    if (seqLen > 0) {
        count += (seqLen * (seqLen + 1)) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the count and the current sequence length.
> - **Optimality Proof:** This approach is optimal because it minimizes the number of operations required to count the substrings with only `1`s, doing so in linear time and constant space.

---

### Final Notes

**Learning Points:**
- The importance of avoiding unnecessary operations and data structures.
- The use of mathematical formulas to simplify counting problems.
- The value of iterating through a string and keeping track of relevant sequences or patterns.

**Mistakes to Avoid:**
- Generating all possible substrings when not necessary.
- Failing to consider mathematical shortcuts for counting problems.
- Not handling edge cases properly, such as the last sequence of `1`s in the string.