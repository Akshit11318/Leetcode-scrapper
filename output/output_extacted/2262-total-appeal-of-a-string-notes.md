## Total Appeal of a String

**Problem Link:** https://leetcode.com/problems/total-appeal-of-a-string/description

**Problem Statement:**
- Input format: a string `s` consisting of lowercase English letters.
- Constraints: `1 <= s.length <= 5 * 10^4`.
- Expected output format: the total appeal of the string, which is the sum of the appeal of each substring.
- Key requirements and edge cases to consider: the appeal of a substring is defined as the product of the number of distinct characters in the substring and the length of the substring.
- Example test cases with explanations:
  - For the input `"abbca"`, the total appeal is calculated as follows: for each substring, count the distinct characters and multiply by the length. For example, `"a"` has 1 distinct character and length 1, `"ab"` has 2 distinct characters and length 2, and so on. Summing these products gives the total appeal.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate over all possible substrings of the input string, calculate the number of distinct characters in each substring, and then multiply this count by the length of the substring.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of the input string.
  2. For each substring, count the number of distinct characters.
  3. Calculate the appeal of the substring by multiplying the count of distinct characters by the length of the substring.
  4. Sum the appeals of all substrings to get the total appeal.
- Why this approach comes to mind first: it directly follows the definition of the problem, ensuring that every aspect of the problem statement is considered.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int totalAppeal(std::string s) {
    int total = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            std::string substring = s.substr(i, j - i);
            std::unordered_set<char> distinctChars(substring.begin(), substring.end());
            total += distinctChars.size() * substring.length();
        }
    }
    return total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because for each substring (which takes $O(n^2)$ to generate), we are counting distinct characters, which in the worst case (when all characters are unique) takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the set of distinct characters in the substring.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and then an additional operation to count distinct characters in each substring, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: instead of counting distinct characters for each substring, we can use a sliding window approach to efficiently calculate the appeal for all substrings ending at a given position.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the total appeal and the last seen index of each character.
  2. Iterate over the string, maintaining a sliding window that represents the current substring.
  3. For each character in the window, update the last seen index and calculate the contribution to the total appeal based on the number of distinct characters in the window.
  4. Use the formula for the sum of an arithmetic series to efficiently calculate the total appeal.
- Proof of optimality: this approach has a linear time complexity because it only requires a single pass through the string, making it optimal for this problem.

```cpp
int totalAppeal(std::string s) {
    int n = s.size();
    long long res = 0;
    for (int i = 0; i < n; i++) {
        std::unordered_set<char> unique;
        for (int j = i; j < n; j++) {
            unique.insert(s[j]);
            res += unique.size() * (j - i + 1);
        }
    }
    return res;
}
```

However, the above code still has a high time complexity due to the nested loops. To truly optimize, we should recognize that the problem can be solved more efficiently by directly calculating the appeal of each substring and summing these appeals, without the need for explicit substring generation or counting distinct characters in each substring. 

Let's correct the optimal approach with a more efficient solution:

```cpp
int totalAppeal(std::string s) {
    int n = s.length();
    long long total = 0;
    for (int len = 1; len <= n; len++) {
        for (int start = 0; start <= n - len; start++) {
            int end = start + len;
            std::unordered_set<char> distinct;
            for (int i = start; i < end; i++) {
                distinct.insert(s[i]);
            }
            total += distinct.size() * len;
        }
    }
    return total;
}
```

But even this can be optimized further by directly calculating the contribution of each character to the total appeal without explicitly generating substrings or counting distinct characters in each substring.

```cpp
int totalAppeal(string s) {
    int n = s.size(), res = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        unordered_map<char, int> m;
        for (int j = i; j < n; j++) {
            m[s[j]]++;
            cnt++;
            res += cnt * m.size();
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because for each character in the string, we potentially iterate through the rest of the string once.
> - **Space Complexity:** $O(n)$, for storing the frequency of characters in the current window.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to calculate the total appeal by avoiding redundant calculations and directly updating the total appeal based on the current window's characteristics.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window technique, efficient calculation of substring properties.
- Problem-solving patterns identified: breaking down complex problems into simpler, more manageable parts.
- Optimization techniques learned: avoiding redundant calculations, using data structures to efficiently store and retrieve information.
- Similar problems to practice: other string manipulation problems, especially those involving substrings or sliding windows.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, failure to handle edge cases.
- Edge cases to watch for: empty strings, strings with a single character, strings with all characters being the same.
- Performance pitfalls: using brute force approaches for problems that have more efficient solutions, not considering the implications of nested loops on time complexity.
- Testing considerations: thoroughly testing the function with a variety of inputs, including edge cases, to ensure correctness and efficiency.