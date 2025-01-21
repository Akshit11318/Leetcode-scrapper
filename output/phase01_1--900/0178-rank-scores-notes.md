## Rank Scores

**Problem Link:** https://leetcode.com/problems/rank-scores/description

**Problem Statement:**
- Input format: A table `Scores` with two columns: `id` (integer) and `score` (integer).
- Constraints: The table contains at least one row and at most 10^5 rows. The `id` is unique, and the `score` is an integer between 1 and 10^7.
- Expected output format: A table with the same columns as the input, plus a new column `rank` which represents the rank of each score.
- Key requirements and edge cases to consider: The ranking should be done in descending order of scores. If two scores are the same, they should have the same rank, and the next lower score should have a rank that is one more than the number of scores that have the same rank.
- Example test cases with explanations: 
    - For the input `Scores` table with rows (1, 100), (2, 80), (3, 90), (4, 80), the output should be (1, 100, 1), (3, 90, 2), (2, 80, 3), (4, 80, 3).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can first sort the scores in descending order. Then, we can iterate over the sorted scores and assign a rank to each score.
- Step-by-step breakdown of the solution:
    1. Sort the scores in descending order.
    2. Initialize the rank to 1.
    3. Iterate over the sorted scores. For each score, assign the current rank to it.
    4. If the current score is different from the next score, increment the rank.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves sorting the scores and then iterating over them to assign ranks.

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

std::vector<Score> rankScores(std::vector<Score>& scores) {
    std::sort(scores.begin(), scores.end(), compareScores);
    std::vector<Score> result;
    int rank = 1;
    for (int i = 0; i < scores.size(); i++) {
        scores[i].rank = rank;
        if (i < scores.size() - 1 && scores[i].score != scores[i + 1].score) {
            rank++;
        }
        result.push_back(scores[i]);
    }
    return result;
}

int main() {
    std::vector<Score> scores = {{1, 100}, {2, 80}, {3, 90}, {4, 80}};
    std::vector<Score> result = rankScores(scores);
    for (const auto& score : result) {
        std::cout << "id: " << score.id << ", score: " << score.score << ", rank: " << score.rank << std::endl;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of rows in the input table.
> - **Space Complexity:** $O(n)$ for storing the sorted scores.
> - **Why these complexities occur:** The sorting step dominates the time complexity, and the space complexity is due to the need to store the sorted scores.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the `DENSE_RANK` function in SQL to achieve the same result more efficiently.
- Detailed breakdown of the approach:
    1. Use the `DENSE_RANK` function to assign a rank to each score based on its value.
    2. The `DENSE_RANK` function assigns a unique rank to each distinct score, without gaps.
- Proof of optimality: This approach is optimal because it uses a built-in function that is designed specifically for ranking, which is more efficient than sorting and iterating over the scores manually.
- Why further optimization is impossible: This approach is already optimal because it uses a single SQL statement to achieve the desired result, which is more efficient than any manual iteration or sorting.

```sql
SELECT 
    id,
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the internal sorting step, where $n$ is the number of rows in the input table.
> - **Space Complexity:** $O(n)$ for storing the ranked scores.
> - **Optimality proof:** The `DENSE_RANK` function is designed specifically for ranking, which makes it more efficient than any manual iteration or sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, ranking, and using built-in functions.
- Problem-solving patterns identified: using a brute force approach to understand the problem, and then optimizing it using a more efficient approach.
- Optimization techniques learned: using built-in functions to achieve the desired result more efficiently.
- Similar problems to practice: other ranking problems, such as ranking scores with ties or ranking scores based on multiple criteria.

**Mistakes to Avoid:**
- Common implementation errors: not handling ties correctly, or not using the correct ranking function.
- Edge cases to watch for: scores with ties, or scores with gaps.
- Performance pitfalls: using a brute force approach for large datasets, or not using built-in functions when available.
- Testing considerations: testing with different input datasets, including edge cases and large datasets.