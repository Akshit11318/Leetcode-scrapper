## Valid Anagram

**Problem Link:** [https://leetcode.com/problems/valid-anagram/description](https://leetcode.com/problems/valid-anagram/description)

**Problem Statement:**
- Input format: Two strings `s` and `t`.
- Constraints: `1 <= s.length, t.length <= 5 * 10^4` and `s` and `t` consist of lowercase English letters.
- Expected output format: A boolean indicating whether `s` and `t` are anagrams of each other.
- Key requirements and edge cases to consider: The strings are anagrams if and only if they contain the same characters in the same quantities, regardless of order.
- Example test cases with explanations:
  - Input: `s = "anagram", t = "nagaram"` Output: `true`
  - Input: `s = "rat", t = "car"` Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if two strings are anagrams, we can sort each string and compare the results.
- Step-by-step breakdown of the solution:
  1. Check if the lengths of the strings are equal. If they are not, the strings cannot be anagrams.
  2. Sort the characters in each string.
  3. Compare the sorted strings. If they are equal, the original strings are anagrams.
- Why this approach comes to mind first: It directly addresses the definition of an anagram by comparing the sorted characters of each string.

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        // Check if lengths are equal
        if (s.length() != t.length()) return false;
        
        // Sort the strings
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // Compare the sorted strings
        return s == t;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the string. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, depending on the sorting algorithm used (e.g., some sorting algorithms may require additional space).
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is influenced by the sorting algorithm's requirements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting, which has a higher time complexity, we can use a frequency count array to compare the occurrence of each character in the strings.
- Detailed breakdown of the approach:
  1. Create a frequency count array of size 26 (since there are 26 lowercase English letters).
  2. Iterate through each string, incrementing the count in the array for each character encountered.
  3. Compare the frequency count arrays for both strings. If they are equal, the strings are anagrams.
- Proof of optimality: This approach has a linear time complexity, making it more efficient than sorting for large strings.
- Why further optimization is impossible: We must at least read the input strings once, which requires $O(n)$ time, making this approach optimal.

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        
        int count[26] = {0}; // Initialize frequency count array
        
        // Count occurrences in the first string
        for (char c : s) {
            count[c - 'a']++; // 'a' is subtracted to map 'a' to 0, 'b' to 1, etc.
        }
        
        // Subtract occurrences in the second string
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // Check if all counts are zero
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we make a constant number of passes through the input strings.
> - **Space Complexity:** $O(1)$, because the size of the frequency count array is constant (26 elements), regardless of the input size.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through each string, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting and the importance of understanding the problem's constraints to choose the optimal data structure.
- Problem-solving patterns identified: Recognizing when a problem can be solved more efficiently by using a specific data structure (like an array for frequency counting) instead of a more general approach (like sorting).
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary operations (in this case, sorting) and using a more efficient algorithm (frequency counting).
- Similar problems to practice: Other string manipulation problems, such as finding duplicates or permutations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly indexing the frequency count array or forgetting to check for equal string lengths before comparing.
- Edge cases to watch for: Empty strings, strings of different lengths, and ensuring the frequency count array is properly initialized.
- Performance pitfalls: Using sorting or other high-complexity operations when a simpler, more efficient approach is available.
- Testing considerations: Ensure to test with strings of varying lengths, including edge cases like empty strings or strings with repeated characters.