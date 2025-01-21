## Classes More Than 5 Students
**Problem Link:** https://leetcode.com/problems/classes-more-than-5-students/description

**Problem Statement:**
- Input format and constraints: You are given a table `courses` with columns `course_id` and `student_id`. The table represents which student is enrolled in which course. 
- Expected output format: Return the `course_id` from the `courses` table where the number of students enrolled in each course is more than 5.
- Key requirements and edge cases to consider: The table can have duplicate enrollments (a student can be enrolled in the same course multiple times), and there can be courses with fewer than 6 students enrolled.
- Example test cases with explanations: For instance, if the `courses` table contains the following data:
  | course_id | student_id |
  |-----------|-----------|
  | 1         | 1         |
  | 1         | 2         |
  | 1         | 3         |
  | 1         | 4         |
  | 1         | 5         |
  | 1         | 6         |
  | 2         | 1         |
  | 2         | 2         |
  | 2         | 3         |
  | 2         | 4         |
  | 2         | 5         |
  The expected output would be:
  | course_id |
  |-----------|
  | 1         |
  Because only course 1 has more than 5 students enrolled.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify all unique `course_id` and `student_id` pairs to handle duplicate enrollments. Then, we need to count the number of unique students for each course.
- Step-by-step breakdown of the solution:
  1. Create a set or dictionary to store unique `student_id` for each `course_id`.
  2. Iterate over the `courses` table and populate the set or dictionary.
  3. Count the number of unique students for each course.
  4. Return the `course_id` where the count is more than 5.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement by counting unique students per course.

```cpp
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// Assuming we have a structure to represent the courses table
struct Course {
    int course_id;
    int student_id;
};

// Function to find courses with more than 5 students
void findCourses(vector<Course>& courses) {
    unordered_map<int, unordered_set<int>> courseStudents;
    
    // Populate courseStudents map
    for (const auto& course : courses) {
        courseStudents[course.course_id].insert(course.student_id);
    }
    
    // Print course_id with more than 5 students
    for (const auto& pair : courseStudents) {
        if (pair.second.size() > 5) {
            cout << pair.first << endl;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of enrollments in the `courses` table, because we iterate over the table once to populate the `courseStudents` map and then iterate over the map to find courses with more than 5 students.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every enrollment in the `courseStudents` map.
> - **Why these complexities occur:** These complexities occur because we are doing a linear scan of the input data and storing unique students for each course.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using SQL, which is more efficient and directly queries the database for the required information without needing to load all data into memory.
- Detailed breakdown of the approach:
  1. Use a `GROUP BY` clause to group the `courses` table by `course_id`.
  2. Use the `COUNT(DISTINCT student_id)` function to count the number of unique students for each course.
  3. Use a `HAVING` clause to filter the results to include only courses with more than 5 students.
- Proof of optimality: This approach is optimal because it directly queries the database for the required information, minimizing the amount of data that needs to be processed and stored in memory.

```sql
SELECT course_id
FROM courses
GROUP BY course_id
HAVING COUNT(DISTINCT student_id) > 5;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `courses` table, because the database needs to sort the data to perform the `GROUP BY` operation.
> - **Space Complexity:** $O(n)$, because the database needs to store the grouped data in memory.
> - **Optimality proof:** This approach is optimal because it uses the database's built-in functionality to perform the required operations, minimizing the amount of data that needs to be processed and stored in memory.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and filtering data using SQL.
- Problem-solving patterns identified: Using database queries to solve problems that involve large amounts of data.
- Optimization techniques learned: Minimizing the amount of data that needs to be processed and stored in memory.
- Similar problems to practice: Problems that involve querying databases to extract specific information.

**Mistakes to Avoid:**
- Common implementation errors: Not using the `DISTINCT` keyword when counting unique students.
- Edge cases to watch for: Courses with duplicate enrollments.
- Performance pitfalls: Loading all data into memory instead of using database queries.
- Testing considerations: Testing the query with different datasets to ensure it produces the correct results.