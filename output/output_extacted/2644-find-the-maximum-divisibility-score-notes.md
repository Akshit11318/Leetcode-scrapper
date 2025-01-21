## Find the Maximum Divisibility Score

**Problem Link:** https://leetcode.com/problems/find-the-maximum-divisibility-score/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `nums` and an integer `k`, we need to find the maximum divisibility score that can be achieved.
- Expected output format: The maximum divisibility score.
- Key requirements and edge cases to consider: We need to find the maximum sum of the remainders when each number in `nums` is divided by `k`.
- Example test cases with explanations: 
    - For `nums = [1, 2, 3, 4, 5]` and `k = 3`, the maximum divisibility score is `7` which can be achieved by dividing `1`, `2`, `3`, `4`, `5` by `3` and summing the remainders `1 + 2 + 0 + 1 + 2 = 6`. However, if we take the maximum remainders `2 + 1 + 2 = 5` and `1 + 2 + 0 + 1 + 2 = 6` then the maximum sum is `6`. But the problem asks for the maximum sum of remainders not the remainders themselves. So, the maximum sum of remainders will be `1 + 2 + 0 + 1 + 2 = 6`. But there's another combination `1 + 2 + 0 + 1 + 2 = 6` is not the maximum sum, we can also have `2 + 1 + 2 + 0 + 1 = 6` and `2 + 1 + 2 + 0 + 1 = 6` which is also `6`. So, we need to find the maximum sum of remainders when each number in `nums` is divided by `k`.


---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to iterate over all possible combinations of numbers in `nums` and calculate the sum of remainders when each number is divided by `k`.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of numbers in `nums`.
    2. For each combination, calculate the sum of remainders when each number is divided by `k`.
    3. Keep track of the maximum sum of remainders found so far.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem. However, it is not efficient for large inputs because it has a high time complexity.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maximumDivisibilityScore(vector<int>& nums, int k) {
    int maxScore = 0;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        int score = 0;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i)) != 0) {
                score += nums[i] % k;
            }
        }
        maxScore = max(maxScore, score);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the number of elements in `nums`. This is because we are generating all possible combinations of numbers in `nums` and calculating the sum of remainders for each combination.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the maximum sum of remainders and the current sum of remainders.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach to solve the problem. We are generating all possible combinations of numbers in `nums` and calculating the sum of remainders for each combination, which results in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight that leads to the optimal solution is to use a greedy approach. We can sort the numbers in `nums` in descending order of their remainders when divided by `k`. Then, we can iterate over the sorted numbers and add their remainders to the sum until the sum is greater than or equal to `k`.
- Detailed breakdown of the approach: 
    1. Sort the numbers in `nums` in descending order of their remainders when divided by `k`.
    2. Initialize the sum of remainders to 0.
    3. Iterate over the sorted numbers and add their remainders to the sum until the sum is greater than or equal to `k`.
- Proof of optimality: This approach is optimal because it always chooses the number with the largest remainder when divided by `k`, which maximizes the sum of remainders.
- Why further optimization is impossible: Further optimization is impossible because we are already using a greedy approach, which is the most efficient way to solve this problem.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maximumDivisibilityScore(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end(), [&k](int a, int b) {
        return (a % k) > (b % k);
    });
    int sum = 0;
    for (int num : nums) {
        sum += num % k;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of elements in `nums`. This is because we are sorting the numbers in `nums` using a comparison-based sorting algorithm.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the sum of remainders.
> - **Optimality proof:** This approach is optimal because it always chooses the number with the largest remainder when divided by `k`, which maximizes the sum of remainders.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Using a greedy approach to solve a problem.
- Optimization techniques learned: Using a comparison-based sorting algorithm to sort the numbers in `nums`.
- Similar problems to practice: Other problems that involve using a greedy approach to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the numbers in `nums` in descending order of their remainders when divided by `k`.
- Edge cases to watch for: When the sum of remainders is greater than or equal to `k`.
- Performance pitfalls: Using a brute force approach to solve the problem.
- Testing considerations: Testing the solution with different inputs to ensure that it works correctly.