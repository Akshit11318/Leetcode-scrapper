## Kids With the Greatest Number of Candies

**Problem Link:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description

**Problem Statement:**
- Input format: An array of integers `candies` representing the number of candies each kid has, and an integer `extraCandies` representing the extra candies.
- Constraints: `2 <= candies.length <= 100`, `1 <= candies[i] <= 100`, and `1 <= extraCandies <= 50`.
- Expected output format: A boolean array where the `i-th` element is `true` if, after giving `extraCandies` to the `i-th` kid, they will have the greatest number of candies among them, and `false` otherwise.
- Key requirements and edge cases to consider: Handling cases where multiple kids can have the greatest number of candies after receiving the extra candies, and ensuring the solution scales for the given constraints.
- Example test cases with explanations: 
  - Input: `candies = [2,3,5,1,3], extraCandies = 3`
    - Expected Output: `[true,true,true,false,true]`
    - Explanation: After giving 3 extra candies to the first kid, they will have 5 candies, which is the greatest among all kids. Similarly, after giving 3 extra candies to the second, third, and fifth kids, they will also have the greatest number of candies.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total number of candies each kid would have if they received the extra candies and compare it with the maximum number of candies any kid currently has.
- Step-by-step breakdown of the solution:
  1. Find the maximum number of candies any kid currently has.
  2. For each kid, calculate the total number of candies they would have if they received the extra candies.
  3. Compare this total with the maximum number of candies and determine if the kid would have the greatest number of candies.
- Why this approach comes to mind first: It directly addresses the problem statement by simulating the scenario described.

```cpp
#include <vector>
#include <algorithm>

std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
    int maxCandies = *std::max_element(candies.begin(), candies.end());
    std::vector<bool> result;
    for (int candy : candies) {
        result.push_back(candy + extraCandies >= maxCandies);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of kids. This is because we are iterating over the array of candies twice: once to find the maximum and once to generate the result.
> - **Space Complexity:** $O(n)$, as we are creating a new array of the same size as the input array to store the results.
> - **Why these complexities occur:** The iteration over the array to find the maximum and to generate the result each contribute to the time complexity, while the creation of the result array contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The previous solution is already quite efficient with a linear time complexity. However, we can slightly optimize it by avoiding the creation of an intermediate vector and directly calculating the result in a single pass.
- Detailed breakdown of the approach: 
  1. Initialize an empty vector to store the results.
  2. Find the maximum number of candies in a single pass through the array.
  3. In the same pass, calculate for each kid whether they would have the greatest number of candies if given the extra candies, and add this result to the vector.
- Proof of optimality: This approach maintains a linear time complexity while minimizing the number of passes through the data, making it optimal for this problem.
- Why further optimization is impossible: Given the need to examine each kid's candies at least once to determine if they would have the greatest number, a linear time complexity is the best achievable.

```cpp
#include <vector>
#include <algorithm>

std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
    int maxCandies = candies[0];
    std::vector<bool> result;
    for (int candy : candies) {
        maxCandies = std::max(maxCandies, candy);
        result.push_back(candy + extraCandies >= maxCandies);
    }
    return result;
}
```

However, this optimization attempt still results in an incorrect output because the `maxCandies` is being updated as we iterate, which affects the comparison for earlier kids. Thus, the original "brute force" approach is actually the correct and optimal solution for this problem, with no further optimizations possible without altering the logic.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of kids.
> - **Space Complexity:** $O(n)$, as we are creating a new array of the same size as the input array to store the results.
> - **Optimality proof:** The solution has a linear time complexity and only requires a single pass through the data (when considering the original, not the attempted optimization), making it optimal for the given problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and vector manipulation.
- Problem-solving patterns identified: Direct simulation of the problem scenario.
- Optimization techniques learned: Minimizing the number of passes through data.
- Similar problems to practice: Other array manipulation and comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating variables during iteration.
- Edge cases to watch for: Ensuring the solution works for all possible input values within the given constraints.
- Performance pitfalls: Unnecessary iterations or data structure creations.
- Testing considerations: Thoroughly testing with various input scenarios to ensure correctness.