## Maximum Employees to be Invited to a Meeting
**Problem Link:** https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description

**Problem Statement:**
- Input format and constraints: Given a list of `first` and `second` preferences of employees, where `first[i]` and `second[i]` represent the first and second choices of the `i-th` employee, respectively.
- Expected output format: Return the maximum number of employees that can be invited to a meeting.
- Key requirements and edge cases to consider: Each employee can only be invited once, and an employee can only be invited if their first or second preference is available.
- Example test cases with explanations: 
    - `first = [1, 2, 3], second = [3, 2, 1]`, the output is `3` because all employees can be invited.
    - `first = [1, 2, 3], second = [2, 1, 3]`, the output is `2` because only two employees can be invited.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of employees and check if they can be invited.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of employees.
    2. For each combination, check if each employee's first or second preference is available.
    3. If all employees in the combination can be invited, update the maximum number of employees.
- Why this approach comes to mind first: It's a straightforward and intuitive solution, but it's inefficient due to the large number of combinations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int maxInvitations(vector<int>& first, vector<int>& second) {
    int n = first.size();
    int maxInvites = 0;
    
    // Generate all possible combinations of employees
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<bool> invited(n, false);
        bool valid = true;
        
        // Check if each employee's first or second preference is available
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (invited[first[i] - 1] || invited[second[i] - 1]) {
                    valid = false;
                    break;
                }
                invited[first[i] - 1] = true;
            }
        }
        
        // Update the maximum number of employees
        if (valid) {
            maxInvites = max(maxInvites, __builtin_popcount(mask));
        }
    }
    
    return maxInvites;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of employees. This is because we generate all possible combinations of employees and check each combination in $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we use a boolean array to keep track of invited employees.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to the generation of all possible combinations, and a linear space complexity due to the use of a boolean array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a greedy approach to invite employees based on their first preference, and then invite employees based on their second preference if their first preference is not available.
- Detailed breakdown of the approach:
    1. Sort the employees based on their first preference.
    2. Invite employees based on their first preference.
    3. If an employee's first preference is not available, invite them based on their second preference.
- Proof of optimality: This approach is optimal because it ensures that the maximum number of employees are invited based on their first preference, and then invites employees based on their second preference if their first preference is not available.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int maxInvitations(vector<int>& first, vector<int>& second) {
    int n = first.size();
    vector<bool> invited(n, false);
    int maxInvites = 0;
    
    // Sort the employees based on their first preference
    vector<pair<int, int>> employees(n);
    for (int i = 0; i < n; i++) {
        employees[i] = {first[i], second[i]};
    }
    sort(employees.begin(), employees.end());
    
    // Invite employees based on their first preference
    for (int i = 0; i < n; i++) {
        if (!invited[employees[i].first - 1]) {
            invited[employees[i].first - 1] = true;
            maxInvites++;
        }
    }
    
    // Invite employees based on their second preference if their first preference is not available
    for (int i = 0; i < n; i++) {
        if (!invited[employees[i].second - 1] && !invited[employees[i].first - 1]) {
            invited[employees[i].second - 1] = true;
            maxInvites++;
        }
    }
    
    return maxInvites;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of employees. This is because we sort the employees based on their first preference.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we use a boolean array to keep track of invited employees.
> - **Optimality proof:** This approach is optimal because it ensures that the maximum number of employees are invited based on their first preference, and then invites employees based on their second preference if their first preference is not available.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Using a greedy approach to solve problems with multiple preferences.
- Optimization techniques learned: Using sorting to improve the efficiency of the algorithm.
- Similar problems to practice: Problems involving multiple preferences, such as scheduling or resource allocation.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty input or invalid preferences.
- Edge cases to watch for: Employees with the same first or second preference, or employees with no available preferences.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach.
- Testing considerations: Testing the algorithm with different input sizes and edge cases to ensure correctness and efficiency.