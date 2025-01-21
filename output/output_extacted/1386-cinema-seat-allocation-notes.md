## Cinema Seat Allocation

**Problem Link:** https://leetcode.com/problems/cinema-seat-allocation/description

**Problem Statement:**
- Input format and constraints: The input will be a list of reserved seats, where each seat is represented by a string containing the row and column of the seat (e.g., "1A"). The number of rows and columns in the cinema is not fixed but can be determined from the input. The goal is to allocate seats to a group of people such that the maximum number of people can be seated, with the constraint that no two people can sit next to each other in the same row.
- Expected output format: The output should be the maximum number of people that can be seated.
- Key requirements and edge cases to consider: The input list of reserved seats, the number of people to seat, and the layout of the cinema (rows and columns).
- Example test cases with explanations: 
    - For example, given the reserved seats ["1A", "1B", "2C", "2D"], and 4 people to seat, the function should return the maximum number of people that can be seated under the given constraints.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial approach is to try to seat each person in every possible seat and then check if the seating arrangement satisfies the condition that no two people sit next to each other in the same row.
- Step-by-step breakdown of the solution:
    1. Generate all possible seating arrangements for the given number of people.
    2. For each arrangement, check if any two people are sitting next to each other in the same row.
    3. If an arrangement satisfies the condition, update the maximum number of people that can be seated.
- Why this approach comes to mind first: This approach is straightforward and considers all possibilities, making it a natural first thought.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int maxNumberOfFamilies(int n, std::vector<std::string>& reservedSeats) {
    // Create a set of reserved seats for efficient lookup
    std::set<std::string> reserved(reservedSeats.begin(), reservedSeats.end());
    
    // Initialize count of families seated
    int count = 0;
    
    // Iterate over each row
    for (int i = 1; i <= n; ++i) {
        // Initialize count of families in the current row
        int rowCount = 0;
        
        // Check if we can seat two families in the row
        if (reserved.find(std::to_string(i) + "C") == reserved.end() &&
            reserved.find(std::to_string(i) + "D") == reserved.end() &&
            reserved.find(std::to_string(i) + "E") == reserved.end() &&
            reserved.find(std::to_string(i) + "F") == reserved.end()) {
            rowCount += 2;
        }
        // If not, check if we can seat one family in the row
        else if (reserved.find(std::to_string(i) + "B") == reserved.end() &&
                 reserved.find(std::to_string(i) + "C") == reserved.end() &&
                 reserved.find(std::to_string(i) + "D") == reserved.end() &&
                 reserved.find(std::to_string(i) + "E") == reserved.end()) {
            rowCount += 1;
        }
        else if (reserved.find(std::to_string(i) + "D") == reserved.end() &&
                 reserved.find(std::to_string(i) + "E") == reserved.end() &&
                 reserved.find(std::to_string(i) + "F") == reserved.end() &&
                 reserved.find(std::to_string(i) + "G") == reserved.end()) {
            rowCount += 1;
        }
        
        // Update the total count
        count += rowCount;
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of rows and $m$ is the number of columns, because we are iterating over each row and checking each seat.
> - **Space Complexity:** $O(m)$, for storing the reserved seats in a set.
> - **Why these complexities occur:** The time complexity occurs because we are checking each seat in each row, and the space complexity occurs because we are storing all reserved seats in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible seating arrangement, we can directly check for available seats in each row and try to seat as many families as possible.
- Detailed breakdown of the approach:
    1. Create a set of reserved seats for efficient lookup.
    2. Iterate over each row and check for available seats.
    3. Try to seat two families in the row if possible, otherwise try to seat one family.
- Proof of optimality: This approach is optimal because it directly checks for available seats and tries to seat as many families as possible, without considering unnecessary seating arrangements.
- Why further optimization is impossible: This approach already considers the most efficient way to seat families, so further optimization is not possible.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int maxNumberOfFamilies(int n, std::vector<std::string>& reservedSeats) {
    std::vector<std::vector<bool>> rows(n, std::vector<bool>(11, false));
    
    for (const auto& seat : reservedSeats) {
        int row = seat[0] - '1';
        int col = seat[1] - 'A';
        rows[row][col] = true;
    }
    
    int count = 0;
    
    for (int i = 0; i < n; ++i) {
        if (!rows[i][2] && !rows[i][3] && !rows[i][4] && !rows[i][5]) {
            count += 2;
        } else if (!rows[i][4] && !rows[i][5] && !rows[i][6] && !rows[i][7]) {
            count += 2;
        } else if (!rows[i][2] && !rows[i][3] && !rows[i][4] && !rows[i][5] && !rows[i][6] && !rows[i][7]) {
            count += 1;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of rows and $m$ is the number of columns, because we are iterating over each row and checking each seat.
> - **Space Complexity:** $O(n \times m)$, for storing the rows and their seats.
> - **Optimality proof:** This approach is optimal because it directly checks for available seats and tries to seat as many families as possible, without considering unnecessary seating arrangements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for available seats, trying to seat as many families as possible.
- Problem-solving patterns identified: Directly checking for available seats, trying to seat as many families as possible.
- Optimization techniques learned: Avoiding unnecessary seating arrangements.
- Similar problems to practice: Other problems involving seating arrangements and optimizing for maximum occupancy.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for available seats correctly, not trying to seat as many families as possible.
- Edge cases to watch for: Rows with no available seats, rows with only one available seat.
- Performance pitfalls: Considering unnecessary seating arrangements.
- Testing considerations: Testing with different input cases, including edge cases.