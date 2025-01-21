## Find Interview Candidates

**Problem Link:** https://leetcode.com/problems/find-interview-candidates/description

**Problem Statement:**
- Input format and constraints: The problem requires finding the candidates who can be invited for an interview based on their skills, experience, and availability.
- Expected output format: The output should be a list of candidate IDs who can be invited for an interview.
- Key requirements and edge cases to consider: The problem requires considering the skills required for the job, the experience and skills of each candidate, and the availability of each candidate.
- Example test cases with explanations: 
    - If a candidate has all the required skills and is available, they should be included in the output.
    - If a candidate is missing any of the required skills or is not available, they should not be included in the output.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each candidate and checking if they have all the required skills and are available.
- Step-by-step breakdown of the solution:
    1. Iterate over each candidate.
    2. For each candidate, check if they have all the required skills.
    3. If a candidate has all the required skills, check if they are available.
    4. If a candidate is available, add them to the output list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first thought.

```cpp
#include <vector>
#include <unordered_set>

std::vector<int> findCandidates(std::vector<std::vector<std::string>>& candidates, 
                                 std::vector<std::string>& requiredSkills, 
                                 std::vector<bool>& availability) {
    std::vector<int> invitedCandidates;
    for (int i = 0; i < candidates.size(); i++) {
        bool hasAllSkills = true;
        for (const auto& skill : requiredSkills) {
            if (std::find(candidates[i].begin(), candidates[i].end(), skill) == candidates[i].end()) {
                hasAllSkills = false;
                break;
            }
        }
        if (hasAllSkills && availability[i]) {
            invitedCandidates.push_back(i);
        }
    }
    return invitedCandidates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of candidates, $m$ is the number of required skills, and $k$ is the average number of skills per candidate. This is because for each candidate, we are checking if they have all the required skills.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candidates. This is because in the worst case, all candidates might be invited.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops over the candidates, required skills, and skills per candidate. The space complexity occurs because of the output list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `std::unordered_set` to store the required skills for efficient lookup.
- Detailed breakdown of the approach:
    1. Create a `std::unordered_set` of required skills.
    2. Iterate over each candidate.
    3. For each candidate, create a `std::unordered_set` of their skills.
    4. Check if the candidate's skills include all the required skills.
    5. If a candidate has all the required skills and is available, add them to the output list.
- Proof of optimality: This approach is optimal because it reduces the time complexity of checking if a candidate has all the required skills from $O(m \cdot k)$ to $O(k)$, where $m$ is the number of required skills and $k$ is the average number of skills per candidate.

```cpp
#include <vector>
#include <unordered_set>

std::vector<int> findCandidates(std::vector<std::vector<std::string>>& candidates, 
                                 std::vector<std::string>& requiredSkills, 
                                 std::vector<bool>& availability) {
    std::unordered_set<std::string> requiredSkillsSet(requiredSkills.begin(), requiredSkills.end());
    std::vector<int> invitedCandidates;
    for (int i = 0; i < candidates.size(); i++) {
        std::unordered_set<std::string> candidateSkills(candidates[i].begin(), candidates[i].end());
        bool hasAllSkills = true;
        for (const auto& skill : requiredSkillsSet) {
            if (candidateSkills.find(skill) == candidateSkills.end()) {
                hasAllSkills = false;
                break;
            }
        }
        if (hasAllSkills && availability[i]) {
            invitedCandidates.push_back(i);
        }
    }
    return invitedCandidates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (m + k))$, where $n$ is the number of candidates, $m$ is the number of required skills, and $k$ is the average number of skills per candidate. This is because we are creating a `std::unordered_set` of required skills and a `std::unordered_set` of skills per candidate.
> - **Space Complexity:** $O(n \cdot k + m)$, where $n$ is the number of candidates, $k$ is the average number of skills per candidate, and $m$ is the number of required skills. This is because we are storing the `std::unordered_set` of required skills and the `std::unordered_set` of skills per candidate.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of checking if a candidate has all the required skills from $O(m \cdot k)$ to $O(k)$, making it more efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `std::unordered_set` for efficient lookup and reducing time complexity.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using data structures to optimize the solution.
- Optimization techniques learned: Using `std::unordered_set` to reduce time complexity and improve performance.
- Similar problems to practice: Problems involving efficient lookup and set operations.

**Mistakes to Avoid:**
- Common implementation errors: Not using `std::unordered_set` for efficient lookup, not checking for edge cases.
- Edge cases to watch for: Candidates with no skills, candidates with all required skills but not available.
- Performance pitfalls: Using nested loops over the candidates and required skills without optimizing the lookup.
- Testing considerations: Testing with large inputs, testing with edge cases.