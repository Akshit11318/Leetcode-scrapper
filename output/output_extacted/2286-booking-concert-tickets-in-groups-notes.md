## Booking Concert Tickets in Groups

**Problem Link:** https://leetcode.com/problems/booking-concert-tickets-in-groups/description

**Problem Statement:**
- Input format: `n` (number of rows), `m` (number of seats in each row), and `groups` (a list of groups where each group is represented as `[size, min_row]`)
- Constraints: $1 \leq n \leq 10^5$, $1 \leq m \leq 10$, $1 \leq groups.length \leq 10^5$, $1 \leq size \leq m$, $1 \leq min_row \leq n$
- Expected output format: The number of groups that can be booked
- Key requirements and edge cases to consider: Groups must be seated in a single row, and each row can be used by at most one group
- Example test cases with explanations:
  - For `n = 2`, `m = 3`, `groups = [[2,1],[3,1]]`, the output should be `1` because only one group can be seated.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try to seat each group in the first available row that meets the minimum row requirement.
- Step-by-step breakdown of the solution:
  1. Sort the groups by their size in descending order.
  2. Iterate over each group.
  3. For each group, try to find the first row that meets the minimum row requirement and has enough seats.
  4. If such a row is found, mark it as used and increment the count of seated groups.
- Why this approach comes to mind first: It's a straightforward greedy approach that tries to seat the largest groups first.

```cpp
int maxNumberOfFamilies(int n, int m, vector<vector<int>>& groups) {
    int count = 0;
    vector<bool> rowUsed(n, false);
    sort(groups.begin(), groups.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] > b[0];
    });
    for (auto& group : groups) {
        int size = group[0], minRow = group[1] - 1;
        bool seated = false;
        for (int i = minRow; i < n; i++) {
            if (!rowUsed[i]) {
                // Check if the row has enough seats
                bool hasEnoughSeats = true;
                for (int j = 0; j < size; j++) {
                    if (j >= m) {
                        hasEnoughSeats = false;
                        break;
                    }
                }
                if (hasEnoughSeats) {
                    rowUsed[i] = true;
                    count++;
                    seated = true;
                    break;
                }
            }
        }
        if (!seated) {
            // Try to seat the group in two separate rows
            for (int i = minRow; i < n - 1; i++) {
                if (!rowUsed[i] && !rowUsed[i + 1]) {
                    rowUsed[i] = true;
                    rowUsed[i + 1] = true;
                    count++;
                    seated = true;
                    break;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot groups.length)$ because in the worst case, we might need to iterate over all rows and seats for each group.
> - **Space Complexity:** $O(n)$ for the `rowUsed` vector.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops and the space complexity is linear due to the additional vector used to track row usage.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient data structure, such as a `map`, to store the available seats in each row.
- Detailed breakdown of the approach:
  1. Create a `map` to store the available seats in each row.
  2. Iterate over each group.
  3. For each group, try to find a row that meets the minimum row requirement and has enough seats.
  4. If such a row is found, update the available seats in that row and increment the count of seated groups.
- Proof of optimality: This approach is optimal because it uses a more efficient data structure to store and update the available seats in each row, reducing the time complexity.

```cpp
int maxNumberOfFamilies(int n, int m, vector<vector<int>>& groups) {
    int count = 0;
    map<int, vector<bool>> rowSeats;
    for (int i = 0; i < n; i++) {
        rowSeats[i] = vector<bool>(m, true);
    }
    sort(groups.begin(), groups.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] > b[0];
    });
    for (auto& group : groups) {
        int size = group[0], minRow = group[1] - 1;
        bool seated = false;
        for (int i = minRow; i < n; i++) {
            if (rowSeats[i].size() >= size) {
                // Check if the row has enough consecutive seats
                bool hasEnoughSeats = false;
                for (int j = 0; j <= rowSeats[i].size() - size; j++) {
                    bool allSeatsAvailable = true;
                    for (int k = 0; k < size; k++) {
                        if (!rowSeats[i][j + k]) {
                            allSeatsAvailable = false;
                            break;
                        }
                    }
                    if (allSeatsAvailable) {
                        hasEnoughSeats = true;
                        // Update the available seats in the row
                        for (int k = 0; k < size; k++) {
                            rowSeats[i][j + k] = false;
                        }
                        break;
                    }
                }
                if (hasEnoughSeats) {
                    count++;
                    seated = true;
                    break;
                }
            }
        }
        if (!seated) {
            // Try to seat the group in two separate rows
            for (int i = minRow; i < n - 1; i++) {
                if (rowSeats[i].size() >= size / 2 && rowSeats[i + 1].size() >= size / 2) {
                    // Update the available seats in the two rows
                    for (int j = 0; j < size / 2; j++) {
                        rowSeats[i][j] = false;
                        rowSeats[i + 1][j] = false;
                    }
                    count++;
                    seated = true;
                    break;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot groups.length)$ because we only need to iterate over each group and the rows that meet the minimum row requirement.
> - **Space Complexity:** $O(n \cdot m)$ for the `rowSeats` map.
> - **Optimality proof:** This approach is optimal because it uses a more efficient data structure to store and update the available seats in each row, reducing the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, data structure optimization
- Problem-solving patterns identified: Using a more efficient data structure to reduce time complexity
- Optimization techniques learned: Using a `map` to store and update available seats in each row
- Similar problems to practice: Other problems that involve seating or scheduling

**Mistakes to Avoid:**
- Common implementation errors: Not checking for enough seats in each row, not updating the available seats correctly
- Edge cases to watch for: Groups with size greater than the number of seats in a row, groups that cannot be seated in a single row
- Performance pitfalls: Using a brute force approach with high time complexity
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.