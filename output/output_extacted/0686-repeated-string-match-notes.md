## Repeated String Match

**Problem Link:** [https://leetcode.com/problems/repeated-string-match/description](https://leetcode.com/problems/repeated-string-match/description)

**Problem Statement:**
- Given two strings `a` and `b`, return the smallest number of times `a` must be repeated to include `b` as a substring. If `b` cannot be a substring of any repetition of `a`, return `-1`.
- Input format: Two strings `a` and `b`.
- Constraints: `1 <= a.length <= 1000`, `1 <= b.length <= 1000`.
- Expected output format: An integer representing the smallest number of repetitions or `-1` if `b` cannot be a substring of any repetition of `a`.
- Key requirements and edge cases to consider: Handling cases where `b` is not a substring of any repetition of `a`, and finding the minimum number of repetitions when `b` is a substring.

Example test cases:
- Input: `a = "abcd", b = "cdabcdab"` Output: `3`
- Input: `a = "a", b = "aa"` Output: `2`
- Input: `a = "a", b = "a"` Output: `1`
- Input: `a = "abc", b = "wxyz"` Output: `-1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible repetition of string `a` to see if it contains string `b` as a substring.
- We start with repeating `a` once and check if `b` is a substring. If not, we repeat `a` again and check, and so on, until `b` is found as a substring or we have repeated `a` more times than the length of `b`.
- This approach is straightforward but inefficient for large inputs because it involves a lot of string concatenation and substring searching.

```cpp
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        int count = 1;
        string repeated = a;
        while (repeated.length() < b.length() * 2) {
            if (repeated.find(b) != string::npos) {
                return count;
            }
            repeated += a;
            count++;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of `a` and $m$ is the length of `b`. This is because in the worst case, we might have to repeat `a` up to `m` times and then search for `b` in the repeated string, which takes $O(n \cdot m)$ time.
> - **Space Complexity:** $O(n \cdot m)$ as we are creating a new string that can be up to `m` times larger than `a`.
> - **Why these complexities occur:** The time and space complexities are high because we are using string concatenation in a loop and then searching for a substring, both of which are expensive operations.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that if `b` is a substring of any repetition of `a`, it must be a substring of a repetition that is at most twice the length of `b`. This is because if `b` were longer than two repetitions of `a`, it would have to contain at least one full repetition of `a` (since `a` is at least as long as half of `b`), and thus could be found in a shorter repetition.
- We only need to check repetitions of `a` up to twice the length of `b`, making the algorithm much more efficient.

```cpp
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        string repeated = a;
        for (int i = 1; i <= b.length() / a.length() + 3; i++) {
            if (repeated.find(b) != string::npos) {
                return i;
            }
            repeated += a;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ where $m$ is the length of `b`, because we only need to repeat `a` up to a constant number of times relative to `b` and then perform a substring search.
> - **Space Complexity:** $O(m)$ as we are creating a new string that can be up to twice the length of `b`.
> - **Optimality proof:** This is optimal because we must at least read `b` once to determine if it's a substring of any repetition of `a`, and our algorithm does this in linear time relative to the size of the input `b`.

---

### Final Notes

**Learning Points:**
- Understanding the properties of string repetition and substring searching.
- Identifying the key insight that allows for a significant reduction in the number of repetitions to check.
- Applying this insight to improve the efficiency of the algorithm.

**Mistakes to Avoid:**
- Not recognizing the limit on the number of repetitions needed to find `b` as a substring.
- Failing to consider the trade-offs between different approaches, especially in terms of time and space complexity.
- Not optimizing the algorithm based on the specific constraints of the problem.