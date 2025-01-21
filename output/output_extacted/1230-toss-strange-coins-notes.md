## Toss Strange Coins

**Problem Link:** https://leetcode.com/problems/toss-strange-coins/description

**Problem Statement:**
- Input format and constraints: You are given an array of integers representing the probability of getting heads when tossing each coin. The goal is to find the maximum probability of getting heads when tossing the coins in a specific order.
- Expected output format: The output should be a floating-point number representing the maximum probability of getting heads.
- Key requirements and edge cases to consider: The input array can contain any number of coins, and the probabilities can range from 0 to 1.
- Example test cases with explanations:
  - For the input `[0.5, 0.5, 0.5]`, the output should be `0.5`, because the maximum probability of getting heads is when we toss the coins in the order that gives us the highest probability of getting heads.
  - For the input `[0.4, 0.6, 0.7]`, the output should be `0.7`, because the maximum probability of getting heads is when we toss the coins in the order that gives us the highest probability of getting heads.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible orders of tossing the coins and calculate the probability of getting heads for each order.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the coins.
  2. For each permutation, calculate the probability of getting heads by multiplying the probabilities of getting heads for each coin in the permutation.
  3. Keep track of the maximum probability of getting heads found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it has to try all possible orders of tossing the coins.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

double maxProbability(std::vector<double>& prob) {
    int n = prob.size();
    double max_prob = 0.0;
    std::vector<int> indices(n);
    for (int i = 0; i < n; i++) {
        indices[i] = i;
    }

    do {
        double prob_product = 1.0;
        for (int i = 0; i < n; i++) {
            prob_product *= prob[indices[i]];
        }
        max_prob = std::max(max_prob, prob_product);
    } while (std::next_permutation(indices.begin(), indices.end()));

    return max_prob;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!) = O(1 \cdot 2 \cdot 3 \cdot ... \cdot n)$, where $n$ is the number of coins. This is because we are generating all permutations of the coins, and there are $n!$ permutations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of coins. This is because we need to store the indices of the coins in the permutation.
> - **Why these complexities occur:** The time complexity occurs because we are generating all permutations of the coins, and the space complexity occurs because we need to store the indices of the coins in the permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that the maximum probability of getting heads is achieved by always choosing the coin with the highest probability of getting heads.
- Detailed breakdown of the approach:
  1. Sort the coins in descending order of their probabilities of getting heads.
  2. Calculate the probability of getting heads by multiplying the probabilities of getting heads for each coin in the sorted order.
- Proof of optimality: This approach is optimal because it always chooses the coin with the highest probability of getting heads, which maximizes the overall probability of getting heads.
- Why further optimization is impossible: Further optimization is impossible because we are already choosing the coin with the highest probability of getting heads at each step.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

double maxProbability(std::vector<double>& prob) {
    std::sort(prob.rbegin(), prob.rend());
    double prob_product = 1.0;
    for (double p : prob) {
        prob_product *= p;
    }
    return prob_product;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n) = O(n \cdot (\log n + \log (n-1) + ... + \log 1))$, where $n$ is the number of coins. This is because we are sorting the coins in descending order of their probabilities of getting heads.
> - **Space Complexity:** $O(1)$, where $n$ is the number of coins. This is because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it always chooses the coin with the highest probability of getting heads, which maximizes the overall probability of getting heads.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key concept demonstrated is the use of sorting to optimize the solution.
- Problem-solving patterns identified: The pattern identified is the use of a greedy approach to solve the problem.
- Optimization techniques learned: The technique learned is the use of sorting to reduce the time complexity of the solution.
- Similar problems to practice: Similar problems to practice include other problems that involve sorting and greedy approaches.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the probability product to 1.0.
- Edge cases to watch for: An edge case to watch for is when the input array is empty.
- Performance pitfalls: A performance pitfall is to use a naive approach that tries all possible orders of tossing the coins.
- Testing considerations: A testing consideration is to test the solution with different input arrays and edge cases.