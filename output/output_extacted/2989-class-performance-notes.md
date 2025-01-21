## Class Performance

**Problem Link:** https://leetcode.com/problems/class-performance/description

**Problem Statement:**
- Input format: A list of `student_id`, `course_id`, and `grade` as integers.
- Constraints: `1 <= student_id <= 10^5`, `1 <= course_id <= 10^5`, and `1 <= grade <= 100`.
- Expected output format: A table with `class` as the only column, where `class` is the grade of each student in the class.
- Key requirements: Calculate the average grade for each student and then determine their class based on the average grade.
- Edge cases to consider: Handling students with no grades, and ensuring the average grade is calculated correctly.
- Example test cases with explanations:
  - If a student has grades 90, 80, and 70, their average grade is 80, which corresponds to a class of 'A' if the threshold is 75.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the average grade for each student by summing up all their grades and dividing by the total number of grades.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the sum of grades and the count of grades for each student.
  2. Iterate over the list of grades to calculate the sum and count of grades for each student.
  3. Calculate the average grade for each student by dividing the sum of grades by the count of grades.
  4. Determine the class of each student based on their average grade.
- Why this approach comes to mind first: It is a straightforward method to calculate the average grade and then determine the class.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct StudentGrade {
    int student_id;
    int course_id;
    int grade;
};

std::vector<int> class_performance(std::vector<StudentGrade>& student_grades) {
    // Create a dictionary to store the sum of grades and the count of grades for each student
    std::unordered_map<int, std::pair<int, int>> student_average;
    
    // Iterate over the list of grades to calculate the sum and count of grades for each student
    for (const auto& grade : student_grades) {
        if (student_average.find(grade.student_id) != student_average.end()) {
            student_average[grade.student_id].first += grade.grade;
            student_average[grade.student_id].second++;
        } else {
            student_average[grade.student_id] = {grade.grade, 1};
        }
    }
    
    // Calculate the average grade for each student and determine their class
    std::vector<int> classes;
    for (const auto& student : student_average) {
        double average = static_cast<double>(student.second.first) / student.second.second;
        char student_class = 'A';
        if (average < 75) student_class = 'F';
        else if (average < 85) student_class = 'B';
        else if (average < 95) student_class = 'C';
        
        // Map the character class to an integer class
        int int_class;
        switch (student_class) {
            case 'A': int_class = 5; break;
            case 'B': int_class = 4; break;
            case 'C': int_class = 3; break;
            case 'F': int_class = 0; break;
            default: int_class = 0; break;
        }
        
        classes.push_back(int_class);
    }
    
    return classes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of student grades, because we iterate over the list of grades once.
> - **Space Complexity:** $O(n)$, because we store the sum and count of grades for each student in a dictionary.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the list of grades once, and the space complexity is linear because we store information for each student.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient data structure to store the student grades.
- Detailed breakdown of the approach:
  1. Use a `std::unordered_map` to store the sum of grades and the count of grades for each student.
  2. Iterate over the list of grades to calculate the sum and count of grades for each student.
  3. Calculate the average grade for each student by dividing the sum of grades by the count of grades.
  4. Determine the class of each student based on their average grade.
- Proof of optimality: This approach is optimal because it only requires a single pass over the list of grades, and it uses a data structure that allows for constant-time lookups and insertions.
- Why further optimization is impossible: This approach already has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct StudentGrade {
    int student_id;
    int course_id;
    int grade;
};

std::vector<int> class_performance(std::vector<StudentGrade>& student_grades) {
    // Create a dictionary to store the sum of grades and the count of grades for each student
    std::unordered_map<int, std::pair<int, int>> student_average;
    
    // Iterate over the list of grades to calculate the sum and count of grades for each student
    for (const auto& grade : student_grades) {
        if (student_average.find(grade.student_id) != student_average.end()) {
            student_average[grade.student_id].first += grade.grade;
            student_average[grade.student_id].second++;
        } else {
            student_average[grade.student_id] = {grade.grade, 1};
        }
    }
    
    // Calculate the average grade for each student and determine their class
    std::vector<int> classes;
    for (const auto& student : student_average) {
        double average = static_cast<double>(student.second.first) / student.second.second;
        char student_class = 'A';
        if (average < 75) student_class = 'F';
        else if (average < 85) student_class = 'B';
        else if (average < 95) student_class = 'C';
        
        // Map the character class to an integer class
        int int_class;
        switch (student_class) {
            case 'A': int_class = 5; break;
            case 'B': int_class = 4; break;
            case 'C': int_class = 3; break;
            case 'F': int_class = 0; break;
            default: int_class = 0; break;
        }
        
        classes.push_back(int_class);
    }
    
    return classes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of student grades, because we iterate over the list of grades once.
> - **Space Complexity:** $O(n)$, because we store the sum and count of grades for each student in a dictionary.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the list of grades, and it uses a data structure that allows for constant-time lookups and insertions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store the sum and count of grades for each student, and calculating the average grade by dividing the sum of grades by the count of grades.
- Problem-solving patterns identified: Using a data structure that allows for constant-time lookups and insertions to improve efficiency.
- Optimization techniques learned: Using a more efficient data structure to store the student grades, and only requiring a single pass over the list of grades.
- Similar problems to practice: Other problems that involve calculating averages or sums, and using data structures to improve efficiency.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a student has no grades, or not calculating the average grade correctly.
- Edge cases to watch for: Handling students with no grades, and ensuring the average grade is calculated correctly.
- Performance pitfalls: Using a data structure that does not allow for constant-time lookups and insertions, or requiring multiple passes over the list of grades.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.