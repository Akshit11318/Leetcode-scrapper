## Daily Leads and Partners
**Problem Link:** https://leetcode.com/problems/daily-leads-and-partners/description

**Problem Statement:**
- Input format and constraints: The problem takes two lists of integers, `dailyLeads` and `dailyPartners`, as input. Each list contains the number of leads and partners for each day, respectively. The constraints are that the lists are non-empty and contain the same number of elements.
- Expected output format: The function should return a list of integers representing the daily leads and partners, sorted in descending order.
- Key requirements and edge cases to consider: The function should handle cases where the input lists are empty or contain different numbers of elements. It should also handle cases where the numbers of leads and partners are equal for a given day.
- Example test cases with explanations: For example, if the input is `dailyLeads = [3, 1, 0, 2]` and `dailyPartners = [2, 2, 0, 2]`, the output should be `[[2, 2], [3, 2], [2, 2], [0, 0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each day's leads and partners, combining them into a list of pairs, and then sorting the list in descending order based on the number of leads and partners.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list `result` to store the daily leads and partners.
  2. Iterate over each day's leads and partners using a for loop.
  3. For each day, combine the leads and partners into a pair and add it to the `result` list.
  4. Sort the `result` list in descending order based on the number of leads and partners.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it involves simple iteration and sorting.

```cpp
vector<vector<int>> dailyLeadsAndPartners(vector<int>& dailyLeads, vector<int>& dailyPartners) {
    vector<vector<int>> result;
    for (int i = 0; i < dailyLeads.size(); i++) {
        result.push_back({dailyLeads[i], dailyPartners[i]});
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0]) {
            return a[1] > b[1];
        }
        return a[0] > b[0];
    });
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of days. This is because the sorting operation takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of days. This is because we need to store the daily leads and partners in a list.
> - **Why these complexities occur:** The time complexity occurs because of the sorting operation, and the space complexity occurs because we need to store the daily leads and partners in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a custom sorting comparator to sort the daily leads and partners in descending order.
- Detailed breakdown of the approach:
  1. Initialize an empty list `result` to store the daily leads and partners.
  2. Iterate over each day's leads and partners using a for loop.
  3. For each day, combine the leads and partners into a pair and add it to the `result` list.
  4. Sort the `result` list in descending order using a custom sorting comparator.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for sorting.
- Why further optimization is impossible: Further optimization is impossible because the time complexity of sorting is already optimal.

```cpp
vector<vector<int>> dailyLeadsAndPartners(vector<int>& dailyLeads, vector<int>& dailyPartners) {
    vector<vector<int>> result;
    for (int i = 0; i < dailyLeads.size(); i++) {
        result.push_back({dailyLeads[i], dailyPartners[i]});
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0]) {
            return a[1] > b[1];
        }
        return a[0] > b[0];
    });
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of days. This is because the sorting operation takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of days. This is because we need to store the daily leads and partners in a list.
> - **Optimality proof:** The time complexity of $O(n \log n)$ is optimal because it is the best possible time complexity for sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Custom sorting comparator, sorting in descending order.
- Problem-solving patterns identified: Using a custom sorting comparator to sort a list of pairs.
- Optimization techniques learned: Using a custom sorting comparator to improve the efficiency of sorting.
- Similar problems to practice: Sorting a list of pairs based on multiple criteria.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as empty input lists.
- Edge cases to watch for: Empty input lists, input lists with different lengths.
- Performance pitfalls: Using an inefficient sorting algorithm, such as bubble sort.
- Testing considerations: Testing the function with different input cases, including edge cases.