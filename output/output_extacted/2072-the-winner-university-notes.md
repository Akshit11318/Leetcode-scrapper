## The Winner University
**Problem Link:** https://leetcode.com/problems/the-winner-university/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the university with the highest average score from a list of scores for different universities.
- Expected output format: The output should be the name of the university with the highest average score.
- Key requirements and edge cases to consider: The input list may be empty, and there may be multiple universities with the same highest average score.
- Example test cases with explanations: For example, if the input is `[["University1", 90], ["University1", 80], ["University2", 95], ["University2", 85]]`, the output should be `"University2"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through the list of scores, calculate the sum and count of scores for each university, and then calculate the average score for each university.
- Step-by-step breakdown of the solution:
  1. Create a `map` to store the sum and count of scores for each university.
  2. Iterate through the list of scores and update the sum and count for each university in the `map`.
  3. Calculate the average score for each university by dividing the sum by the count.
  4. Find the university with the highest average score.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

string winnerUniversity(vector<vector<string>>& scores) {
    map<string, pair<int, int>> universityScores;
    for (const auto& score : scores) {
        string university = score[0];
        int scoreValue = stoi(score[1]);
        if (universityScores.find(university) != universityScores.end()) {
            universityScores[university].first += scoreValue;
            universityScores[university].second++;
        } else {
            universityScores[university] = {scoreValue, 1};
        }
    }
    string winner;
    double maxAverage = 0.0;
    for (const auto& universityScore : universityScores) {
        double average = static_cast<double>(universityScore.second.first) / universityScore.second.second;
        if (average > maxAverage) {
            maxAverage = average;
            winner = universityScore.first;
        }
    }
    return winner;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of scores, because we iterate through the list of scores once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of universities, because we use a `map` to store the sum and count of scores for each university.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the list of scores once, and the space complexity is proportional to the number of universities because we use a `map` to store the sum and count of scores for each university.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, because we need to iterate through the list of scores at least once to calculate the sum and count of scores for each university.
- Detailed breakdown of the approach:
  1. Create a `map` to store the sum and count of scores for each university.
  2. Iterate through the list of scores and update the sum and count for each university in the `map`.
  3. Calculate the average score for each university by dividing the sum by the count.
  4. Find the university with the highest average score.
- Proof of optimality: This approach is optimal because we need to iterate through the list of scores at least once to calculate the sum and count of scores for each university.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate through the list of scores at least once to calculate the sum and count of scores for each university.

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

string winnerUniversity(vector<vector<string>>& scores) {
    map<string, pair<int, int>> universityScores;
    for (const auto& score : scores) {
        string university = score[0];
        int scoreValue = stoi(score[1]);
        if (universityScores.find(university) != universityScores.end()) {
            universityScores[university].first += scoreValue;
            universityScores[university].second++;
        } else {
            universityScores[university] = {scoreValue, 1};
        }
    }
    string winner;
    double maxAverage = 0.0;
    for (const auto& universityScore : universityScores) {
        double average = static_cast<double>(universityScore.second.first) / universityScore.second.second;
        if (average > maxAverage) {
            maxAverage = average;
            winner = universityScore.first;
        }
    }
    return winner;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of scores, because we iterate through the list of scores once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of universities, because we use a `map` to store the sum and count of scores for each university.
> - **Optimality proof:** This approach is optimal because we need to iterate through the list of scores at least once to calculate the sum and count of scores for each university.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, `map` data structure, average calculation.
- Problem-solving patterns identified: Calculate sum and count of scores for each university, calculate average score for each university, find university with highest average score.
- Optimization techniques learned: None, because the optimal solution is the same as the brute force approach.
- Similar problems to practice: Problems that involve calculating averages or finding maximum/minimum values.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, using incorrect data types.
- Edge cases to watch for: Empty input list, multiple universities with same highest average score.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Test with empty input list, test with multiple universities with same highest average score.