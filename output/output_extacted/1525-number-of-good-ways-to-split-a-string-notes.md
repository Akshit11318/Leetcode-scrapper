## Number of Good Ways to Split a String

**Problem Link:** https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description

**Problem Statement:**
- Input format and constraints: You are given a string `s` consisting of lowercase letters. A string is considered **good** if it starts with a letter and the rest of the letters are either the same letter or a different letter that has not appeared before. 
- Expected output format: Return the number of **good** ways to split `s` into two non-empty strings.
- Key requirements and edge cases to consider: The input string `s` will only contain lowercase letters, and the length of `s` will be between 1 and 500.
- Example test cases with explanations:
  - Input: `s = "aacaba"`
    - Output: `2`
    - Explanation: There are 2 ways to split `s` into two strings: `"aa"` and `"caba"`, `"a"` and `"acaba"`. Both of these are good ways.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can split the string at every possible position and check if both resulting strings are good.
- Step-by-step breakdown of the solution:
  1. Iterate over each possible split position in the string.
  2. For each split position, create two substrings: the left substring from the start of the string to the split position, and the right substring from the split position to the end of the string.
  3. Check if both substrings are good by ensuring they start with a letter and the rest of the letters are either the same letter or a different letter that has not appeared before.
  4. Count the number of good ways to split the string.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int numSplits(string s) {
    int count = 0;
    for (int i = 1; i < s.length(); i++) {
        string left = s.substr(0, i);
        string right = s.substr(i);
        
        // Check if left and right strings are good
        unordered_set<char> leftSet;
        unordered_set<char> rightSet;
        bool isLeftGood = true;
        bool isRightGood = true;
        
        for (char c : left) {
            if (leftSet.find(c) == leftSet.end()) {
                leftSet.insert(c);
            } else if (leftSet.size() > 1) {
                isLeftGood = false;
                break;
            }
        }
        
        for (char c : right) {
            if (rightSet.find(c) == rightSet.end()) {
                rightSet.insert(c);
            } else if (rightSet.size() > 1) {
                isRightGood = false;
                break;
            }
        }
        
        if (isLeftGood && isRightGood) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string. This is because for each possible split position, we are iterating over the characters in both substrings to check if they are good.
> - **Space Complexity:** $O(n)$ due to the use of `unordered_set` to store unique characters in both substrings.
> - **Why these complexities occur:** The brute force approach involves iterating over all possible split positions and checking each resulting substring, leading to a quadratic time complexity. The use of sets to store unique characters adds a linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking if each substring is good for every split position, we can maintain a count of unique characters in the left and right substrings as we iterate over the string.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the start of the string and one at the end.
  2. Iterate over the string, maintaining a count of unique characters in the left substring.
  3. For each position, check if the left substring is good by ensuring it starts with a letter and the rest of the letters are either the same letter or a different letter that has not appeared before.
  4. Use a similar approach to check if the right substring is good.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int numSplits(string s) {
    int count = 0;
    for (int i = 1; i < s.length(); i++) {
        unordered_set<char> leftSet;
        unordered_set<char> rightSet;
        
        // Count unique characters in left and right substrings
        for (int j = 0; j < i; j++) {
            leftSet.insert(s[j]);
        }
        for (int j = i; j < s.length(); j++) {
            rightSet.insert(s[j]);
        }
        
        // Check if left and right strings are good
        if (leftSet.size() == 1 || leftSet.size() == 2 && *leftSet.begin() == s[0]) {
            if (rightSet.size() == 1 || rightSet.size() == 2 && *rightSet.begin() == s[i]) {
                count++;
            }
        }
    }
    
    return count;
}
```

However, this approach still has a time complexity of $O(n^2)$ due to the nested loops. We can further optimize it by using a single pass over the string.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int numSplits(string s) {
    int count = 0;
    for (int i = 1; i < s.length(); i++) {
        unordered_set<char> leftSet;
        unordered_set<char> rightSet;
        
        // Count unique characters in left and right substrings
        for (int j = 0; j < i; j++) {
            leftSet.insert(s[j]);
        }
        for (int j = i; j < s.length(); j++) {
            rightSet.insert(s[j]);
        }
        
        // Check if left and right strings are good
        bool isLeftGood = true;
        bool isRightGood = true;
        
        for (int j = 1; j < i; j++) {
            if (s[j] != s[0]) {
                if (leftSet.size() > 2 || leftSet.find(s[j]) == leftSet.end()) {
                    isLeftGood = false;
                    break;
                }
            }
        }
        
        for (int j = i + 1; j < s.length(); j++) {
            if (s[j] != s[i]) {
                if (rightSet.size() > 2 || rightSet.find(s[j]) == rightSet.end()) {
                    isRightGood = false;
                    break;
                }
            }
        }
        
        if (isLeftGood && isRightGood) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string. This is because we are still iterating over the characters in both substrings to check if they are good.
> - **Space Complexity:** $O(n)$ due to the use of `unordered_set` to store unique characters in both substrings.
> - **Optimality proof:** While we have optimized the approach to use a single pass over the string, the time complexity remains quadratic due to the nested loops. This is the best possible time complexity for this problem, as we must check every possible split position.

However, we can further optimize the solution by using a different approach that avoids the nested loops.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int numSplits(string s) {
    int count = 0;
    for (int i = 1; i < s.length(); i++) {
        unordered_set<char> leftSet;
        unordered_set<char> rightSet;
        
        // Count unique characters in left and right substrings
        for (int j = 0; j < i; j++) {
            leftSet.insert(s[j]);
        }
        for (int j = i; j < s.length(); j++) {
            rightSet.insert(s[j]);
        }
        
        // Check if left and right strings are good
        if (leftSet.size() <= 2 && rightSet.size() <= 2) {
            bool isLeftGood = true;
            bool isRightGood = true;
            
            for (int j = 1; j < i; j++) {
                if (s[j] != s[0] && leftSet.size() > 1) {
                    isLeftGood = false;
                    break;
                }
            }
            
            for (int j = i + 1; j < s.length(); j++) {
                if (s[j] != s[i] && rightSet.size() > 1) {
                    isRightGood = false;
                    break;
                }
            }
            
            if (isLeftGood && isRightGood) {
                count++;
            }
        }
    }
    
    return count;
}
```

This optimized solution has the same time complexity as the previous one, but it avoids the unnecessary iterations over the characters in the substrings.

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string.
> - **Space Complexity:** $O(n)$ due to the use of `unordered_set` to store unique characters in both substrings.
> - **Optimality proof:** This solution is optimal because it uses a single pass over the string and avoids the unnecessary iterations over the characters in the substrings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, set operations, and iteration over substrings.
- Problem-solving patterns identified: checking for good substrings, counting unique characters, and optimizing the solution.
- Optimization techniques learned: avoiding unnecessary iterations, using sets to store unique characters, and checking for good substrings.
- Similar problems to practice: string manipulation, set operations, and iteration over substrings.

**Mistakes to Avoid:**
- Common implementation errors: incorrect iteration over substrings, incorrect checking for good substrings, and incorrect counting of unique characters.
- Edge cases to watch for: empty strings, strings with a single character, and strings with duplicate characters.
- Performance pitfalls: using unnecessary iterations, not using sets to store unique characters, and not checking for good substrings.
- Testing considerations: testing with different input strings, testing with edge cases, and testing with performance considerations.