## Find the Minimum Cost Array Permutation
**Problem Link:** https://leetcode.com/problems/find-the-minimum-cost-array-permutation/description

**Problem Statement:**
- Input: Two integer arrays `cost` and `mask` of the same length.
- Constraints: Both arrays have the same length `n`, where `1 <= n <= 10^5`.
- Expected Output: The minimum cost to permute the `cost` array such that the sum of the product of corresponding elements from `cost` and `mask` arrays is minimized.
- Key Requirements and Edge Cases:
  - Each element in `mask` is a permutation of numbers from `1` to `n`.
  - The permutation of the `cost` array must result in the minimum possible sum of products.

**Example Test Cases:**
- For `cost = [1, 2, 3]` and `mask = [3, 1, 2]`, the minimum cost permutation of `cost` would be `[2, 3, 1]`, resulting in a total cost of `(2*3) + (3*1) + (1*2) = 6 + 3 + 2 = 11`.
- For `cost = [10, 20, 30]` and `mask = [2, 3, 1]`, the minimum cost permutation of `cost` would be `[20, 30, 10]`, resulting in a total cost of `(20*2) + (30*3) + (10*1) = 40 + 90 + 10 = 140`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible permutations of the `cost` array and calculating the sum of products for each permutation.
- For each permutation, multiply corresponding elements from the permuted `cost` array and the `mask` array, then sum these products.
- The permutation with the smallest sum of products is the solution.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minCost(vector<int>& cost, vector<int>& mask) {
    int n = cost.size();
    int minCost = INT_MAX;
    vector<int> perm = cost;
    
    // Generate all permutations
    do {
        int currCost = 0;
        for (int i = 0; i < n; ++i) {
            currCost += perm[i] * mask[i];
        }
        minCost = min(minCost, currCost);
    } while (next_permutation(perm.begin(), perm.end()));
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ because we are generating all permutations of the array, and there are $n!$ permutations for an array of length $n$.
> - **Space Complexity:** $O(n)$ for storing the current permutation.
> - **Why these complexities occur:** The brute force approach is inherently expensive due to the generation of all permutations, leading to a factorial time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight here is to use a greedy approach based on sorting. We can sort the `cost` array in ascending order and the `mask` array in descending order. This way, the smallest costs are multiplied by the largest masks, minimizing the total cost.
- This approach works because the problem essentially asks for a permutation that minimizes the sum of products. By aligning the smallest costs with the largest masks, we achieve this minimization efficiently.

```cpp
int minCost(vector<int>& cost, vector<int>& mask) {
    int n = cost.size();
    vector<int> sortedCost = cost;
    vector<int> sortedMask = mask;
    
    // Sort cost in ascending order and mask in descending order
    sort(sortedCost.begin(), sortedCost.end());
    sort(sortedMask.rbegin(), sortedMask.rend());
    
    int minCost = 0;
    for (int i = 0; i < n; ++i) {
        minCost += sortedCost[i] * sortedMask[i];
    }
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operations.
> - **Space Complexity:** $O(n)$ for the sorted arrays.
> - **Optimality proof:** This approach is optimal because it minimizes the sum of products by ensuring that the smallest costs are always multiplied by the largest masks, which is the most efficient way to reduce the total cost.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of permutations and sorting to solve optimization problems.
- Problem-solving patterns identified include the application of greedy algorithms for minimizing costs.
- Optimization techniques learned include the importance of aligning costs and benefits (or penalties) in an optimal manner.
- Similar problems to practice include other optimization problems that involve permutations or sorting.

**Mistakes to Avoid:**
- Common implementation errors include incorrect sorting or permutation generation.
- Edge cases to watch for include arrays with duplicate elements or arrays of length 1.
- Performance pitfalls include using inefficient algorithms (like the brute force approach) for large inputs.
- Testing considerations include verifying the solution with various input sizes and edge cases.