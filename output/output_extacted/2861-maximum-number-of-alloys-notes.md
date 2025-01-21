## Maximum Number of Alloys

**Problem Link:** https://leetcode.com/problems/maximum-number-of-alloys/description

**Problem Statement:**
- Input format: An integer array `recyclable` and an integer `k`.
- Constraints: `1 <= recyclable.length <= 5 * 10^4`, `1 <= k <= 5 * 10^4`.
- Expected output format: The maximum number of alloys that can be obtained.
- Key requirements and edge cases to consider: Ensure that the total number of alloys does not exceed `k`.
- Example test cases with explanations:
  - For `recyclable = [9, 4, 2]` and `k = 5`, the maximum number of alloys that can be obtained is `2`.
  - For `recyclable = [4, 2, 7, 6, 9]` and `k = 5`, the maximum number of alloys that can be obtained is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of recyclable alloys and calculate the total number of alloys for each combination.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store all combinations of recyclable alloys.
  2. Use a recursive function to generate all possible combinations of recyclable alloys.
  3. For each combination, calculate the total number of alloys by summing up the weights of the alloys in the combination.
  4. Check if the total number of alloys does not exceed `k`.
  5. Keep track of the maximum number of alloys that can be obtained.
- Why this approach comes to mind first: It is a straightforward approach that ensures all possible combinations are considered.

```cpp
#include <iostream>
#include <vector>

using namespace std;

void generateCombinations(vector<int>& recyclable, int index, vector<int>& currentCombination, int k, int& maxAlloys) {
    if (index == recyclable.size()) {
        int totalAlloys = 0;
        for (int alloy : currentCombination) {
            totalAlloys += alloy;
        }
        if (totalAlloys <= k && currentCombination.size() > maxAlloys) {
            maxAlloys = currentCombination.size();
        }
        return;
    }

    // Include the current alloy in the combination
    currentCombination.push_back(recyclable[index]);
    generateCombinations(recyclable, index + 1, currentCombination, k, maxAlloys);
    currentCombination.pop_back();

    // Exclude the current alloy from the combination
    generateCombinations(recyclable, index + 1, currentCombination, k, maxAlloys);
}

int maximumAlloys(vector<int>& recyclable, int k) {
    int maxAlloys = 0;
    vector<int> currentCombination;
    generateCombinations(recyclable, 0, currentCombination, k, maxAlloys);
    return maxAlloys;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of recyclable alloys. This is because we generate all possible combinations of recyclable alloys.
> - **Space Complexity:** $O(n)$, where $n$ is the number of recyclable alloys. This is because we use a recursive function to generate all possible combinations.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of recyclable alloys, which results in exponential time complexity. The space complexity is linear due to the recursive function call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the maximum number of alloys that can be obtained for each possible total weight.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size `k + 1`, where `dp[i]` represents the maximum number of alloys that can be obtained with a total weight of `i`.
  2. Iterate over each recyclable alloy and update the dynamic programming table accordingly.
  3. For each alloy, iterate from `k` down to the weight of the alloy and update `dp[i]` to be the maximum of its current value and `dp[i - alloy] + 1`.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of recyclable alloys and store the maximum number of alloys that can be obtained for each possible total weight.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(nk)$, which is the best possible time complexity for this problem.

```cpp
int maximumAlloys(vector<int>& recyclable, int k) {
    vector<int> dp(k + 1, 0);
    for (int alloy : recyclable) {
        for (int i = k; i >= alloy; i--) {
            dp[i] = max(dp[i], dp[i - alloy] + 1);
        }
    }
    return dp[k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of recyclable alloys and $k$ is the maximum total weight.
> - **Space Complexity:** $O(k)$, where $k$ is the maximum total weight.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of recyclable alloys and store the maximum number of alloys that can be obtained for each possible total weight.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive functions.
- Problem-solving patterns identified: Using dynamic programming to store the maximum number of alloys that can be obtained for each possible total weight.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to polynomial.
- Similar problems to practice: 0/1 Knapsack Problem, Subset Sum Problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not updating the dynamic programming table correctly.
- Edge cases to watch for: Handling cases where the total weight exceeds `k`, handling cases where the number of recyclable alloys is zero.
- Performance pitfalls: Using a brute force approach that generates all possible combinations of recyclable alloys, resulting in exponential time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.