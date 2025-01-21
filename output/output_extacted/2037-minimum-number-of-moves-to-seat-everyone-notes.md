## Minimum Number of Moves to Seat Everyone

**Problem Link:** https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description

**Problem Statement:**
- Input format: Two integer arrays `seats` and `students`, each of length `n`, where `seats[i]` and `students[j]` represent the position of the `i`-th seat and the `j`-th student, respectively.
- Constraints: `1 <= n <= 100`, `1 <= seats[i], students[j] <= 100`.
- Expected output format: The minimum number of moves to seat every student in their assigned seat.
- Key requirements and edge cases to consider: Each student must be seated in their assigned seat, and we want to minimize the total number of moves.
- Example test cases with explanations: 
  - `seats = [3,1,5]`, `students = [2,7,9]`: The minimum number of moves is `4` (move the first student to seat `1`, move the second student to seat `3`, move the third student to seat `5`).
  - `seats = [4,1,5,9]`, `students = [1,3,2,6]`: The minimum number of moves is `7` (move the first student to seat `1`, move the second student to seat `3`, move the third student to seat `5`, move the fourth student to seat `9`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible permutations of students and calculate the total number of moves for each permutation.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of students.
  2. For each permutation, calculate the total number of moves by summing the absolute differences between the positions of each student and their assigned seat.
  3. Return the minimum total number of moves among all permutations.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible permutations and calculate the total number of moves for each one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minMovesToSeat(std::vector<int>& seats, std::vector<int>& students) {
    std::sort(seats.begin(), seats.end());
    std::sort(students.begin(), students.end());
    int moves = 0;
    for (int i = 0; i < seats.size(); i++) {
        moves += abs(seats[i] - students[i]);
    }
    return moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of seats and students.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the input arrays and the result.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is constant because we do not use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by simply sorting both arrays and then calculating the total number of moves by summing the absolute differences between the positions of each student and their assigned seat.
- Detailed breakdown of the approach:
  1. Sort the `seats` array in ascending order.
  2. Sort the `students` array in ascending order.
  3. Calculate the total number of moves by summing the absolute differences between the positions of each student and their assigned seat.
- Proof of optimality: This approach is optimal because it minimizes the total number of moves by assigning each student to the seat that is closest to their original position.

```cpp
int minMovesToSeat(std::vector<int>& seats, std::vector<int>& students) {
    std::sort(seats.begin(), seats.end());
    std::sort(students.begin(), students.end());
    int moves = 0;
    for (int i = 0; i < seats.size(); i++) {
        moves += abs(seats[i] - students[i]);
    }
    return moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of seats and students.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the input arrays and the result.
> - **Optimality proof:** This approach is optimal because it minimizes the total number of moves by assigning each student to the seat that is closest to their original position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and calculating absolute differences.
- Problem-solving patterns identified: Using sorting to minimize the total number of moves.
- Optimization techniques learned: Minimizing the total number of moves by assigning each student to the seat that is closest to their original position.
- Similar problems to practice: Other problems that involve sorting and calculating absolute differences, such as the "Assign Cookies" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the input arrays correctly.
- Edge cases to watch for: Empty input arrays or arrays with duplicate elements.
- Performance pitfalls: Using inefficient sorting algorithms or not minimizing the total number of moves correctly.
- Testing considerations: Testing the function with different input arrays and edge cases to ensure it works correctly.