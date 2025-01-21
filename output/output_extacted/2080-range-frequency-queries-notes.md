## Range Frequency Queries
**Problem Link:** https://leetcode.com/problems/range-frequency-queries/description

**Problem Statement:**
- Input format: `arr`, an array of integers, and `queries`, a 2D array of queries where each query is in the format `[left, right, value]`.
- Constraints: `1 <= arr.length <= 100000`, `1 <= queries.length <= 100000`, `0 <= left <= right < arr.length`, and `1 <= value <= 10^9`.
- Expected output format: An array of booleans where each boolean corresponds to the result of a query.
- Key requirements and edge cases to consider: Handling queries that span the entire array, queries with identical left and right indices, and queries where the value is not present in the specified range.
- Example test cases with explanations:
    - For `arr = [12, 33, 4, 56, 22, 2, 34, 33, 33, 78, 78, 78]` and `queries = [[1, 2, 4], [3, 4, 33], [5, 7, 33], [0, 11, 78]]`, the output should be `[true, true, true, true]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate over the specified range in the array and count the occurrences of the given value.
- Step-by-step breakdown of the solution:
    1. Iterate over each query.
    2. For each query, iterate over the specified range in the array.
    3. Count the occurrences of the given value within the range.
    4. Check if the count matches the query's requirement (in this case, simply if the value exists or not, but the approach can be generalized).
- Why this approach comes to mind first: It directly addresses the problem statement by checking each query against the array.

```cpp
vector<bool> answerQueries(vector<int>& arr, vector<vector<int>>& queries) {
    vector<bool> results;
    for (auto& query : queries) {
        int left = query[0], right = query[1], value = query[2];
        int count = 0;
        for (int i = left; i <= right; ++i) {
            if (arr[i] == value) {
                count++;
            }
        }
        results.push_back(count > 0);
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of queries, $m$ is the average length of the query range, and $k$ is the number of elements in the array that need to be checked for each query. However, in the worst case, $m$ could be as large as the size of the array, making the time complexity $O(n \cdot k^2)$ where $k$ is the size of the array.
> - **Space Complexity:** $O(n)$ for storing the results of the queries.
> - **Why these complexities occur:** The brute force approach involves iterating over the array for each query, leading to high time complexity. The space complexity is relatively low as we only need to store the results of the queries.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a data structure that allows for efficient range queries, such as a segment tree or a prefix sum array, but since the problem specifically asks for the existence of a value within a range, a more straightforward approach is to use a hash map to store the indices of each number in the array and then for each query, check the range in the hash map.
- Detailed breakdown of the approach:
    1. Create a hash map where the keys are the numbers in the array and the values are vectors of indices where each number appears.
    2. For each query, use the hash map to find the indices of the given value.
    3. Check if any of these indices fall within the query's range.
- Proof of optimality: This approach is optimal because it reduces the time complexity of checking each query from linear to logarithmic or even constant time in the case of hash map lookups, assuming a good hash function.

```cpp
vector<bool> answerQueries(vector<int>& arr, vector<vector<int>>& queries) {
    unordered_map<int, vector<int>> indexMap;
    for (int i = 0; i < arr.size(); ++i) {
        indexMap[arr[i]].push_back(i);
    }
    
    vector<bool> results;
    for (auto& query : queries) {
        int left = query[0], right = query[1], value = query[2];
        if (indexMap.find(value) == indexMap.end()) {
            results.push_back(false);
            continue;
        }
        
        auto& indices = indexMap[value];
        auto it = lower_bound(indices.begin(), indices.end(), left);
        if (it != indices.end() && *it <= right) {
            results.push_back(true);
        } else {
            results.push_back(false);
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log k)$, where $n$ is the size of the array, $m$ is the number of queries, and $k$ is the average number of occurrences of a value. This is because creating the index map takes $O(n)$ time, and for each query, finding the appropriate range in the index map takes $O(\log k)$ time due to the use of `lower_bound`.
> - **Space Complexity:** $O(n)$ for storing the index map.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity of both creating the data structure and querying it, leveraging the efficiency of hash maps and binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient range querying, use of hash maps for indexing, and binary search for finding ranges.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (e.g., creating an index map and then querying it).
- Optimization techniques learned: Using appropriate data structures to reduce time complexity.
- Similar problems to practice: Other range query problems, such as finding the sum or minimum/maximum within a range.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty arrays or queries), not validating inputs.
- Edge cases to watch for: Queries that span the entire array, queries with identical left and right indices, and queries where the value is not present in the specified range.
- Performance pitfalls: Using inefficient data structures or algorithms for range queries.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large datasets.