## Minimum Absolute Difference Queries
**Problem Link:** https://leetcode.com/problems/minimum-absolute-difference-queries/description

**Problem Statement:**
- Input format and constraints: The input is a list of integers `nums` and a list of queries `queries`. Each query is a list of two integers `[value, pos]`.
- Expected output format: The output is a list of integers where each integer represents the minimum absolute difference for the corresponding query.
- Key requirements and edge cases to consider: For each query, find the minimum absolute difference between the query value and any number in the `nums` array at or to the right of the query position `pos`.
- Example test cases with explanations: 
    - For `nums = [1, 4, 5, 8, 10, 20, 70]` and `queries = [[1, 0], [-3, 2], [4, 3], [5, 4], [8, 6]]`, the output should be `[1, 4, 2, 0, 0]`.

### Brute Force Approach
**Explanation:**
- Initial thought process: For each query, iterate over the `nums` array from the query position to the end and calculate the absolute difference between the query value and each number in the array.
- Step-by-step breakdown of the solution:
    1. Iterate over each query.
    2. For each query, iterate over the `nums` array from the query position to the end.
    3. Calculate the absolute difference between the query value and each number in the array.
    4. Update the minimum absolute difference if a smaller difference is found.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> minAbsoluteDifferenceQueries(vector<int>& nums, vector<vector<int>>& queries) {
    vector<int> result;
    for (auto& query : queries) {
        int minValue = INT_MAX;
        for (int i = query[1]; i < nums.size(); i++) {
            minValue = min(minValue, abs(query[0] - nums[i]));
        }
        result.push_back(minValue);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot q \cdot m)$ where $n$ is the size of `nums`, $q$ is the number of queries, and $m$ is the average number of elements in `nums` from the query position to the end. In the worst case, $m = n$, resulting in a time complexity of $O(n^2 \cdot q)$.
> - **Space Complexity:** $O(q)$ for storing the result of each query.
> - **Why these complexities occur:** The brute force approach involves nested loops: one for iterating over the queries and another for iterating over the `nums` array from the query position to the end.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Create a sorted copy of the `nums` array to enable binary search for finding the closest number to the query value.
- Detailed breakdown of the approach:
    1. Create a sorted copy of the `nums` array.
    2. For each query, use binary search to find the closest number to the query value in the sorted copy of the `nums` array.
    3. If the closest number is at or to the right of the query position, update the minimum absolute difference.
- Proof of optimality: This approach reduces the time complexity from $O(n^2 \cdot q)$ to $O(n \cdot q \cdot log(n))$, which is optimal for this problem.

```cpp
vector<int> minAbsoluteDifferenceQueries(vector<int>& nums, vector<vector<int>>& queries) {
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    vector<int> result;
    for (auto& query : queries) {
        int minValue = INT_MAX;
        auto it = lower_bound(sortedNums.begin(), sortedNums.end(), query[0]);
        if (it != sortedNums.end() && distance(nums.begin(), lower_bound(nums.begin(), nums.end(), *it)) >= query[1]) {
            minValue = min(minValue, abs(query[0] - *it));
        }
        if (it != sortedNums.begin() && distance(nums.begin(), lower_bound(nums.begin(), nums.end(), *(it - 1))) >= query[1]) {
            minValue = min(minValue, abs(query[0] - *(it - 1)));
        }
        result.push_back(minValue == INT_MAX ? -1 : minValue);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot q \cdot log(n))$ where $n$ is the size of `nums` and $q$ is the number of queries.
> - **Space Complexity:** $O(n + q)$ for storing the sorted copy of `nums` and the result of each query.
> - **Optimality proof:** The optimal approach reduces the time complexity by using binary search to find the closest number to the query value, resulting in a significant improvement over the brute force approach.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, sorting, and iteration.
- Problem-solving patterns identified: Using a sorted copy of the input array to enable binary search.
- Optimization techniques learned: Reducing the time complexity by using binary search instead of linear search.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing binary search or sorting.
- Edge cases to watch for: Handling cases where the query position is at the end of the `nums` array or where the query value is not found in the `nums` array.
- Performance pitfalls: Using a brute force approach that results in a high time complexity.
- Testing considerations: Thoroughly testing the implementation with different input scenarios to ensure correctness.