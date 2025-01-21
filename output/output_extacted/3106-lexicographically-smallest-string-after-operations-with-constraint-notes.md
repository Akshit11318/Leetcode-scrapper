## Lexicographically Smallest String After Applying Operations

**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description

**Problem Statement:**
- Given a string `s` and an integer `k`, return the lexicographically smallest string that can be obtained by applying the following operations:
  - Swap any two characters in `s`.
  - Remove the last character from `s` and append the character `k` times.
- The goal is to find the lexicographically smallest string after applying these operations.

**Input Format and Constraints:**
- `s`: a non-empty string consisting of lowercase English letters.
- `k`: a positive integer.

**Expected Output Format:**
- The lexicographically smallest string that can be obtained after applying the operations.

**Key Requirements and Edge Cases:**
- The string `s` can have any length.
- The integer `k` can be any positive value.
- The operations can be applied any number of times.

**Example Test Cases:**
- Input: `s = "leetcode", k = 2`
  - Output: "deec"
- Input: `s = "ab", k = 1`
  - Output: "a"
- Input: `s = "cba", k = 1`
  - Output: "ac"

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible strings that can be obtained by applying the operations and then find the lexicographically smallest one.
- This approach involves generating all permutations of the string `s` and then applying the operations to each permutation.

```cpp
#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

string lexicographicallySmallestString(string s, int k) {
    set<string> allStrings;
    allStrings.insert(s);
    
    // Generate all permutations of the string s
    sort(s.begin(), s.end());
    
    do {
        allStrings.insert(s);
    } while (next_permutation(s.begin(), s.end()));
    
    // Apply the operations to each permutation
    for (auto& str : allStrings) {
        for (int i = 0; i < str.size(); i++) {
            for (int j = i + 1; j < str.size(); j++) {
                string temp = str;
                swap(temp[i], temp[j]);
                allStrings.insert(temp);
            }
        }
    }
    
    // Remove the last character and append the character k times
    for (auto& str : allStrings) {
        for (int i = 0; i < str.size(); i++) {
            string temp = str.substr(0, i);
            temp += string(k, str[i]);
            allStrings.insert(temp);
        }
    }
    
    // Find the lexicographically smallest string
    string result = *allStrings.begin();
    for (auto& str : allStrings) {
        if (str < result) {
            result = str;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot k)$, where $n$ is the length of the string `s`. This is because we generate all permutations of the string `s`, apply the operations to each permutation, and then find the lexicographically smallest string.
> - **Space Complexity:** $O(n! \cdot n \cdot k)$, where $n$ is the length of the string `s`. This is because we store all permutations of the string `s` and the resulting strings after applying the operations.
> - **Why these complexities occur:** These complexities occur because we generate all permutations of the string `s` and apply the operations to each permutation, resulting in a large number of strings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a greedy approach. We can start by removing the last character of the string `s` and appending the character `k` times. Then, we can repeatedly apply this operation until we cannot improve the lexicographically smallest string.
- We can use a `priority_queue` to store the characters of the string `s` and the character `k`. We can then repeatedly remove the smallest character from the `priority_queue` and append it to the result string.

```cpp
#include <iostream>
#include <string>
#include <queue>

using namespace std;

string lexicographicallySmallestString(string s, int k) {
    priority_queue<char, vector<char>, greater<char>> pq;
    
    // Add the characters of the string s to the priority queue
    for (char c : s) {
        pq.push(c);
    }
    
    // Add the character k to the priority queue
    pq.push('a');
    
    string result;
    
    // Repeatedly remove the smallest character from the priority queue and append it to the result string
    while (!pq.empty()) {
        result += pq.top();
        pq.pop();
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the string `s`. This is because we use a `priority_queue` to store the characters of the string `s` and the character `k`, and we repeatedly remove the smallest character from the `priority_queue`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the characters of the string `s` and the character `k` in the `priority_queue`.
> - **Optimality proof:** This approach is optimal because we use a greedy approach to find the lexicographically smallest string. We repeatedly remove the smallest character from the `priority_queue` and append it to the result string, resulting in the lexicographically smallest string.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a greedy approach to find the lexicographically smallest string.
- The problem-solving pattern identified is the use of a `priority_queue` to store the characters of the string `s` and the character `k`.
- The optimization technique learned is the use of a greedy approach to improve the time complexity of the solution.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach to generate all permutations of the string `s` and apply the operations to each permutation.
- An edge case to watch for is when the string `s` is empty or the integer `k` is 0.
- A performance pitfall is to use a `priority_queue` with a large number of elements, resulting in a high time complexity.