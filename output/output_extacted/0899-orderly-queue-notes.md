## Orderly Queue

**Problem Link:** https://leetcode.com/problems/orderly-queue/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= 10`, `1 <= s.length <= 10^3`, `s` consists of lowercase English letters.
- Expected output: The lexicographically smallest string that can be obtained after any number of moves.
- Key requirements: 
  - A move is defined as either rotating the string of length `n` one position to the right, or reversing the string and then rotating it one position to the right.
  - We need to find the lexicographically smallest string that can be obtained after any number of moves.
- Example test cases:
  - Input: `s = "cba"`, `k = 2`
  - Output: `"acb"`
  - Explanation: In the first move, we reverse the string to get `"abc"`, and then rotate it one position to the right to get `"bca"`. In the second move, we rotate the string one position to the right to get `"acb"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible combinations of moves and find the lexicographically smallest string.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store unique strings.
  2. Perform a breadth-first search (BFS) with the initial string `s`.
  3. In each iteration of BFS, generate all possible next strings by rotating the current string one position to the right, or reversing the string and then rotating it one position to the right.
  4. Add each generated string to the set of unique strings.
  5. Repeat the BFS process until no new unique strings are generated.
  6. Find the lexicographically smallest string in the set of unique strings.

```cpp
#include <iostream>
#include <string>
#include <set>
#include <queue>

string orderlyQueue(string s, int k) {
    if (k > 1) {
        sort(s.begin(), s.end());
        return s;
    }
    
    set<string> unique;
    queue<string> q;
    q.push(s);
    
    while (!q.empty()) {
        string curr = q.front();
        q.pop();
        
        if (unique.find(curr) == unique.end()) {
            unique.insert(curr);
            
            // Generate next strings by rotating the current string one position to the right
            string next = curr.substr(1) + curr[0];
            q.push(next);
            
            // Generate next strings by reversing the string and then rotating it one position to the right
            string reversed = curr;
            reverse(reversed.begin(), reversed.end());
            string nextReversed = reversed.substr(1) + reversed[0];
            q.push(nextReversed);
        }
    }
    
    string result = *unique.begin();
    for (const auto& str : unique) {
        if (str < result) {
            result = str;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we generate all possible combinations of moves, and each move involves rotating or reversing the string.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we store all unique strings generated during the BFS process.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of moves, which leads to exponential time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: If `k` is greater than 1, we can simply sort the characters in the string to get the lexicographically smallest string. If `k` is 1, we need to try all possible rotations of the string and find the lexicographically smallest one.
- Detailed breakdown of the approach:
  1. If `k` is greater than 1, sort the characters in the string `s` and return the sorted string.
  2. If `k` is 1, generate all possible rotations of the string `s` and find the lexicographically smallest one.

```cpp
string orderlyQueue(string s, int k) {
    if (k > 1) {
        sort(s.begin(), s.end());
        return s;
    }
    
    string result = s;
    for (int i = 0; i < s.length(); i++) {
        string rotated = s.substr(i) + s.substr(0, i);
        if (rotated < result) {
            result = rotated;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ if `k` is greater than 1, where $n$ is the length of the string `s`. This is because we sort the characters in the string. If `k` is 1, the time complexity is $O(n)$, where $n$ is the length of the string `s`. This is because we generate all possible rotations of the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the rotated strings.
> - **Optimality proof:** The optimal approach is optimal because it takes advantage of the fact that if `k` is greater than 1, we can simply sort the characters in the string to get the lexicographically smallest string. If `k` is 1, we need to try all possible rotations of the string, which can be done in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, string rotation, and BFS.
- Problem-solving patterns identified: taking advantage of the properties of the problem to reduce the search space.
- Optimization techniques learned: using the fact that if `k` is greater than 1, we can simply sort the characters in the string to get the lexicographically smallest string.
- Similar problems to practice: problems involving string manipulation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, such as when `k` is greater than 1 or when the string is empty.
- Edge cases to watch for: when `k` is 1, we need to try all possible rotations of the string.
- Performance pitfalls: using a brute force approach when a more efficient solution is available.
- Testing considerations: testing the solution with different inputs, including edge cases, to ensure correctness.