## Number of Equal Count Substrings
**Problem Link:** https://leetcode.com/problems/number-of-equal-count-substrings/description

**Problem Statement:**
- Input: a string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= k <= 10^5`, `s` consists of lowercase English letters.
- Expected Output: the number of substrings where the count of each character is equal to `k`.
- Key Requirements: consider all substrings of `s`, count the occurrences of each character in each substring, and compare these counts to `k`.
- Example Test Cases:
  - Input: `s = "aaabc", k = 3`, Output: `3` (Substrings "aaa", "aaab", and "aaabc" have characters with counts equal to `k`).
  - Input: `s = "abcd", k = 2`, Output: `0` (No substring has characters with counts equal to `k`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s`.
- For each substring, count the occurrences of each character and compare these counts to `k`.
- If all characters in a substring have a count equal to `k`, increment the result.

```cpp
int numberOfSubstrings(string s, int k) {
    int n = s.length(), res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            unordered_map<char, int> count;
            bool valid = true;
            for (int p = i; p < j; p++) {
                count[s[p]]++;
                if (count[s[p]] > k) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;
            for (auto& pair : count) {
                if (pair.second != k) {
                    valid = false;
                    break;
                }
            }
            if (valid) res++;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each substring (generated in $O(n^2)$ time), we potentially iterate over its characters again to count them.
> - **Space Complexity:** $O(n)$, for storing the character counts in the `unordered_map`.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate all substrings and then additional work to count characters within these substrings, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- To optimize, we recognize that a substring can only have characters with counts equal to `k` if its length is a multiple of `k`.
- We iterate over all possible substring lengths that are multiples of `k` and use a sliding window approach to efficiently count character occurrences.
- For each valid length, we maintain a window of that length and slide it over the string, updating character counts as we move.

```cpp
int numberOfSubstrings(string s, int k) {
    int n = s.length(), res = 0;
    for (int len = k; len <= n; len += k) {
        unordered_map<char, int> count;
        for (int i = 0; i < len; i++) {
            count[s[i]]++;
        }
        if (all_of(count.begin(), count.end(), [k](auto& pair){ return pair.second == k; })) {
            res++;
        }
        for (int i = len; i < n; i++) {
            count[s[i - len]]--;
            if (count[s[i - len]] == 0) count.erase(s[i - len]);
            count[s[i]]++;
            if (all_of(count.begin(), count.end(), [k](auto& pair){ return pair.second == k; })) {
                res++;
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \frac{n}{k})$, simplifying to $O(\frac{n^2}{k})$. This is because we have an outer loop that runs up to $n$ (with a step of $k$), and for each iteration, we potentially slide a window of size up to $n$.
> - **Space Complexity:** $O(n)$, for storing character counts in the `unordered_map`.
> - **Optimality proof:** This approach is more efficient than the brute force because it only considers substrings of lengths that are multiples of `k`, reducing the number of substrings to consider. It also uses a sliding window to efficiently update character counts, avoiding redundant work.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns and constraints in the input (e.g., substring length being a multiple of `k`).
- Using a sliding window approach to efficiently update counts or sums over substrings.
- Optimizing by reducing the number of iterations or operations within loops.

**Mistakes to Avoid:**
- Failing to consider the constraints of the problem (e.g., not realizing that only substrings with lengths that are multiples of `k` can satisfy the condition).
- Not optimizing the iteration over substrings and character counts.
- Incorrectly implementing the sliding window approach or character count updates.