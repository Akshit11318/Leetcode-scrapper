## Number of Students Unable to Eat Lunch

**Problem Link:** https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description

**Problem Statement:**
- Input format and constraints: Given two integer arrays `students` and `sandwiches`, where `students[i]` is the preference of the `i`-th student and `sandwiches[j]` is the type of the `j`-th sandwich. The students are standing in a line and will eat in this order. Each student will only eat the sandwich that is their preference (0 or 1).
- Expected output format: The number of students who cannot eat lunch because the sandwich they prefer is no longer available.
- Key requirements and edge cases to consider: Students will only eat their preferred type of sandwich, and the order in which they eat is fixed.
- Example test cases with explanations:
  - Example 1:
    - Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
    - Output: 0
    - Explanation: All students can eat their preferred type of sandwich.
  - Example 2:
    - Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    - Output: 3
    - Explanation: The first three students cannot eat lunch because there are no more sandwiches of their preferred type (1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each student and check if their preferred sandwich is available. If it is, remove the sandwich from the list of available sandwiches and continue with the next student. If the preferred sandwich is not available, increment the count of students who cannot eat lunch.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to keep track of the number of students who cannot eat lunch.
  2. Iterate over each student in the `students` array.
  3. For each student, check if their preferred sandwich is available in the `sandwiches` array.
  4. If the preferred sandwich is available, remove it from the `sandwiches` array and continue with the next student.
  5. If the preferred sandwich is not available, increment the `count` variable.
- Why this approach comes to mind first: It directly addresses the problem by simulating the process of students eating their preferred sandwiches.

```cpp
int countStudents(vector<int>& students, vector<int>& sandwiches) {
    int count = 0;
    for (int student : students) {
        bool found = false;
        for (int i = 0; i < sandwiches.size(); i++) {
            if (student == sandwiches[i]) {
                sandwiches.erase(sandwiches.begin() + i);
                found = true;
                break;
            }
        }
        if (!found) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of students. This is because for each student, we potentially iterate over all remaining sandwiches.
> - **Space Complexity:** $O(1)$, since we modify the input `sandwiches` array in-place and use a constant amount of extra space to store the `count` variable.
> - **Why these complexities occur:** The time complexity is high because of the nested loop structure, where for each student, we search through the remaining sandwiches. The space complexity is low because we only use a constant amount of extra space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over the sandwiches for each student, we can count the number of students who prefer each type of sandwich and compare it to the number of available sandwiches of each type.
- Detailed breakdown of the approach:
  1. Count the number of students who prefer each type of sandwich (0 and 1).
  2. Compare these counts to the number of available sandwiches of each type.
  3. The number of students who cannot eat lunch is the minimum between the count of students who prefer a type of sandwich and the count of available sandwiches of that type, subtracted from the total count of students who prefer that type of sandwich.
- Proof of optimality: This approach directly calculates the number of students who cannot eat lunch without needing to simulate the eating process, making it more efficient than the brute force approach.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best we can achieve given that we must at least read the input.

```cpp
int countStudents(vector<int>& students, vector<int>& sandwiches) {
    int pref0 = 0, pref1 = 0;
    for (int student : students) {
        if (student == 0) pref0++;
        else pref1++;
    }
    for (int sandwich : sandwiches) {
        if (sandwich == 0) {
            if (pref0 > 0) pref0--;
            else break;
        } else {
            if (pref1 > 0) pref1--;
            else break;
        }
    }
    return pref0 + pref1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of students and sandwiches. This is because we make two passes: one over the students and one over the sandwiches.
> - **Space Complexity:** $O(1)$, since we use a constant amount of extra space to store the counts of students who prefer each type of sandwich.
> - **Optimality proof:** This is the optimal solution because it achieves a linear time complexity, which is the best possible given the need to read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, comparison, and optimization.
- Problem-solving patterns identified: Direct simulation vs. calculating aggregates and comparing them.
- Optimization techniques learned: Avoiding unnecessary iterations and using aggregate counts to simplify the problem.
- Similar problems to practice: Other problems involving counting, comparison, and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating counts or comparing them.
- Edge cases to watch for: Handling cases where there are more students who prefer a type of sandwich than there are sandwiches of that type.
- Performance pitfalls: Using nested loops when a simpler, more efficient approach is available.
- Testing considerations: Ensure that the solution works correctly for all possible combinations of student preferences and sandwich types.