## All the Pairs with the Maximum Number of Common Followers

**Problem Link:** https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/description

**Problem Statement:**
- Input format and constraints: The problem involves two lists of integers, `id1` and `id2`, each representing user IDs, and a list of integers `followers1` and `followers2`, where `followers1[i]` and `followers2[i]` are the number of common followers between `id1[i]` and `id2[i]`.
- Expected output format: The task is to return a list of pairs of user IDs with the maximum number of common followers.
- Key requirements and edge cases to consider: The input lists are non-empty, and the number of common followers is non-negative.
- Example test cases with explanations:
  - For example, if `id1 = [1, 2, 3]`, `id2 = [3, 1, 2]`, and `followers1 = [1000, 2000, 3000]`, `followers2 = [3000, 1000, 2000]`, the output should be `[[1, 3], [2, 1], [3, 2]]` because the pairs `(1, 3)`, `(2, 1)`, and `(3, 2)` have the maximum number of common followers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all pairs of user IDs and calculating the number of common followers for each pair.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Iterate over all pairs of user IDs.
  3. For each pair, calculate the number of common followers by finding the maximum number of common followers between the two IDs in the `followers1` and `followers2` lists.
  4. If the number of common followers for the current pair is greater than the maximum found so far, update the maximum and reset the result list with the current pair.
  5. If the number of common followers for the current pair is equal to the maximum found so far, add the current pair to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

std::vector<std::vector<int>> maximizeCommonFollowers(std::vector<int>& id1, std::vector<int>& id2, std::vector<int>& followers1, std::vector<int>& followers2) {
    int maxFollowers = 0;
    std::vector<std::vector<int>> result;
    
    for (int i = 0; i < id1.size(); i++) {
        for (int j = 0; j < id2.size(); j++) {
            int commonFollowers = std::max(followers1[i], followers2[j]);
            if (commonFollowers > maxFollowers) {
                maxFollowers = commonFollowers;
                result.clear();
                result.push_back({id1[i], id2[j]});
            } else if (commonFollowers == maxFollowers) {
                result.push_back({id1[i], id2[j]});
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of user IDs, because we are iterating over all pairs of user IDs.
> - **Space Complexity:** $O(n)$, where $n$ is the number of user IDs, because we are storing the result in a list.
> - **Why these complexities occur:** The time complexity is high because we are iterating over all pairs of user IDs, and the space complexity is moderate because we are storing the result in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach involves finding the maximum number of common followers by comparing the `followers1` and `followers2` lists directly, without iterating over all pairs of user IDs.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the result.
  2. Initialize a variable to store the maximum number of common followers.
  3. Iterate over the `followers1` and `followers2` lists simultaneously.
  4. For each pair of common followers, check if the number of common followers is greater than the maximum found so far.
  5. If it is, update the maximum and reset the result list with the current pair of user IDs.
  6. If the number of common followers is equal to the maximum found so far, add the current pair of user IDs to the result list.
- Proof of optimality: This approach is optimal because it only requires a single pass over the `followers1` and `followers2` lists, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass over the input lists.

```cpp
#include <vector>
#include <algorithm>

std::vector<std::vector<int>> maximizeCommonFollowers(std::vector<int>& id1, std::vector<int>& id2, std::vector<int>& followers1, std::vector<int>& followers2) {
    int maxFollowers = 0;
    std::vector<std::vector<int>> result;
    
    for (int i = 0; i < id1.size(); i++) {
        if (followers1[i] > maxFollowers) {
            maxFollowers = followers1[i];
            result.clear();
            result.push_back({id1[i], id2[i]});
        } else if (followers1[i] == maxFollowers) {
            result.push_back({id1[i], id2[i]});
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of user IDs, because we are only iterating over the `followers1` and `followers2` lists once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of user IDs, because we are storing the result in a list.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input lists, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of optimizing algorithms by reducing the number of iterations.
- Problem-solving patterns identified: The problem requires identifying the maximum value in a list and returning the corresponding indices.
- Optimization techniques learned: The problem demonstrates the use of a single pass over the input lists to optimize the algorithm.
- Similar problems to practice: Other problems that involve finding the maximum value in a list and returning the corresponding indices.

**Mistakes to Avoid:**
- Common implementation errors: Iterating over all pairs of user IDs instead of using a single pass over the input lists.
- Edge cases to watch for: Handling cases where the input lists are empty or contain duplicate values.
- Performance pitfalls: Using an algorithm with a high time complexity, such as $O(n^2)$, instead of an optimal algorithm with a time complexity of $O(n)$.
- Testing considerations: Testing the algorithm with large input lists to ensure that it performs efficiently.