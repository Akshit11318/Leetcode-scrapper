## Number of Unique Subjects Taught by Each Teacher

**Problem Link:** https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description

**Problem Statement:**
- Input format and constraints: The input consists of two arrays, `teacher` and `subject`, where `teacher[i]` represents the teacher ID and `subject[i]` represents the subject ID that the teacher is teaching.
- Expected output format: The output should be an array where each element at index `i` represents the number of unique subjects taught by the `i-th` teacher.
- Key requirements and edge cases to consider: We need to ensure that we correctly count the unique subjects for each teacher and handle cases where a teacher may not be teaching any subjects.
- Example test cases with explanations:
  - Example 1: `teacher = [1, 2, 3], subject = [1, 2, 3]`. In this case, each teacher is teaching a unique subject, so the output should be `[1, 1, 1]`.
  - Example 2: `teacher = [1, 2, 3], subject = [1, 1, 1]`. In this case, all teachers are teaching the same subject, so the output should be `[1, 1, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the `teacher` and `subject` arrays and using a separate data structure to keep track of the unique subjects for each teacher.
- Step-by-step breakdown of the solution:
  1. Create a map to store the unique subjects for each teacher.
  2. Iterate over the `teacher` and `subject` arrays simultaneously.
  3. For each pair of teacher and subject, check if the subject is already in the map for that teacher.
  4. If the subject is not in the map, add it to the map.
  5. After iterating over all pairs, create an output array where each element at index `i` represents the number of unique subjects taught by the `i-th` teacher.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

vector<int> uniqueSubjects(int teacher[], int subject[], int n) {
    unordered_map<int, unordered_set<int>> teacherSubjects;
    for (int i = 0; i < n; i++) {
        teacherSubjects[teacher[i]].insert(subject[i]);
    }
    
    vector<int> output(n);
    for (int i = 0; i < n; i++) {
        output[i] = teacherSubjects[i + 1].size();
    }
    
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of teachers, since we iterate over the `teacher` and `subject` arrays once.
> - **Space Complexity:** $O(n)$, since we use a map to store the unique subjects for each teacher.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the input arrays once, and the space complexity occurs because we use a map to store the unique subjects for each teacher.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an unordered map to store the unique subjects for each teacher, and then use a vector to store the output.
- Detailed breakdown of the approach:
  1. Create an unordered map to store the unique subjects for each teacher.
  2. Iterate over the `teacher` and `subject` arrays simultaneously.
  3. For each pair of teacher and subject, insert the subject into the map for that teacher.
  4. Create an output vector where each element at index `i` represents the number of unique subjects taught by the `i-th` teacher.
- Proof of optimality: This approach is optimal because it uses a single pass over the input arrays and uses a map to efficiently store the unique subjects for each teacher.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the minimum required to iterate over the input arrays.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

vector<int> uniqueSubjects(int teacher[], int subject[], int n) {
    unordered_map<int, unordered_set<int>> teacherSubjects;
    for (int i = 0; i < n; i++) {
        teacherSubjects[teacher[i]].insert(subject[i]);
    }
    
    vector<int> output(n);
    for (int i = 0; i < n; i++) {
        output[i] = teacherSubjects[i + 1].size();
    }
    
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of teachers, since we iterate over the `teacher` and `subject` arrays once.
> - **Space Complexity:** $O(n)$, since we use a map to store the unique subjects for each teacher.
> - **Optimality proof:** This approach is optimal because it uses a single pass over the input arrays and uses a map to efficiently store the unique subjects for each teacher.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an unordered map to store unique subjects for each teacher.
- Problem-solving patterns identified: Using a single pass over the input arrays to efficiently solve the problem.
- Optimization techniques learned: Using a map to efficiently store the unique subjects for each teacher.
- Similar problems to practice: Other problems that involve using maps to efficiently store and retrieve data.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check if a subject is already in the map before inserting it.
- Edge cases to watch for: Handling cases where a teacher may not be teaching any subjects.
- Performance pitfalls: Using a non-optimal data structure, such as a vector, to store the unique subjects for each teacher.
- Testing considerations: Testing the solution with different input arrays and edge cases to ensure it works correctly.