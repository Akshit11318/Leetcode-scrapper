## Lexicographically Smallest String After Substring Operation
**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description

**Problem Statement:**
- Input format: You are given a string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 100`, `1 <= k <= 10^9`.
- Expected output format: The lexicographically smallest string after applying the given operation `k` times.
- Key requirements and edge cases to consider: The operation involves finding the lexicographically smallest substring of `s` and replacing it with the lexicographically smallest possible string by changing some characters to 'a'.
- Example test cases with explanations:
  - Input: `s = "leecode", k = 2`
  - Output: `"aeeeb"
  - Explanation: In the first operation, the lexicographically smallest substring is "lee" and it can be changed to "aee". After the first operation, the string becomes "aeeecode". In the second operation, the lexicographically smallest substring is "code" and it can be changed to "aode" or "aode" can be further changed to "aade" or "aade" can be further changed to "aaae" and so on. After the second operation, the string becomes "aeeeb".

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the lexicographically smallest string after applying the given operation `k` times, we need to apply the operation `k` times and in each operation, we need to find the lexicographically smallest substring and replace it with the lexicographically smallest possible string.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the result string.
  2. Apply the operation `k` times.
  3. In each operation, find the lexicographically smallest substring of the current string.
  4. Replace the lexicographically smallest substring with the lexicographically smallest possible string by changing some characters to 'a'.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. However, it may not be efficient for large inputs because it involves finding the lexicographically smallest substring in each operation.

```cpp
class Solution {
public:
    string lexicographicallySmallestString(string s, int k) {
        for (int i = 0; i < k; i++) {
            int minIndex = 0;
            for (int j = 1; j < s.size(); j++) {
                if (s[j] < s[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex == 0) break;
            for (int j = minIndex; j < s.size(); j++) {
                s[j] = 'a';
            }
        }
        return s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n^2)$, where $n$ is the length of the string `s`. This is because we are applying the operation `k` times and in each operation, we are finding the lexicographically smallest substring which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, because we are modifying the input string in-place.
> - **Why these complexities occur:** The time complexity occurs because we are applying the operation `k` times and in each operation, we are finding the lexicographically smallest substring. The space complexity occurs because we are modifying the input string in-place.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can find the lexicographically smallest substring in $O(n)$ time and replace it with the lexicographically smallest possible string in $O(n)$ time.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the result string.
  2. Apply the operation `k` times.
  3. In each operation, find the lexicographically smallest substring of the current string.
  4. Replace the lexicographically smallest substring with the lexicographically smallest possible string by changing some characters to 'a'.
- Proof of optimality: This approach is optimal because we are finding the lexicographically smallest substring in $O(n)$ time and replacing it with the lexicographically smallest possible string in $O(n)$ time.
- Why further optimization is impossible: Further optimization is impossible because we need to find the lexicographically smallest substring and replace it with the lexicographically smallest possible string in each operation.

```cpp
class Solution {
public:
    string lexicographicallySmallestString(string s, int k) {
        for (int i = 0; i < k; i++) {
            int minIndex = 0;
            for (int j = 1; j < s.size(); j++) {
                if (s[j] < s[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex == 0) break;
            for (int j = minIndex; j < s.size(); j++) {
                s[j] = 'a';
            }
        }
        return s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n)$, where $n$ is the length of the string `s`. This is because we are applying the operation `k` times and in each operation, we are finding the lexicographically smallest substring which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, because we are modifying the input string in-place.
> - **Optimality proof:** This approach is optimal because we are finding the lexicographically smallest substring in $O(n)$ time and replacing it with the lexicographically smallest possible string in $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concepts demonstrated in this problem are finding the lexicographically smallest substring and replacing it with the lexicographically smallest possible string.
- Problem-solving patterns identified: The problem-solving pattern identified in this problem is applying an operation repeatedly until a certain condition is met.
- Optimization techniques learned: The optimization technique learned in this problem is finding the lexicographically smallest substring in $O(n)$ time and replacing it with the lexicographically smallest possible string in $O(n)$ time.
- Similar problems to practice: Similar problems to practice are finding the lexicographically smallest substring and replacing it with the lexicographically smallest possible string.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is not checking if the lexicographically smallest substring is already the lexicographically smallest possible string.
- Edge cases to watch for: An edge case to watch for is when the input string is already the lexicographically smallest possible string.
- Performance pitfalls: A performance pitfall is not optimizing the operation of finding the lexicographically smallest substring and replacing it with the lexicographically smallest possible string.
- Testing considerations: A testing consideration is to test the function with different inputs and edge cases to ensure it is working correctly.