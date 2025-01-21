## Hopper Company Queries I
**Problem Link:** https://leetcode.com/problems/hopper-company-queries-i/description

**Problem Statement:**
- Input format and constraints: The problem involves a list of queries, where each query is a tuple of `(query_type, id, time)`. The `query_type` is either 1 or 2, indicating whether the query is for a pickup or a dropoff. The `id` is a unique identifier for the query, and the `time` is the timestamp of the query.
- Expected output format: The output should be a list of integers, where each integer represents the time difference between the pickup and dropoff for each query.
- Key requirements and edge cases to consider: The queries are ordered by time, and each pickup has a corresponding dropoff. If a query is a pickup, the next query with the same `id` must be a dropoff. If a query is a dropoff, the previous query with the same `id` must be a pickup.
- Example test cases with explanations:
    - Example 1: `queries = [(1, 1, 10), (2, 1, 15), (1, 2, 20), (2, 2, 25)]`. The output should be `[5, 5]`, because the time difference between the pickup and dropoff for the first query is 5, and the time difference between the pickup and dropoff for the second query is also 5.

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each query and check if it's a pickup or a dropoff. If it's a pickup, store the time and id. If it's a dropoff, find the corresponding pickup and calculate the time difference.
- Step-by-step breakdown of the solution:
    1. Initialize an empty dictionary to store the pickup times.
    2. Iterate through each query.
    3. If the query is a pickup, store the time in the dictionary with the id as the key.
    4. If the query is a dropoff, find the corresponding pickup time in the dictionary and calculate the time difference.
    5. Store the time difference in a list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it simply iterates through each query and performs the necessary calculations.

```cpp
vector<int> find_time_difference(vector<vector<int>>& queries) {
    unordered_map<int, int> pickup_times;
    vector<int> time_differences;
    
    for (auto& query : queries) {
        int query_type = query[0];
        int id = query[1];
        int time = query[2];
        
        if (query_type == 1) {
            pickup_times[id] = time;
        } else {
            int pickup_time = pickup_times[id];
            int time_difference = time - pickup_time;
            time_differences.push_back(time_difference);
        }
    }
    
    return time_differences;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of queries. This is because we iterate through each query once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries. This is because we store the pickup times in a dictionary, which can potentially store all queries.
> - **Why these complexities occur:** The time complexity is linear because we iterate through each query once. The space complexity is also linear because we store the pickup times in a dictionary, which can potentially store all queries.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the pickup times and calculate the time differences in a single pass through the queries.
- Detailed breakdown of the approach:
    1. Initialize an empty dictionary to store the pickup times.
    2. Iterate through each query.
    3. If the query is a pickup, store the time in the dictionary with the id as the key.
    4. If the query is a dropoff, find the corresponding pickup time in the dictionary and calculate the time difference.
    5. Store the time difference in a list.
- Proof of optimality: This approach is optimal because it only requires a single pass through the queries and uses a dictionary to store the pickup times, which allows for constant-time lookups.

```cpp
vector<int> find_time_difference(vector<vector<int>>& queries) {
    unordered_map<int, int> pickup_times;
    vector<int> time_differences;
    
    for (auto& query : queries) {
        int query_type = query[0];
        int id = query[1];
        int time = query[2];
        
        if (query_type == 1) {
            pickup_times[id] = time;
        } else {
            int pickup_time = pickup_times[id];
            int time_difference = time - pickup_time;
            time_differences.push_back(time_difference);
        }
    }
    
    return time_differences;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of queries. This is because we iterate through each query once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries. This is because we store the pickup times in a dictionary, which can potentially store all queries.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the queries and uses a dictionary to store the pickup times, which allows for constant-time lookups.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store and retrieve data in constant time.
- Problem-solving patterns identified: Iterating through a list of queries and performing calculations based on the query type.
- Optimization techniques learned: Using a dictionary to store pickup times and calculate time differences in a single pass through the queries.
- Similar problems to practice: Problems that involve iterating through a list of queries and performing calculations based on the query type.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a pickup time exists in the dictionary before trying to retrieve it.
- Edge cases to watch for: Queries with invalid or missing data.
- Performance pitfalls: Using a data structure with slow lookup times, such as a list, to store pickup times.
- Testing considerations: Testing the function with a variety of input queries, including edge cases and invalid data.