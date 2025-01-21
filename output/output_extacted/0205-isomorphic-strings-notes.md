## Isomorphic Strings

**Problem Link:** https://leetcode.com/problems/isomorphic-strings/description

**Problem Statement:**
- Input format: Two strings `s` and `t`.
- Constraints: $1 \leq s.length \leq 5 \times 10^4$ and $s.length == t.length$.
- Expected output format: A boolean indicating whether `s` and `t` are isomorphic.
- Key requirements: Determine if there exists a character substitution that makes `s` and `t` identical.
- Edge cases: Empty strings, strings with different lengths, and strings with repeating characters.

**Example Test Cases:**
- `s = "egg", t = "add"`: True, because `e` can be mapped to `a` and `g` can be mapped to `d`.
- `s = "foo", t = "bar"`: False, because `o` cannot be mapped to both `o` and `a`.
- `s = "paper", t = "title"`: True, because each character in `s` can be uniquely mapped to a character in `t`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each character in both strings and check for a one-to-one mapping.
- We can use two arrays or vectors to keep track of the mappings from `s` to `t` and from `t` to `s`.
- This approach comes to mind first because it directly addresses the requirement of finding a character substitution.

```cpp
bool isIsomorphic(string s, string t) {
    // Check if the strings have the same length
    if (s.length() != t.length()) return false;
    
    // Initialize arrays to store mappings
    int sToT[256] = {0}, tToS[256] = {0};
    
    // Iterate over the characters in the strings
    for (int i = 0; i < s.length(); i++) {
        char sc = s[i], tc = t[i];
        
        // If the characters are not mapped and the mapping is consistent, map them
        if (sToT[sc] != tc && tToS[tc] != sc) {
            sToT[sc] = tc;
            tToS[tc] = sc;
        } 
        // If the mapping is inconsistent, return false
        else if (sToT[sc] != tc || tToS[tc] != sc) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings, because we iterate over each character once.
> - **Space Complexity:** $O(1)$, because we use a fixed-size array to store the mappings, regardless of the input size.
> - **Why these complexities occur:** The iteration over the characters causes the linear time complexity, and the use of fixed-size arrays causes the constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use two `unordered_map`s to store the mappings from `s` to `t` and from `t` to `s`.
- We iterate over the characters in the strings and check if the mappings are consistent.
- This approach is optimal because it has the same time complexity as the brute force approach but uses more efficient data structures.

```cpp
bool isIsomorphic(string s, string t) {
    // Check if the strings have the same length
    if (s.length() != t.length()) return false;
    
    // Initialize unordered maps to store mappings
    unordered_map<char, char> sToT, tToS;
    
    // Iterate over the characters in the strings
    for (int i = 0; i < s.length(); i++) {
        char sc = s[i], tc = t[i];
        
        // If the characters are not mapped and the mapping is consistent, map them
        if (sToT.find(sc) == sToT.end() && tToS.find(tc) == tToS.end()) {
            sToT[sc] = tc;
            tToS[tc] = sc;
        } 
        // If the mapping is inconsistent, return false
        else if (sToT[sc] != tc || tToS[tc] != sc) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings, because we iterate over each character once and use constant-time operations for the `unordered_map`s.
> - **Space Complexity:** $O(n)$, because in the worst case, we store a mapping for each character in the strings.
> - **Optimality proof:** This approach is optimal because it uses the most efficient data structures and has the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- The importance of using efficient data structures, such as `unordered_map`s, to store mappings.
- The need to check for consistent mappings in both directions.
- The use of iteration to check each character in the strings.

**Mistakes to Avoid:**
- Not checking if the strings have the same length before attempting to find a mapping.
- Not using efficient data structures to store the mappings.
- Not checking for consistent mappings in both directions.

**Similar Problems to Practice:**
- Other string manipulation problems, such as finding the longest common substring or the shortest palindrome.
- Problems involving mappings or substitutions, such as finding the minimum number of operations to transform one string into another.