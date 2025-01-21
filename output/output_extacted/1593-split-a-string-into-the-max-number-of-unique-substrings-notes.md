## Split a String into the Max Number of Unique Substrings
**Problem Link:** https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description

**Problem Statement:**
- Input: A string `s`.
- Output: The maximum number of unique substrings that can be obtained from `s`.
- Key Requirements: 
    - Split `s` into substrings.
    - Each substring must be unique.
- Edge Cases: 
    - Empty string.
    - Single character string.
    - String with duplicate characters.

**Example Test Cases:**
- Input: `s = "ababccc"`
  Output: `5`
  Explanation: `["a", "b", "ab", "c", "cc"]`
- Input: `s = "abc"`
  Output: `6`
  Explanation: `["a", "ab", "abc", "b", "bc", "c"]`
- Input: `s = "aaa"`
  Output: `3`
  Explanation: `["a", "aa", "aaa"]`

---

### Brute Force Approach
**Explanation:**
- Generate all possible substrings of the input string.
- Store unique substrings in a set.
- Return the size of the set.

```cpp
class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> uniqueSubstrings;
        int maxCount = 0;
        
        function<void(string, int)> backtrack = 
            [&](string current, int start) {
                if (start == s.size()) {
                    maxCount = max(maxCount, (int)uniqueSubstrings.size());
                    return;
                }
                
                for (int i = start; i < s.size(); ++i) {
                    string substring = s.substr(start, i - start + 1);
                    if (uniqueSubstrings.find(substring) == uniqueSubstrings.end()) {
                        uniqueSubstrings.insert(substring);
                        backtrack(s, i + 1);
                        uniqueSubstrings.erase(substring);
                    }
                }
            };
        
        backtrack(s, 0);
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because in the worst case, we generate all possible substrings.
> - **Space Complexity:** $O(2^n \cdot n)$, for storing all unique substrings.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings and checking for uniqueness, leading to exponential time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Use backtracking to generate substrings.
- Use a set to keep track of unique substrings.
- Prune branches that lead to duplicate substrings.
- The maximum number of unique substrings is the size of the set at any point during the backtracking process.

```cpp
class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> uniqueSubstrings;
        int maxCount = 0;
        
        function<void(int)> backtrack = 
            [&](int start) {
                if (start == s.size()) {
                    maxCount = max(maxCount, (int)uniqueSubstrings.size());
                    return;
                }
                
                for (int i = start; i < s.size(); ++i) {
                    string substring = s.substr(start, i - start + 1);
                    if (uniqueSubstrings.find(substring) == uniqueSubstrings.end()) {
                        uniqueSubstrings.insert(substring);
                        backtrack(i + 1);
                        uniqueSubstrings.erase(substring);
                    }
                }
            };
        
        backtrack(0);
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because in the worst case, we still generate all possible substrings.
> - **Space Complexity:** $O(2^n \cdot n)$, for storing all unique substrings.
> - **Optimality proof:** This approach is optimal because it generates all possible unique substrings exactly once, ensuring that no better solution exists in terms of time complexity. However, the actual running time may vary due to pruning of duplicate substrings.

---

### Final Notes

**Learning Points:**
- Backtracking can be used to generate all possible substrings of a string.
- Using a set to keep track of unique substrings can help prune branches that lead to duplicate substrings.
- The maximum number of unique substrings is the size of the set at any point during the backtracking process.

**Mistakes to Avoid:**
- Not using a set to keep track of unique substrings, leading to duplicate substrings being counted.
- Not pruning branches that lead to duplicate substrings, leading to unnecessary computation.
- Not considering edge cases, such as an empty string or a string with duplicate characters.