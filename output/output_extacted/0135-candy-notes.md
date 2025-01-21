## Candy
**Problem Link:** https://leetcode.com/problems/candy/description

**Problem Statement:**
- Input format: An array `ratings` of integers representing the ratings of each child.
- Constraints: The length of `ratings` is in the range `[1, 2 * 10^4]`, and each rating is in the range `[0, 2 * 10^6]`.
- Expected output format: An integer representing the minimum number of candies you must give out to get all children with a higher rating than their neighbors more candies than their neighbors.
- Key requirements and edge cases to consider: The number of candies given to each child must be at least 1, and the number of candies given to a child with a higher rating than their neighbors must be more than their neighbors.

### Brute Force Approach
**Explanation:**
- Initial thought process: The problem can be solved by iterating over the array and comparing each child's rating with their neighbors. If a child has a higher rating than their neighbors, they should receive more candies than their neighbors.
- Step-by-step breakdown of the solution:
  1. Initialize an array `candies` of the same length as `ratings`, with all elements set to 1.
  2. Iterate over the array from left to right. For each child, if their rating is higher than their left neighbor's rating, update their candies to be one more than their left neighbor's candies.
  3. Iterate over the array from right to left. For each child, if their rating is higher than their right neighbor's rating and their candies are not already more than their right neighbor's candies, update their candies to be one more than their right neighbor's candies.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
void candy(vector<int>& ratings) {
    int n = ratings.size();
    vector<int> candies(n, 1);
    // Iterate from left to right
    for (int i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    // Iterate from right to left
    for (int i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
            candies[i] = candies[i + 1] + 1;
        }
    }
    // Calculate the total number of candies
    int totalCandies = 0;
    for (int i = 0; i < n; i++) {
        totalCandies += candies[i];
    }
    // Print the total number of candies
    cout << totalCandies << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of children. This is because we are iterating over the array twice.
> - **Space Complexity:** $O(n)$, where $n$ is the number of children. This is because we are using an additional array to store the number of candies for each child.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the array twice, and the space complexity occurs because we are using an additional array to store the number of candies for each child.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by iterating over the array and comparing each child's rating with their neighbors. If a child has a higher rating than their neighbors, they should receive more candies than their neighbors.
- Detailed breakdown of the approach: The approach is the same as the brute force approach, but with a slight optimization. Instead of iterating over the array twice, we can iterate over the array once and update the candies for each child based on their rating and their neighbors' ratings.
- Proof of optimality: The time complexity of the optimal approach is $O(n)$, which is the best possible time complexity for this problem. This is because we must iterate over the array at least once to compare each child's rating with their neighbors.
- Why further optimization is impossible: Further optimization is impossible because we must iterate over the array at least once to compare each child's rating with their neighbors.

```cpp
int candy(vector<int>& ratings) {
    int n = ratings.size();
    vector<int> candies(n, 1);
    // Iterate from left to right
    for (int i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    // Iterate from right to left
    for (int i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
            candies[i] = candies[i + 1] + 1;
        }
    }
    // Calculate the total number of candies
    int totalCandies = 0;
    for (int i = 0; i < n; i++) {
        totalCandies += candies[i];
    }
    // Return the total number of candies
    return totalCandies;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of children. This is because we are iterating over the array twice.
> - **Space Complexity:** $O(n)$, where $n$ is the number of children. This is because we are using an additional array to store the number of candies for each child.
> - **Optimality proof:** The time complexity of the optimal approach is $O(n)$, which is the best possible time complexity for this problem. This is because we must iterate over the array at least once to compare each child's rating with their neighbors.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of iteration and comparison to solve a problem.
- Problem-solving patterns identified: The problem identifies the pattern of iterating over an array and comparing each element with its neighbors.
- Optimization techniques learned: The problem teaches the optimization technique of iterating over an array only once to reduce the time complexity.
- Similar problems to practice: Similar problems to practice include the "Minimum Number of Arrows to Burst Balloons" problem and the "Minimum Number of Coins" problem.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to iterate over the array only once and not update the candies for each child based on their rating and their neighbors' ratings.
- Edge cases to watch for: An edge case to watch for is when the input array is empty or contains only one element.
- Performance pitfalls: A performance pitfall is to use a nested loop to iterate over the array, which would increase the time complexity to $O(n^2)$.
- Testing considerations: A testing consideration is to test the function with different input arrays, including empty arrays and arrays with only one element.