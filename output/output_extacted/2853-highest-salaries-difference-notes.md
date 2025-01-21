## Highest Salaries Difference

**Problem Link:** https://leetcode.com/problems/highest-salaries-difference/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the highest salaries difference for a company, given a table of employee salaries.
- Expected output format: The output should be the maximum possible difference between the highest and lowest salaries.
- Key requirements and edge cases to consider: The company must have at least one employee to calculate the difference, and all salaries must be non-negative.
- Example test cases with explanations:
  - If the company has only one employee with a salary of 100, the difference is 0.
  - If the company has two employees with salaries 100 and 200, the difference is 100.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To calculate the highest salaries difference, we can simply subtract the lowest salary from the highest salary.
- Step-by-step breakdown of the solution:
  1. Find the highest salary in the table.
  2. Find the lowest salary in the table.
  3. Calculate the difference between the highest and lowest salaries.
- Why this approach comes to mind first: It is the most straightforward way to calculate the difference between the highest and lowest salaries.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int highestSalariesDifference(std::vector<int>& salaries) {
    if (salaries.size() < 2) {
        return 0;
    }

    int highestSalary = *std::max_element(salaries.begin(), salaries.end());
    int lowestSalary = *std::min_element(salaries.begin(), salaries.end());

    return highestSalary - lowestSalary;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we need to iterate over all employees to find the highest and lowest salaries.
> - **Space Complexity:** $O(1)$, as we only need to store the highest and lowest salaries.
> - **Why these complexities occur:** The time complexity is linear because we need to examine each employee's salary once. The space complexity is constant because we only need a fixed amount of space to store the highest and lowest salaries.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass to find both the highest and lowest salaries, reducing the time complexity.
- Detailed breakdown of the approach:
  1. Initialize the highest and lowest salaries to the first employee's salary.
  2. Iterate over the remaining employees, updating the highest and lowest salaries as needed.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we must examine each employee's salary at least once.

```cpp
int highestSalariesDifference(std::vector<int>& salaries) {
    if (salaries.size() < 2) {
        return 0;
    }

    int highestSalary = salaries[0];
    int lowestSalary = salaries[0];

    for (int i = 1; i < salaries.size(); i++) {
        if (salaries[i] > highestSalary) {
            highestSalary = salaries[i];
        }
        if (salaries[i] < lowestSalary) {
            lowestSalary = salaries[i];
        }
    }

    return highestSalary - lowestSalary;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we only need to iterate over the employees once.
> - **Space Complexity:** $O(1)$, as we only need to store the highest and lowest salaries.
> - **Optimality proof:** The time complexity is optimal because we must examine each employee's salary at least once. The space complexity is optimal because we only need a fixed amount of space to store the highest and lowest salaries.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the maximum and minimum values in an array.
- Problem-solving patterns identified: Using a single pass to find multiple values.
- Optimization techniques learned: Reducing the number of passes over the data.
- Similar problems to practice: Finding the median or mode of a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty or single-element array.
- Edge cases to watch for: Empty or single-element arrays, as well as arrays with duplicate maximum or minimum values.
- Performance pitfalls: Using multiple passes over the data when a single pass is possible.
- Testing considerations: Testing with a variety of input sizes and edge cases to ensure correctness and performance.