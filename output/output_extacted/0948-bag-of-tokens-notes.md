## Bag of Tokens
**Problem Link:** https://leetcode.com/problems/bag-of-tokens/description

**Problem Statement:**
- Input format: You are given an array of integers `tokens` and an integer `power`.
- Constraints: `1 <= tokens.length <= 1000` and `0 <= tokens[i] <= 1000`.
- Expected output format: Return the maximum number of consecutive points you can collect.
- Key requirements and edge cases to consider: You can either collect a point or use a token to increase your power.
- Example test cases with explanations:
  - Input: `tokens = [100]`, `power = 50`. Output: `0`. Explanation: You cannot collect the point because your power is less than the token value.
  - Input: `tokens = [100,200]`, `power = 150`. Output: `1`. Explanation: You can collect the first point and then use the token to increase your power.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of collecting points and using tokens to increase power.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the tokens array.
  2. For each permutation, try to collect points and use tokens to increase power.
  3. Keep track of the maximum number of consecutive points collected.
- Why this approach comes to mind first: It's a straightforward way to explore all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int bagOfTokensScore(vector<int>& tokens, int power) {
    int maxScore = 0;
    sort(tokens.begin(), tokens.end());
    for (int i = 0; i < (1 << tokens.size()); i++) {
        int currentPower = power;
        int currentScore = 0;
        for (int j = 0; j < tokens.size(); j++) {
            if ((i & (1 << j)) != 0) {
                if (currentPower >= tokens[j]) {
                    currentPower -= tokens[j];
                    currentScore++;
                } else {
                    break;
                }
            }
        }
        maxScore = max(maxScore, currentScore);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot log(n))$, where $n$ is the number of tokens. The $2^n$ term comes from generating all permutations, and the $n \cdot log(n)$ term comes from sorting the tokens array.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tokens. This is because we need to store the tokens array and the permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations of the tokens array, which leads to an exponential time complexity. The sorting step adds a $n \cdot log(n)$ term to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to collect points and use tokens to increase power.
- Detailed breakdown of the approach:
  1. Sort the tokens array in ascending order.
  2. Initialize two pointers, one at the beginning and one at the end of the tokens array.
  3. Try to collect points by moving the left pointer to the right.
  4. If we cannot collect a point, use a token to increase our power by moving the right pointer to the left.
- Proof of optimality: This approach is optimal because we always try to collect points first and only use tokens to increase our power when necessary.

```cpp
int bagOfTokensScore(vector<int>& tokens, int power) {
    sort(tokens.begin(), tokens.end());
    int maxScore = 0;
    int currentScore = 0;
    int left = 0;
    int right = tokens.size() - 1;
    while (left <= right) {
        if (power >= tokens[left]) {
            power -= tokens[left];
            currentScore++;
            left++;
            maxScore = max(maxScore, currentScore);
        } else if (currentScore > 0) {
            power += tokens[right];
            currentScore--;
            right--;
        } else {
            break;
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$, where $n$ is the number of tokens. The $n \cdot log(n)$ term comes from sorting the tokens array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store the pointers and the current score.
> - **Optimality proof:** This approach is optimal because we always try to collect points first and only use tokens to increase our power when necessary. This ensures that we maximize the number of consecutive points collected.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting, and two-pointer technique.
- Problem-solving patterns identified: Using a greedy approach to solve optimization problems.
- Optimization techniques learned: Using a two-pointer technique to reduce the search space.
- Similar problems to practice: Other problems that involve using a greedy approach to solve optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the tokens array or not using a two-pointer technique.
- Edge cases to watch for: Handling the case where the power is less than the token value.
- Performance pitfalls: Using a brute force approach that generates all permutations of the tokens array.
- Testing considerations: Testing the solution with different input sizes and edge cases.