## The Change in Global Rankings
**Problem Link:** https://leetcode.com/problems/the-change-in-global-rankings/description

**Problem Statement:**
- Input format: A table `scores` containing `id`, `score`, and `country_id`.
- Constraints: The table contains at least one row.
- Expected output format: A table with the same columns as the input, but with the global rankings updated based on the score.
- Key requirements and edge cases to consider: Handling ties in scores, and ensuring that the global ranking is updated correctly.
- Example test cases with explanations:
  - Test case 1: A simple table with no ties.
  - Test case 2: A table with ties in scores.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the table by score in descending order, then assign a global ranking to each row based on its position in the sorted table.
- Step-by-step breakdown of the solution:
  1. Sort the table by score in descending order.
  2. Initialize a variable to keep track of the current ranking.
  3. Iterate over the sorted table, assigning the current ranking to each row.
  4. If a row has the same score as the previous row, assign the same ranking.
- Why this approach comes to mind first: It is a straightforward solution that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Score {
    int id;
    int score;
    int country_id;
    int global_ranking;
};

bool compareScores(const Score& a, const Score& b) {
    return a.score > b.score;
}

void updateGlobalRankings(std::vector<Score>& scores) {
    // Sort the scores in descending order
    std::sort(scores.begin(), scores.end(), compareScores);

    int currentRanking = 1;
    int previousScore = scores[0].score;

    for (int i = 0; i < scores.size(); i++) {
        if (i > 0 && scores[i].score != previousScore) {
            currentRanking = i + 1;
        }
        scores[i].global_ranking = currentRanking;
        previousScore = scores[i].score;
    }
}

int main() {
    // Example usage
    std::vector<Score> scores = {{1, 100, 1}, {2, 80, 1}, {3, 90, 2}, {4, 70, 2}, {5, 80, 3}};
    updateGlobalRankings(scores);

    for (const auto& score : scores) {
        std::cout << "ID: " << score.id << ", Score: " << score.score << ", Country ID: " << score.country_id << ", Global Ranking: " << score.global_ranking << std::endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the table.
> - **Space Complexity:** $O(n)$ for the sorting operation, where $n$ is the number of rows in the table.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to the extra memory required for the sorting operation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a single pass over the data to calculate the global rankings, avoiding the need for sorting.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the current ranking and the previous score.
  2. Iterate over the table, assigning the current ranking to each row based on its score.
  3. If a row has the same score as the previous row, assign the same ranking.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal for this problem since we must examine each row at least once.
- Why further optimization is impossible: We must examine each row at least once to calculate the global rankings, so a time complexity of $O(n)$ is the best we can achieve.

```cpp
#include <iostream>
#include <vector>

struct Score {
    int id;
    int score;
    int country_id;
    int global_ranking;
};

void updateGlobalRankings(std::vector<Score>& scores) {
    int currentRanking = 1;
    int previousScore = -1;

    for (int i = 0; i < scores.size(); i++) {
        if (scores[i].score != previousScore) {
            currentRanking = i + 1;
        }
        scores[i].global_ranking = currentRanking;
        previousScore = scores[i].score;
    }
}

int main() {
    // Example usage
    std::vector<Score> scores = {{1, 100, 1}, {2, 80, 1}, {3, 90, 2}, {4, 70, 2}, {5, 80, 3}};
    std::sort(scores.begin(), scores.end(), [](const Score& a, const Score& b) { return a.score > b.score; });
    updateGlobalRankings(scores);

    for (const auto& score : scores) {
        std::cout << "ID: " << score.id << ", Score: " << score.score << ", Country ID: " << score.country_id << ", Global Ranking: " << score.global_ranking << std::endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the table.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output, since we only use a constant amount of extra memory.
> - **Optimality proof:** This approach has a time complexity of $O(n \log n)$ due to the sorting, but we can't do better than $O(n)$ for the ranking calculation. However, we must sort the data first to ensure the rankings are correct.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and ranking calculation.
- Problem-solving patterns identified: Using a single pass over the data to calculate the global rankings.
- Optimization techniques learned: Avoiding unnecessary sorting operations.
- Similar problems to practice: Other ranking and sorting problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle ties in scores, or using an incorrect sorting algorithm.
- Edge cases to watch for: Handling empty tables, or tables with duplicate scores.
- Performance pitfalls: Using inefficient sorting algorithms, or iterating over the data multiple times.
- Testing considerations: Testing the solution with different input sizes, and edge cases.