## Calculate Salaries
**Problem Link:** https://leetcode.com/problems/calculate-salaries/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of employee records, each containing `id`, `month`, `salary`, and `bonus`. The task is to calculate the total salary for each employee.
- Expected output format: The output should be a list of employee records with the total salary calculated for each employee.
- Key requirements and edge cases to consider: The problem requires handling duplicate employee records, calculating the total salary correctly, and sorting the output by employee ID.
- Example test cases with explanations:
  - Test case 1: Single employee record with no duplicates.
  - Test case 2: Multiple employee records with duplicates.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each employee record and calculate the total salary.
- Step-by-step breakdown of the solution:
  1. Create a map to store the total salary for each employee.
  2. Iterate over each employee record.
  3. For each record, calculate the total salary and update the map.
  4. Finally, create the output list by iterating over the map and sorting it by employee ID.
- Why this approach comes to mind first: It's a straightforward solution that involves iterating over each record and calculating the total salary.

```cpp
vector<vector<int>> calculateSalaries(vector<vector<int>>& records) {
    unordered_map<int, long long> salaryMap;
    for (const auto& record : records) {
        int id = record[0];
        long long salary = record[2];
        long long bonus = record[3];
        if (salaryMap.find(id) != salaryMap.end()) {
            salaryMap[id] += (salary + bonus);
        } else {
            salaryMap[id] = (salary + bonus);
        }
    }
    vector<vector<int>> result;
    for (const auto& pair : salaryMap) {
        result.push_back({pair.first, pair.second});
    }
    sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique employees. This is because we're using a map to store the salaries and sorting the output list.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique employees. This is because we're using a map to store the salaries.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, while the space complexity is due to the map used to store the salaries.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a map to store the total salary for each employee and calculate it in a single pass.
- Detailed breakdown of the approach:
  1. Create a map to store the total salary for each employee.
  2. Iterate over each employee record and update the map.
  3. Finally, create the output list by iterating over the map and sorting it by employee ID.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input data and uses a map to store the salaries, resulting in a time complexity of $O(n \log n)$.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass over the input data and uses a map to store the salaries.

```cpp
vector<vector<int>> calculateSalaries(vector<vector<int>>& records) {
    unordered_map<int, long long> salaryMap;
    for (const auto& record : records) {
        int id = record[0];
        long long salary = record[2];
        long long bonus = record[3];
        salaryMap[id] += (salary + bonus);
    }
    vector<vector<int>> result;
    for (const auto& pair : salaryMap) {
        result.push_back({pair.first, pair.second});
    }
    sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique employees. This is because we're using a map to store the salaries and sorting the output list.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique employees. This is because we're using a map to store the salaries.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input data and uses a map to store the salaries, resulting in a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store and calculate the total salary for each employee.
- Problem-solving patterns identified: Iterating over each record and updating the map.
- Optimization techniques learned: Using a map to store the salaries and sorting the output list.
- Similar problems to practice: Problems involving calculating aggregates and sorting data.

**Mistakes to Avoid:**
- Common implementation errors: Not handling duplicate employee records correctly.
- Edge cases to watch for: Handling empty input data and duplicate employee records.
- Performance pitfalls: Not using a map to store the salaries, resulting in a higher time complexity.
- Testing considerations: Testing the solution with different input data, including empty data and duplicate employee records.