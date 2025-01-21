## Consecutive Available Seats

**Problem Link:** https://leetcode.com/problems/consecutive-available-seats/description

**Problem Statement:**
- Input: A list of `seat` objects with `id` and `student` properties, where `id` represents the seat number and `student` indicates whether the seat is occupied (`0` for free, `1` for occupied).
- Constraints: The input list contains at least two elements, and the `id` values are distinct.
- Expected output: The maximum number of consecutive available seats.
- Key requirements and edge cases to consider:
  - Handling empty lists or lists with a single element.
  - Seats are considered consecutive if their `id` values are consecutive integers.
- Example test cases with explanations:
  - Input: `[[1,0],[2,0],[3,1]]`, Output: `2`. Explanation: Seats 1 and 2 are consecutive and available.
  - Input: `[[3,1],[3,0],[4,1],[1,0],[4,0],[1,0]]`, Output: `2`. Explanation: Seats 4 and 1 are consecutive and available.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the seats by their `id` values and then iterate through the list to find consecutive available seats.
- Step-by-step breakdown of the solution:
  1. Sort the seats based on their `id` values.
  2. Initialize variables to keep track of the maximum number of consecutive available seats and the current count.
  3. Iterate through the sorted list of seats.
  4. If a seat is available, increment the current count. If it's occupied, reset the current count.
  5. Update the maximum count if the current count is higher.
- Why this approach comes to mind first: It's a straightforward and intuitive solution that checks every possible sequence of seats.

```cpp
#include <algorithm>
#include <vector>

int maxConsecutiveAvailableSeats(std::vector<std::vector<int>>& seats) {
    // Sort the seats by their id values
    std::sort(seats.begin(), seats.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });

    int maxCount = 0;
    int currentCount = 0;

    for (const auto& seat : seats) {
        if (seat[1] == 0) { // If the seat is available
            currentCount++;
            maxCount = std::max(maxCount, currentCount);
        } else { // If the seat is occupied
            currentCount = 0;
        }
    }

    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of seats, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum and current counts.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant because we only use a fixed amount of space to store the counts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the seats, we can use a `std::map` to store the seats and their corresponding availability. This allows us to iterate through the seats in sorted order without explicitly sorting them.
- Detailed breakdown of the approach:
  1. Create a `std::map` to store the seats and their availability.
  2. Iterate through the input list and insert each seat into the map.
  3. Initialize variables to keep track of the maximum number of consecutive available seats and the current count.
  4. Iterate through the map in sorted order.
  5. If a seat is available, increment the current count. If it's occupied, reset the current count.
  6. Update the maximum count if the current count is higher.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is optimal because we must at least read the input once.

```cpp
#include <map>
#include <vector>

int maxConsecutiveAvailableSeats(std::vector<std::vector<int>>& seats) {
    std::map<int, int> seatMap;

    for (const auto& seat : seats) {
        seatMap[seat[0]] = seat[1];
    }

    int maxCount = 0;
    int currentCount = 0;

    for (const auto& pair : seatMap) {
        if (pair.second == 0) { // If the seat is available
            currentCount++;
            maxCount = std::max(maxCount, currentCount);
        } else { // If the seat is occupied
            currentCount = 0;
        }
    }

    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of seats, because we iterate through the input list and the map once.
> - **Space Complexity:** $O(n)$, because we store all seats in the map.
> - **Optimality proof:** This approach is optimal because we must at least read the input once, and the map allows us to iterate through the seats in sorted order without explicit sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, using `std::map` for efficient lookup and iteration.
- Problem-solving patterns identified: Using a map to store and iterate through data in sorted order.
- Optimization techniques learned: Avoiding unnecessary sorting operations.
- Similar problems to practice: Problems involving sorting, maps, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as empty lists or lists with a single element.
- Edge cases to watch for: Seats with consecutive `id` values, seats with non-consecutive `id` values.
- Performance pitfalls: Using inefficient data structures or algorithms, such as explicit sorting.
- Testing considerations: Testing with different input sizes, edge cases, and expected outputs.