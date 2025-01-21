## Check If Strings Can Be Made Equal With Operations II

**Problem Link:** https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description

**Problem Statement:**
- Given two strings `s` and `t`, determine if we can make `s` equal to `t` by performing the following operation any number of times: 
  - Select a character `c` in `s` and remove it.
  - Select a character `c` in `s` and insert it at any position in `s`.
- The goal is to check if it's possible to make `s` equal to `t` after any number of these operations.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of removals and insertions to see if we can transform `s` into `t`.
- This approach involves generating all permutations of `s` and checking if any of them match `t`.
- However, this approach is impractical due to its high computational complexity.

```cpp
#include <iostream>
#include <string>
#include <set>
using namespace std;

bool canMakeEqual(string s, string t) {
    set<string> permutations;
    // Function to generate all permutations of a string
    void generatePermutations(string str, int start, int end) {
        if (start == end) {
            permutations.insert(str);
        } else {
            for (int i = start; i <= end; i++) {
                string swapped = str;
                swap(swapped[start], swapped[i]);
                generatePermutations(swapped, start + 1, end);
            }
        }
    }
    
    generatePermutations(s, 0, s.length() - 1);
    
    // Check if t is in the set of permutations
    return permutations.find(t) != permutations.end();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of `s`, due to generating all permutations of `s`.
> - **Space Complexity:** $O(n!)$, for storing all permutations of `s`.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of `s`, which leads to exponential time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we can make `s` equal to `t` if and only if the set of characters in `s` is a superset of the set of characters in `t`.
- This is because we can remove any characters in `s` that are not in `t` and rearrange the remaining characters to form `t`.
- We can count the frequency of each character in `s` and `t` and check if the frequency of each character in `s` is greater than or equal to its frequency in `t`.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

bool canMakeEqual(string s, string t) {
    unordered_map<char, int> countS, countT;
    
    // Count the frequency of each character in s and t
    for (char c : s) countS[c]++;
    for (char c : t) countT[c]++;
    
    // Check if the frequency of each character in s is greater than or equal to its frequency in t
    for (auto& pair : countT) {
        if (countS[pair.first] < pair.second) return false;
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(n + m)$, for storing the frequency counts of characters in `s` and `t`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through each string to count the frequency of each character, resulting in linear time complexity.

### Final Notes

**Learning Points:**
- The importance of character frequency counting in string problems.
- How to optimize brute force approaches by identifying key insights and simplifying the problem.
- The use of `unordered_map` for efficient frequency counting.

**Mistakes to Avoid:**
- Not considering the character frequencies in `s` and `t`.
- Not checking for the superset condition between the sets of characters in `s` and `t`.
- Using inefficient data structures for frequency counting, such as arrays or linked lists.