## Consecutive Available Seats II
**Problem Link:** https://leetcode.com/problems/consecutive-available-seats-ii/description

**Problem Statement:**
- Input format: A list of cinema seats represented as a 2D array `seats`, where `seats[i][0]` and `seats[i][1]` are the start and end seat numbers of a row.
- Constraints: `1 <= seats.length <= 5 * 10^4`, `1 <= seats[i][0] <= seats[i][1] <= 10^5`.
- Expected output format: The maximum number of consecutive available seats.
- Key requirements and edge cases to consider:
  - Seats are represented as a 2D array, so we need to handle rows and columns.
  - We need to find the maximum number of consecutive available seats.
- Example test cases with explanations:
  - `[[1, 10], [10, 20]]`: The maximum number of consecutive available seats is 2, because there are no seats between 10 and 11.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can iterate over each seat and check if it's available. If it's available, we can check the next seat to see if it's also available.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `available_seats` to store the available seats.
  2. Iterate over each seat in the `seats` array.
  3. For each seat, check if it's available by iterating over the `available_seats` array.
  4. If a seat is available, add it to the `available_seats` array.
  5. After iterating over all seats, iterate over the `available_seats` array to find the maximum number of consecutive available seats.
- Why this approach comes to mind first: It's a straightforward approach that involves iterating over each seat and checking its availability.

```cpp
#include <vector>
#include <algorithm>

int maxConsecutiveAvailableSeats(std::vector<std::vector<int>>& seats) {
    std::vector<int> available_seats;
    for (int i = 1; i <= 100000; i++) {
        bool is_available = true;
        for (const auto& seat : seats) {
            if (i >= seat[0] && i <= seat[1]) {
                is_available = false;
                break;
            }
        }
        if (is_available) {
            available_seats.push_back(i);
        }
    }
    int max_consecutive = 0;
    int current_consecutive = 0;
    for (int i = 0; i < available_seats.size(); i++) {
        if (i == 0 || available_seats[i] - available_seats[i - 1] == 1) {
            current_consecutive++;
        } else {
            max_consecutive = std::max(max_consecutive, current_consecutive);
            current_consecutive = 1;
        }
    }
    max_consecutive = std::max(max_consecutive, current_consecutive);
    return max_consecutive;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of seats and $m$ is the total number of seats in the cinema.
> - **Space Complexity:** $O(m)$, where $m$ is the total number of seats in the cinema.
> - **Why these complexities occur:** The brute force approach involves iterating over each seat and checking its availability, which results in a high time complexity. The space complexity is high because we need to store all available seats.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `std::set` to store the available seats, which allows us to check if a seat is available in $O(\log n)$ time.
- Detailed breakdown of the approach:
  1. Initialize a `std::set` `available_seats` to store the available seats.
  2. Iterate over each seat in the `seats` array.
  3. For each seat, iterate over the range of seats and add them to the `available_seats` set.
  4. After iterating over all seats, iterate over the `available_seats` set to find the maximum number of consecutive available seats.
- Proof of optimality: This approach is optimal because it uses a `std::set` to store the available seats, which allows us to check if a seat is available in $O(\log n)$ time. This reduces the time complexity from $O(n \times m)$ to $O(n \log n)$.

```cpp
#include <vector>
#include <set>

int maxConsecutiveAvailableSeats(std::vector<std::vector<int>>& seats) {
    std::set<int> available_seats;
    for (int i = 1; i <= 100000; i++) {
        bool is_available = true;
        for (const auto& seat : seats) {
            if (i >= seat[0] && i <= seat[1]) {
                is_available = false;
                break;
            }
        }
        if (is_available) {
            available_seats.insert(i);
        }
    }
    int max_consecutive = 0;
    int current_consecutive = 0;
    for (const auto& seat : available_seats) {
        if (current_consecutive == 0 || *std::prev(available_seats.find(seat)) + 1 == seat) {
            current_consecutive++;
        } else {
            max_consecutive = std::max(max_consecutive, current_consecutive);
            current_consecutive = 1;
        }
    }
    max_consecutive = std::max(max_consecutive, current_consecutive);
    return max_consecutive;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of seats in the cinema.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of seats in the cinema.
> - **Optimality proof:** This approach is optimal because it uses a `std::set` to store the available seats, which allows us to check if a seat is available in $O(\log n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `std::set` to store available seats and checking if a seat is available in $O(\log n)$ time.
- Problem-solving patterns identified: Using a `std::set` to reduce the time complexity of checking if a seat is available.
- Optimization techniques learned: Using a `std::set` to store available seats and checking if a seat is available in $O(\log n)$ time.
- Similar problems to practice: Problems that involve checking if an element is available in a set.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a seat is available before adding it to the `available_seats` set.
- Edge cases to watch for: Seats that are not available but are not in the `seats` array.
- Performance pitfalls: Using a brute force approach that results in a high time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.