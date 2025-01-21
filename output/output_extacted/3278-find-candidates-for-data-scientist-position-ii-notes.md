## Find Candidates for Data Scientist Position II
**Problem Link:** https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii/description

**Problem Statement:**
- Input format: `candidates` table with columns `id`, `experience`, and `salary`
- Constraints: 
    - `candidates` table contains at least one row.
    - `experience` is in the range `[0, 100]`.
    - `salary` is in the range `[0, 100000]`.
- Expected output format: A list of `id`s of candidates who meet the condition that there exists another candidate with the same `experience` but a higher `salary`.
- Key requirements and edge cases to consider:
    - Duplicate `experience` values are possible.
    - Handling `NULL` values is not required as the problem statement does not mention them.
- Example test cases with explanations:
    - For the input `candidates` table with rows `(1, 5, 50000)`, `(2, 5, 60000)`, `(3, 7, 70000)`, the output should be `[1]` because there is another candidate (with `id` `2`) who has the same `experience` (`5`) but a higher `salary` (`60000`).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each candidate with every other candidate to find those who have the same `experience` but a lower `salary`.
- Step-by-step breakdown of the solution:
    1. Iterate through the `candidates` table.
    2. For each candidate, iterate through the table again to find another candidate with the same `experience` but a higher `salary`.
    3. If such a candidate is found, add the current candidate's `id` to the result list.
- Why this approach comes to mind first: It is a straightforward, intuitive method that directly addresses the problem statement without requiring any advanced techniques or optimizations.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

struct Candidate {
    int id;
    int experience;
    int salary;
};

std::vector<int> findCandidates(std::vector<Candidate>& candidates) {
    std::vector<int> result;
    for (int i = 0; i < candidates.size(); ++i) {
        for (int j = 0; j < candidates.size(); ++j) {
            if (i != j && candidates[i].experience == candidates[j].experience && candidates[i].salary < candidates[j].salary) {
                result.push_back(candidates[i].id);
                break;
            }
        }
    }
    return result;
}

int main() {
    // Example usage
    std::vector<Candidate> candidates = {{1, 5, 50000}, {2, 5, 60000}, {3, 7, 70000}};
    std::vector<int> result = findCandidates(candidates);
    for (int id : result) {
        std::cout << id << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rows in the `candidates` table. This is because for each candidate, we potentially iterate through the entire table again.
> - **Space Complexity:** $O(n)$ for storing the result. In the worst case, every candidate could meet the condition and thus be added to the result list.
> - **Why these complexities occur:** The brute force approach involves nested loops over the data, leading to quadratic time complexity. The space complexity is linear because we store the result in a list that can potentially contain every candidate.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each candidate with every other candidate, we can group candidates by their `experience` and then find the maximum `salary` within each group. A candidate is included in the result if their `salary` is less than the maximum `salary` in their group.
- Detailed breakdown of the approach:
    1. Create a hashmap where the keys are `experience` values and the values are the maximum `salary` seen so far for that `experience`.
    2. Iterate through the `candidates` table, updating the hashmap as we go.
    3. For each candidate, check if their `salary` is less than the maximum `salary` for their `experience` group. If so, add their `id` to the result list.
- Proof of optimality: This approach ensures that we only need to iterate through the data once, making it more efficient than the brute force approach.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Candidate {
    int id;
    int experience;
    int salary;
};

std::vector<int> findCandidates(std::vector<Candidate>& candidates) {
    std::unordered_map<int, int> maxSalaries;
    std::vector<int> result;
    
    for (const auto& candidate : candidates) {
        if (maxSalaries.find(candidate.experience) != maxSalaries.end() && candidate.salary < maxSalaries[candidate.experience]) {
            result.push_back(candidate.id);
        } else {
            maxSalaries[candidate.experience] = std::max(maxSalaries[candidate.experience], candidate.salary);
        }
    }
    
    return result;
}

int main() {
    // Example usage
    std::vector<Candidate> candidates = {{1, 5, 50000}, {2, 5, 60000}, {3, 7, 70000}};
    std::vector<int> result = findCandidates(candidates);
    for (int id : result) {
        std::cout << id << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `candidates` table. This is because we make a single pass through the data.
> - **Space Complexity:** $O(n)$ for storing the result and the hashmap. In the worst case, every candidate could meet the condition, and we need to store all unique `experience` values.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best possible for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap usage for efficient grouping and lookup.
- Problem-solving patterns identified: Reducing quadratic complexity to linear by avoiding nested loops.
- Optimization techniques learned: Using data structures to keep track of maximum values within groups.
- Similar problems to practice: Problems involving grouping, sorting, or finding maximum/minimum values within groups.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input table.
- Edge cases to watch for: Duplicate `experience` values, `NULL` values (if they were part of the problem statement).
- Performance pitfalls: Using nested loops over large datasets without considering more efficient algorithms.
- Testing considerations: Ensure to test with various input sizes, including edge cases like an empty table or a table with a single row.