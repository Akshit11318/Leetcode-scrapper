## Count the Number of Substrings with Dominant Ones

**Problem Link:** https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` as input, where `s` only consists of `0`s and `1`s. The length of `s` is between 1 and 10^5.
- Expected output format: The problem asks to return the number of substrings where the number of `1`s is greater than the number of `0`s.
- Key requirements and edge cases to consider: The input string can be empty, or it can contain only `0`s or only `1`s. The substrings can be of any length from 1 to the length of the string.
- Example test cases with explanations:
  - For the input `"001"` the output is 2 because there are two substrings ("01", "1") where the number of `1`s is greater than or equal to the number of `0`s but in this problem we only count when `1`s are strictly greater than `0`s.
  - For the input `"1100"` the output is 3 because there are three substrings ("11", "110", "1") where the number of `1`s is greater than the number of `0`s.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to generate all possible substrings of the input string, count the number of `1`s and `0`s in each substring, and then check if the number of `1`s is greater than the number of `0`s.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string.
  2. For each substring, count the number of `1`s and `0`s.
  3. If the number of `1`s is greater than the number of `0`s, increment a counter.
- Why this approach comes to mind first: It is the most intuitive way to solve the problem because it directly addresses the problem statement by checking every possible substring.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                string substr = s.substr(i, j - i);
                int ones = 0, zeros = 0;
                for (char c : substr) {
                    if (c == '1') ones++;
                    else zeros++;
                }
                if (ones > zeros) count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string. This is because we are generating all substrings ($O(n^2)$) and then for each substring, we are counting the number of `1`s and `0`s ($O(n)$).
> - **Space Complexity:** $O(n)$ because in the worst case, the length of the substring can be equal to the length of the input string.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that checks every possible substring and then counts the `1`s and `0`s in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting the number of `1`s and `0`s for each substring, we can use a sliding window approach to keep track of the count of `1`s and `0`s as we expand or shrink the window.
- Detailed breakdown of the approach:
  1. Initialize a counter for the number of substrings with dominant `1`s.
  2. Use two nested loops to represent the start and end of the sliding window.
  3. For each window, count the number of `1`s and `0`s.
  4. If the number of `1`s is greater than the number of `0`s, increment the counter.
- Why further optimization is impossible: This approach is optimal because it still needs to check every possible substring but does so in a more efficient manner by not recalculating the counts of `1`s and `0`s for overlapping substrings.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                int ones = 0, zeros = 0;
                for (int k = i; k < j; k++) {
                    if (s[k] == '1') ones++;
                    else zeros++;
                }
                if (ones > zeros) count++;
            }
        }
        return count;
    }
};
```

However, a more efficient solution can be achieved by observing that for a substring to have more `1`s than `0`s, the difference between the counts of `1`s and `0`s must be positive.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            int c1 = 0, c2 = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '1') c1++;
                else c2++;
                if (c1 > c2) res++;
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string. This is because we are using two nested loops to generate all substrings.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the counts and the result.
> - **Optimality proof:** This is the optimal solution because we must check every possible substring to count those with dominant `1`s, and we do so in a single pass through the string for each starting position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, counting, and substring generation.
- Problem-solving patterns identified: The need to consider all possible substrings and the importance of efficient counting.
- Optimization techniques learned: Avoiding redundant calculations by using a sliding window approach.
- Similar problems to practice: Other problems involving substring generation and counting, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly counting the number of `1`s and `0`s in substrings or failing to consider all possible substrings.
- Edge cases to watch for: Empty strings, strings with only `0`s or only `1`s, and substrings of length 1.
- Performance pitfalls: Using inefficient algorithms that result in high time complexity, such as the initial brute force approach.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure correctness and efficiency.