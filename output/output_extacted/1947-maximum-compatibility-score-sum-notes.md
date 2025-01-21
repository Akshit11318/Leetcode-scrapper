## Maximum Compatibility Score Sum
**Problem Link:** https://leetcode.com/problems/maximum-compatibility-score-sum/description

**Problem Statement:**
- Input format and constraints: The input consists of two parameters: `students` and `mentors`. `students` is a 2D vector where each inner vector represents a student's preferences for mentors, and `mentors` is a 2D vector where each inner vector represents a mentor's preferences for students. Both `students` and `mentors` have the same number of inner vectors, and each inner vector has the same length.
- Expected output format: The function should return the maximum compatibility score sum that can be achieved by matching students with mentors.
- Key requirements and edge cases to consider: The function should handle cases where the number of students or mentors is 0, and it should also handle cases where the preferences of students and mentors are not mutually exclusive.
- Example test cases with explanations:
    - Example 1:
        - Input: `students = [[1,2,3],[3,2,1],[2,1,3]]`, `mentors = [[1,2,3],[3,2,1],[2,1,3]]`
        - Output: 8
        - Explanation: The maximum compatibility score sum can be achieved by matching the first student with the first mentor, the second student with the second mentor, and the third student with the third mentor.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible permutations of mentor assignments for the students and calculating the compatibility score sum for each permutation.
- Step-by-step breakdown of the solution:
    1. Generate all possible permutations of mentor assignments for the students.
    2. For each permutation, calculate the compatibility score sum by iterating over the students and mentors and checking their preferences.
    3. Keep track of the maximum compatibility score sum found so far.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it has a high time complexity due to the generation of all possible permutations.

```cpp
#include <vector>
#include <algorithm>

int maxCompatibilitySum(std::vector<std::vector<int>>& students, std::vector<std::vector<int>>& mentors) {
    int n = students.size();
    int maxScore = 0;
    std::vector<int> mentorAssignments(n);
    for (int i = 0; i < n; i++) {
        mentorAssignments[i] = i;
    }

    do {
        int score = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < students[i].size(); j++) {
                if (mentors[mentorAssignments[i]][j] == students[i][j]) {
                    score++;
                }
            }
        }
        maxScore = std::max(maxScore, score);
    } while (std::next_permutation(mentorAssignments.begin(), mentorAssignments.end()));

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the number of students. This is because we generate all possible permutations of mentor assignments, which has a time complexity of $O(n!)$, and for each permutation, we calculate the compatibility score sum, which has a time complexity of $O(n^2)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we need to store the mentor assignments for each student.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible permutations of mentor assignments, which has an exponential time complexity. The space complexity occurs because we need to store the mentor assignments for each student.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a backtracking approach to find the maximum compatibility score sum. We can use a recursive function to try all possible mentor assignments for each student and keep track of the maximum score found so far.
- Detailed breakdown of the approach:
    1. Initialize a variable to store the maximum score found so far.
    2. Define a recursive function that takes the current student index and the current score as parameters.
    3. In the recursive function, try all possible mentor assignments for the current student and recursively call the function for the next student.
    4. Update the maximum score found so far if a higher score is found.
- Proof of optimality: The backtracking approach is optimal because it tries all possible mentor assignments for each student and keeps track of the maximum score found so far. This ensures that we find the maximum compatibility score sum.

```cpp
#include <vector>

int maxCompatibilitySum(std::vector<std::vector<int>>& students, std::vector<std::vector<int>>& mentors) {
    int n = students.size();
    int maxScore = 0;
    std::vector<bool> usedMentors(n, false);

    function<void(int, int)> backtrack = [&](int studentIndex, int currentScore) {
        if (studentIndex == n) {
            maxScore = std::max(maxScore, currentScore);
            return;
        }

        for (int mentorIndex = 0; mentorIndex < n; mentorIndex++) {
            if (!usedMentors[mentorIndex]) {
                int score = currentScore;
                for (int i = 0; i < students[studentIndex].size(); i++) {
                    if (mentors[mentorIndex][i] == students[studentIndex][i]) {
                        score++;
                    }
                }
                usedMentors[mentorIndex] = true;
                backtrack(studentIndex + 1, score);
                usedMentors[mentorIndex] = false;
            }
        }
    };

    backtrack(0, 0);
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the number of students. This is because we try all possible mentor assignments for each student, which has a time complexity of $O(n!)$, and for each assignment, we calculate the compatibility score sum, which has a time complexity of $O(n^2)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we need to store the used mentor assignments for each student.
> - **Optimality proof:** The backtracking approach is optimal because it tries all possible mentor assignments for each student and keeps track of the maximum score found so far. This ensures that we find the maximum compatibility score sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and permutation generation.
- Problem-solving patterns identified: Trying all possible solutions and keeping track of the best solution found so far.
- Optimization techniques learned: Using a recursive function to try all possible mentor assignments for each student.
- Similar problems to practice: Other problems that involve trying all possible solutions and keeping track of the best solution found so far.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not handling edge cases correctly, and not using the correct data structures.
- Edge cases to watch for: Cases where the number of students or mentors is 0, and cases where the preferences of students and mentors are not mutually exclusive.
- Performance pitfalls: Using an inefficient algorithm or data structure, which can lead to high time or space complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure that it works correctly and efficiently.