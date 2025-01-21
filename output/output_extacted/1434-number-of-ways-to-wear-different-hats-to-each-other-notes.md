## Number of Ways to Wear Different Hats to Each Other

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/description

**Problem Statement:**
- Input format: An integer `n` representing the number of hats and a 2D array `preferences` where `preferences[i]` is a list of hats that the `i-th` person likes, in the order of preference.
- Constraints: `1 <= n <= 10`, `1 <= preferences.length <= 10`, `1 <= preferences[i].length <= 10`.
- Expected output format: Return the number of ways to distribute the hats such that each person gets a different hat.
- Key requirements and edge cases to consider: Each person can only get one hat, and each hat can only be given to one person.
- Example test cases with explanations:
  - Example 1: `n = 3`, `preferences = [[1,2,3],[3,1,2],[1,2,3]]`. There are 6 ways to distribute the hats: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of hats for each person and count the combinations where each person gets a different hat.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of hats.
  2. For each permutation, check if each person gets a hat they like.
  3. Count the permutations where each person gets a hat they like.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int numberWays(vector<vector<int>>& preferences) {
    int n = preferences.size();
    vector<int> hats(n);
    for (int i = 0; i < n; i++) {
        hats[i] = i + 1;
    }
    int count = 0;
    do {
        bool valid = true;
        for (int i = 0; i < n; i++) {
            bool likes = false;
            for (int j = 0; j < preferences[i].size(); j++) {
                if (preferences[i][j] == hats[i]) {
                    likes = true;
                    break;
                }
            }
            if (!likes) {
                valid = false;
                break;
            }
        }
        if (valid) {
            count++;
        }
    } while (next_permutation(hats.begin(), hats.end()));
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot m)$ where $n$ is the number of people and $m$ is the maximum number of hats a person likes. The $n!$ comes from generating all permutations of hats, and the $n \cdot m$ comes from checking if each person likes the hat they got.
> - **Space Complexity:** $O(n)$ for storing the current permutation of hats.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of hats, which leads to the high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use backtracking to try all possible combinations of hats for each person, and stop exploring a branch as soon as we find a person who doesn't like the hat they got.
- Detailed breakdown of the approach:
  1. Start with the first person and try each hat they like.
  2. For each hat, recursively try to assign hats to the remaining people.
  3. If a person doesn't like the hat they got, stop exploring that branch.
- Proof of optimality: This approach tries all possible combinations of hats, but stops exploring branches as soon as possible, which reduces the time complexity.
- Why further optimization is impossible: We must try all possible combinations of hats to find the correct count.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int numberWays(vector<vector<int>>& preferences) {
    int n = preferences.size();
    vector<bool> used(n + 1, false);
    int count = 0;
    function<void(int)> backtrack = [&](int person) {
        if (person == n) {
            count++;
            return;
        }
        for (int hat : preferences[person]) {
            if (!used[hat]) {
                used[hat] = true;
                backtrack(person + 1);
                used[hat] = false;
            }
        }
    };
    backtrack(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$ where $n$ is the number of people and $m$ is the maximum number of hats a person likes. The $n!$ comes from trying all permutations of hats, and the $m$ comes from trying each hat a person likes.
> - **Space Complexity:** $O(n)$ for storing the used hats.
> - **Optimality proof:** This approach tries all possible combinations of hats, but stops exploring branches as soon as possible, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, permutations.
- Problem-solving patterns identified: Trying all possible combinations, stopping exploration of branches as soon as possible.
- Optimization techniques learned: Using backtracking to reduce time complexity.
- Similar problems to practice: Permutations, combinations, backtracking problems.

**Mistakes to Avoid:**
- Common implementation errors: Not stopping exploration of branches as soon as possible, not using backtracking correctly.
- Edge cases to watch for: People not liking any hats, people liking the same hat.
- Performance pitfalls: Trying all possible combinations without stopping exploration of branches.
- Testing considerations: Test with different inputs, including edge cases.