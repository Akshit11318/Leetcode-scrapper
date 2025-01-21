## Buddy Strings

**Problem Link:** https://leetcode.com/problems/buddy-strings/description

**Problem Statement:**
- Input format: Two strings `s` and `goal`.
- Constraints: Both strings have the same length.
- Expected output format: A boolean indicating whether the strings can be made equal by swapping two characters.
- Key requirements and edge cases to consider: 
    - The strings may have repeated characters.
    - If the strings are already equal, they can be made equal by swapping two identical characters.
    - If there are more than two differences between the strings, they cannot be made equal by a single swap.
- Example test cases with explanations:
    - `s = "ab"`, `goal = "ba"`: True because swapping 'a' and 'b' makes the strings equal.
    - `s = "ab"`, `goal = "ab"`: True because the strings are already equal, and swapping 'a' with 'a' or 'b' with 'b' keeps them equal.
    - `s = "aa"`, `goal = "aa"`: True for the same reason as the previous example.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each character in `s` with each character in `goal` to find a pair of characters that can be swapped to make the strings equal.
- Step-by-step breakdown of the solution:
    1. Iterate over each character in `s`.
    2. For each character in `s`, iterate over each character in `goal`.
    3. If a pair of characters is found that can be swapped to make the strings equal, return True.
    4. If no such pair is found after checking all characters, return False.

```cpp
bool buddyStrings(string s, string goal) {
    if (s.length() != goal.length()) return false;
    
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j < s.length(); j++) {
            string temp = s;
            swap(temp[i], temp[j]);
            if (temp == goal) return true;
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the strings. This is because for each character, we potentially swap and compare the entire string.
> - **Space Complexity:** $O(n)$ for the temporary string created during the swap operation.
> - **Why these complexities occur:** The nested loops cause the high time complexity, and the temporary string causes the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible swaps, we can directly compare the strings character by character and find the first two differences. If these differences can be swapped to make the strings equal, we return True.
- Detailed breakdown of the approach:
    1. Compare `s` and `goal` character by character.
    2. Find the first two differences.
    3. If exactly two differences are found and swapping them makes the strings equal, return True.
    4. If the strings are already equal and there are at least two identical characters, return True because swapping these identical characters keeps the strings equal.
    5. Otherwise, return False.

```cpp
bool buddyStrings(string s, string goal) {
    if (s.length() != goal.length()) return false;
    
    if (s == goal) {
        // Check if there are at least two identical characters
        int count[26] = {0};
        for (char c : s) count[c - 'a']++;
        for (int i = 0; i < 26; i++) {
            if (count[i] > 1) return true;
        }
        return false;
    }
    
    vector<int> diff;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != goal[i]) diff.push_back(i);
        if (diff.size() > 2) return false;
    }
    
    if (diff.size() == 2) {
        swap(s[diff[0]], s[diff[1]]);
        return s == goal;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the strings. This is because we make a single pass through the strings.
> - **Space Complexity:** $O(1)$ for the count array and the vector to store differences, assuming the size of the alphabet (26) is constant.
> - **Optimality proof:** This is optimal because we only need to compare the strings once to find the differences and determine if a swap can make them equal. Any less would not provide enough information to solve the problem correctly.