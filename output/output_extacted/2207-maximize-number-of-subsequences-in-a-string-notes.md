## Maximize Number of Subsequences in a String

**Problem Link:** https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/description

**Problem Statement:**
- Input format: Given a string `text` and an array of strings `strings`.
- Constraints: `1 <= strings.length <= 100`, `1 <= strings[i].length <= 10`, and `1 <= text.length <= 1000`.
- Expected output format: The maximum number of strings that can be inserted as subsequences into `text`.
- Key requirements and edge cases to consider: A string can only be inserted into `text` if it is a subsequence of `text`.
- Example test cases with explanations:
  - If `text = "abc"` and `strings = ["a","b","c"]`, the output should be `3` because all strings can be inserted as subsequences into `text`.
  - If `text = "abc"` and `strings = ["a","ab","abc"]`, the output should be `3` because all strings can be inserted as subsequences into `text`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each string in `strings`, check if it is a subsequence of `text`. If it is, increment the count of strings that can be inserted as subsequences into `text`.
- Step-by-step breakdown of the solution:
  1. Iterate over each string in `strings`.
  2. For each string, check if it is a subsequence of `text` by using two pointers to traverse both the string and `text`.
  3. If the string is a subsequence of `text`, increment the count of strings that can be inserted as subsequences into `text`.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    int maxNumberOfSubsequences(string text, vector<string>& strings) {
        int count = 0;
        for (const auto& str : strings) {
            if (isSubsequence(text, str)) {
                count++;
            }
        }
        return count;
    }

    bool isSubsequence(const string& text, const string& str) {
        int i = 0, j = 0;
        while (i < text.size() && j < str.size()) {
            if (text[i] == str[j]) {
                j++;
            }
            i++;
        }
        return j == str.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of strings, $m$ is the maximum length of a string, and $k$ is the length of `text`. This is because for each string, we are potentially traversing the entire string and `text`.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is high because we are using a nested loop structure to check each string against `text`. The space complexity is low because we are only using a constant amount of space to store the count and indices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient algorithm to check if a string is a subsequence of `text`, such as using a single pass through `text` and maintaining a count of the current position in `text` for each string.
- Detailed breakdown of the approach:
  1. Initialize a count of strings that can be inserted as subsequences into `text`.
  2. Iterate over each string in `strings`.
  3. For each string, use a single pass through `text` to check if it is a subsequence of `text`.
  4. If the string is a subsequence of `text`, increment the count of strings that can be inserted as subsequences into `text`.
- Proof of optimality: This approach is optimal because it only requires a single pass through `text` for each string, resulting in a time complexity of $O(n \cdot k)$, where $n$ is the number of strings and $k$ is the length of `text`.

```cpp
class Solution {
public:
    int maxNumberOfSubsequences(string text, vector<string>& strings) {
        int count = 0;
        for (const auto& str : strings) {
            if (isSubsequence(text, str)) {
                count++;
            }
        }
        return count;
    }

    bool isSubsequence(const string& text, const string& str) {
        int i = 0;
        for (char c : text) {
            if (i < str.size() && c == str[i]) {
                i++;
            }
        }
        return i == str.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of strings and $k$ is the length of `text`. This is because for each string, we are potentially traversing the entire `text`.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `text` for each string, resulting in a time complexity of $O(n \cdot k)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Subsequence checking, single pass through `text`.
- Problem-solving patterns identified: Using a more efficient algorithm to check if a string is a subsequence of `text`.
- Optimization techniques learned: Reducing the number of passes through `text` for each string.
- Similar problems to practice: Subsequence problems, string matching problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty `text` or an empty string in `strings`.
- Edge cases to watch for: Empty `text`, empty string in `strings`, `text` and string in `strings` having different lengths.
- Performance pitfalls: Using a nested loop structure to check each string against `text`, resulting in a high time complexity.
- Testing considerations: Test with different lengths of `text` and strings in `strings`, test with edge cases.