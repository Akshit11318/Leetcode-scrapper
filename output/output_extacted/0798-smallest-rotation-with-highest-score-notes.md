## Smallest Rotation with Highest Score
**Problem Link:** https://leetcode.com/problems/smallest-rotation-with-highest-score/description

**Problem Statement:**
- Input format: An array of integers `nums` representing the scores of students in a class.
- Constraints: The length of `nums` is in the range `[2, 1000]`, and `1 <= nums[i] <= 10^6`.
- Expected output format: The minimum number of rotations required to achieve the highest score.
- Key requirements and edge cases to consider: The score of the class is calculated by summing the scores of students who are in their original position after rotation.
- Example test cases with explanations:
  - Example 1: Input: `nums = [2,3,1,4,0]`, Output: `3`
  - Example 2: Input: `nums = [1,3,0,2]`, Output: `3`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible rotations and calculate the score for each rotation.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum number of rotations to infinity.
  2. Iterate over all possible rotations (from 0 to `n-1`, where `n` is the length of `nums`).
  3. For each rotation, calculate the score by summing the scores of students who are in their original position after rotation.
  4. Update the minimum number of rotations if the current rotation results in a higher score.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible rotations and calculate the score for each rotation.

```cpp
int bestRotation(vector<int>& nums) {
    int n = nums.size();
    int minRotations = INT_MAX;
    for (int rotations = 0; rotations < n; rotations++) {
        int score = 0;
        for (int i = 0; i < n; i++) {
            if ((i - rotations + n) % n == nums[i]) {
                score++;
            }
        }
        if (score > 0) {
            minRotations = min(minRotations, rotations);
        }
    }
    return minRotations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we are iterating over all possible rotations and for each rotation, we are calculating the score by iterating over all students.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity is constant because we are only using a fixed amount of space to store the minimum number of rotations.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can calculate the score for each rotation in $O(n)$ time by using a single pass over the array.
- Detailed breakdown of the approach:
  1. Initialize the minimum number of rotations to infinity and the maximum score to 0.
  2. Iterate over all possible rotations (from 0 to `n-1`, where `n` is the length of `nums`).
  3. For each rotation, calculate the score by summing the scores of students who are in their original position after rotation.
  4. Update the minimum number of rotations if the current rotation results in a higher score.
- Proof of optimality: This approach is optimal because it only requires a single pass over the array to calculate the score for each rotation.

```cpp
int bestRotation(vector<int>& nums) {
    int n = nums.size();
    int minRotations = INT_MAX;
    int maxScore = 0;
    for (int rotations = 0; rotations < n; rotations++) {
        int score = 0;
        for (int i = 0; i < n; i++) {
            if ((i - rotations + n) % n == nums[i]) {
                score++;
            }
        }
        if (score > maxScore) {
            maxScore = score;
            minRotations = rotations;
        }
    }
    return minRotations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we are iterating over all possible rotations and for each rotation, we are calculating the score by iterating over all students.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the array to calculate the score for each rotation. However, we can further optimize the solution by using a single pass over the array to calculate the score for each rotation.

However, a more optimal approach exists by using a different method to calculate the score.

```cpp
int bestRotation(vector<int>& nums) {
    int n = nums.size();
    vector<int> diff(n + 1);
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        diff[(n - i) % n]--;
        if (x < n) {
            diff[x]--;
            diff[x + n]++;
        }
    }
    int maxScore = 0, maxRot = 0;
    int score = 0;
    for (int i = 0; i < n; i++) {
        score += diff[i];
        if (score > maxScore) {
            maxScore = score;
            maxRot = i;
        }
    }
    return maxRot;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we are only iterating over the array once.
> - **Space Complexity:** $O(n)$, as we are using a additional space to store the `diff` array.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the array to calculate the score for each rotation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, score calculation, and optimization.
- Problem-solving patterns identified: Using a single pass over the array to calculate the score for each rotation.
- Optimization techniques learned: Using a different method to calculate the score for each rotation.
- Similar problems to practice: Problems that involve iteration, score calculation, and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases.
- Edge cases to watch for: Empty array, array with a single element.
- Performance pitfalls: Using nested loops, not optimizing the solution.
- Testing considerations: Testing the solution with different inputs, testing the solution with edge cases.