## Number of People That Can Be Seen in a Grid

**Problem Link:** https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/description

**Problem Statement:**
- Input: A 2D array `people` where `people[i][j]` represents the height of the person standing in the `i-th` row and `j-th` column.
- Constraints: The number of rows and columns in the grid is in the range `[1, 100]`. The height of each person is in the range `[1, 100]`.
- Expected Output: The number of people that can be seen in the grid.
- Key Requirements: A person can be seen if there is no person standing in front of them who is taller or of the same height.
- Edge Cases: If there are multiple people of the same height in a column, only the one at the back can be seen.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each person in the grid and check if they can be seen by comparing their height with the heights of people standing in front of them.
- We will use two nested loops to iterate over each person in the grid.
- For each person, we will check if they can be seen by comparing their height with the heights of people standing in front of them.

```cpp
int maxPeopleVisible(vector<vector<int>>& people) {
    int count = 0;
    for (int i = 0; i < people.size(); i++) {
        for (int j = 0; j < people[i].size(); j++) {
            bool canBeSeen = true;
            for (int k = 0; k < i; k++) {
                if (people[k][j] >= people[i][j]) {
                    canBeSeen = false;
                    break;
                }
            }
            if (canBeSeen) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of rows and $m$ is the number of columns. This is because we are using three nested loops to iterate over each person in the grid.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity occurs because we are using three nested loops, and the space complexity is constant because we are not using any extra space.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a single loop to iterate over each column and keep track of the maximum height seen so far.
- For each person in the column, we will check if they can be seen by comparing their height with the maximum height seen so far.
- If a person can be seen, we will increment the count and update the maximum height seen so far.

```cpp
int maxPeopleVisible(vector<vector<int>>& people) {
    int count = 0;
    for (int j = 0; j < people[0].size(); j++) {
        int maxHeight = 0;
        for (int i = people.size() - 1; i >= 0; i--) {
            if (people[i][j] > maxHeight) {
                count++;
                maxHeight = people[i][j];
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of rows and $m$ is the number of columns. This is because we are using two nested loops to iterate over each column and each person in the column.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with input size.
> - **Optimality proof:** This is the optimal solution because we are only iterating over each person in the grid once, and we are using a single loop to keep track of the maximum height seen so far.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, comparison, and counting.
- Problem-solving patterns identified: using a single loop to keep track of the maximum height seen so far.
- Optimization techniques learned: reducing the number of loops and comparisons.

**Mistakes to Avoid:**
- Common implementation errors: using unnecessary loops or comparisons.
- Edge cases to watch for: people of the same height in a column.
- Performance pitfalls: using too many loops or comparisons.
- Testing considerations: testing with different input sizes and edge cases.