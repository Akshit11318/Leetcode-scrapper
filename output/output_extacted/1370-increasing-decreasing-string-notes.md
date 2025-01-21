## Increasing Decreasing String

**Problem Link:** https://leetcode.com/problems/increasing-decreasing-string/description

**Problem Statement:**
- Input: A string `s` and an integer array `indices`.
- Constraints: `8 <= s.length <= 8 * 10^4`, `s` contains only lowercase English letters, and `indices.length == s.length`.
- Expected Output: A new string where the characters are rearranged such that the characters at each index `i` in the new string is the character at index `indices[i]` in the original string, and the resulting string is in a specific order.
- Key Requirements: The resulting string should first be in increasing order, then in decreasing order.
- Edge Cases: Empty input, single character input, and cases where the `indices` array is not a valid permutation of the string indices.

**Example Test Cases:**
- `s = "aaa", indices = [0,1,2]`, the output is `"aaa"`.
- `s = "rat", indices = [0,2,1]`, the output is `"art"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to first sort the string based on the `indices` array, then rearrange the characters to achieve the increasing-decreasing order.
- This approach involves multiple steps: sorting the string, then rearranging the characters.
- It comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

string increasingDecreasingString(string s, vector<int>& indices) {
    string result = s;
    // Create a vector of pairs to store characters and their corresponding indices
    vector<pair<char, int>> chars;
    for (int i = 0; i < s.length(); i++) {
        chars.push_back({s[i], indices[i]});
    }
    // Sort the vector based on the indices
    sort(chars.begin(), chars.end(), [](pair<char, int> a, pair<char, int> b) {
        return a.second < b.second;
    });
    // Rearrange the characters to achieve the increasing-decreasing order
    int mid = (s.length() + 1) / 2;
    string firstHalf, secondHalf;
    for (int i = 0; i < mid; i++) {
        firstHalf += chars[i].first;
    }
    for (int i = mid; i < s.length(); i++) {
        secondHalf += chars[i].first;
    }
    sort(firstHalf.begin(), firstHalf.end());
    sort(secondHalf.begin(), secondHalf.end(), [](char a, char b) {
        return a > b;
    });
    result = firstHalf + secondHalf;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the vector of pairs and the strings.
> - **Space Complexity:** $O(n)$ for storing the vector of pairs and the result strings.
> - **Why these complexities occur:** The sorting operations dominate the time complexity, while the space complexity is due to the additional data structures used.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to directly construct the result string in the desired order without intermediate sorting steps.
- This approach involves a single pass through the input string and the `indices` array.
- It is optimal because it minimizes the number of operations required to achieve the desired output.

```cpp
#include <iostream>
#include <string>
#include <vector>

string increasingDecreasingString(string s, vector<int>& indices) {
    int n = s.length();
    vector<char> result(n);
    // Create a vector to store the characters at their corresponding indices
    for (int i = 0; i < n; i++) {
        result[indices[i]] = s[i];
    }
    // Initialize variables to keep track of the current character in the increasing and decreasing parts
    char inc = 'a', dec = 'z';
    // Initialize variables to keep track of the current position in the increasing and decreasing parts
    int pos = 0;
    // Construct the result string
    for (int i = 0; i < n; i++) {
        if (i < (n + 1) / 2) {
            while (pos < n && result[pos] != 0 && result[pos] < inc) {
                pos++;
            }
            if (pos < n && result[pos] == 0) {
                result[pos] = inc;
                inc++;
            } else {
                // If no position is found, try to find the next available position
                while (pos < n && result[pos] != 0) {
                    pos++;
                }
                if (pos < n) {
                    result[pos] = inc;
                    inc++;
                }
            }
        } else {
            while (pos < n && result[pos] != 0 && result[pos] > dec) {
                pos++;
            }
            if (pos < n && result[pos] == 0) {
                result[pos] = dec;
                dec--;
            } else {
                // If no position is found, try to find the next available position
                while (pos < n && result[pos] != 0) {
                    pos++;
                }
                if (pos < n) {
                    result[pos] = dec;
                    dec--;
                }
            }
        }
    }
    // Convert the vector to a string
    string strResult(result.begin(), result.end());
    return strResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we make a single pass through the input.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string, because we use a vector to store the characters.
> - **Optimality proof:** This solution is optimal because it directly constructs the result string in the desired order, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- The importance of directly constructing the result string in the desired order.
- How to minimize the number of operations required to achieve the desired output.
- The use of vectors to store characters and their corresponding indices.

**Mistakes to Avoid:**
- Using unnecessary sorting steps.
- Not considering the optimal approach that directly constructs the result string.
- Not handling edge cases properly.

By following the optimal approach, we can solve the problem efficiently and effectively. The key insight is to directly construct the result string in the desired order, minimizing the number of operations required. This approach demonstrates the importance of careful analysis and optimization in solving problems.