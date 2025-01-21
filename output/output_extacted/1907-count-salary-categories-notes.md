## Count Salary Categories

**Problem Link:** https://leetcode.com/problems/count-salary-categories/description

**Problem Statement:**
- Input: A list of salaries where each salary is represented as an integer.
- Constraints: The input list will contain at least one and at most $10^5$ salaries.
- Expected Output: The number of different salary categories. A salary category is defined as follows:
  - "low" if the salary is less than $10^3$,
  - "medium" if the salary is greater than or equal to $10^3$ and less than $10^4$,
  - "high" if the salary is greater than or equal to $10^4$ and less than $10^5$, and
  - "very_high" if the salary is greater than or equal to $10^5$.
- Key Requirements and Edge Cases:
  - Handle empty lists.
  - Ensure the output is accurate for lists containing salaries across different categories.
- Example Test Cases:
  - Input: `[2000, 10000, 100000]`, Expected Output: `3` because there are three different categories: "medium", "high", and "very_high".
  - Input: `[1000, 1000, 1000]`, Expected Output: `1` because there is only one category: "low".

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves categorizing each salary into its respective category and counting the number of unique categories.
- We iterate through each salary in the list, determine its category based on the given criteria, and add it to a set if it's not already present.
- This approach comes to mind first because it directly addresses the problem statement by categorizing and counting.

```cpp
#include <iostream>
#include <set>

int countSalaryCategories(vector<int>& salaries) {
    set<string> categories;
    for (int salary : salaries) {
        string category;
        if (salary < 1000) {
            category = "low";
        } else if (salary >= 1000 && salary < 10000) {
            category = "medium";
        } else if (salary >= 10000 && salary < 100000) {
            category = "high";
        } else {
            category = "very_high";
        }
        categories.insert(category);
    }
    return categories.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of salaries. This is because we perform a constant amount of work for each salary.
> - **Space Complexity:** $O(n)$ in the worst case, where every salary falls into a different category, and $O(1)$ in the best case, where all salaries fall into the same category. The space complexity is due to the use of a set to store unique categories.
> - **Why these complexities occur:** The time complexity is linear because we process each salary once. The space complexity depends on the number of unique categories because we store each unique category in a set.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to check for the presence of each category once, and we can do this by directly checking the conditions for each category.
- This approach is optimal because it minimizes the number of operations required to solve the problem.
- We initialize counters for each category and then iterate through the salaries, updating the counters as necessary.

```cpp
int countSalaryCategories(vector<int>& salaries) {
    bool low = false, medium = false, high = false, veryHigh = false;
    for (int salary : salaries) {
        if (salary < 1000) {
            low = true;
        } else if (salary < 10000) {
            medium = true;
        } else if (salary < 100000) {
            high = true;
        } else {
            veryHigh = true;
        }
    }
    int count = 0;
    if (low) count++;
    if (medium) count++;
    if (high) count++;
    if (veryHigh) count++;
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of salaries. This is because we still need to check each salary once.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the flags for each category.
> - **Optimality proof:** This is the optimal solution because it uses the least amount of space possible (constant space) and still achieves the necessary time complexity of $O(n)$, which is the minimum required to examine each salary at least once.

---

### Final Notes

**Learning Points:**
- The importance of categorizing data based on given criteria.
- Using sets or flags to keep track of unique categories.
- Optimizing space complexity by minimizing the use of extra space.

**Mistakes to Avoid:**
- Incorrectly categorizing salaries.
- Failing to handle edge cases such as empty lists or lists with a single element.
- Using more complex data structures than necessary, leading to increased space complexity.

**Similar Problems to Practice:**
- Problems involving categorization and counting of unique elements.
- Problems that require optimization of space complexity.