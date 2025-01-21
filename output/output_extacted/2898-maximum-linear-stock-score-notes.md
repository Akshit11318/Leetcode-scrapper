## Maximum Linear Stock Score

**Problem Link:** https://leetcode.com/problems/maximum-linear-stock-score/description

**Problem Statement:**
- Input format and constraints: Given a list of integers representing stock prices, and a list of integers representing the number of days to wait before buying or selling the stock.
- Expected output format: The maximum possible score that can be achieved.
- Key requirements and edge cases to consider: The score is calculated by multiplying the price of the stock by the number of days to wait before buying or selling it. The goal is to maximize this score.
- Example test cases with explanations: 
    - For example, if the stock prices are [1, 2, 3, 4, 5] and the number of days to wait are [1, 2, 3, 4, 5], the maximum score can be achieved by buying the stock on the first day and selling it on the last day.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of buying and selling the stock, and calculate the score for each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of buying and selling the stock.
    2. For each combination, calculate the score by multiplying the price of the stock by the number of days to wait before buying or selling it.
    3. Keep track of the maximum score achieved so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& prices, std::vector<int>& days) {
    int max_score = 0;
    for (int i = 0; i < prices.size(); i++) {
        for (int j = i + 1; j < prices.size(); j++) {
            int score = prices[j] * days[i];
            max_score = std::max(max_score, score);
        }
    }
    return max_score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of days. This is because we are generating all possible combinations of buying and selling the stock, which takes quadratic time.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum score.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible combinations of buying and selling the stock, which results in quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the data to find the maximum score.
- Detailed breakdown of the approach:
    1. Initialize the maximum score to negative infinity.
    2. Iterate through the prices and days, and for each pair, calculate the score by multiplying the price by the day.
    3. Update the maximum score if the current score is higher.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data, and it keeps track of the maximum score achieved so far.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass through the data.

```cpp
int maxScore(std::vector<int>& prices, std::vector<int>& days) {
    int max_score = 0;
    for (int i = 0; i < prices.size(); i++) {
        int score = prices[i] * days[i];
        max_score = std::max(max_score, score);
    }
    return max_score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of days. This is because we are only making a single pass through the data.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum score.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the data, and it keeps track of the maximum score achieved so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of using a single pass through the data to find the maximum score.
- Problem-solving patterns identified: Using a single pass through the data to find the maximum score is a common pattern in algorithmic problems.
- Optimization techniques learned: Avoiding unnecessary iterations and using a single pass through the data can significantly improve the efficiency of an algorithm.
- Similar problems to practice: Other problems that involve finding the maximum score or value, such as the "Maximum Subarray" problem.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize the maximum score to negative infinity, or failing to update the maximum score correctly.
- Edge cases to watch for: Handling cases where the input data is empty or contains negative values.
- Performance pitfalls: Using unnecessary iterations or failing to use a single pass through the data.
- Testing considerations: Testing the algorithm with different input data, including edge cases and large inputs.