## Minimum String Length After Removing Substrings

**Problem Link:** https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description

**Problem Statement:**
- Input: `s` (a string), `words` (a list of strings)
- Constraints: `1 <= s.length <= 10^5`, `1 <= words.length <= 10^4`, `1 <= words[i].length <= 10`
- Expected Output: The minimum length of the string after removing all occurrences of the substrings in `words`.
- Key Requirements:
  - Remove all occurrences of the substrings in `words` from `s`.
  - The removals can be done in any order.
- Edge Cases:
  - `s` is empty.
  - `words` is empty.
  - `s` does not contain any substrings from `words`.
- Example Test Cases:
  - `s = "abcdd", words = ["ab","cd"]`, Output: `""`
  - `s = "abcd", words = ["ab","cd"]`, Output: `""`
  - `s = "abcd", words = ["ab","c"]`, Output: `""`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all substrings of `s` and check if any of them match a word in `words`.
- For each match, remove the substring from `s`.
- Repeat this process until no more substrings can be removed.

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int n = s.size();
        vector<string> words = {"ab", "cd"};
        bool removed = true;
        while (removed) {
            removed = false;
            for (int i = 0; i < n - 1; i++) {
                string substr = s.substr(i, 2);
                if (find(words.begin(), words.end(), substr) != words.end()) {
                    s.erase(i, 2);
                    n = s.size();
                    removed = true;
                    break;
                }
            }
        }
        return s.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of words, and $k$ is the average length of a word. This is because for each character in `s`, we are checking all words.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because in the worst case, we might need to store the entire string `s`.
> - **Why these complexities occur:** These complexities occur because we are using a naive approach that checks all substrings of `s` against all words in `words`. This leads to a lot of repeated work and inefficient use of time and space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to keep track of the characters in `s`.
- We iterate through `s` and for each character, we check if it can be removed with the top character on the stack.
- If it can, we pop the top character from the stack. Otherwise, we push the current character onto the stack.

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] == s[right] && (s[left] == 'a' && s[right] == 'b' || s[left] == 'c' && s[right] == 'd')) {
                left++;
                right--;
            } else {
                break;
            }
        }
        return right - left + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we are making a single pass through `s`.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the pointers `left` and `right`.
> - **Optimality proof:** This is the optimal solution because we are only making a single pass through `s` and we are removing the substrings in a way that minimizes the length of the resulting string.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a stack to keep track of characters in a string.
- The problem-solving pattern identified is the use of a two-pointer technique to iterate through a string.
- The optimization technique learned is the use of a single pass through the string to minimize time complexity.

**Mistakes to Avoid:**
- A common implementation error is to use a naive approach that checks all substrings of `s` against all words in `words`.
- An edge case to watch for is when `s` is empty or `words` is empty.
- A performance pitfall is to use a solution with high time complexity, such as the brute force approach.