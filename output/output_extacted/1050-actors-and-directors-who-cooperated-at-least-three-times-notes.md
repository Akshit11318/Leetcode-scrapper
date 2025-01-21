## Actors and Directors Who Cooperated at Least Three Times

**Problem Link:** https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description

**Problem Statement:**
- Input: A table `Actors` containing actor names and a table `Directors` containing director names, along with a table `Actors_Directors` containing the collaborations between actors and directors.
- Constraints: The `Actors_Directors` table contains duplicate collaborations between the same actor and director.
- Expected Output: A result set containing the names of actors and directors who have collaborated at least three times.
- Key Requirements:
  - Count the collaborations between each actor and director pair.
  - Filter pairs with at least three collaborations.
- Edge Cases:
  - Handling duplicate collaborations in the `Actors_Directors` table.
  - Ensuring the output only includes pairs with at least three collaborations.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the `Actors_Directors` table, count the collaborations for each actor-director pair, and then filter pairs with at least three collaborations.
- Step-by-step breakdown:
  1. Initialize a dictionary to store the collaboration counts for each actor-director pair.
  2. Iterate over the `Actors_Directors` table and update the collaboration counts.
  3. Filter the dictionary for pairs with at least three collaborations.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>

// Assuming the input is a vector of pairs representing the Actors_Directors table
std::vector<std::pair<std::string, std::string>> bruteForceApproach(const std::vector<std::pair<std::string, std::string>>& collaborations) {
    std::map<std::pair<std::string, std::string>, int> collaborationCounts;
    
    // Count collaborations
    for (const auto& collaboration : collaborations) {
        if (collaborationCounts.find(collaboration) != collaborationCounts.end()) {
            collaborationCounts[collaboration]++;
        } else {
            collaborationCounts[collaboration] = 1;
        }
    }
    
    // Filter pairs with at least three collaborations
    std::vector<std::pair<std::string, std::string>> result;
    for (const auto& pair : collaborationCounts) {
        if (pair.second >= 3) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of collaborations. This is because we iterate over the collaborations twice: once to count the collaborations and once to filter the pairs.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique actor-director pairs. This is because we store the collaboration counts in a dictionary.
> - **Why these complexities occur:** The brute force approach has linear time and space complexity due to the iteration over the collaborations and the storage of collaboration counts.

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a SQL query to count the collaborations and filter the pairs in a single step.
- Detailed breakdown:
  1. Use a `GROUP BY` clause to group the collaborations by actor and director.
  2. Use a `HAVING` clause to filter the groups with at least three collaborations.

```sql
SELECT actor_id, director_id
FROM Actors_Directors
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of collaborations. This is because the database performs a single pass over the collaborations to count and filter the pairs.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique actor-director pairs. This is because the database stores the group counts in memory.
> - **Optimality proof:** The optimal approach has the same time and space complexity as the brute force approach but is more efficient in practice due to the optimized database operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: counting, filtering, and grouping.
- Problem-solving patterns identified: using dictionaries to store counts and filtering pairs based on conditions.
- Optimization techniques learned: using SQL queries to perform operations in a single step.
- Similar problems to practice: counting and filtering pairs in other contexts, such as counting word frequencies in a text.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle duplicate collaborations, incorrect filtering conditions.
- Edge cases to watch for: handling empty input, ensuring the output is correct for small inputs.
- Performance pitfalls: using inefficient data structures or algorithms, not optimizing database queries.
- Testing considerations: testing the solution with various inputs, including edge cases and large datasets.