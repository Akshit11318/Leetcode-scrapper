## Permutation Difference Between Two Strings

**Problem Link:** https://leetcode.com/problems/permutation-difference-between-two-strings/description

**Problem Statement:**
- Input format: Two strings `s1` and `s2` of the same length.
- Constraints: The length of `s1` and `s2` is `n`, where `1 <= n <= 10^5`, and the strings only contain lowercase English letters.
- Expected output format: The minimum number of operations to transform `s1` into `s2`.
- Key requirements and edge cases to consider: 
  - The strings only contain lowercase English letters.
  - The length of the strings is the same.
- Example test cases with explanations:
  - Example 1: `s1 = "abc", s2 = "bca"`: The output should be `2` because we can transform `s1` into `s2` by swapping the first and second characters, and then swapping the second and third characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all permutations of `s1` and checking if any of them are equal to `s2`. If we find a match, we can calculate the minimum number of operations to transform `s1` into `s2` by counting the number of different characters at the same positions.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `s1`.
  2. For each permutation, compare it with `s2` character by character.
  3. If a match is found, calculate the minimum number of operations to transform `s1` into `s2`.
- Why this approach comes to mind first: It's a straightforward approach that involves generating all possible permutations and checking if any of them match `s2`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void permute(string s, int start, int end, string &s2) {
    if (start == end) {
        int diff = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != s2[i]) {
                diff++;
            }
        }
        cout << diff << endl;
    } else {
        for (int i = start; i <= end; i++) {
            swap(s[start], s[i]);
            permute(s, start + 1, end, s2);
            swap(s[start], s[i]); // backtrack
        }
    }
}

int main() {
    string s1 = "abc";
    string s2 = "bca";
    permute(s1, 0, s1.size() - 1, s2);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the strings, because we generate all permutations of `s1`.
> - **Space Complexity:** $O(n)$, because we need to store the current permutation.
> - **Why these complexities occur:** The time complexity is high because we generate all permutations of `s1`, and the space complexity is relatively low because we only need to store the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the concept of `permutation cycles` to find the minimum number of operations to transform `s1` into `s2`. A permutation cycle is a sequence of elements that can be transformed into each other by a series of swaps.
- Detailed breakdown of the approach:
  1. Create a mapping of characters in `s1` to their indices.
  2. Iterate through `s2` and for each character, find its index in `s1`.
  3. If the character is not at the correct position, increment the cycle count and continue to the next character.
  4. The minimum number of operations is `n - cycle_count`, where `n` is the length of the strings.
- Proof of optimality: This approach is optimal because it uses the concept of permutation cycles to find the minimum number of operations to transform `s1` into `s2`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int permutationDifference(string s1, string s2) {
    int n = s1.size();
    vector<bool> visited(n, false);
    int cycle_count = 0;
    
    for (int i = 0; i < n; i++) {
        if (visited[i] || s1[i] == s2[i]) {
            continue;
        }
        
        cycle_count++;
        int j = i;
        while (s1[j] != s2[i]) {
            j = s2.find(s1[j]);
        }
        
        while (j != i) {
            swap(s1[i], s1[j]);
            j = s2.find(s1[j]);
        }
    }
    
    return n - cycle_count;
}

int main() {
    string s1 = "abc";
    string s2 = "bca";
    cout << permutationDifference(s1, s2) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings, because we iterate through `s2` once.
> - **Space Complexity:** $O(n)$, because we need to store the visited indices.
> - **Optimality proof:** This approach is optimal because it uses the concept of permutation cycles to find the minimum number of operations to transform `s1` into `s2`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Permutation cycles, mapping of characters to indices.
- Problem-solving patterns identified: Using permutation cycles to find the minimum number of operations to transform one string into another.
- Optimization techniques learned: Using a mapping of characters to indices to reduce the time complexity.
- Similar problems to practice: Other problems involving permutation cycles, such as finding the minimum number of operations to transform one array into another.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty strings or strings of different lengths.
- Edge cases to watch for: Empty strings, strings of different lengths, strings with duplicate characters.
- Performance pitfalls: Using a brute force approach, not using a mapping of characters to indices.
- Testing considerations: Test the function with different input strings, including edge cases.