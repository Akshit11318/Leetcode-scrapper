## Minimum Window Substring

**Problem Link:** https://leetcode.com/problems/minimum-window-substring/description

**Problem Statement:**
- Input format and constraints: Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. 
- Expected output format: A string representing the minimum window.
- Key requirements and edge cases to consider:
  - Handling cases where `t` is longer than `s`.
  - Dealing with duplicate characters in both `s` and `t`.
  - Ensuring the solution is case-sensitive.
- Example test cases with explanations:
  - `s = "ADOBECODEBANC", t = "ABC"` should return `"BANC"`.
  - `s = "a", t = "a"` should return `"a"`.
  - `s = "a", t = "aa"` should return an empty string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `s` to see if it contains all characters of `t`.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if it contains all characters of `t`.
  3. If a substring contains all characters of `t` and is smaller than the current minimum window, update the minimum window.
- Why this approach comes to mind first: It's the most straightforward way to ensure we don't miss any possible windows.

```cpp
string minWindow(string s, string t) {
    if (t.size() > s.size()) return "";
    unordered_map<char, int> tCount;
    for (char c : t) tCount[c]++;
    
    string minWindow = "";
    for (int i = 0; i < s.size(); i++) {
        for (int j = i; j < s.size(); j++) {
            unordered_map<char, int> windowCount;
            for (int k = i; k <= j; k++) windowCount[s[k]]++;
            bool isWindow = true;
            for (auto &pair : tCount) {
                if (windowCount[pair.first] < pair.second) {
                    isWindow = false;
                    break;
                }
            }
            if (isWindow && (minWindow == "" || j - i + 1 < minWindow.size())) {
                minWindow = s.substr(i, j - i + 1);
            }
        }
    }
    return minWindow;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `s`. The reason is we have three nested loops: two for generating substrings and one for comparing characters in the substring with `t`.
> - **Space Complexity:** $O(n)$ for storing the counts of characters in the window.
> - **Why these complexities occur:** The brute force approach involves checking every possible substring, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach and maintain counts of characters in `t` and the current window.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of `s`.
  2. Expand the window to the right by moving `right` and updating the count of characters in the window.
  3. When the window contains all characters of `t`, try to minimize it by moving `left` to the right and updating counts.
  4. Keep track of the minimum window found so far.
- Proof of optimality: This approach ensures we check all possible windows in a linear fashion, avoiding unnecessary comparisons.

```cpp
string minWindow(string s, string t) {
    if (t.size() > s.size()) return "";
    unordered_map<char, int> tCount, windowCount;
    for (char c : t) tCount[c]++;
    
    int required = tCount.size();
    int formed = 0;
    
    int windowSize = INT_MAX;
    int left = 0;
    int ans[2] = {0, 0}; // Stores the starting and ending indices of the min window
    
    for (int right = 0; right < s.size(); right++) {
        char c = s[right];
        windowCount[c]++;
        
        if (tCount.find(c) != tCount.end() && windowCount[c] == tCount[c]) {
            formed++;
        }
        
        while (left <= right && formed == required) {
            char c = s[left];
            
            if (right - left + 1 < windowSize) {
                windowSize = right - left + 1;
                ans[0] = left;
                ans[1] = right;
            }
            
            windowCount[c]--;
            if (tCount.find(c) != tCount.end() && windowCount[c] < tCount[c]) {
                formed--;
            }
            
            left++;
        }
    }
    
    return windowSize == INT_MAX ? "" : s.substr(ans[0], ans[1] - ans[0] + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `s`, as we process each character once.
> - **Space Complexity:** $O(n)$ for storing the counts of characters in `t` and the window.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find the minimum window, achieving linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, character counting.
- Problem-solving patterns identified: Minimizing a window that satisfies certain conditions.
- Optimization techniques learned: Reducing comparisons by maintaining counts and using a sliding window.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating counts or moving the window pointers.
- Edge cases to watch for: Handling cases where `t` is longer than `s`, or when there are duplicate characters.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases and large strings.