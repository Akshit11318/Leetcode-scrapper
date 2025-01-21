## Minimum Length of Anagram Concatenation

**Problem Link:** https://leetcode.com/problems/minimum-length-of-anagram-concatenation/description

**Problem Statement:**
- Input format: Two strings `s1` and `s2`.
- Constraints: Both strings consist of lowercase English letters.
- Expected output format: The minimum length of the concatenated string such that `s1` and `s2` are anagrams of each other.
- Key requirements: Find the minimum length by appending characters to `s1` and/or `s2`.
- Edge cases: If `s1` and `s2` cannot be anagrams of each other, return -1.

Example test cases:
- `s1 = "abc", s2 = "bca"`: Output is 3.
- `s1 = "abc", s2 = "bcb"`: Output is 4.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of appending characters to `s1` and/or `s2`.
- Step-by-step breakdown:
  1. Generate all permutations of `s1` and `s2`.
  2. For each permutation, check if it is an anagram of the other string.
  3. If an anagram is found, calculate the length of the concatenated string.
  4. Keep track of the minimum length found.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isAnagram(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
}

int minLength(string s1, string s2) {
    int minLen = INT_MAX;
    for (int i = 0; i < (1 << s1.size()); i++) {
        string s1Temp = s1;
        for (int j = 0; j < s1.size(); j++) {
            if (i & (1 << j)) {
                s1Temp.erase(j, 1);
                j--;
            }
        }
        for (int j = 0; j < (1 << s2.size()); j++) {
            string s2Temp = s2;
            for (int k = 0; k < s2.size(); k++) {
                if (j & (1 << k)) {
                    s2Temp.erase(k, 1);
                    k--;
                }
            }
            if (isAnagram(s1Temp, s2Temp)) {
                minLen = min(minLen, (int)s1Temp.size() + (int)s2Temp.size());
            }
        }
    }
    return minLen == INT_MAX ? -1 : minLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n+m} \cdot n \cdot m \cdot log(n+m))$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively. This is due to generating all permutations and sorting the strings.
> - **Space Complexity:** $O(n+m)$, for storing the temporary strings.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input strings, which leads to an exponential time complexity. The sorting operation within the `isAnagram` function adds a logarithmic factor.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the concept of **frequency counting** to determine the minimum length of the concatenated string.
- Step-by-step breakdown:
  1. Count the frequency of each character in `s1` and `s2`.
  2. Calculate the difference in frequency counts between `s1` and `s2`.
  3. The minimum length is the sum of the lengths of `s1` and `s2` minus twice the number of common characters.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int minLength(string s1, string s2) {
    unordered_map<char, int> count1, count2;
    for (char c : s1) count1[c]++;
    for (char c : s2) count2[c]++;
    
    int common = 0;
    for (auto& pair : count1) {
        if (count2.find(pair.first) != count2.end()) {
            common += min(pair.second, count2[pair.first]);
        }
    }
    
    return s1.size() + s2.size() - 2 * common;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n+m)$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively. This is due to counting the frequency of characters in both strings.
> - **Space Complexity:** $O(n+m)$, for storing the frequency counts.
> - **Optimality proof:** The optimal approach has a linear time complexity, which is the best possible complexity for this problem. This is because we must at least read the input strings once.

---

### Final Notes

**Learning Points:**
- The importance of **frequency counting** in solving string problems.
- How to use **unordered maps** to efficiently count character frequencies.
- The concept of **optimality** in algorithm design.

**Mistakes to Avoid:**
- Using brute force approaches for problems with large input sizes.
- Not considering the **trade-offs** between time and space complexity.
- Failing to **validate** the input data before processing it.