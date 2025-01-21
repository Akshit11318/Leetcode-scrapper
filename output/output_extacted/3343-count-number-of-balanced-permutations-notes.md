## Count Number of Balanced Permutations
**Problem Link:** https://leetcode.com/problems/count-number-of-balanced-permutations/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, where `1 <= n <= 30`.
- Expected output format: The number of `balanced permutations` of `n`.
- Key requirements and edge cases to consider: A permutation of `n` is considered balanced if it has at least one pair of consecutive elements that sum up to `n + 1`.
- Example test cases with explanations:
  - For `n = 2`, the only balanced permutation is `[1, 2]`, so the output is `1`.
  - For `n = 3`, the balanced permutations are `[1, 2, 3]`, `[1, 3, 2]`, `[3, 1, 2]`, `[3, 2, 1]`, `[2, 1, 3]`, `[2, 3, 1]`, so the output is `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of numbers from `1` to `n`, then check each permutation to see if it's balanced.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `n`.
  2. For each permutation, check if there exists at least one pair of consecutive elements that sum up to `n + 1`.
  3. Count the number of permutations that satisfy the condition.
- Why this approach comes to mind first: It's the most straightforward way to ensure that all cases are considered.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void permute(vector<int>& nums, int start, int end, int n, int& count) {
    if (start == end) {
        bool is_balanced = false;
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] + nums[i + 1] == n + 1) {
                is_balanced = true;
                break;
            }
        }
        if (is_balanced) {
            count++;
        }
    } else {
        for (int i = start; i <= end; i++) {
            swap(nums[start], nums[i]);
            permute(nums, start + 1, end, n, count);
            swap(nums[start], nums[i]); // backtrack
        }
    }
}

int count_balanced_permutations(int n) {
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    int count = 0;
    permute(nums, 0, n - 1, n, count);
    return count;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Number of balanced permutations: " << count_balanced_permutations(n);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$. Generating all permutations of `n` elements takes $n!$ time, and checking each permutation takes $O(n)$ time, but the permutation generation dominates the complexity.
> - **Space Complexity:** $O(n)$. The space used by the recursion stack and the permutation vector.
> - **Why these complexities occur:** The brute force approach checks all possible permutations, which leads to exponential time complexity due to the nature of permutation generation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that any permutation where the numbers `1` and `n` are not adjacent is balanced, because placing `1` and `n` next to each other would be the only way to avoid having a pair that sums to `n + 1`. Thus, the total number of balanced permutations can be found by subtracting the number of permutations where `1` and `n` are adjacent from the total number of permutations.
- Detailed breakdown of the approach:
  1. Calculate the total number of permutations of `n`, which is $n!$.
  2. Consider `1` and `n` as a single unit. The number of permutations where `1` and `n` are adjacent is $(n-1)! * 2$, because we can treat `1` and `n` as one entity and then multiply by `2` to account for the two possible orders of `1` and `n` within this entity.
  3. Subtract the number of permutations where `1` and `n` are adjacent from the total number of permutations to get the number of balanced permutations.
- Proof of optimality: This approach is optimal because it directly calculates the number of balanced permutations without generating all permutations, reducing the time complexity significantly.

```cpp
#include <iostream>

using namespace std;

long long factorial(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int count_balanced_permutations(int n) {
    if (n == 1) return 0; // Base case
    long long total_permutations = factorial(n);
    long long adjacent_permutations = 2 * factorial(n - 1);
    return total_permutations - adjacent_permutations;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Number of balanced permutations: " << count_balanced_permutations(n);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$. Calculating the factorial of `n` takes linear time.
> - **Space Complexity:** $O(1)$. The space used does not grow with the size of the input, making it constant.
> - **Optimality proof:** This approach is optimal because it avoids the need to generate all permutations, reducing the time complexity from exponential to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Permutations, factorials, and the importance of identifying key insights to optimize solutions.
- Problem-solving patterns identified: Looking for ways to avoid brute force by identifying patterns or properties of the problem that can simplify the solution.
- Optimization techniques learned: Using mathematical formulas to calculate results instead of generating all possibilities.
- Similar problems to practice: Other permutation and combination problems, especially those that involve identifying specific properties or patterns.

**Mistakes to Avoid:**
- Common implementation errors: Not considering edge cases, such as when `n` is `1`.
- Edge cases to watch for: Small values of `n`, and ensuring that the solution handles these cases correctly.
- Performance pitfalls: Using brute force approaches for large inputs, which can lead to extremely long execution times or even crashes due to memory limits.
- Testing considerations: Ensure to test with a variety of inputs, including small and large values of `n`, to verify the correctness and performance of the solution.