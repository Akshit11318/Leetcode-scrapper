## Count Substrings That Can Be Rearranged to Contain a String I

**Problem Link:** https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and a string `target`, return the number of substrings in `s` that can be rearranged to contain `target`.
- Expected output format: The number of substrings that can be rearranged to contain `target`.
- Key requirements and edge cases to consider: 
  - `s` and `target` are non-empty strings.
  - The characters in `target` are distinct.
  - The length of `target` is less than or equal to the length of `s`.
- Example test cases with explanations:
  - `s = "ab", target = "ba"`: The answer is 2 because the substrings "ab" and "ba" can both be rearranged to contain "ba".
  - `s = "abc", target = "abc"`: The answer is 1 because only the substring "abc" can be rearranged to contain "abc".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each substring in `s`, check if it can be rearranged to contain `target`.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of `s`.
  2. For each substring, check if it can be rearranged to contain `target` by comparing the sorted characters in both strings.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible substrings and uses sorting to simplify the comparison.

```cpp
int countSubstrings(string s, string target) {
    int count = 0;
    int n = s.size();
    int m = target.size();
    
    // Generate all substrings of s
    for (int i = 0; i < n; ++i) {
        for (int j = i + m; j <= n; ++j) {
            string substring = s.substr(i, j - i);
            
            // Check if substring can be rearranged to contain target
            string sortedSubstring = substring;
            string sortedTarget = target;
            sort(sortedSubstring.begin(), sortedSubstring.end());
            sort(sortedTarget.begin(), sortedTarget.end());
            
            if (sortedSubstring.find(sortedTarget) != string::npos) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m \cdot \log(m))$ where $n$ is the length of `s` and $m$ is the length of `target`. This is because we generate all substrings of `s` (which takes $O(n^2)$ time), and for each substring, we sort it and `target` (which takes $O(m \cdot \log(m))$ time).
> - **Space Complexity:** $O(m)$ for sorting `target`.
> - **Why these complexities occur:** The brute force approach has high time complexity due to generating all substrings and sorting each one, which makes it inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all substrings of `s`, we can use a sliding window approach to efficiently check all substrings of length `m`.
- Detailed breakdown of the approach:
  1. Initialize a frequency count for `target`.
  2. Use a sliding window of size `m` to iterate over `s`.
  3. For each window, count the frequency of characters in the window.
  4. Compare the frequency count of the window with the frequency count of `target`.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it only checks substrings of length `m`, which reduces the number of comparisons needed.

```cpp
int countSubstrings(string s, string target) {
    int count = 0;
    int n = s.size();
    int m = target.size();
    
    // Initialize frequency count for target
    unordered_map<char, int> targetCount;
    for (char c : target) {
        targetCount[c]++;
    }
    
    // Use sliding window to iterate over s
    for (int i = 0; i <= n - m; ++i) {
        unordered_map<char, int> windowCount;
        for (int j = i; j < i + m; ++j) {
            windowCount[s[j]]++;
        }
        
        // Compare frequency count of window with target
        bool match = true;
        for (auto& pair : targetCount) {
            if (windowCount[pair.first] < pair.second) {
                match = false;
                break;
            }
        }
        
        if (match) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of `s` and `m` is the length of `target`. This is because we use a sliding window of size `m` to iterate over `s`, and for each window, we count the frequency of characters.
> - **Space Complexity:** $O(m)$ for storing the frequency count of `target` and the window.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity with respect to the length of `s`, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window, frequency counting.
- Problem-solving patterns identified: Using a sliding window to efficiently check all substrings of a certain length.
- Optimization techniques learned: Reducing the number of comparisons needed by using a frequency count.
- Similar problems to practice: Other problems that involve checking substrings or using a sliding window.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the frequency count correctly, not checking the edge cases.
- Edge cases to watch for: When `s` is empty, when `target` is empty, when `m` is greater than `n`.
- Performance pitfalls: Using a brute force approach that has high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution works correctly.