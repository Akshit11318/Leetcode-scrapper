## Delete Columns to Make Sorted

**Problem Link:** https://leetcode.com/problems/delete-columns-to-make-sorted/description

**Problem Statement:**
- Input: A 2D array `strs` containing strings, where each string has the same length.
- Constraints: $1 \leq strs.length \leq 100$, $1 \leq strs[i].length \leq 100$, and $strs[i]$ consists only of lowercase English letters.
- Expected Output: The minimum number of columns that need to be deleted to make the strings in `strs` sorted lexicographically.
- Key Requirements:
  - Compare strings character by character from left to right.
  - If a string is a prefix of another (i.e., one string is a substring of the other from the start), it is considered lexicographically smaller.
- Edge Cases:
  - Empty input array.
  - Single-element input array.
  - All strings are identical.

**Example Test Cases:**
1. Input: `strs = ["cba","daf","ghi"]`
   Output: `1`
   Explanation: Removing the first column makes the strings sorted: ["ba", "af", "hi"].
2. Input: `strs = ["a","b"]`
   Output: `0`
   Explanation: The strings are already sorted.
3. Input: `strs = ["zyx","wvu","tsr"]`
   Output: `3`
   Explanation: Need to remove all columns to make the strings sorted.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subset of columns to see if deleting those columns would make the strings sorted.
- This involves generating all subsets of the columns and for each subset, checking if the strings are sorted after removing those columns.
- This approach comes to mind first because it exhaustively checks all possibilities, ensuring that the minimum number of columns to delete is found.

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs[0].size();
        int minDeletions = INT_MAX;
        
        // Generate all possible subsets of columns
        for (int mask = 0; mask < (1 << n); ++mask) {
            vector<string> tempStrs;
            bool isSorted = true;
            
            // For each subset, create temporary strings by removing the columns in the subset
            for (const auto& str : strs) {
                string tempStr;
                for (int j = 0; j < n; ++j) {
                    if (!(mask & (1 << j))) {
                        tempStr += str[j];
                    }
                }
                tempStrs.push_back(tempStr);
            }
            
            // Check if the temporary strings are sorted
            for (int i = 1; i < tempStrs.size(); ++i) {
                if (tempStrs[i - 1] > tempStrs[i]) {
                    isSorted = false;
                    break;
                }
            }
            
            // If the temporary strings are sorted, update the minimum number of deletions
            if (isSorted) {
                int deletions = __builtin_popcount(mask);
                minDeletions = min(minDeletions, deletions);
            }
        }
        
        return minDeletions;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the length of the strings and $m$ is the number of strings. The $2^n$ factor comes from generating all subsets of columns, and for each subset, we iterate through the strings and their characters.
> - **Space Complexity:** $O(m \cdot n)$, as we store temporary strings for each subset of columns.
> - **Why these complexities occur:** The brute force approach is inherently exponential due to generating all subsets of columns, leading to high time complexity. The space complexity is linear with respect to the input size because we only store a constant number of strings for each subset.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to compare the strings character by character from left to right and stop as soon as we find a pair of strings that are not in sorted order. If we find such a pair, we know that the current column needs to be deleted.
- We iterate through the columns and for each column, we check if all strings are in sorted order with respect to the strings in the previous columns.
- This approach is optimal because it only requires a single pass through the columns and does not involve generating all subsets of columns.

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs[0].size();
        int deletions = 0;
        
        for (int j = 0; j < n; ++j) {
            bool isSorted = true;
            
            for (int i = 1; i < strs.size(); ++i) {
                if (strs[i - 1][j] > strs[i][j]) {
                    isSorted = false;
                    break;
                }
            }
            
            if (!isSorted) {
                ++deletions;
            }
        }
        
        return deletions;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of strings and $n$ is the length of the strings. We iterate through the columns and for each column, we iterate through the strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the number of deletions.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the columns and does not involve generating all subsets of columns. It also correctly identifies the minimum number of columns that need to be deleted to make the strings sorted.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and using them to optimize the solution.
- The use of bit manipulation to generate all subsets of columns in the brute force approach.
- The key insight in the optimal approach that allows us to stop as soon as we find a pair of strings that are not in sorted order.

**Mistakes to Avoid:**
- Not considering the problem constraints and using an approach that has high time complexity.
- Not optimizing the solution to reduce the number of iterations.
- Not correctly identifying the minimum number of columns that need to be deleted to make the strings sorted.