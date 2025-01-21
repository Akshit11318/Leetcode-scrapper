## Remove Colored Pieces If Both Neighbors Are the Same Color

**Problem Link:** https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description

**Problem Statement:**
- Input: A string `a` and `b` representing colored pieces.
- Constraints: Both strings only contain `'W'` or `'B'`, and both have the same length.
- Expected Output: Return `true` if it is possible to remove all colored pieces, `false` otherwise.
- Key Requirements: Two pieces can be removed if they are the same color and adjacent.
- Example Test Cases:
  - `a = "AABBCC"`, `b = "CCBBAA"`, Return `true` because we can remove all pieces.
  - `a = "AA"`, `b = "AB"`, Return `false` because we cannot remove all pieces.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of removing pieces to see if we can remove all of them.
- Step-by-step breakdown:
  1. Generate all permutations of `a` and `b`.
  2. For each permutation, try to remove pieces from left to right if they are the same color and adjacent.
  3. Check if all pieces can be removed for any permutation.

```cpp
class Solution {
public:
    bool winnerOfGame(string a, string b) {
        int n = a.length();
        int countA = 0, countB = 0;
        
        // Count 'A's and 'B's in string a
        for (char c : a) {
            if (c == 'A') countA++;
            else if (c == 'B') countB++;
        }
        
        // If 'A's are more than 'B's, Alice can win
        if (countA > countB) return true;
        
        // If 'B's are more than 'A's, Bob can win
        if (countA < countB) return false;
        
        // If 'A's and 'B's are equal, it's a draw
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `a`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** We only iterate through the strings once to count the 'A's and 'B's.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that Alice can win if there are more 'A's than 'B's in string `a`.
- Detailed breakdown:
  1. Count the number of 'A's and 'B's in string `a`.
  2. If 'A's are more than 'B's, Alice can win.
- Proof of optimality: This is the optimal solution because we only need to compare the counts of 'A's and 'B's to determine the winner.

```cpp
class Solution {
public:
    bool winnerOfGame(string a, string b) {
        int countA = 0, countB = 0;
        
        // Count 'A's and 'B's in string a
        for (char c : a) {
            if (c == 'A') countA++;
            else if (c == 'B') countB++;
        }
        
        // If 'A's are more than 'B's, Alice can win
        return countA > countB;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `a`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This is the optimal solution because we only need to compare the counts of 'A's and 'B's to determine the winner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: counting and comparison.
- Problem-solving patterns identified: using counts to determine the winner.
- Optimization techniques learned: reducing the problem to a simple comparison.
- Similar problems to practice: other games where the winner is determined by counts or comparisons.

**Mistakes to Avoid:**
- Common implementation errors: incorrect counting or comparison.
- Edge cases to watch for: empty strings or strings with only one character.
- Performance pitfalls: using inefficient algorithms or data structures.
- Testing considerations: testing with different inputs and edge cases.