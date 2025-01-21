## Seat Reservation Manager

**Problem Link:** https://leetcode.com/problems/seat-reservation-manager/description

**Problem Statement:**
- Design a seat reservation manager for a theater with `n` rows of seats, where each row has 10 seats.
- Implement the following methods:
  - `SeatManager(int n_rows)`: Initializes the seat reservation manager with `n_rows` rows of seats.
  - `int reserve()`: Reserves a seat and returns the row and column of the reserved seat.
  - `void unreserve(int row, int col)`: Unreserves a seat at the given row and column.

**Expected Output Format:**
- The `reserve()` method returns an integer array `[row, col]` representing the reserved seat.
- The `unreserve(row, col)` method does not return any value.

**Key Requirements and Edge Cases to Consider:**
- The seat reservation manager should allocate seats in a way that minimizes the row number and maximizes the column number.
- If there are no available seats, the `reserve()` method should return an empty array.
- The `unreserve(row, col)` method should only unreserve a seat that was previously reserved.

**Example Test Cases with Explanations:**
- `SeatManager(1)`: Initializes the seat reservation manager with 1 row of seats.
- `reserve()`: Reserves a seat and returns the row and column of the reserved seat. For example, `[0, 9]`.
- `unreserve(0, 9)`: Unreserves the seat at row 0 and column 9.
- `reserve()`: Reserves another seat and returns the row and column of the reserved seat. For example, `[0, 8]`.

---

### Brute Force Approach

**Explanation:**
- Initialize a 2D array `seats` to represent the seats in the theater, where `seats[i][j]` represents the seat at row `i` and column `j`.
- In the `reserve()` method, iterate over the rows and columns to find an available seat and reserve it.
- In the `unreserve(row, col)` method, simply set the seat at the given row and column to available.

```cpp
class SeatManager {
private:
    vector<vector<bool>> seats;

public:
    SeatManager(int n_rows) {
        seats.resize(n_rows, vector<bool>(10, false));
    }

    vector<int> reserve() {
        for (int i = 0; i < seats.size(); i++) {
            for (int j = 9; j >= 0; j--) {
                if (!seats[i][j]) {
                    seats[i][j] = true;
                    return {i, j};
                }
            }
        }
        return {};
    }

    void unreserve(int row, int col) {
        seats[row][col] = false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10)$, where $n$ is the number of rows. This is because in the worst case, we need to iterate over all rows and columns to find an available seat.
> - **Space Complexity:** $O(n \cdot 10)$, where $n$ is the number of rows. This is because we need to store the availability of each seat in the `seats` array.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it uses a simple iterative approach to find an available seat and stores the availability of each seat in an array.

---

### Optimal Approach (Required)

**Explanation:**
- Use a priority queue to store the available seats, where the priority is the row number and the column number.
- In the `reserve()` method, simply pop the seat with the highest priority from the queue and reserve it.
- In the `unreserve(row, col)` method, push the unreserved seat back into the queue.

```cpp
class SeatManager {
private:
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> available_seats;

public:
    SeatManager(int n_rows) {
        for (int i = 0; i < n_rows; i++) {
            for (int j = 9; j >= 0; j--) {
                available_seats.push({i, j});
            }
        }
    }

    vector<int> reserve() {
        if (available_seats.empty()) {
            return {};
        }
        pair<int, int> seat = available_seats.top();
        available_seats.pop();
        return {seat.first, seat.second};
    }

    void unreserve(int row, int col) {
        available_seats.push({row, col});
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of seats. This is because we use a priority queue to store the available seats, and the `push` and `pop` operations have a time complexity of $O(\log n)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of seats. This is because we need to store the available seats in the priority queue.
> - **Optimality proof:** The optimal approach is optimal because it uses a priority queue to store the available seats, which allows us to find the seat with the highest priority in $O(\log n)$ time. This is the best possible time complexity because we need to consider all available seats to find the one with the highest priority.

---

### Final Notes

**Learning Points:**
- The importance of using data structures such as priority queues to optimize the solution.
- The trade-off between time and space complexity in the brute force and optimal approaches.
- The use of `greater` as the comparison function in the priority queue to get the seat with the highest priority.

**Mistakes to Avoid:**
- Not considering the time and space complexity of the solution.
- Not using a priority queue to store the available seats, which leads to a high time complexity.
- Not handling the case where there are no available seats in the `reserve()` method.