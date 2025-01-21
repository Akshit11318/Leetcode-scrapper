## Find Top Scoring Students
**Problem Link:** https://leetcode.com/problems/find-top-scoring-students/description

**Problem Statement:**
- Input format: The problem takes in `scores` (a list of integers representing the scores of each student), `preferences` (a list of lists of integers representing the preferences of each student), and `threshold` (an integer representing the threshold score).
- Expected output format: The function should return a list of integers representing the IDs of the top-scoring students.
- Key requirements and edge cases to consider: 
  - Each student has a unique ID.
  - The scores and preferences of each student are given.
  - The threshold score is given.
- Example test cases with explanations:
  - For example, given `scores = [10, 20, 30]`, `preferences = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]`, and `threshold = 10`, the function should return `[1, 3]` because students with IDs 1 and 3 have the highest scores and their preferences are the same as their scores.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the score of each student based on their preferences and the given scores, then comparing these scores to the threshold.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the scores of each student.
  2. Iterate over each student's preferences and calculate their score based on the given scores.
  3. Compare each student's score to the threshold and add their ID to the result list if their score is greater than or equal to the threshold.
  4. Sort the result list in descending order of the scores and then in ascending order of the student IDs.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
vector<int> findTopScoringStudents(vector<int>& scores, vector<vector<int>>& preferences, int threshold) {
    int n = scores.size();
    vector<int> studentScores(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (preferences[i][j] == i + 1) {
                studentScores[i] = scores[i];
                break;
            }
        }
    }
    vector<pair<int, int>> scoresWithIds;
    for (int i = 0; i < n; i++) {
        scoresWithIds.push_back({studentScores[i], i + 1});
    }
    sort(scoresWithIds.begin(), scoresWithIds.end(), [](const auto& a, const auto& b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first > b.first;
    });
    vector<int> result;
    for (auto& score : scoresWithIds) {
        if (score.first >= threshold) {
            result.push_back(score.second);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of students. This is because we iterate over each student's preferences, which can be of length $n$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we store the scores of each student in a list.
> - **Why these complexities occur:** These complexities occur because we use nested loops to calculate the score of each student and store the scores in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient data structure to store the scores and preferences of each student, such as a map or a vector of pairs.
- Detailed breakdown of the approach:
  1. Initialize an empty map to store the scores and preferences of each student.
  2. Iterate over each student's preferences and calculate their score based on the given scores.
  3. Store the score and ID of each student in the map.
  4. Sort the map in descending order of the scores and then in ascending order of the student IDs.
- Proof of optimality: This approach is optimal because we only iterate over each student's preferences once and use a efficient data structure to store the scores and preferences.

```cpp
vector<int> findTopScoringStudents(vector<int>& scores, vector<vector<int>>& preferences, int threshold) {
    int n = scores.size();
    vector<pair<int, int>> studentScores;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (preferences[i][j] == i + 1) {
                studentScores.push_back({scores[i], i + 1});
                break;
            }
        }
    }
    sort(studentScores.begin(), studentScores.end(), [](const auto& a, const auto& b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first > b.first;
    });
    vector<int> result;
    for (auto& score : studentScores) {
        if (score.first >= threshold) {
            result.push_back(score.second);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of students. This is because we iterate over each student's preferences, which can be of length $n$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we store the scores and IDs of each student in a vector.
> - **Optimality proof:** This approach is optimal because we only iterate over each student's preferences once and use a efficient data structure to store the scores and preferences.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and data structure usage.
- Problem-solving patterns identified: Using a more efficient data structure to store and retrieve data.
- Optimization techniques learned: Reducing the number of iterations and using a more efficient data structure.
- Similar problems to practice: Problems that involve sorting, iteration, and data structure usage.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases, and not using efficient data structures.
- Edge cases to watch for: Empty input, invalid input, and large input.
- Performance pitfalls: Using inefficient algorithms, not optimizing code, and not using efficient data structures.
- Testing considerations: Testing for edge cases, testing for large input, and testing for performance.