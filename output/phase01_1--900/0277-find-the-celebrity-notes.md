## Find the Celebrity
**Problem Link:** https://leetcode.com/problems/find-the-celebrity/description

**Problem Statement:**
- Input format and constraints: Given a list of `n` people, where `n` is the number of people, and a function `knows(a, b)` which returns `true` if person `a` knows person `b` and `false` otherwise. The function `knows(a, b)` is symmetric, i.e., if `knows(a, b)` is `true`, then `knows(b, a)` is also `true`. A celebrity is a person who is known by everyone but knows no one.
- Expected output format: Return the label of the celebrity if they exist, otherwise return `-1`.
- Key requirements and edge cases to consider: 
  - There can be at most one celebrity.
  - If there is no celebrity, return `-1`.
- Example test cases with explanations:
  - If `n = 3` and `knows(0, 1) = true`, `knows(0, 2) = false`, `knows(1, 0) = false`, `knows(1, 2) = true`, `knows(2, 0) = true`, `knows(2, 1) = false`, then the output should be `2` because person `2` is known by everyone but knows no one.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every person to see if they are a celebrity by verifying if they are known by everyone and if they know no one.
- Step-by-step breakdown of the solution: 
  1. Iterate through each person `i` from `0` to `n-1`.
  2. For each person `i`, iterate through every other person `j` from `0` to `n-1`.
  3. If `i` knows `j` and `i` is not equal to `j`, then `i` is not a celebrity. If `i` does not know `j` and `i` is not equal to `j`, then `j` is not a celebrity.
  4. If after checking all `j`, `i` is still a potential celebrity, then check if `i` knows any `j`. If `i` knows any `j`, then `i` is not a celebrity.
- Why this approach comes to mind first: It's a straightforward way to check every condition for being a celebrity.

```cpp
class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0; i < n; i++) {
            bool isCelebrity = true;
            for (int j = 0; j < n; j++) {
                if (i == j) continue; // A person cannot know themselves
                if (knows(i, j)) {
                    isCelebrity = false;
                    break;
                }
                if (!knows(j, i)) {
                    isCelebrity = false;
                    break;
                }
            }
            if (isCelebrity) return i;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each person, we are checking every other person.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and we're not using any data structures that scale with input size, hence constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can reduce the number of `knows` function calls by first finding a candidate for the celebrity and then verifying if this candidate is indeed a celebrity.
- Detailed breakdown of the approach: 
  1. Initialize a candidate for the celebrity as the first person.
  2. Iterate through the rest of the people. For each person `i`, if the candidate knows `i`, then the candidate cannot be a celebrity, so update the candidate to `i`.
  3. After finding a candidate, verify if this candidate is indeed a celebrity by checking if every other person knows the candidate and if the candidate knows no one.
- Proof of optimality: This approach reduces the number of `knows` function calls to $O(n)$ because we only need to make one pass through all people to find a candidate and then another pass to verify this candidate.

```cpp
class Solution {
public:
    int findCelebrity(int n) {
        int candidate = 0;
        // Find a candidate for the celebrity
        for (int i = 1; i < n; i++) {
            if (knows(candidate, i)) {
                candidate = i;
            }
        }
        // Verify if the candidate is a celebrity
        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1;
            }
        }
        return candidate;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make two passes through the people.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space.
> - **Optimality proof:** This is optimal because we must check every person at least once to determine if they are a celebrity or not, and we do this in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reduction of problem complexity by identifying a candidate and then verifying this candidate.
- Problem-solving patterns identified: Using a two-step process to solve a problem, first finding a potential solution and then verifying it.
- Optimization techniques learned: Reducing the number of function calls to improve efficiency.
- Similar problems to practice: Other problems involving finding a specific element in a list or array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when there is no celebrity.
- Edge cases to watch for: When `n` is `0` or `1`, and when there is no celebrity.
- Performance pitfalls: Using a brute force approach when a more efficient solution exists.
- Testing considerations: Test with different inputs, including edge cases, to ensure the solution works correctly.