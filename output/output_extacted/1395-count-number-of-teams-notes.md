## Count Number of Teams
**Problem Link:** https://leetcode.com/problems/count-number-of-teams/description

**Problem Statement:**
- Input format: An array of integers `rating` representing the ratings of soldiers.
- Constraints: The length of `rating` is between 1 and 10^5, and each rating is between 1 and 10^5.
- Expected output format: The number of teams that can be formed.
- Key requirements and edge cases to consider: A team can be formed if there is a soldier with a rating between the ratings of two other soldiers. The team must have at least three soldiers.
- Example test cases with explanations:
  - `rating = [2,5,3,4,1]`: The number of teams that can be formed is 3. The teams are `[2,3,4]`, `[2,4,5]`, and `[2,3,5]`.
  - `rating = [2,1,3]`: The number of teams that can be formed is 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to find all possible combinations of three soldiers and check if a team can be formed.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of three soldiers.
  2. For each combination, check if a team can be formed by checking if there is a soldier with a rating between the ratings of the other two soldiers.
  3. Count the number of combinations where a team can be formed.

```cpp
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if ((rating[i] < rating[j] && rating[j] < rating[k]) ||
                        (rating[i] > rating[j] && rating[j] > rating[k])) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the `rating` array. This is because we are generating all possible combinations of three soldiers.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are using three nested loops to generate all possible combinations of three soldiers. The space complexity is constant because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to count the number of teams that can be formed.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the `rating` array.
  2. For each soldier, count the number of soldiers with a lower rating on the left and the number of soldiers with a higher rating on the right.
  3. Use these counts to calculate the number of teams that can be formed.

```cpp
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int count = 0;
        for (int j = 1; j < n - 1; j++) {
            int leftSmaller = 0, leftLarger = 0;
            int rightSmaller = 0, rightLarger = 0;
            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j]) leftSmaller++;
                if (rating[i] > rating[j]) leftLarger++;
            }
            for (int k = j + 1; k < n; k++) {
                if (rating[k] < rating[j]) rightSmaller++;
                if (rating[k] > rating[j]) rightLarger++;
            }
            count += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `rating` array. This is because we are using two nested loops to count the number of soldiers with a lower or higher rating.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This is the optimal solution because we are counting the number of teams that can be formed in a single pass through the `rating` array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, counting.
- Problem-solving patterns identified: Using counts to calculate the number of teams that can be formed.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Counting problems, two-pointer technique problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the pointers correctly, not counting the number of soldiers with a lower or higher rating correctly.
- Edge cases to watch for: When the `rating` array has a length of 1 or 2, no teams can be formed.
- Performance pitfalls: Using a brute force approach, not using a two-pointer technique to reduce the time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases.