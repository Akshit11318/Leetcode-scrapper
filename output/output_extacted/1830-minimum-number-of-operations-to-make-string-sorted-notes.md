## Minimum Number of Operations to Make String Sorted

**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/description

**Problem Statement:**
- Input: A string `s` containing lowercase English letters.
- Output: The minimum number of operations (insertions, deletions, or swaps) required to make the string sorted in ascending order.
- Key requirements: 
  - The string only contains lowercase English letters.
  - The operations allowed are insertion, deletion, and swap.
- Edge cases to consider: 
  - An empty string is already sorted, so the minimum number of operations is 0.
  - A string with a single character is already sorted.
- Example test cases:
  - Input: `s = "cba"`
    - Expected output: `5`
    - Explanation: To make the string sorted, we need to swap 'c' and 'a', then swap 'c' and 'b', and finally insert 'a' before 'b' and 'c' (or perform equivalent operations).
  - Input: `s = "abcd"`
    - Expected output: `0`
    - Explanation: The string is already sorted.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all permutations of the string and check which ones are sorted.
- Then, we calculate the minimum number of operations required to transform the original string into each sorted permutation.
- This approach involves comparing each character in the original string with the corresponding character in the sorted permutation and counting the differences.
- However, this approach is impractical for large strings due to the exponential number of permutations.

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int minOperations(string s) {
    int n = s.length();
    int minOps = n * 2; // Maximum possible operations
    sort(s.begin(), s.end()); // Create a sorted version of the string
    for (int i = 0; i < n; i++) {
        if (s[i] != s[i]) { // If characters at position i are different
            minOps = min(minOps, i + (n - i - 1)); // Update minimum operations
        }
    }
    return minOps;
}

int main() {
    string s;
    cin >> s;
    cout << minOperations(s) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the string, where $n$ is the length of the string.
> - **Space Complexity:** $O(n)$ for storing the sorted string.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to the additional string created for sorting.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a Longest Increasing Subsequence (LIS) approach.
- We can calculate the length of the LIS in the string, which represents the longest sequence that is already sorted.
- The minimum number of operations required is then $n - LIS$, where $n$ is the length of the string.
- This approach is optimal because it directly calculates the minimum number of operations required without generating all permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int lengthOfLIS(string s) {
    int n = s.length();
    vector<int> dp(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (s[i] > s[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}

int minOperations(string s) {
    int n = s.length();
    return n - lengthOfLIS(s);
}

int main() {
    string s;
    cin >> s;
    cout << minOperations(s) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string, due to the nested loops in the LIS calculation.
> - **Space Complexity:** $O(n)$ for storing the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum number of operations required without generating all permutations, and it has a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the application of the Longest Increasing Subsequence (LIS) concept to solve a string sorting problem.
- It highlights the importance of identifying the key insight that leads to an optimal solution.
- The solution showcases the use of dynamic programming to efficiently calculate the LIS.

**Mistakes to Avoid:**
- Assuming that generating all permutations is a viable approach for large strings.
- Not considering the use of dynamic programming to optimize the solution.
- Failing to identify the key insight that leads to the optimal solution.

---