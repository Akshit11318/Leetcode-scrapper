## Find the Longest Balanced Substring of a Binary String

**Problem Link:** https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description

**Problem Statement:**
- Input: A binary string `s`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output: The length of the longest balanced substring.
- Key requirements: A balanced substring has an equal number of `0`s and `1`s.
- Edge cases: Empty string, string with only `0`s or only `1`s, or a string with no balanced substrings.

**Example Test Cases:**
- `s = "01000111"`: The longest balanced substring is `"01000111"`, so the answer is `8`.
- `s = "00111"`: The longest balanced substring is `"0"`, so the answer is `2`.
- `s = "111"`: The longest balanced substring is `"11"`, so the answer is `2`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible substring of the input string.
- For each substring, count the number of `0`s and `1`s and check if they are equal.
- Keep track of the maximum length of a balanced substring found so far.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                int zeros = 0, ones = 0;
                for (int k = i; k <= j; k++) {
                    if (s[k] == '0') zeros++;
                    else ones++;
                }
                if (zeros == ones) maxLength = max(maxLength, j - i + 1);
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string, because we have three nested loops.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum length and the current counts of `0`s and `1`s.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of checking every possible substring, while the low space complexity is because we do not need to store any additional data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass through the string, maintaining a balance between `0`s and `1`s by incrementing or decrementing a counter based on the current character.
- We use a hashmap to store the first occurrence of each balance value, allowing us to efficiently calculate the length of the current balanced substring.
- We update the maximum length whenever we find a longer balanced substring.
- This approach is optimal because it only requires a single pass through the string, resulting in a significant reduction in time complexity.

```cpp
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int maxLength = 0;
        int balance = 0;
        unordered_map<int, int> firstOccurrence;
        firstOccurrence[0] = -1; // Initialize with 0 balance at position -1
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') balance--;
            else balance++;
            if (firstOccurrence.find(balance) != firstOccurrence.end()) {
                maxLength = max(maxLength, i - firstOccurrence[balance]);
            } else {
                firstOccurrence[balance] = i;
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every balance value in the hashmap.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string, and we use a hashmap to efficiently store and retrieve the first occurrence of each balance value, allowing us to calculate the length of the current balanced substring in constant time.

### Final Notes

**Learning Points:**
- The importance of using a single pass through the data to reduce time complexity.
- The utility of hashmaps in storing and retrieving data efficiently.
- The concept of maintaining a balance between two types of elements (in this case, `0`s and `1`s) to solve the problem.

**Mistakes to Avoid:**
- Using brute force approaches that result in high time complexities.
- Not considering the use of data structures like hashmaps to improve efficiency.
- Failing to update the maximum length whenever a longer balanced substring is found.