## Rearrange Characters to Make Target String
**Problem Link:** https://leetcode.com/problems/rearrange-characters-to-make-target-string/description

**Problem Statement:**
- Input: Two strings `str` and `target`.
- Constraints: `1 <= str.length <= 100`, `1 <= target.length <= 100`, `str` and `target` consist of lowercase English letters.
- Expected Output: Return `true` if it is possible to rearrange the characters in `str` to spell `target`, and `false` otherwise.
- Key Requirements: Determine if the characters in `str` can be rearranged to form `target`.
- Example Test Cases:
  - `str = "abc", target = "bca"`: Returns `true` because the characters in `str` can be rearranged to spell `target`.
  - `str = "abc", target = "bcb"`: Returns `false` because the characters in `str` cannot be rearranged to spell `target`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all permutations of `str` and check if `target` is among them.
- This approach is straightforward but inefficient due to the large number of permutations for even moderately sized strings.

```cpp
#include <algorithm>
#include <string>

bool canRearrange(const std::string& str, const std::string& target) {
    std::string temp = str;
    do {
        if (temp == target) return true;
    } while (std::next_permutation(temp.begin(), temp.end()));
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of `str`, because there are $n!$ permutations of `str`.
> - **Space Complexity:** $O(n)$, as we need to store the current permutation of `str`.
> - **Why these complexities occur:** The time complexity is due to generating all permutations, and the space complexity is due to storing the current permutation.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to compare the frequency of each character in `str` and `target`.
- If the frequency of any character in `target` exceeds its frequency in `str`, it's impossible to rearrange `str` to spell `target`.
- This approach is optimal because it directly addresses the requirement without unnecessary computations.

```cpp
#include <string>
#include <unordered_map>

bool canRearrange(const std::string& str, const std::string& target) {
    if (str.length() < target.length()) return false;
    
    std::unordered_map<char, int> strCount;
    std::unordered_map<char, int> targetCount;
    
    for (char c : str) strCount[c]++;
    for (char c : target) targetCount[c]++;
    
    for (const auto& pair : targetCount) {
        if (strCount[pair.first] < pair.second) return false;
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `str` and `target`, respectively, because we iterate through each string once.
> - **Space Complexity:** $O(n + m)$, as in the worst case, all characters in `str` and `target` are unique.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input strings once to determine if `str` can be rearranged to spell `target`.

---

### Final Notes
**Learning Points:**
- The importance of understanding the problem constraints and requirements.
- How to approach problems by first considering brute force solutions and then optimizing.
- The use of frequency counting to solve string rearrangement problems.

**Mistakes to Avoid:**
- Not considering the constraints of the problem, leading to inefficient solutions.
- Failing to validate the input or handle edge cases.
- Not optimizing the solution when possible, leading to performance issues.