## Letter Tile Possibilities

**Problem Link:** https://leetcode.com/problems/letter-tile-possibilities/description

**Problem Statement:**
- Input: A string `tiles` containing letters.
- Constraints: `1 <= tiles.length <= 7`.
- Expected Output: The number of possible non-empty strings that can be formed using the letters in `tiles`.
- Key Requirements: Each letter in `tiles` can be used at most once in each string, and the order of letters matters.
- Example Test Cases:
  - Input: `"AAB"`
    - Output: `8` (Possible strings: `"A", "A", "B", "AB", "AA", "BA", "AB", "BA"`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of the input string and count them.
- Step-by-step breakdown:
  1. Generate all permutations of the input string.
  2. Count the number of unique permutations.

```cpp
#include <iostream>
#include <set>
#include <string>
using namespace std;

int numTilePossibilities(string tiles) {
    set<string> uniqueStrings;
    int count = 0;

    // Function to generate all permutations
    void generatePermutations(string current, string remaining) {
        if (!current.empty()) {
            uniqueStrings.insert(current);
        }
        for (int i = 0; i < remaining.size(); ++i) {
            string newCurrent = current + remaining[i];
            string newRemaining = remaining.substr(0, i) + remaining.substr(i + 1);
            generatePermutations(newCurrent, newRemaining);
        }
    }

    generatePermutations("", tiles);
    return uniqueStrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the length of the input string, because in the worst case, we generate all possible subsets of the input string.
> - **Space Complexity:** $O(2^n)$, as we store all unique permutations in a set.
> - **Why these complexities occur:** The brute force approach generates all possible permutations, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a backtracking approach with a frequency array to keep track of used letters.
- Detailed breakdown:
  1. Initialize a frequency array to keep track of the count of each letter.
  2. Define a recursive function to generate all possible strings.
  3. In each recursive call, iterate through the frequency array and if a letter is available, decrement its count and make a recursive call.
  4. After the recursive call, increment the count back to restore the state.

```cpp
#include <iostream>
#include <string>
using namespace std;

int numTilePossibilities(string tiles) {
    int freq[26] = {0};
    for (char c : tiles) {
        freq[c - 'A']++;
    }

    int count = 0;
    void backtrack() {
        for (int i = 0; i < 26; ++i) {
            if (freq[i] > 0) {
                freq[i]--;
                count++;
                backtrack();
                freq[i]++;
            }
        }
    }
    backtrack();
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n)$, where $n$ is the length of the input string. However, this is an overestimation because not all branches are explored due to the early pruning when a letter's frequency reaches zero.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it explores all possible combinations of letters without generating duplicate strings, thus minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Backtracking with frequency arrays.
- Problem-solving pattern: Using recursion to explore all possible combinations.
- Optimization technique: Pruning branches early when a condition is met (in this case, when a letter's frequency reaches zero).

**Mistakes to Avoid:**
- Not restoring the state after recursive calls, leading to incorrect counts.
- Not checking for the base case (frequency of a letter reaching zero) before making recursive calls.
- Failing to consider the impact of duplicate letters on the overall count of unique strings.