## Students and Examinations
**Problem Link:** https://leetcode.com/problems/students-and-examinations/description

**Problem Statement:**
- Input format and constraints: The problem involves a list of students and their examination scores. The input is an array of integers representing the scores of students in each subject.
- Expected output format: The output should be an array of integers representing the average score of each student in each subject.
- Key requirements and edge cases to consider: The input array will have a size of n x 2, where n is the number of students. The output should be an array of size n x 2, where each element represents the average score of a student in a particular subject.
- Example test cases with explanations: For example, if the input is [[1,2],[3,4],[5,6]], the output should be [[1.5],[3.5],[5.5]].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over the input array, calculate the sum of scores for each student in each subject, and then divide by the number of subjects to get the average score.
- Step-by-step breakdown of the solution: 
  1. Initialize an array to store the sum of scores for each student in each subject.
  2. Iterate over the input array, adding the score of each student in each subject to the corresponding element in the sum array.
  3. Initialize an array to store the average score of each student in each subject.
  4. Iterate over the sum array, dividing each element by the number of subjects to get the average score, and store the result in the average array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a good starting point for solving the problem.

```cpp
#include <vector>
#include <numeric>

std::vector<std::vector<double>> averageOfLevels(std::vector<std::vector<int>>& scores) {
    int n = scores.size();
    std::vector<std::vector<double>> averages(n, std::vector<double>(2));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            double sum = 0;
            for (int k = 0; k < n; k++) {
                sum += scores[k][j];
            }
            averages[i][j] = sum / n;
        }
    }
    return averages;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of students. This is because we have two nested loops that iterate over the input array.
> - **Space Complexity:** $O(n)$, where n is the number of students. This is because we need to store the sum and average arrays.
> - **Why these complexities occur:** The time complexity is high because we are iterating over the input array for each student, and the space complexity is moderate because we need to store the sum and average arrays.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over the input array for each student, we can iterate over the array only once and calculate the sum of scores for each subject.
- Detailed breakdown of the approach: 
  1. Initialize an array to store the sum of scores for each subject.
  2. Iterate over the input array, adding the score of each student in each subject to the corresponding element in the sum array.
  3. Initialize an array to store the average score of each student in each subject.
  4. Iterate over the sum array, dividing each element by the number of students to get the average score, and store the result in the average array.
- Proof of optimality: This approach is optimal because we only need to iterate over the input array once, reducing the time complexity to $O(n)$.
- Why further optimization is impossible: This approach is already optimal because we need to iterate over the input array at least once to calculate the sum of scores for each subject.

```cpp
#include <vector>
#include <numeric>

std::vector<std::vector<double>> averageOfLevels(std::vector<std::vector<int>>& scores) {
    int n = scores.size();
    std::vector<double> sums(2, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            sums[j] += scores[i][j];
        }
    }
    std::vector<std::vector<double>> averages(n, std::vector<double>(2));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            averages[i][j] = sums[j] / n;
        }
    }
    return averages;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of students. This is because we only need to iterate over the input array once.
> - **Space Complexity:** $O(n)$, where n is the number of students. This is because we need to store the sum and average arrays.
> - **Optimality proof:** This approach is optimal because we only need to iterate over the input array once, reducing the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of iterating over the input array only once to reduce the time complexity.
- Problem-solving patterns identified: The problem requires identifying the key insight that leads to the optimal solution, which is to iterate over the array only once and calculate the sum of scores for each subject.
- Optimization techniques learned: The problem demonstrates the importance of reducing the number of iterations over the input array to optimize the solution.
- Similar problems to practice: Similar problems to practice include calculating the average score of students in a particular subject, or calculating the sum of scores for each subject.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to iterate over the input array for each student, which increases the time complexity.
- Edge cases to watch for: An edge case to watch for is when the input array is empty, in which case the solution should return an empty array.
- Performance pitfalls: A performance pitfall is to use a brute force approach that iterates over the input array for each student, which can lead to high time complexity.
- Testing considerations: The solution should be tested with different input arrays to ensure that it works correctly and efficiently.