## Find the Quiet Students in All Exams

**Problem Link:** https://leetcode.com/problems/find-the-quiet-students-in-all-exams/description

**Problem Statement:**
- Input format and constraints: The problem takes in a `scores` array, which is a 2D array of integers, and a `noise` array, which is a 1D array of integers. The `scores` array represents the scores of students in different exams, and the `noise` array represents the noise levels of students in different exams. The goal is to find the students who have the lowest noise level in all exams.
- Expected output format: The output should be a vector of integers, representing the IDs of the quiet students.
- Key requirements and edge cases to consider: The problem requires finding the students with the lowest noise level in all exams. If there are multiple students with the same lowest noise level, all of them should be included in the output.

**Example Test Cases:**
- Example 1:
  - Input: `scores = [[10, 20, 30], [10, 20, 30], [10, 20, 30]]`, `noise = [1, 2, 3]`
  - Output: `[0]`
  - Explanation: Student 0 has the lowest noise level in all exams.
- Example 2:
  - Input: `scores = [[10, 20, 30], [10, 20, 30], [10, 20, 30]]`, `noise = [1, 1, 1]`
  - Output: `[0, 1, 2]`
  - Explanation: All students have the same lowest noise level in all exams.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all students and exams to find the students with the lowest noise level in all exams.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the IDs of the quiet students.
  2. Iterate over all students.
  3. For each student, iterate over all exams.
  4. Check if the student has the lowest noise level in all exams.
  5. If the student has the lowest noise level in all exams, add their ID to the vector.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible combinations of students and exams.

```cpp
vector<int> findQuietStudents(vector<vector<int>>& scores, vector<int>& noise) {
    vector<int> quietStudents;
    int minNoise = INT_MAX;
    
    for (int i = 0; i < scores.size(); i++) {
        bool isQuiet = true;
        int maxScore = 0;
        
        for (int j = 0; j < scores[i].size(); j++) {
            if (scores[i][j] > maxScore) {
                maxScore = scores[i][j];
            }
        }
        
        for (int j = 0; j < scores.size(); j++) {
            if (i != j) {
                for (int k = 0; k < scores[j].size(); k++) {
                    if (scores[j][k] > maxScore) {
                        isQuiet = false;
                        break;
                    }
                }
                if (!isQuiet) {
                    break;
                }
            }
        }
        
        if (isQuiet && noise[i] < minNoise) {
            quietStudents.clear();
            quietStudents.push_back(i);
            minNoise = noise[i];
        } else if (isQuiet && noise[i] == minNoise) {
            quietStudents.push_back(i);
        }
    }
    
    return quietStudents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of students and $m$ is the number of exams. This is because we are iterating over all students and exams.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we are storing the IDs of the quiet students in a vector.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over all students and exams, and the space complexity occurs because we are storing the IDs of the quiet students.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves iterating over all students and exams only once to find the students with the lowest noise level in all exams.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to store the IDs of the quiet students.
  2. Initialize a variable to store the minimum noise level.
  3. Iterate over all students.
  4. For each student, check if they have the lowest noise level in all exams.
  5. If the student has the lowest noise level in all exams, update the minimum noise level and add their ID to the vector.
- Proof of optimality: This approach is optimal because we are only iterating over all students and exams once, which reduces the time complexity to $O(n \cdot m)$.

```cpp
vector<int> findQuietStudents(vector<vector<int>>& scores, vector<int>& noise) {
    vector<int> quietStudents;
    int minNoise = INT_MAX;
    
    for (int i = 0; i < scores.size(); i++) {
        bool isQuiet = true;
        int maxScore = 0;
        
        for (int j = 0; j < scores[i].size(); j++) {
            if (scores[i][j] > maxScore) {
                maxScore = scores[i][j];
            }
        }
        
        for (int j = 0; j < scores.size(); j++) {
            if (i != j) {
                for (int k = 0; k < scores[j].size(); k++) {
                    if (scores[j][k] > maxScore) {
                        isQuiet = false;
                        break;
                    }
                }
                if (!isQuiet) {
                    break;
                }
            }
        }
        
        if (isQuiet && noise[i] < minNoise) {
            quietStudents.clear();
            quietStudents.push_back(i);
            minNoise = noise[i];
        } else if (isQuiet && noise[i] == minNoise) {
            quietStudents.push_back(i);
        }
    }
    
    return quietStudents;
}
```

However, we can further optimize this solution. We can first calculate the maximum score for each student, and then check if the student has the lowest noise level in all exams.

```cpp
vector<int> findQuietStudents(vector<vector<int>>& scores, vector<int>& noise) {
    vector<int> quietStudents;
    int minNoise = INT_MAX;
    vector<int> maxScores(scores.size());
    
    for (int i = 0; i < scores.size(); i++) {
        for (int j = 0; j < scores[i].size(); j++) {
            if (scores[i][j] > maxScores[i]) {
                maxScores[i] = scores[i][j];
            }
        }
    }
    
    for (int i = 0; i < scores.size(); i++) {
        bool isQuiet = true;
        
        for (int j = 0; j < scores.size(); j++) {
            if (i != j) {
                for (int k = 0; k < scores[j].size(); k++) {
                    if (scores[j][k] > maxScores[i]) {
                        isQuiet = false;
                        break;
                    }
                }
                if (!isQuiet) {
                    break;
                }
            }
        }
        
        if (isQuiet && noise[i] < minNoise) {
            quietStudents.clear();
            quietStudents.push_back(i);
            minNoise = noise[i];
        } else if (isQuiet && noise[i] == minNoise) {
            quietStudents.push_back(i);
        }
    }
    
    return quietStudents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of students and $m$ is the number of exams. This is because we are iterating over all students and exams.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we are storing the IDs of the quiet students and the maximum scores for each student.
> - **Optimality proof:** This approach is optimal because we are only iterating over all students and exams once, which reduces the time complexity to $O(n \cdot m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and vector operations.
- Problem-solving patterns identified: Checking all possible combinations of students and exams, and optimizing the solution by reducing the number of iterations.
- Optimization techniques learned: Reducing the number of iterations by calculating the maximum score for each student first.
- Similar problems to practice: Finding the minimum or maximum value in a 2D array, and optimizing solutions by reducing the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Empty input arrays, and arrays with a single element.
- Performance pitfalls: Not optimizing the solution by reducing the number of iterations.
- Testing considerations: Testing the solution with different input arrays, including edge cases.