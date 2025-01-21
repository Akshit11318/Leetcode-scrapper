## Fair Candy Swap
**Problem Link:** [https://leetcode.com/problems/fair-candy-swap/description](https://leetcode.com/problems/fair-candy-swap/description)

**Problem Statement:**
- Input: Two arrays `A` and `B`, representing the number of candies Alice and Bob have, respectively.
- Constraints: Both arrays are non-empty and contain only positive integers.
- Expected Output: Find one candy from `A` and one candy from `B` such that swapping them will result in the total number of candies being equal in both arrays.
- Key Requirements:
  - Each candy can only be used once.
  - The total number of candies in both arrays after the swap must be equal.
- Edge Cases:
  - If no such swap exists, return an empty array.
  - If there are multiple possible swaps, any valid swap is acceptable.
- Example Test Cases:
  - Input: `A = [1,1]`, `B = [2,2]`
    - Output: `[1,2]`
  - Input: `A = [1,2,5]`, `B = [2,4]`
    - Output: `[5,4]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible pair of candies from `A` and `B` to see if swapping them would result in an equal total number of candies in both arrays.
- Step-by-Step Breakdown:
  1. Calculate the total number of candies in `A` and `B`.
  2. Iterate through each candy in `A` and each candy in `B`.
  3. For each pair, calculate the new totals if the candies were swapped.
  4. Check if the new totals are equal. If they are, return the pair of candies.
- Why this approach comes to mind first: It's the most straightforward method to ensure all possibilities are considered.

```cpp
vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
    int sumA = 0, sumB = 0;
    for (int a : A) sumA += a;
    for (int b : B) sumB += b;
    
    for (int a : A) {
        for (int b : B) {
            if (sumA - a + b == sumB - b + a) {
                return {a, b};
            }
        }
    }
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because we are iterating through each element in `A` for each element in `B`.
> - **Space Complexity:** $O(1)$, not including the space needed for the output, as we only use a constant amount of space to store the sums and the current elements being compared.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic in terms of the input sizes, while the space complexity remains constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of checking every possible pair, we can calculate the difference in the total number of candies between `A` and `B` and then find a pair of candies that makes up half of this difference.
- Detailed Breakdown:
  1. Calculate the total number of candies in `A` and `B`.
  2. Find the difference in the totals, which is `sumA - sumB`.
  3. To make the totals equal, we need to find a candy in `A` and a candy in `B` such that `a - b = (sumB - sumA) / 2`.
  4. We can use a set to store the elements of `A` for efficient lookup.
- Proof of Optimality: This approach ensures we find a solution if one exists, and it does so in linear time, which is optimal because we must at least read the input.

```cpp
vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
    int sumA = 0, sumB = 0;
    for (int a : A) sumA += a;
    for (int b : B) sumB += b;
    
    unordered_set<int> setA(A.begin(), A.end());
    int diff = (sumA - sumB) / 2;
    
    for (int b : B) {
        if (setA.find(b + diff) != setA.end()) {
            return {b + diff, b};
        }
    }
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because we make a single pass through each array.
> - **Space Complexity:** $O(n)$, for storing the elements of `A` in a set.
> - **Optimality Proof:** This solution is optimal because it achieves a linear time complexity, which is the best we can do since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they can be used to optimize the solution.
- Using data structures like sets for efficient lookup.
- Breaking down complex problems into simpler, manageable parts.

**Mistakes to Avoid:**
- Not considering the problem constraints and thus overlooking potential optimizations.
- Not validating the input or handling edge cases properly.
- Failing to optimize the solution, leading to inefficient algorithms.