## Combination Sum III
**Problem Link:** https://leetcode.com/problems/combination-sum-iii/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers `k` and `n` as input. `k` represents the number of elements to choose, and `n` represents the target sum. The goal is to find all combinations of `k` numbers from the range `[1, 9]` that sum up to `n`.
- Expected output format: The output should be a list of all valid combinations, where each combination is a list of `k` numbers.
- Key requirements and edge cases to consider: The input integers `k` and `n` are guaranteed to be positive, and `k` is less than or equal to `9`. The output should not contain duplicate combinations.
- Example test cases with explanations:
    - Example 1: Input `k = 3`, `n = 10`. Output: `[[1,2,7],[1,3,6],[1,4,5],[2,3,5]]`. Explanation: These are all the possible combinations of 3 numbers from the range `[1, 9]` that sum up to 10.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to generate all possible combinations of `k` numbers from the range `[1, 9]` and then filter out the ones that do not sum up to `n`.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of `k` numbers from the range `[1, 9]`.
    2. For each combination, calculate the sum of its elements.
    3. If the sum equals `n`, add the combination to the result list.
- Why this approach comes to mind first: This approach is intuitive because it directly addresses the problem statement. However, it is inefficient due to the large number of combinations that need to be generated and checked.

```cpp
#include <vector>
using namespace std;

void backtrack(int k, int n, vector<int>& path, vector<vector<int>>& result, int start) {
    if (path.size() == k) {
        int sum = 0;
        for (int num : path) {
            sum += num;
        }
        if (sum == n) {
            result.push_back(path);
        }
        return;
    }
    for (int i = start; i <= 9; i++) {
        path.push_back(i);
        backtrack(k, n, path, result, i + 1);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum3(int k, int n) {
    vector<vector<int>> result;
    vector<int> path;
    backtrack(k, n, path, result, 1);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(9^k)$, where $k$ is the number of elements to choose. This is because in the worst case, we need to generate all possible combinations of `k` numbers from the range `[1, 9]`.
> - **Space Complexity:** $O(k)$, where $k$ is the number of elements to choose. This is because we need to store the current combination being generated.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible combinations, and the space complexity is relatively low because we only need to store the current combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations and then filtering them, we can use a backtracking approach that prunes branches that are guaranteed to exceed the target sum `n`.
- Detailed breakdown of the approach:
    1. Start with an empty combination and a sum of 0.
    2. Iterate over the numbers from 1 to 9.
    3. For each number, calculate the new sum if the number is added to the current combination.
    4. If the new sum exceeds `n`, skip this number and move to the next one.
    5. If the new sum equals `n` and the combination has `k` elements, add the combination to the result list.
    6. If the new sum is less than `n` and the combination has less than `k` elements, recursively add the next numbers to the combination.
- Proof of optimality: This approach is optimal because it avoids generating combinations that are guaranteed to exceed the target sum `n`, reducing the number of branches to explore.

```cpp
#include <vector>
using namespace std;

void backtrack(int k, int n, vector<int>& path, vector<vector<int>>& result, int start) {
    if (path.size() == k) {
        int sum = 0;
        for (int num : path) {
            sum += num;
        }
        if (sum == n) {
            result.push_back(path);
        }
        return;
    }
    for (int i = start; i <= 9; i++) {
        int sum = 0;
        for (int num : path) {
            sum += num;
        }
        if (sum + i > n) {
            break;
        }
        path.push_back(i);
        backtrack(k, n, path, result, i + 1);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum3(int k, int n) {
    vector<vector<int>> result;
    vector<int> path;
    backtrack(k, n, path, result, 1);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{9!}{k!(9-k)!})$, where $k$ is the number of elements to choose. This is because we are generating all possible combinations of `k` numbers from the range `[1, 9]`, but pruning branches that exceed the target sum `n`.
> - **Space Complexity:** $O(k)$, where $k` is the number of elements to choose. This is because we need to store the current combination being generated.
> - **Optimality proof:** The time complexity is reduced compared to the brute force approach because we are pruning branches that are guaranteed to exceed the target sum `n`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, pruning, and recursion.
- Problem-solving patterns identified: Using backtracking to solve combinatorial problems.
- Optimization techniques learned: Pruning branches that are guaranteed to exceed the target sum.
- Similar problems to practice: Combination Sum, Combination Sum II, and Permutations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as `k` being greater than `9`.
- Edge cases to watch for: `k` being 0 or `n` being 0.
- Performance pitfalls: Generating all possible combinations without pruning.
- Testing considerations: Testing the function with different values of `k` and `n`, including edge cases.