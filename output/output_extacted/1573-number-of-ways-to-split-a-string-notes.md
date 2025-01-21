## Number of Ways to Split a String
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-split-a-string/description

**Problem Statement:**
- Input format and constraints: The input string `s` consists of `0`s and `1`s only. The length of `s` is between `1` and `10^5`. 
- Expected output format: The number of ways to split the string into three non-empty substrings such that each substring contains an even number of `1`s.
- Key requirements and edge cases to consider: Handle cases where the input string is too short to be split into three substrings, and consider the parity of `1`s in each substring.
- Example test cases with explanations:
  - For `s = "10101"`, the output should be `4` because the valid splits are `"10|10|1"`, `"10|1|01"`, `"101|0|1"`, and `"1|010|1"`.
  - For `s = "1001"`, the output should be `0` because there are no valid splits.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible splits of the string into three substrings and count those where each substring has an even number of `1`s.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible split positions for the first and second substrings.
  2. For each split, calculate the number of `1`s in each substring.
  3. If all substrings have an even number of `1`s, increment the count of valid splits.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all possible ways to split the string and checking each for the required condition.

```cpp
int numWays(string s) {
    int n = s.size();
    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            string a = s.substr(0, i);
            string b = s.substr(i, j - i);
            string c = s.substr(j);
            if (countBits(a) % 2 == 0 && countBits(b) % 2 == 0 && countBits(c) % 2 == 0) {
                count++;
            }
        }
    }
    return count;
}

int countBits(string s) {
    int count = 0;
    for (char c : s) {
        if (c == '1') count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the length of the string and $m$ is the maximum length of a substring. This is because for each of the $O(n^2)$ possible splits, we count the bits in each of the three substrings, which takes $O(m)$ time.
> - **Space Complexity:** $O(m)$ for storing the substrings.
> - **Why these complexities occur:** The brute force approach checks all possible splits and counts the bits in each substring for every split, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible split, we can use the fact that a string has an even number of `1`s if the difference between the total count of `1`s and the count of `1`s up to a certain point is even. We can calculate the prefix sum of `1`s and then find the number of ways to split the string based on this sum.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of `1`s in the string.
  2. Iterate over the string to find all positions where the prefix sum is even, which are potential split points.
  3. For each potential split point, check if there's another split point later that would result in the third substring also having an even number of `1`s.
- Proof of optimality: This approach is optimal because it avoids unnecessary checks by only considering positions where the prefix sum is even, thus reducing the number of iterations significantly.

```cpp
int numWays(string s) {
    int n = s.size();
    int ones = 0;
    for (char c : s) if (c == '1') ones++;
    if (ones % 2 == 1) return 0; // If total ones is odd, no valid splits
    ones /= 2; // Target number of ones for each half
    int count = 0;
    int prefixOnes = 0;
    for (int i = 0; i < n - 2; i++) {
        if (s[i] == '1') prefixOnes++;
        if (prefixOnes == ones) {
            int suffixOnes = 0;
            for (int j = n - 1; j > i + 1; j--) {
                if (s[j] == '1') suffixOnes++;
                if (suffixOnes == ones) {
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we make two passes over the string: one to calculate the prefix sum and another to find the split points.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it only checks positions where the prefix sum is even, reducing the number of iterations to linear time, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sums, optimization by reducing unnecessary checks.
- Problem-solving patterns identified: Using prefix sums to efficiently calculate properties of substrings.
- Optimization techniques learned: Avoiding unnecessary iterations by only considering relevant positions.
- Similar problems to practice: Other string manipulation and optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating prefix sums or misinterpreting the conditions for valid splits.
- Edge cases to watch for: Handling strings with odd total counts of `1`s, ensuring that substrings are non-empty.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large strings.