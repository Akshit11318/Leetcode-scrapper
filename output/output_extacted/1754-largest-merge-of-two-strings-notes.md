## Largest Merge of Two Strings
**Problem Link:** https://leetcode.com/problems/largest-merge-of-two-strings/description

**Problem Statement:**
- Input: Two strings `word1` and `word2`.
- Constraints: `1 <= word1.length, word2.length <= 1000`, `word1` and `word2` consist of lowercase letters.
- Expected Output: The largest possible merged string.
- Key Requirements: The merged string should be the lexicographically largest possible string.
- Edge Cases: If one string is empty, the other string is the merged string.

**Example Test Cases:**
- `word1 = "abc"`, `word2 = "def"`, Output: `"abcdef"`
- `word1 = "abcd"`, `word2 = "efgh"`, Output: `"abcdefgh"`
- `word1 = "a"`, `word2 = "b"`, Output: `"ab"`

---

### Brute Force Approach
**Explanation:**
- Generate all possible permutations of `word1` and `word2`.
- Compare each permutation to find the lexicographically largest one.
- This approach is intuitive but inefficient due to the large number of permutations.

```cpp
#include <string>
#include <algorithm>
using namespace std;

string largestMerge(string word1, string word2) {
    string merged = word1 + word2;
    sort(merged.begin(), merged.end());
    reverse(merged.begin(), merged.end());
    return merged;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the total length of `word1` and `word2`, due to the sorting operation.
> - **Space Complexity:** $O(n)$ for the merged string.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the merged string's size determines the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Compare characters from `word1` and `word2` one by one.
- Choose the character that results in the lexicographically largest merged string.
- If one string is exhausted, append the remaining characters from the other string.
- This approach ensures the merged string is lexicographically largest without generating all permutations.

```cpp
#include <string>
using namespace std;

string largestMerge(string word1, string word2) {
    string result;
    while (!word1.empty() && !word2.empty()) {
        if (word1 > word2) {
            result += word1[0];
            word1.erase(0, 1);
        } else {
            result += word2[0];
            word2.erase(0, 1);
        }
    }
    result += word1;
    result += word2;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the total length of `word1` and `word2`, since we iterate through each character once.
> - **Space Complexity:** $O(n)$ for the merged string.
> - **Optimality proof:** This approach is optimal because it ensures the merged string is lexicographically largest by comparing characters one by one and choosing the larger one, without generating all permutations.

---

### Final Notes
**Learning Points:**
- Key algorithmic concept: **greedy algorithm**, where we make the locally optimal choice at each step to ensure the globally optimal solution.
- Problem-solving pattern: **string manipulation** and **comparison**.
- Optimization technique: **avoiding unnecessary computations** by comparing characters one by one instead of generating all permutations.

**Mistakes to Avoid:**
- Common implementation error: **not handling edge cases** where one string is empty.
- Performance pitfall: **using inefficient sorting algorithms**.
- Testing consideration: **testing with different input sizes** to ensure the solution scales well.