## Maximize Distance to Closest Person

**Problem Link:** https://leetcode.com/problems/maximize-distance-to-closest-person/description

**Problem Statement:**
- Input format and constraints: You are given an integer array `seats` representing a row of seats where `seats[i] = 1` means the seat at index `i` is occupied, and `seats[i] = 0` means the seat at index `i` is empty. The array is guaranteed to have at least one empty seat and one occupied seat. The goal is to maximize the minimum distance to the nearest occupied seat for any person sitting in an empty seat.
- Expected output format: The function should return the maximum minimum distance to the nearest occupied seat.
- Key requirements and edge cases to consider: The function should handle edge cases such as a single occupied seat, a single empty seat, and cases where there are multiple occupied seats with varying distances to the nearest empty seat.
- Example test cases with explanations: 
  - For the input `seats = [1,0,0,0,1,0,1]`, the output should be `2` because the person can sit in the middle seat to maximize the minimum distance to the nearest occupied seat.
  - For the input `seats = [1,0,0,0,1]`, the output should be `2` because the person can sit in the middle seat to maximize the minimum distance to the nearest occupied seat.
  - For the input `seats = [0,1]`, the output should be `1` because the person can sit in the first seat to maximize the minimum distance to the nearest occupied seat.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible seating arrangement to find the one that maximizes the minimum distance to the nearest occupied seat.
- Step-by-step breakdown of the solution: 
  1. Iterate over each empty seat in the `seats` array.
  2. For each empty seat, calculate the minimum distance to the nearest occupied seat by checking the distances to the previous and next occupied seats.
  3. Keep track of the maximum minimum distance found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs because it involves checking every possible seating arrangement.

```cpp
int maxDistToClosest(vector<int>& seats) {
    int max_min_distance = 0;
    for (int i = 0; i < seats.size(); i++) {
        if (seats[i] == 0) {
            int min_distance = INT_MAX;
            for (int j = 0; j < seats.size(); j++) {
                if (seats[j] == 1) {
                    min_distance = min(min_distance, abs(i - j));
                }
            }
            max_min_distance = max(max_min_distance, min_distance);
        }
    }
    return max_min_distance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of seats, because for each empty seat, we are checking all other seats to find the minimum distance to the nearest occupied seat.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the maximum minimum distance and the minimum distance for each empty seat.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are using nested loops to check all possible seating arrangements, and the space complexity is $O(1)$ because we are only using a constant amount of space to store the maximum minimum distance and the minimum distance for each empty seat.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible seating arrangements, we can use a single pass to find the maximum minimum distance to the nearest occupied seat.
- Detailed breakdown of the approach: 
  1. Initialize variables to keep track of the maximum minimum distance and the previous occupied seat index.
  2. Iterate over the `seats` array from left to right to find the maximum minimum distance to the nearest occupied seat on the left side.
  3. Iterate over the `seats` array from right to left to find the maximum minimum distance to the nearest occupied seat on the right side.
  4. Keep track of the maximum minimum distance found so far.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem because we must check each seat at least once to find the maximum minimum distance.

```cpp
int maxDistToClosest(vector<int>& seats) {
    int max_min_distance = 0;
    int prev_occupied = -1;
    for (int i = 0; i < seats.size(); i++) {
        if (seats[i] == 1) {
            if (prev_occupied == -1) {
                max_min_distance = max(max_min_distance, i);
            } else {
                max_min_distance = max(max_min_distance, (i - prev_occupied) / 2);
            }
            prev_occupied = i;
        }
    }
    max_min_distance = max(max_min_distance, seats.size() - 1 - prev_occupied);
    return max_min_distance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of seats, because we are making a single pass over the `seats` array.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the maximum minimum distance and the previous occupied seat index.
> - **Optimality proof:** This approach is optimal because we must check each seat at least once to find the maximum minimum distance, and we are doing so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The optimal approach demonstrates the use of a single pass to find the maximum minimum distance to the nearest occupied seat.
- Problem-solving patterns identified: The problem-solving pattern used here is to iterate over the `seats` array from left to right and right to left to find the maximum minimum distance to the nearest occupied seat.
- Optimization techniques learned: The optimization technique used here is to use a single pass to find the maximum minimum distance instead of checking all possible seating arrangements.
- Similar problems to practice: Similar problems to practice include finding the maximum minimum distance to the nearest occupied seat in a 2D array or finding the maximum minimum distance to the nearest occupied seat in a graph.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use nested loops to check all possible seating arrangements, which results in a time complexity of $O(n^2)$.
- Edge cases to watch for: Edge cases to watch for include cases where there is only one occupied seat, cases where there is only one empty seat, and cases where there are multiple occupied seats with varying distances to the nearest empty seat.
- Performance pitfalls: A performance pitfall is to use a brute force approach that checks all possible seating arrangements, which results in a time complexity of $O(n^2)$.
- Testing considerations: Testing considerations include testing the function with different input sizes, testing the function with different input values, and testing the function with edge cases.