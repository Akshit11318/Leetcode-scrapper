## Happy Students

**Problem Link:** https://leetcode.com/problems/happy-students/description

**Problem Statement:**
- Input format and constraints: The problem takes in a 2D array `happiness` where `happiness[i][j]` is the happiness of student `i` when sitting next to student `j`, and a 2D array `sitting` where `sitting[i][j]` is `true` if student `i` is sitting next to student `j`.
- Expected output format: The maximum possible total happiness.
- Key requirements and edge cases to consider: The happiness of each student can be negative, and the total happiness should be maximized.
- Example test cases with explanations: For example, if `happiness = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` and `sitting = [[true, false, false], [false, true, false], [false, false, true]]`, the maximum possible total happiness is `1 + 4 + 7 = 12`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of students and calculating the total happiness for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of students.
  2. For each permutation, calculate the total happiness by summing up the happiness of each student sitting next to another student.
  3. Keep track of the maximum total happiness found.
- Why this approach comes to mind first: This approach is straightforward and guarantees the correct solution, but it is inefficient due to the large number of permutations.

```cpp
#include <vector>
#include <algorithm>

int maxHappiness(std::vector<std::vector<int>>& happiness, std::vector<std::vector<bool>>& sitting) {
    int n = happiness.size();
    int maxHappiness = -1e9;
    
    std::vector<int> students(n);
    for (int i = 0; i < n; i++) {
        students[i] = i;
    }
    
    do {
        int totalHappiness = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (sitting[i][j]) {
                    totalHappiness += happiness[i][students[j]];
                }
            }
        }
        maxHappiness = std::max(maxHappiness, totalHappiness);
    } while (std::next_permutation(students.begin(), students.end()));
    
    return maxHappiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the number of students. This is because we generate all permutations of students and calculate the total happiness for each permutation, which takes $O(n^2)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of students. This is because we need to store the current permutation of students.
> - **Why these complexities occur:** The time complexity is high due to the large number of permutations, and the space complexity is low because we only need to store a single permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a bitmask to represent the students and their neighbors.
- Detailed breakdown of the approach:
  1. Use a bitmask to represent the students and their neighbors.
  2. For each bitmask, calculate the total happiness by summing up the happiness of each student sitting next to another student.
  3. Keep track of the maximum total happiness found.
- Proof of optimality: This approach is optimal because it tries all possible combinations of students and their neighbors in a more efficient way than the brute force approach.

```cpp
#include <vector>
#include <algorithm>

int maxHappiness(std::vector<std::vector<int>>& happiness, std::vector<std::vector<bool>>& sitting) {
    int n = happiness.size();
    int maxHappiness = -1e9;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalHappiness = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << i)) && (mask & (1 << j)) && sitting[i][j]) {
                    totalHappiness += happiness[i][j];
                }
            }
        }
        maxHappiness = std::max(maxHappiness, totalHappiness);
    }
    
    return maxHappiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of students. This is because we try all possible bitmasks and calculate the total happiness for each bitmask, which takes $O(n^2)$ time.
> - **Space Complexity:** $O(1)$, where $n$ is the number of students. This is because we only need to store a single bitmask.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of students and their neighbors in a more efficient way than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmasking and permutation generation.
- Problem-solving patterns identified: Using bitmasks to represent combinations of students and their neighbors.
- Optimization techniques learned: Using bitmasks to reduce the time complexity of the algorithm.
- Similar problems to practice: Problems involving permutation generation and bitmasking.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the total happiness for each combination of students.
- Edge cases to watch for: Handling cases where the happiness of each student is negative.
- Performance pitfalls: Using inefficient algorithms that have high time complexities.
- Testing considerations: Testing the algorithm with different inputs to ensure it produces the correct output.