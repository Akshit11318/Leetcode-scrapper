## Check If Strings Can Be Made Equal With Operations I
**Problem Link:** https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description

**Problem Statement:**
- Input format and constraints: Two strings `s1` and `s2` are given. The goal is to check if `s1` can be made equal to `s2` by performing operations on `s1`.
- Expected output format: Return `true` if `s1` can be made equal to `s2`, otherwise return `false`.
- Key requirements and edge cases to consider: 
    - The only allowed operation is doubling `s1` and checking if `s2` is a substring of the doubled string.
    - Consider edge cases like empty strings, strings of different lengths, and when `s1` or `s2` is empty.
- Example test cases with explanations:
    - `s1 = "abc", s2 = "cabcab"` returns `true` because `"abcabc"` contains `"cabcab"`.
    - `s1 = "abc", s2 = "cab"` returns `false` because doubling `"abc"` does not contain `"cab"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might think to brute force all possible combinations of doubling `s1` and checking if `s2` is a substring.
- Step-by-step breakdown of the solution:
    1. Double `s1` and check if `s2` is a substring.
    2. If `s2` is found in the doubled `s1`, return `true`.
    3. If `s2` is not found, return `false`.
- Why this approach comes to mind first: It's the most straightforward way to check if `s2` can be found in a doubled version of `s1`.

```cpp
class Solution {
public:
    bool checkIfCanBreak(const string& s1, const string& s2) {
        string doubledS1 = s1 + s1;
        if (doubledS1.find(s2) != string::npos) return true;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `s1` and $m$ is the length of `s2`, because we're performing a single pass to double `s1` and then searching for `s2` in the doubled string.
> - **Space Complexity:** $O(n)$, because we're storing the doubled version of `s1`.
> - **Why these complexities occur:** The time complexity is linear because we're performing constant time operations for each character in `s1` and `s2`. The space complexity is linear because we need to store the doubled version of `s1`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We only need to check if `s2` is a substring of the doubled `s1`.
- Detailed breakdown of the approach:
    1. Double `s1`.
    2. Use a string search algorithm (like KMP or the standard library's `find` function) to check if `s2` is a substring of the doubled `s1`.
- Proof of optimality: This approach is optimal because we're only performing a constant number of operations for each character in `s1` and `s2`.
- Why further optimization is impossible: We must at least read the input strings once, so the time complexity cannot be improved beyond linear.

```cpp
class Solution {
public:
    bool checkIfCanBreak(const string& s1, const string& s2) {
        string doubledS1 = s1 + s1;
        return doubledS1.find(s2) != string::npos;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `s1` and $m$ is the length of `s2`.
> - **Space Complexity:** $O(n)$, because we're storing the doubled version of `s1`.
> - **Optimality proof:** This is the optimal solution because we're only performing a constant number of operations for each character in `s1` and `s2`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String search, doubling a string, and substring checking.
- Problem-solving patterns identified: Checking for substrings in a modified version of the original string.
- Optimization techniques learned: Using standard library functions for string operations.
- Similar problems to practice: Other string manipulation problems, such as checking for anagrams or finding the longest common substring.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases like empty strings or strings of different lengths.
- Edge cases to watch for: Empty strings, strings of different lengths, and when `s1` or `s2` is empty.
- Performance pitfalls: Using inefficient string search algorithms or not using standard library functions for string operations.
- Testing considerations: Test with a variety of input cases, including edge cases and large input strings.