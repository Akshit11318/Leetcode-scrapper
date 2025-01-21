## Rearrange K Substrings to Form Target String

**Problem Link:** https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/description

**Problem Statement:**
- Input format: Given a string `s` and an integer `k`.
- Constraints: `1 <= k <= 27`, `1 <= s.length <= 10^5`.
- Expected output format: Return `true` if it is possible to rearrange `s` into `k` substrings such that each substring is the same, and `false` otherwise.
- Key requirements and edge cases to consider: 
  - Handling cases where `k` is a divisor of the length of `s`.
  - Checking if all characters in `s` can be evenly distributed into `k` substrings.
- Example test cases with explanations: 
  - Input: `s = "abcabc", k = 2`, Output: `true`. Explanation: We can rearrange `s` into two substrings: `"abc"` and `"abc"`.
  - Input: `s = "ab", k = 1`, Output: `true`. Explanation: We can rearrange `s` into one substring: `"ab"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of rearranging `s` into `k` substrings and check if each combination results in the same substring repeated `k` times.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of rearranging `s` into `k` substrings.
  2. For each combination, check if all substrings are the same.
  3. If a combination is found where all substrings are the same, return `true`.
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations and check if any of them satisfy the condition.

```cpp
class Solution {
public:
    bool canDivideString(string s, int k) {
        int n = s.length();
        if (n % k != 0) return false;
        string sub = "";
        for (int i = 0; i < n; i++) {
            sub += s[i];
            if (sub.length() == n / k) {
                string temp = sub;
                for (int j = 0; j < k - 1; j++) {
                    sub += temp;
                }
                if (sub == s) return true;
                sub = "";
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \frac{n}{k} \cdot k)$, where $n$ is the length of `s`. This simplifies to $O(nk)$.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible combinations of rearranging `s` into `k` substrings and checking if each combination results in the same substring repeated `k` times. The space complexity occurs because we need to store the substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations, we can check if the length of `s` is divisible by `k` and if all characters in `s` can be evenly distributed into `k` substrings.
- Detailed breakdown of the approach:
  1. Check if the length of `s` is divisible by `k`.
  2. If it is, count the frequency of each character in `s`.
  3. For each character, check if its frequency is divisible by `k`.
  4. If all frequencies are divisible by `k`, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string `s` to count the frequency of each character, resulting in a time complexity of $O(n)$.

```cpp
class Solution {
public:
    bool canDivideString(string s, int k) {
        int n = s.length();
        if (n % k != 0) return false;
        unordered_map<char, int> count;
        for (char c : s) {
            count[c]++;
        }
        for (auto& pair : count) {
            if (pair.second % k != 0) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string `s` to count the frequency of each character, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - **Hashing**: Using an unordered map to count the frequency of each character in `s`.
  - **Divisibility**: Checking if the length of `s` is divisible by `k` and if all frequencies are divisible by `k`.
- Problem-solving patterns identified: 
  - **Frequency counting**: Counting the frequency of each character in `s` to check if all frequencies are divisible by `k`.
- Optimization techniques learned: 
  - **Single pass**: Only requiring a single pass through the string `s` to count the frequency of each character, resulting in a time complexity of $O(n)$.
- Similar problems to practice: 
  - **Rearrange Array Elements by Sign**: Rearranging an array of integers to group all positive numbers first, followed by all negative numbers.
  - **Group Anagrams**: Grouping a list of strings into anagrams.

**Mistakes to Avoid:**
- Common implementation errors: 
  - **Not checking for divisibility**: Not checking if the length of `s` is divisible by `k` before counting the frequency of each character.
  - **Not handling edge cases**: Not handling edge cases where `k` is 1 or where `s` is empty.
- Edge cases to watch for: 
  - **Empty string**: Handling the case where `s` is empty.
  - **k is 1**: Handling the case where `k` is 1.
- Performance pitfalls: 
  - **Using inefficient data structures**: Using inefficient data structures such as arrays instead of unordered maps to count the frequency of each character.
- Testing considerations: 
  - **Test for divisibility**: Testing if the length of `s` is divisible by `k`.
  - **Test for frequency**: Testing if all frequencies are divisible by `k`.