## Bitwise ORs of Subarrays
**Problem Link:** https://leetcode.com/problems/bitwise-ors-of-subarrays/description

**Problem Statement:**
- Input: An integer array `arr`.
- Constraints: $1 \leq arr.length \leq 5 \times 10^4$, $0 \leq arr[i] \leq 10^6$.
- Expected Output: The number of distinct results of `arr[i] | arr[i+1] | ... | arr[j]` for every possible subarray.
- Key Requirements: Consider all possible subarrays, compute the bitwise OR for each, and count distinct results.
- Example Test Cases:
  - Input: `arr = [1,2,4]`
  - Output: `6`
  - Explanation: The possible subarray results are:
    - `[1]` = 1
    - `[2]` = 2
    - `[1, 2]` = 3
    - `[4]` = 4
    - `[1, 2, 4]` = 7
    - `[2, 4]` = 6

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subarrays, compute the bitwise OR for each, and store results in a set to ensure uniqueness.
- Step-by-step breakdown:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, compute the bitwise OR of its elements.
  3. Store each result in a set to automatically eliminate duplicates.
  4. Return the size of the set as the number of distinct bitwise OR results.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int subarrayBitwiseORs(std::vector<int>& arr) {
    std::unordered_set<int> distinctResults;
    int n = arr.size();
    
    for (int i = 0; i < n; i++) {
        int orResult = 0;
        for (int j = i; j < n; j++) {
            orResult |= arr[j];
            distinctResults.insert(orResult);
        }
    }
    
    return distinctResults.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array, because we generate all possible subarrays and compute their bitwise OR.
> - **Space Complexity:** $O(n^2)$, as in the worst case, we might store all subarray results in the set.
> - **Why these complexities occur:** The nested loop structure for generating subarrays and computing their bitwise OR leads to quadratic time complexity. The space complexity is also quadratic due to storing all distinct results.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Realize that the bitwise OR operation has a property where `a | b | c` equals `(a | b) | c`. This means we can compute the bitwise OR of subarrays incrementally.
- Detailed breakdown:
  1. Initialize a set to store the distinct bitwise OR results of subarrays ending at the current position.
  2. For each element in the array, compute the bitwise OR with each result in the set from the previous step and add new results to the set.
  3. After processing all elements, return the total number of distinct results found.

```cpp
int subarrayBitwiseORs(std::vector<int>& arr) {
    std::unordered_set<int> curr, next;
    curr.insert(0);
    
    for (int num : arr) {
        next.clear();
        next.insert(num);
        for (int prev : curr) {
            next.insert(prev | num);
        }
        curr = next;
    }
    
    return curr.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of elements in the array and $m$ is the maximum number of distinct bitwise OR results for subarrays ending at any position. In the worst case, $m$ could be up to $n$ but is typically much smaller due to the properties of bitwise OR.
> - **Space Complexity:** $O(m)$, for storing the distinct bitwise OR results.
> - **Optimality proof:** This approach is optimal because it efficiently computes and stores only the distinct bitwise OR results for all subarrays, avoiding redundant computations.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of operations (in this case, bitwise OR) to optimize algorithms.
- How to apply incremental computation to reduce redundancy in solving problems involving subarrays.
- The use of sets for efficiently storing and counting distinct results.

**Mistakes to Avoid:**
- Failing to consider the properties of operations that can simplify computations.
- Not optimizing for space and time complexities by removing redundant computations.
- Overlooking the use of appropriate data structures (like sets) for efficient storage and lookup of distinct results.