## Partition String into Minimum Beautiful Substrings

**Problem Link:** https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/description

**Problem Statement:**
- Input: A string `s` containing lowercase English letters.
- Output: The minimum number of beautiful substrings that `s` can be partitioned into.
- Key requirements: A beautiful substring is one where every character appears an even number of times.
- Edge cases: Empty string, single character, or strings with only one unique character.

**Example Test Cases:**
- Input: `s = "abc"` - Output: `2` because "a" and "bc" are beautiful substrings.
- Input: `s = "abcb"` - Output: `1` because "abcb" is a beautiful substring itself.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible substrings and check if they are beautiful.
- We can use a nested loop to generate all substrings and then check each one.
- However, this approach is inefficient due to its high time complexity.

```cpp
int partitionString(string s) {
    int count = 0;
    while (!s.empty()) {
        for (int i = 1; i <= s.size(); ++i) {
            string substr = s.substr(0, i);
            if (isBeautiful(substr)) {
                s = s.substr(i);
                count++;
                break;
            }
        }
    }
    return count;
}

bool isBeautiful(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    for (auto &pair : freq) {
        if (pair.second % 2 != 0) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string, due to the nested loop and the `isBeautiful` function.
> - **Space Complexity:** $O(n)$ for storing the frequency map and substrings.
> - **Why these complexities occur:** The brute force approach tries all possible substrings, leading to a high time complexity, and uses additional space to store frequency maps and substrings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach and maintain a frequency map of characters within the current window.
- We expand the window to the right and update the frequency map.
- When a character's frequency becomes odd, we know the current window is not beautiful and need to start a new window.
- This approach ensures we find the minimum number of beautiful substrings efficiently.

```cpp
int partitionString(string s) {
    int count = 0;
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
        if (freq[c] % 2 == 0) {
            bool allEven = true;
            for (auto &pair : freq) {
                if (pair.second % 2 != 0) {
                    allEven = false;
                    break;
                }
            }
            if (allEven) {
                count++;
                freq.clear();
            }
        }
    }
    if (!freq.empty()) {
        count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$ for storing the frequency map.
> - **Optimality proof:** This approach is optimal because it uses a single pass through the string and maintains a minimal amount of information (the frequency map), ensuring we find the minimum number of beautiful substrings in linear time.

---

### Final Notes

**Learning Points:**
- The importance of using a sliding window approach for string problems.
- Maintaining a frequency map to track character occurrences efficiently.
- The concept of beautiful substrings and how to identify them.
- Optimization techniques to reduce time complexity from $O(n^3)$ to $O(n)$.

**Mistakes to Avoid:**
- Using brute force approaches for large inputs.
- Not considering edge cases like empty strings or single-character strings.
- Not optimizing the solution for better time complexity.
- Not validating the input and handling potential errors.