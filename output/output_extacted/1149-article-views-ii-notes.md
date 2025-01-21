## Article Views II
**Problem Link:** https://leetcode.com/problems/article-views-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the number of views for each article within a given time range. We're given a list of `views` where each view is represented as `[article_id, author_id, view_time]`, and a list of `queries` where each query is represented as `[article_id, timestamp]`. The task is to determine the number of views for each article at the specified timestamp.
- Expected output format: The output should be a list of integers where each integer represents the number of views for the corresponding article at the specified timestamp.
- Key requirements and edge cases to consider: We need to ensure that we're counting views that occur before or at the specified timestamp. We should also handle cases where there are multiple views for the same article and cases where there are no views for an article.
- Example test cases with explanations:
    - For example, given `views = [[1, 3, 5], [1, 3, 7], [2, 4, 6], [2, 4, 8]]` and `queries = [[1, 5], [2, 7]]`, the output should be `[2, 1]` because article 1 has 2 views before or at timestamp 5, and article 2 has 1 view before or at timestamp 7.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One straightforward way to solve this problem is to iterate through each query and count the number of views for the corresponding article that occur before or at the specified timestamp.
- Step-by-step breakdown of the solution:
    1. Iterate through each query.
    2. For each query, iterate through each view.
    3. If the view is for the same article and occurs before or at the specified timestamp, increment the count.
    4. After checking all views, add the count to the result list.
- Why this approach comes to mind first: This approach is intuitive because it directly addresses the problem statement by counting views for each article at the specified timestamp.

```cpp
vector<int> articleViewsII(vector<vector<int>>& views, vector<vector<int>>& queries) {
    vector<int> result;
    for (auto& query : queries) {
        int article_id = query[0];
        int timestamp = query[1];
        int count = 0;
        for (auto& view : views) {
            if (view[0] == article_id && view[2] <= timestamp) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot v)$, where $q$ is the number of queries and $v$ is the number of views, because for each query, we potentially iterate through all views.
> - **Space Complexity:** $O(q)$, where $q$ is the number of queries, because we store the result for each query.
> - **Why these complexities occur:** The time complexity is high because we use nested loops to iterate through queries and views. The space complexity is relatively low because we only store the count for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can improve the solution by sorting the views by article ID and timestamp. This allows us to use a single pass through the sorted views to count the views for each article at the specified timestamp.
- Detailed breakdown of the approach:
    1. Sort the views by article ID and timestamp.
    2. Iterate through each query.
    3. For each query, use a binary search to find the last view that occurs before or at the specified timestamp.
    4. Count the number of views for the article that occur before or at the specified timestamp.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(q \cdot v)$ to $O(v \log v + q \log v)$, where $v$ is the number of views and $q$ is the number of queries.

```cpp
vector<int> articleViewsII(vector<vector<int>>& views, vector<vector<int>>& queries) {
    sort(views.begin(), views.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] != b[0]) return a[0] < b[0];
        return a[2] < b[2];
    });
    vector<int> result;
    for (auto& query : queries) {
        int article_id = query[0];
        int timestamp = query[1];
        int count = 0;
        auto it = lower_bound(views.begin(), views.end(), vector<int>{article_id, 0, timestamp + 1}, [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[2] < b[2];
        });
        if (it != views.begin()) {
            it--;
        }
        while (it != views.begin() && it->0 == article_id && it->2 <= timestamp) {
            count++;
            it--;
        }
        if (it != views.end() && it->0 == article_id && it->2 <= timestamp) {
            count++;
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(v \log v + q \log v)$, where $v$ is the number of views and $q$ is the number of queries, because we sort the views and use binary search to find the last view that occurs before or at the specified timestamp.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store the count and the iterator.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity by using a sorted data structure and binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, binary search, and counting.
- Problem-solving patterns identified: Using a sorted data structure to improve the efficiency of queries.
- Optimization techniques learned: Reducing the time complexity by using a single pass through the sorted data and binary search.
- Similar problems to practice: Problems that involve counting or querying a sorted data structure.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty input or a query with no matching views.
- Edge cases to watch for: Handling cases where there are multiple views for the same article and cases where there are no views for an article.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.