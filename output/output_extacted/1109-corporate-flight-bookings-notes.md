## Corporate Flight Bookings

**Problem Link:** [https://leetcode.com/problems/corporate-flight-bookings/description](https://leetcode.com/problems/corporate-flight-bookings/description)

**Problem Statement:**
- Input: `bookings` array where each element is a pair `[start, end, seats]`, and an integer `n` representing the number of flights.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= bookings.length <= 2 * 10^5`, `1 <= start < end <= n`, `1 <= seats <= 10^8`.
- Expected output: An array of length `n` where each element at index `i` represents the total number of seats booked for the `i-th` flight.
- Key requirements: Calculate the total number of seats booked for each flight considering all bookings.
- Example test cases:
  - Input: `bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5`
    - Output: `[10,55,45,25,25]`
  - Explanation: For the first flight, there are 10 seats booked. For the second flight, there are 10 seats from the first booking and 20 seats from the second booking, plus 25 seats from the third booking, totaling 55 seats.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each booking and updating the seat count for each flight within the booking's range.
- Step-by-step breakdown:
  1. Initialize an array `seats` of length `n` with all elements set to 0, representing the number of seats booked for each flight.
  2. Iterate through each booking in the `bookings` array.
  3. For each booking, iterate from `start` to `end - 1` (inclusive) and add the `seats` value of the current booking to the corresponding index in the `seats` array.
  4. After processing all bookings, return the `seats` array.

```cpp
vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
    vector<int> seats(n, 0);
    for (auto& booking : bookings) {
        int start = booking[0] - 1; // Adjust for 0-based index
        int end = booking[1] - 1; // Adjust for 0-based index
        int bookedSeats = booking[2];
        for (int i = start; i <= end; ++i) {
            seats[i] += bookedSeats;
        }
    }
    return seats;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of flights and $m$ is the number of bookings, because in the worst case, we might need to iterate through all flights for each booking.
> - **Space Complexity:** $O(n)$ for storing the `seats` array.
> - **Why these complexities occur:** The brute force approach involves nested iterations over bookings and flights, leading to high time complexity. The space complexity is linear due to the need to store the seat count for each flight.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `difference array` or `prefix sum` approach to efficiently calculate the total seats booked for each flight.
- Step-by-step breakdown:
  1. Initialize an array `diff` of length `n + 1` with all elements set to 0. This array will store the differences in seat counts between consecutive flights.
  2. Iterate through each booking and update the `diff` array:
    - At the start of the booking (`start`), add the `seats` value to `diff[start]`.
    - At the end of the booking (`end + 1`), subtract the `seats` value from `diff[end + 1]`.
  3. Calculate the prefix sum of the `diff` array to obtain the total seats booked for each flight.
  4. Return the prefix sum array (excluding the last element which is always 0).

```cpp
vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
    vector<int> diff(n + 1, 0);
    for (auto& booking : bookings) {
        int start = booking[0];
        int end = booking[1];
        int seats = booking[2];
        diff[start - 1] += seats; // Adjust for 0-based index
        diff[end] -= seats;
    }
    vector<int> result;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += diff[i];
        result.push_back(sum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of flights and $m$ is the number of bookings, because we only need to iterate through each booking once and then calculate the prefix sum.
> - **Space Complexity:** $O(n)$ for storing the `diff` and `result` arrays.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to calculate the total seats booked for each flight, leveraging the concept of difference arrays to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Difference array or prefix sum approach for efficient calculation of cumulative sums.
- Problem-solving patterns identified: Using auxiliary arrays to store differences or prefix sums to simplify calculations.
- Optimization techniques learned: Minimizing redundant calculations by leveraging properties of arrays and prefix sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to adjust for 0-based indexing, or misinterpreting the problem statement.
- Edge cases to watch for: Handling bookings that start or end at the first or last flight, ensuring correct calculation for these edge cases.
- Performance pitfalls: Using brute force approaches that lead to high time complexity, neglecting the use of efficient algorithms and data structures.