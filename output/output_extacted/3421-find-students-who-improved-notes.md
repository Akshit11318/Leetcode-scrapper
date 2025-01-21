## Find Students Who Improved

**Problem Link:** https://leetcode.com/problems/find-students-who-improved/description

**Problem Statement:**
- Input format and constraints: Given two tables, `scores` and `students`, where `scores` has columns `id`, `student_id`, `subject`, and `score`, and `students` has columns `id`, `name`, `grade`, and `class`. The task is to find the students who improved their score in a specific subject.
- Expected output format: A list of student IDs and names who improved their score in the specified subject.
- Key requirements and edge cases to consider: 
    - There may be multiple scores for the same student in the same subject.
    - There may be students with no scores in the specified subject.
    - The subject may not exist in the scores table.
- Example test cases with explanations:
    - Test case 1: A student has two scores in the same subject, and the second score is higher.
    - Test case 2: A student has no scores in the specified subject.
    - Test case 3: The subject does not exist in the scores table.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the students who improved their score in a specific subject, we need to compare each student's scores in that subject.
- Step-by-step breakdown of the solution:
    1. Get all scores for each student in the specified subject.
    2. Sort the scores in ascending order of date.
    3. Compare each score with the previous one to check if the score has improved.
    4. If the score has improved, add the student to the result list.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct Score {
    int id;
    int student_id;
    std::string subject;
    int score;
};

struct Student {
    int id;
    std::string name;
};

std::vector<std::pair<int, std::string>> findImprovedStudents(std::vector<Score>& scores, std::vector<Student>& students, std::string subject) {
    std::map<int, std::vector<Score>> studentScores;
    for (const auto& score : scores) {
        if (score.subject == subject) {
            studentScores[score.student_id].push_back(score);
        }
    }

    std::vector<std::pair<int, std::string>> improvedStudents;
    for (const auto& student : students) {
        if (studentScores.find(student.id) != studentScores.end()) {
            std::vector<Score>& scores = studentScores[student.id];
            std::sort(scores.begin(), scores.end(), [](const Score& a, const Score& b) {
                return a.id < b.id;
            });

            for (int i = 1; i < scores.size(); i++) {
                if (scores[i].score > scores[i - 1].score) {
                    improvedStudents.push_back({student.id, student.name});
                    break;
                }
            }
        }
    }

    return improvedStudents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m)$, where $n$ is the number of scores and $m$ is the number of students. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of scores and $m$ is the number of students. We need to store all scores and students in memory.
> - **Why these complexities occur:** The sorting operation causes the time complexity to be $O(n \log n)$, and the space complexity is $O(n + m)$ because we need to store all scores and students.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the scores table to find the students who improved their score.
- Detailed breakdown of the approach:
    1. Create a map to store the maximum score for each student in the specified subject.
    2. Iterate through the scores table and update the maximum score for each student.
    3. If a student's score is greater than their previous maximum score, add the student to the result list.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal because we need to iterate through the scores table at least once.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct Score {
    int id;
    int student_id;
    std::string subject;
    int score;
};

struct Student {
    int id;
    std::string name;
};

std::vector<std::pair<int, std::string>> findImprovedStudents(std::vector<Score>& scores, std::vector<Student>& students, std::string subject) {
    std::map<int, int> studentMaxScores;
    std::map<int, bool> improvedStudents;

    for (const auto& score : scores) {
        if (score.subject == subject) {
            if (studentMaxScores.find(score.student_id) == studentMaxScores.end() || score.score > studentMaxScores[score.student_id]) {
                studentMaxScores[score.student_id] = score.score;
                if (studentMaxScores[score.student_id] > score.score) {
                    improvedStudents[score.student_id] = true;
                }
            }
        }
    }

    std::vector<std::pair<int, std::string>> result;
    for (const auto& student : students) {
        if (improvedStudents.find(student.id) != improvedStudents.end()) {
            result.push_back({student.id, student.name});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of scores and $m$ is the number of students. We iterate through the scores table and students table once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of scores and $m$ is the number of students. We need to store the maximum score for each student and the improved students.
> - **Optimality proof:** This approach is optimal because we need to iterate through the scores table and students table at least once to find the students who improved their score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and map usage.
- Problem-solving patterns identified: Finding the maximum score for each student and checking for improvement.
- Optimization techniques learned: Using a single pass through the scores table and storing the maximum score for each student.
- Similar problems to practice: Finding the top-scoring students in a subject, finding the students with the highest average score.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of a subject in the scores table, not handling the case where a student has no scores in the specified subject.
- Edge cases to watch for: A student having multiple scores in the same subject, a student having no scores in the specified subject.
- Performance pitfalls: Using a brute force approach with a high time complexity, not optimizing the solution for large inputs.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.