## Find the Longest Valid Obstacle Course at Each Position

**Problem Link:** https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description

**Problem Statement:**
- Input format: An array of integers `obstacles` representing the heights of obstacles.
- Constraints: `1 <= obstacles.length <= 10^5`, `1 <= obstacles[i] <= 10^6`.
- Expected output format: An array of integers where each element at index `i` represents the length of the longest valid obstacle course at position `i`.
- Key requirements and edge cases to consider: A valid obstacle course is one where the height of each obstacle is greater than or equal to the height of the previous obstacle, or if the height is less than the previous obstacle, there must be a previous obstacle with a height less than or equal to the current obstacle.
- Example test cases with explanations: 
    - For `obstacles = [1,2,3,2]`, the output should be `[1,2,3,3]` because at each position, we can form a valid obstacle course by including the current obstacle if its height is greater than or equal to the previous one or if there's a previous obstacle that's smaller.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the longest valid obstacle course at each position, we can check all previous obstacles to see if we can extend the course.
- Step-by-step breakdown of the solution:
    1. For each obstacle, iterate over all previous obstacles.
    2. Check if the current obstacle can be added to the course by comparing its height with the previous obstacles.
    3. If it can be added, update the length of the longest valid obstacle course at the current position.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks all possibilities.

```cpp
vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
    int n = obstacles.size();
    vector<int> result(n);
    for (int i = 0; i < n; ++i) {
        int maxLength = 1; // Minimum length is 1 (the obstacle itself)
        for (int j = 0; j < i; ++j) {
            if (obstacles[i] >= obstacles[j]) {
                maxLength = max(maxLength, result[j] + 1);
            }
        }
        result[i] = maxLength;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each of the $n$ obstacles, we potentially iterate over all previous obstacles.
> - **Space Complexity:** $O(n)$ for storing the lengths of the longest valid obstacle courses at each position.
> - **Why these complexities occur:** The nested loop structure causes the quadratic time complexity, and we need to store the result for each obstacle, hence the linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the correct position to insert the current obstacle in a sorted list of obstacles that form a valid course. This is because a valid course can be represented as a sorted list where each element is the height of an obstacle.
- Detailed breakdown of the approach:
    1. Initialize an empty list `courses` to store the heights of obstacles in valid courses.
    2. For each obstacle, find the first course in `courses` that is greater than the current obstacle's height using binary search. If no such course exists, append the current obstacle's height to `courses`.
    3. Update the length of the longest valid obstacle course at the current position based on the found or inserted course.
- Proof of optimality: This approach ensures that we always consider the longest possible valid course that can be extended by the current obstacle, thus maximizing the length at each position.
- Why further optimization is impossible: This approach already minimizes the number of comparisons needed by using binary search, making it optimal for this problem.

```cpp
vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
    int n = obstacles.size();
    vector<int> result(n);
    vector<int> courses; // Stores the heights of obstacles in valid courses
    
    for (int i = 0; i < n; ++i) {
        auto it = upper_bound(courses.begin(), courses.end(), obstacles[i]);
        if (it == courses.end()) {
            // If no course is greater, append to the end
            courses.push_back(obstacles[i]);
            result[i] = courses.size();
        } else {
            // Replace the first course greater than the current obstacle
            *it = obstacles[i];
            result[i] = it - courses.begin() + 1;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ because for each obstacle, we perform a binary search in the `courses` list, which has at most $n$ elements.
> - **Space Complexity:** $O(n)$ for storing the `courses` list.
> - **Optimality proof:** The use of binary search to find the appropriate position in the `courses` list minimizes the number of comparisons, making this approach optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and dynamic programming (implicitly through the use of the `courses` list to track valid courses).
- Problem-solving patterns identified: Using a sorted list to represent a valid sequence and updating it efficiently.
- Optimization techniques learned: Applying binary search to reduce the time complexity.
- Similar problems to practice: Other problems involving finding the longest increasing subsequence or similar constructs.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the binary search or updating the `courses` list.
- Edge cases to watch for: Handling the case when the `courses` list is empty or when the current obstacle's height is less than all previous ones.
- Performance pitfalls: Using a linear search instead of binary search, leading to higher time complexity.
- Testing considerations: Ensuring that the solution works correctly for obstacles of varying heights and for both increasing and decreasing sequences.