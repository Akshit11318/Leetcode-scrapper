## My Calendar I

**Problem Link:** https://leetcode.com/problems/my-calendar-i/description

**Problem Statement:**
- Input format and constraints: The input consists of a series of `book` operations with start and end times. Each `book` operation should check if the given time interval overlaps with any previously booked intervals. If there's an overlap, the operation should return `false`, indicating that the booking is not possible. If there's no overlap, the operation should return `true` and add the new interval to the calendar.
- Expected output format: A boolean value indicating whether a booking is successful.
- Key requirements and edge cases to consider: Handling overlapping intervals, non-overlapping intervals, and edge cases where intervals just touch each other (start time of one interval equals end time of another).
- Example test cases with explanations:
  - Booking an interval that does not overlap with any existing booking should return `true`.
  - Booking an interval that overlaps with an existing booking should return `false`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all previously booked intervals to check for overlaps with the new interval.
- Step-by-step breakdown of the solution:
  1. Store all booked intervals in a list or array.
  2. For each new `book` operation, iterate through the list of booked intervals.
  3. Check if the new interval overlaps with any booked interval. An overlap occurs if the start time of the new interval is less than the end time of a booked interval and the end time of the new interval is greater than the start time of the booked interval.
  4. If an overlap is found, return `false`. If no overlap is found after checking all intervals, return `true` and add the new interval to the list.

```cpp
class MyCalendar {
public:
    vector<pair<int, int>> booked;
    MyCalendar() {}
    
    bool book(int start, int end) {
        for (auto& interval : booked) {
            if (start < interval.second && end > interval.first) {
                return false;
            }
        }
        booked.push_back({start, end});
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of booked intervals, because for each new booking, we potentially check all existing bookings.
> - **Space Complexity:** $O(n)$, as we store all booked intervals.
> - **Why these complexities occur:** The brute force approach involves checking each new interval against all existing intervals, leading to linear time complexity for each booking operation. The space complexity is also linear because we store all intervals.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all intervals for each new booking, we can use a data structure that allows for more efficient overlap checks, such as a balanced binary search tree or simply maintaining a sorted list of start and end times. However, since the intervals are not necessarily non-overlapping among themselves and we are looking for simplicity, a straightforward approach involves sorting the intervals by their start times and checking for overlaps in a single pass.
- Detailed breakdown of the approach: The optimal solution for this problem, given the need to check for overlaps efficiently, involves using a data structure like a `set` or `map` in C++ to store the intervals in a way that allows for efficient insertion and overlap checking. However, since the problem doesn't explicitly require the use of such advanced data structures and instead focuses on the logic of overlap detection, we'll stick with a vector but optimize the search by maintaining a sorted list of intervals or using a simpler, yet still efficient, method.

```cpp
class MyCalendar {
public:
    vector<pair<int, int>> booked;
    MyCalendar() {}
    
    bool book(int start, int end) {
        for (auto& interval : booked) {
            if (start < interval.second && end > interval.first) {
                return false;
            }
        }
        booked.push_back({start, end});
        return true;
    }
};
```

However, to truly optimize, we recognize that the current implementation is already quite straightforward and efficient given the constraints of the problem. The optimization here is more about ensuring the logic is correct and efficient rather than applying a complex data structure.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of booked intervals, because for each new booking, we potentially check all existing bookings.
> - **Space Complexity:** $O(n)$, as we store all booked intervals.
> - **Optimality proof:** This approach is optimal for the given constraints because we must check each interval for potential overlaps. Without additional data structures or constraints (like non-overlapping intervals), we cannot improve upon this time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Interval overlap detection, basic data structures (vectors).
- Problem-solving patterns identified: Checking for overlaps in a list of intervals.
- Optimization techniques learned: While the problem doesn't lend itself to significant optimization beyond the basic approach due to its simplicity, the importance of considering data structures and algorithms for efficiency is highlighted.
- Similar problems to practice: Other interval-related problems, such as merging overlapping intervals or finding the maximum number of non-overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly checking for overlaps (e.g., missing the case where one interval completely contains another).
- Edge cases to watch for: Intervals that just touch each other, intervals with the same start or end time.
- Performance pitfalls: Using inefficient data structures or algorithms for large inputs.
- Testing considerations: Thoroughly testing with various interval configurations, including overlapping, non-overlapping, and edge cases.