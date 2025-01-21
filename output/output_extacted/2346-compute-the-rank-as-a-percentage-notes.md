## Compute the Rank as a Percentage
**Problem Link:** https://leetcode.com/problems/compute-the-rank-as-a-percentage/description

**Problem Statement:**
- Input: A table `Scores` with columns `id` and `score`.
- Constraints: The table may contain duplicate scores.
- Expected output: A table with columns `id` and `rank`, where `rank` is the percentage rank of the score.
- Key requirements: Calculate the rank as a percentage, considering duplicate scores.
- Example test cases:
  - Input: `Scores` table with scores 10, 20, 30, 20, 10.
  - Output: The corresponding percentage ranks.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the scores and calculate the rank of each score.
- Step-by-step breakdown:
  1. Sort the scores in descending order.
  2. Calculate the rank of each score by finding its position in the sorted list.
  3. Handle duplicate scores by assigning the same rank to all occurrences.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Score {
    int id;
    int score;
};

bool compareScores(const Score& a, const Score& b) {
    return a.score > b.score;
}

std::vector<double> calculateRanks(std::vector<Score>& scores) {
    std::sort(scores.begin(), scores.end(), compareScores);
    int n = scores.size();
    std::vector<double> ranks(n);
    double rank = 1.0;
    for (int i = 0; i < n; i++) {
        if (i > 0 && scores[i].score != scores[i - 1].score) {
            rank = (i + 1.0) / n * 100;
        }
        ranks[i] = rank;
    }
    return ranks;
}

int main() {
    std::vector<Score> scores = {{1, 10}, {2, 20}, {3, 30}, {4, 20}, {5, 10}};
    std::vector<double> ranks = calculateRanks(scores);
    for (int i = 0; i < scores.size(); i++) {
        std::cout << "id: " << scores[i].id << ", score: " << scores[i].score << ", rank: " << ranks[i] << "%" << std::endl;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for the output vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the output vector contributes to the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use the `DENSE_RANK` function in SQL to calculate the rank as a percentage.
- Detailed breakdown:
  1. Use the `DENSE_RANK` function to assign a unique rank to each distinct score.
  2. Calculate the percentage rank by dividing the rank by the total number of distinct scores and multiplying by 100.
- Proof of optimality: This approach is optimal because it uses a single SQL query to calculate the rank as a percentage.

```cpp
SELECT id, score,
       (DENSE_RANK() OVER (ORDER BY score DESC) * 100.0) / COUNT(DISTINCT score) OVER () AS percentage_rank
FROM Scores
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for the output.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to calculate the rank as a percentage, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: sorting, ranking, and percentage calculation.
- Problem-solving patterns: using SQL queries to solve problems.
- Optimization techniques: minimizing the number of operations required.

**Mistakes to Avoid:**
- Common implementation errors: not handling duplicate scores correctly.
- Edge cases to watch for: empty input tables or tables with a single row.
- Performance pitfalls: using inefficient algorithms or queries.
- Testing considerations: testing the solution with different input tables and edge cases.