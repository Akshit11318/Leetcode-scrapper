## Take K of Each Character From Left and Right
**Problem Link:** https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= k <= 10^5`.
- Expected Output: The maximum number of characters that can be taken from the string `s` by taking `k` characters from the left and `k` characters from the right.
- Key Requirements:
  - The characters taken from the left and right must be the same.
  - If there are multiple possible characters to take, take the one that maximizes the total number of characters taken.
- Edge Cases:
  - If `k` is greater than the length of the string, return 0.
  - If the string is empty, return 0.
- Example Test Cases:
  - `s = "abcabcabc", k = 2`, expected output: 6.
  - `s = "ababcab", k = 2`, expected output: 4.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible characters in the string and see which one can be taken the most times from both the left and the right.
- We will use two nested loops to try all possible characters.
- For each character, we will count the number of times it appears in the first `k` characters and the last `k` characters.
- We will keep track of the maximum count found so far.

```cpp
int takeKofEachCharacterFromLeftAndRight(string s, int k) {
    int n = s.length();
    int maxCount = 0;
    
    // Try all possible characters
    for (char c = 'a'; c <= 'z'; c++) {
        int leftCount = 0;
        int rightCount = 0;
        
        // Count the number of times the character appears in the first k characters
        for (int i = 0; i < k && i < n; i++) {
            if (s[i] == c) {
                leftCount++;
            }
        }
        
        // Count the number of times the character appears in the last k characters
        for (int i = n - 1; i >= n - k && i >= 0; i--) {
            if (s[i] == c) {
                rightCount++;
            }
        }
        
        // Update the maximum count
        maxCount = max(maxCount, leftCount + rightCount);
    }
    
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26 \cdot k)$, where $26$ is the number of possible characters and $k$ is the number of characters to take from the left and right.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum count.
> - **Why these complexities occur:** The time complexity occurs because we try all possible characters and count the number of times each character appears in the first `k` and last `k` characters. The space complexity occurs because we only use a constant amount of space to store the maximum count.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a hash map to store the count of each character in the first `k` characters and the last `k` characters.
- We can then iterate through the hash map to find the character with the maximum count.
- We can use a single loop to count the number of times each character appears in the first `k` characters and the last `k` characters.

```cpp
int takeKofEachCharacterFromLeftAndRight(string s, int k) {
    int n = s.length();
    unordered_map<char, int> leftCount;
    unordered_map<char, int> rightCount;
    
    // Count the number of times each character appears in the first k characters
    for (int i = 0; i < k && i < n; i++) {
        leftCount[s[i]]++;
    }
    
    // Count the number of times each character appears in the last k characters
    for (int i = n - 1; i >= n - k && i >= 0; i--) {
        rightCount[s[i]]++;
    }
    
    // Find the character with the maximum count
    int maxCount = 0;
    for (auto& pair : leftCount) {
        if (rightCount.find(pair.first) != rightCount.end()) {
            maxCount = max(maxCount, pair.second + rightCount[pair.first]);
        }
    }
    
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of characters to take from the left and right.
> - **Space Complexity:** $O(k)$, as we use a hash map to store the count of each character in the first `k` characters and the last `k` characters.
> - **Optimality proof:** This is the optimal solution because we only need to iterate through the first `k` characters and the last `k` characters to find the character with the maximum count. We use a hash map to store the count of each character, which allows us to find the character with the maximum count in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hash map, counting characters.
- Problem-solving patterns identified: using a hash map to store the count of each character.
- Optimization techniques learned: using a single loop to count the number of times each character appears in the first `k` characters and the last `k` characters.
- Similar problems to practice: counting characters in a string, finding the maximum count of a character in a string.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the character is in the hash map before trying to access it.
- Edge cases to watch for: when `k` is greater than the length of the string, when the string is empty.
- Performance pitfalls: using a brute force approach that tries all possible characters.
- Testing considerations: testing the function with different inputs, such as an empty string, a string with a single character, a string with multiple characters.