## Reward Top K Students
**Problem Link:** https://leetcode.com/problems/reward-top-k-students/description

**Problem Statement:**
- Input format and constraints: Given a list of strings `positive_feedback` and `negative_feedback`, and a list of integers `report`, and an integer `k`, return the top k students with the highest score.
- Expected output format: A list of integers representing the top k students.
- Key requirements and edge cases to consider: The score is calculated based on the number of positive and negative feedbacks, and the top k students should be returned in descending order of their scores.
- Example test cases with explanations:
  - If `positive_feedback = ["smart", "brilliant", "excellent"]`, `negative_feedback = ["not"]`, `report = ["This student is not smart.", "This student is brilliant."`, and `k = 1`, then the output should be `[1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to calculate the score for each student based on the positive and negative feedbacks in their report.
- Step-by-step breakdown of the solution:
  1. Iterate over each report and calculate the score by checking the number of positive and negative feedbacks.
  2. Store the scores in a map with the student index as the key.
  3. Sort the map based on the scores in descending order.
  4. Return the top k students with the highest scores.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem by iterating over each report and calculating the score.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, int k) {
    map<int, int> scores;
    for (int i = 0; i < report.size(); i++) {
        int score = 0;
        for (const auto& feedback : positive_feedback) {
            if (report[i].find(feedback) != string::npos) {
                score++;
            }
        }
        for (const auto& feedback : negative_feedback) {
            if (report[i].find(feedback) != string::npos) {
                score--;
            }
        }
        scores[i] = score;
    }
    vector<pair<int, int>> sorted_scores;
    for (const auto& score : scores) {
        sorted_scores.push_back(score);
    }
    sort(sorted_scores.begin(), sorted_scores.end(), [](const auto& a, const auto& b) {
        return a.second > b.second || (a.second == b.second && a.first < b.first);
    });
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(sorted_scores[i].first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot p)$, where $n$ is the number of reports, $m$ is the number of positive feedbacks, and $p$ is the number of negative feedbacks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of reports.
> - **Why these complexities occur:** The time complexity is due to the iteration over each report and the feedbacks, and the space complexity is due to the storage of the scores in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a similar approach as the brute force, but with some optimizations to reduce the time complexity.
- Detailed breakdown of the approach:
  1. Iterate over each report and calculate the score by checking the number of positive and negative feedbacks.
  2. Store the scores in a vector of pairs with the student index as the first element and the score as the second element.
  3. Sort the vector based on the scores in descending order.
  4. Return the top k students with the highest scores.
- Proof of optimality: The time complexity of the optimal solution is $O(n \cdot (m + p) + n \log n)$, which is optimal because it is necessary to iterate over each report and feedback, and to sort the scores.

```cpp
vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, int k) {
    vector<pair<int, int>> scores;
    for (int i = 0; i < report.size(); i++) {
        int score = 0;
        for (const auto& feedback : positive_feedback) {
            if (report[i].find(feedback) != string::npos) {
                score++;
            }
        }
        for (const auto& feedback : negative_feedback) {
            if (report[i].find(feedback) != string::npos) {
                score--;
            }
        }
        scores.push_back({i, score});
    }
    sort(scores.begin(), scores.end(), [](const auto& a, const auto& b) {
        return a.second > b.second || (a.second == b.second && a.first < b.first);
    });
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(scores[i].first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (m + p) + n \log n)$, where $n$ is the number of reports, $m$ is the number of positive feedbacks, and $p$ is the number of negative feedbacks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of reports.
> - **Optimality proof:** The time complexity is optimal because it is necessary to iterate over each report and feedback, and to sort the scores.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, iteration, and string searching.
- Problem-solving patterns identified: calculating scores based on feedbacks and sorting them to find the top k students.
- Optimization techniques learned: reducing the time complexity by using a vector of pairs and sorting it.
- Similar problems to practice: problems involving sorting, iteration, and string searching.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as empty reports or feedbacks.
- Edge cases to watch for: reports or feedbacks with special characters, and reports with multiple feedbacks.
- Performance pitfalls: using inefficient data structures or algorithms, such as using a map to store the scores and then sorting it.
- Testing considerations: testing the solution with different inputs, such as empty reports or feedbacks, and reports with multiple feedbacks.