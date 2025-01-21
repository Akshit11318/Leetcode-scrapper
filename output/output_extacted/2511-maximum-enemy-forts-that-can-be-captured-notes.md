## Maximum Enemy Forts That Can Be Captured
**Problem Link:** https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description

**Problem Statement:**
- Input format: A list of integers representing the locations of enemy forts.
- Constraints: The number of enemy forts is less than or equal to 10^5.
- Expected output format: The maximum number of enemy forts that can be captured.
- Key requirements and edge cases to consider:
  - The `k` parameter, which is the maximum allowed distance between the two farthest enemy forts.
  - Handling cases where there are no enemy forts or the `k` value is very large.
- Example test cases with explanations:
  - For example, given the locations `[1, 2, 3, 5, 6]` and `k = 3`, the maximum number of enemy forts that can be captured is 3, since we can capture the forts at locations 1, 2, and 3.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible subsets of enemy forts and check if the maximum distance between the farthest forts is less than or equal to `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of enemy forts.
  2. For each subset, calculate the maximum distance between the farthest forts.
  3. Check if the maximum distance is less than or equal to `k`.
  4. If it is, update the maximum number of enemy forts that can be captured.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is inefficient due to the large number of subsets.

```cpp
int maxCapturedForts(vector<int>& forts, int k) {
    int maxForts = 0;
    int n = forts.size();
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subset.push_back(forts[i]);
            }
        }
        if (subset.empty()) continue;
        sort(subset.begin(), subset.end());
        int maxDist = subset.back() - subset.front();
        if (maxDist <= k) {
            maxForts = max(maxForts, (int)subset.size());
        }
    }
    return maxForts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot \log n)$, where $n$ is the number of enemy forts. This is because we generate all possible subsets of enemy forts, sort each subset, and calculate the maximum distance between the farthest forts.
> - **Space Complexity:** $O(n)$, where $n$ is the number of enemy forts. This is because we store each subset of enemy forts.
> - **Why these complexities occur:** The brute force approach is inefficient due to the large number of subsets and the sorting operation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to find the maximum number of enemy forts that can be captured. We maintain two pointers, `left` and `right`, where `left` is the leftmost fort and `right` is the rightmost fort.
- Detailed breakdown of the approach:
  1. Sort the enemy forts in ascending order.
  2. Initialize `left` to 0 and `right` to 0.
  3. Move `right` to the right until the distance between `forts[right]` and `forts[left]` is greater than `k`.
  4. Update the maximum number of enemy forts that can be captured.
  5. Move `left` to the right and repeat steps 3-4 until `right` reaches the end of the array.
- Proof of optimality: This approach is optimal because we only need to consider the maximum distance between the farthest forts, and the two-pointer technique allows us to do so efficiently.

```cpp
int maxCapturedForts(vector<int>& forts, int k) {
    sort(forts.begin(), forts.end());
    int maxForts = 0;
    for (int left = 0; left < forts.size(); left++) {
        int right = left;
        while (right < forts.size() && forts[right] - forts[left] <= k) {
            right++;
        }
        maxForts = max(maxForts, right - left);
    }
    return maxForts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the number of enemy forts. This is because we sort the enemy forts and use a two-pointer technique to find the maximum number of enemy forts that can be captured.
> - **Space Complexity:** $O(1)$, where $n$ is the number of enemy forts. This is because we only use a constant amount of space to store the pointers and the maximum number of enemy forts that can be captured.
> - **Optimality proof:** This approach is optimal because we only need to consider the maximum distance between the farthest forts, and the two-pointer technique allows us to do so efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting.
- Problem-solving patterns identified: Using a two-pointer technique to find the maximum number of enemy forts that can be captured.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Problems that involve finding the maximum or minimum value in an array using a two-pointer technique.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array or a `k` value of 0.
- Edge cases to watch for: Handling cases where there are no enemy forts or the `k` value is very large.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach.
- Testing considerations: Testing the function with different inputs, including edge cases.