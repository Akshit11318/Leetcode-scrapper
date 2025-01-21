## Smallest Sufficient Team
**Problem Link:** https://leetcode.com/problems/smallest-sufficient-team/description

**Problem Statement:**
- Input format and constraints: The problem takes in a 2D array `req_skills` where each row represents a person's skills and a 1D array `person` where each element is a person's index. The goal is to find the smallest sufficient team that covers all skills.
- Expected output format: The function should return a list of person indices that form the smallest sufficient team.
- Key requirements and edge cases to consider: The team must cover all skills, and the team size should be minimized. Edge cases include an empty input array, a person with no skills, and a person with all skills.
- Example test cases with explanations:
  - Input: `req_skills = [[1,2,3],[3,4,5],[1,2,5]]`, `person = [1,2,3]`
  - Output: `[0,1]`
  - Explanation: The smallest sufficient team is the team that includes person 0 and person 1, which covers all skills.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible teams and checking if each team covers all skills.
- Step-by-step breakdown of the solution:
  1. Generate all possible teams using a bitmask.
  2. For each team, check if it covers all skills.
  3. If a team covers all skills, update the smallest team if necessary.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to understand, but it has exponential time complexity.

```cpp
class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& person) {
        unordered_map<string, int> skill_to_id;
        for (int i = 0; i < req_skills.size(); i++) {
            skill_to_id[req_skills[i]] = i;
        }
        
        vector<int> skill_set(req_skills.size(), 0);
        for (int i = 0; i < person.size(); i++) {
            int person_skill = 0;
            for (const auto& skill : person[i]) {
                person_skill |= 1 << skill_to_id[skill];
            }
            skill_set[i] = person_skill;
        }
        
        vector<int> smallest_team;
        int smallest_team_size = INT_MAX;
        
        for (int team = 0; team < (1 << person.size()); team++) {
            int team_skill = 0;
            vector<int> team_members;
            for (int i = 0; i < person.size(); i++) {
                if ((team >> i) & 1) {
                    team_skill |= skill_set[i];
                    team_members.push_back(i);
                }
            }
            
            if (team_skill == (1 << req_skills.size()) - 1) {
                if (team_members.size() < smallest_team_size) {
                    smallest_team = team_members;
                    smallest_team_size = team_members.size();
                }
            }
        }
        
        return smallest_team;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of people and $m$ is the number of skills.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the number of skills.
> - **Why these complexities occur:** The brute force approach generates all possible teams, which has exponential time complexity. The space complexity comes from storing the skills of each person.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution uses a bitmask to represent the skills of each person and the skills covered by the current team.
- Detailed breakdown of the approach:
  1. Use a bitmask to represent the skills of each person.
  2. Use a bitmask to represent the skills covered by the current team.
  3. Use a dynamic programming approach to find the smallest team that covers all skills.
- Proof of optimality: The dynamic programming approach ensures that the smallest team is found, and the bitmask representation reduces the time complexity.

```cpp
class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& person) {
        unordered_map<string, int> skill_to_id;
        for (int i = 0; i < req_skills.size(); i++) {
            skill_to_id[req_skills[i]] = i;
        }
        
        vector<int> skill_set(person.size(), 0);
        for (int i = 0; i < person.size(); i++) {
            int person_skill = 0;
            for (const auto& skill : person[i]) {
                person_skill |= 1 << skill_to_id[skill];
            }
            skill_set[i] = person_skill;
        }
        
        vector<int> smallest_team;
        int smallest_team_size = INT_MAX;
        
        vector<vector<int>> dp(1 << req_skills.size(), vector<int>(person.size(), -1));
        for (int i = 0; i < person.size(); i++) {
            dp[skill_set[i]][i] = i;
        }
        
        for (int mask = 0; mask < (1 << req_skills.size()); mask++) {
            for (int i = 0; i < person.size(); i++) {
                if (dp[mask][i] != -1) {
                    for (int j = 0; j < person.size(); j++) {
                        int new_mask = mask | skill_set[j];
                        if (new_mask != mask && dp[new_mask][j] == -1) {
                            dp[new_mask][j] = i;
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < person.size(); i++) {
            if (dp[(1 << req_skills.size()) - 1][i] != -1) {
                vector<int> team;
                int mask = (1 << req_skills.size()) - 1;
                while (mask != 0) {
                    team.push_back(i);
                    int new_mask = mask ^ skill_set[i];
                    i = dp[mask][i];
                    mask = new_mask;
                }
                if (team.size() < smallest_team_size) {
                    smallest_team = team;
                    smallest_team_size = team.size();
                }
            }
        }
        
        return smallest_team;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of people.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the number of people.
> - **Optimality proof:** The dynamic programming approach ensures that the smallest team is found, and the bitmask representation reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: bitmask, dynamic programming.
- Problem-solving patterns identified: using bitmask to represent skills, using dynamic programming to find the smallest team.
- Optimization techniques learned: using bitmask to reduce time complexity, using dynamic programming to find the optimal solution.
- Similar problems to practice: problems that involve finding the smallest subset that covers all elements.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dp array, not handling the edge case where the input array is empty.
- Edge cases to watch for: the input array is empty, a person has no skills, a person has all skills.
- Performance pitfalls: using a brute force approach, not using a bitmask to represent skills.
- Testing considerations: test the function with different input arrays, test the function with edge cases.