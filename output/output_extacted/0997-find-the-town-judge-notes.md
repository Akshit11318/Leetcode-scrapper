## Find the Town Judge
**Problem Link:** https://leetcode.com/problems/find-the-town-judge/description

**Problem Statement:**
- Input format and constraints: We are given a 2D integer array `trust` where `trust[i] = [a, b]` means person `a` trusts person `b`, and an integer `n` representing the number of people in the town.
- Expected output format: The index of the town judge if one exists, otherwise -1.
- Key requirements and edge cases to consider: 
  - The town judge trusts nobody.
  - Everybody (except for the town judge) trusts the town judge.
  - There is at most one person who is the town judge.
- Example test cases with explanations:
  - `trust = [[1,3],[2,3],[3,1]]`, `n = 3` should return -1 because person 3 trusts person 1, violating the condition that the town judge trusts nobody.
  - `trust = [[1,3],[2,3]]`, `n = 3` should return 3 because person 3 is the only one who is trusted by everyone else and does not trust anyone.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each person to see if they satisfy the conditions of being the town judge.
- Step-by-step breakdown of the solution:
  1. Initialize an array `trust_count` of size `n+1` to keep track of how many people each person trusts and how many people trust them.
  2. Iterate over the `trust` array to update `trust_count`.
  3. Iterate over `trust_count` to find the person who trusts nobody and is trusted by everybody else.
- Why this approach comes to mind first: It's a straightforward way to check all conditions for each person.

```cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> trust_count(n + 1, 0);
        for (auto& t : trust) {
            trust_count[t[0]]--; // Person t[0] trusts someone, so decrease their trust count
            trust_count[t[1]]++; // Person t[1] is trusted by someone, so increase their trust count
        }
        
        for (int i = 1; i <= n; i++) {
            if (trust_count[i] == n - 1) { // If person i is trusted by everyone else and trusts nobody
                return i;
            }
        }
        
        return -1; // No town judge found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of trust relationships, because we iterate over the `trust` array once and then over the `trust_count` array once.
> - **Space Complexity:** $O(n)$, because we use an array of size $n+1$ to store the trust counts.
> - **Why these complexities occur:** The time complexity is linear because we perform constant-time operations for each trust relationship and each person. The space complexity is linear because we need to store trust counts for each person.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach because it already has a linear time complexity which is optimal for this problem.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Since we must at least read the input, which takes $O(n + m)$ time, our solution is optimal.
- Why further optimization is impossible: Any algorithm must at least examine each trust relationship once, resulting in a time complexity of at least $O(m)$. Additionally, it must consider each person, resulting in a time complexity of at least $O(n)$. Thus, $O(n + m)$ is the best we can achieve.

```cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> trust_count(n + 1, 0);
        for (auto& t : trust) {
            trust_count[t[0]]--; 
            trust_count[t[1]]++; 
        }
        
        for (int i = 1; i <= n; i++) {
            if (trust_count[i] == n - 1) { 
                return i;
            }
        }
        
        return -1; 
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of trust relationships.
> - **Space Complexity:** $O(n)$, because we use an array of size $n+1$ to store the trust counts.
> - **Optimality proof:** The solution is optimal because it must at least read the input, and it does so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, using arrays to keep track of counts.
- Problem-solving patterns identified: Checking conditions for each element in the input.
- Optimization techniques learned: None beyond the initial solution, as it was already optimal.
- Similar problems to practice: Other problems involving trust networks or social graph analysis.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `trust_count` array correctly, not checking for the town judge conditions correctly.
- Edge cases to watch for: When `n` is 1, the town judge is person 1 if there are no trust relationships. When `trust` is empty, the town judge is person `n` if `n` is 1, otherwise there is no town judge.
- Performance pitfalls: Using unnecessary nested loops or data structures that increase the time or space complexity beyond $O(n + m)$.
- Testing considerations: Test with different sizes of `n` and `trust`, including edge cases like when `n` is 1 or when `trust` is empty.