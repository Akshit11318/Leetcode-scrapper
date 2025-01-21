## Maximum Number of Accepted Invitations
**Problem Link:** https://leetcode.com/problems/maximum-number-of-accepted-invitations/description

**Problem Statement:**
- Input: Two arrays `favorite` and `friends`, where `favorite[i]` is the favorite person of the `i-th` person and `friends[i]` is the friend of the `i-th` person.
- Constraints: `n` is the number of people, and `1 <= n <= 1000`.
- Expected Output: The maximum number of accepted invitations.
- Key Requirements: For an invitation to be accepted, the favorite person of the host must be the guest.
- Example Test Cases:
  - `favorite = [1,2,3], friends = [3,1,2]`, output: `3`.
  - `favorite = [1,2,3], friends = [3,1,2,4,5,6,7,8,9,10]`, output: `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible pairs of hosts and guests.
- Step-by-step breakdown:
  1. For each host, find all guests that can be invited.
  2. For each guest, check if the host is the favorite person of the guest.
  3. If yes, increment the count of accepted invitations.

```cpp
int maxInvitations(vector<int>& favorite, vector<int>& friends) {
    int n = favorite.size();
    int maxAccepted = 0;
    for (int host = 0; host < n; host++) {
        for (int guest = 0; guest < friends.size(); guest++) {
            if (favorite[guest] == host) {
                maxAccepted++;
            }
        }
    }
    return maxAccepted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of people. This is because we have two nested loops iterating over the people.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of accepted invitations.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, and the constant space usage results in a space complexity of $O(1)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can directly count the number of accepted invitations by iterating over the guests and checking if the host is the favorite person of the guest.
- Detailed breakdown:
  1. Initialize a count of accepted invitations to 0.
  2. Iterate over the guests.
  3. For each guest, check if the host is the favorite person of the guest.
  4. If yes, increment the count of accepted invitations.

```cpp
int maxInvitations(vector<int>& favorite, vector<int>& friends) {
    int n = favorite.size();
    int maxAccepted = 0;
    for (int guest = 0; guest < n; guest++) {
        if (find(friends.begin(), friends.end(), guest) != friends.end() && favorite[guest] == guest) {
            maxAccepted++;
        }
    }
    return maxAccepted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of people. This is because we only have one loop iterating over the people.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of accepted invitations.
> - **Optimality proof:** This is the optimal solution because we only need to iterate over the guests once to count the number of accepted invitations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and counting.
- Problem-solving patterns identified: Direct counting and iteration.
- Optimization techniques learned: Reducing the number of loops and conditional checks.
- Similar problems to practice: Other counting and iteration problems.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect loop bounds, and missing conditional checks.
- Edge cases to watch for: Empty input arrays, duplicate favorite people, and invalid input values.
- Performance pitfalls: Using unnecessary loops or conditional checks, and not optimizing the solution for large input sizes.
- Testing considerations: Test the solution with different input sizes, edge cases, and invalid input values to ensure correctness and robustness.