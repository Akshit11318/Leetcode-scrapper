## Find Substring with Given Hash Value

**Problem Link:** https://leetcode.com/problems/find-substring-with-given-hash-value/description

**Problem Statement:**
- Input: A string `s` and a hash value `p`.
- Constraints: The length of `s` is at most $10^5$, and `p` is a non-negative integer.
- Expected Output: The lexicographically smallest substring that has a hash value equal to `p`, or an empty string if no such substring exists.
- Key Requirements: The hash of a string is calculated using the formula $H = c_0 + c_1 \times p + c_2 \times p^2 + ... + c_{n-1} \times p^{n-1}$, where $c_i$ is the ASCII value of the character at index $i$.
- Edge Cases: The input string may be empty, and the hash value `p` may be zero.

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the hash value of every possible substring of `s` and compare it with `p`.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. Calculate the hash value of each substring using the given formula.
  3. Compare the calculated hash value with `p`.
  4. If a match is found, store the substring as the lexicographically smallest match.
- This approach comes to mind first because it is straightforward and ensures that all possible substrings are considered.

```cpp
string substringWithHashValue(string s, int p) {
    int n = s.length();
    string result = "";
    
    // Iterate over all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            long long hash = 0;
            
            // Calculate the hash value of the current substring
            for (int k = 0; k < substr.length(); k++) {
                hash += (long long)(substr[k]) * pow(p, k);
            }
            
            // Compare the calculated hash value with p
            if (hash == p) {
                // Update the result if the current substring is lexicographically smaller
                if (result.empty() || substr < result) {
                    result = substr;
                }
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \times log(n))$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$), calculate the hash value of each substring ($O(n)$), and use the `pow` function which has a time complexity of $O(log(n))$.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we store the lexicographically smallest substring that matches the hash value.
> - **Why these complexities occur:** The time complexity is high because we consider all possible substrings and calculate their hash values. The space complexity is relatively low because we only store a single substring.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a rolling hash technique to efficiently calculate the hash value of substrings.
- Detailed breakdown:
  1. Initialize the hash value of the first character.
  2. Iterate over the string, updating the hash value by multiplying the current hash value by `p` and adding the ASCII value of the next character.
  3. Use a prefix hash array to store the hash values of all prefixes of the string.
  4. Iterate over all possible substrings, using the prefix hash array to efficiently calculate their hash values.
- This approach is optimal because it reduces the time complexity of calculating the hash value of substrings.

```cpp
string substringWithHashValue(string s, int p) {
    int n = s.length();
    string result = "";
    long long prefixHash[n + 1];
    prefixHash[0] = 0;
    
    // Calculate the prefix hash array
    for (int i = 0; i < n; i++) {
        prefixHash[i + 1] = prefixHash[i] * p + (long long)(s[i]);
    }
    
    // Iterate over all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            long long hash = prefixHash[j] - prefixHash[i];
            if (i > 0) {
                hash -= prefixHash[i] * pow(p, j - i);
            }
            
            // Compare the calculated hash value with p
            if (hash == p) {
                // Update the result if the current substring is lexicographically smaller
                if (result.empty() || s.substr(i, j - i) < result) {
                    result = s.substr(i, j - i);
                }
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times log(n))$, where $n$ is the length of the input string. This is because we calculate the prefix hash array ($O(n)$), iterate over all possible substrings ($O(n^2)$), and use the `pow` function which has a time complexity of $O(log(n))$.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we store the prefix hash array.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of calculating the hash value of substrings, making it more efficient than the brute force approach.

### Final Notes

**Learning Points:**
- The importance of using a rolling hash technique to efficiently calculate the hash value of substrings.
- The use of a prefix hash array to store the hash values of all prefixes of the string.
- The optimization of the brute force approach by reducing the time complexity of calculating the hash value of substrings.

**Mistakes to Avoid:**
- Not considering the use of a rolling hash technique, leading to a high time complexity.
- Not using a prefix hash array, resulting in redundant calculations.
- Not optimizing the brute force approach, leading to inefficient code.