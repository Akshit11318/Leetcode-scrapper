## House Robber II

**Problem Link:** [https://leetcode.com/problems/house-robber-ii/description](https://leetcode.com/problems/house-robber-ii/description)

**Problem Statement:**
- Input format: An array of integers `nums` representing the amount of money in each house.
- Constraints: The array is circular, meaning the first house is connected to the last house.
- Expected output format: The maximum amount of money that can be stolen.
- Key requirements and edge cases to consider: The thief cannot steal from adjacent houses.
- Example test cases with explanations:
  - `nums = [2,3,2]`, the maximum amount of money that can be stolen is `3`.
  - `nums = [1,2,3,1]`, the maximum amount of money that can be stolen is `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of stealing from houses.
- Step-by-step breakdown of the solution: For each house, try stealing from it and then recursively try all possible combinations of stealing from the remaining houses.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it is inefficient due to the large number of possible combinations.

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int maxAmount = 0;
        for (int i = 0; i < n; i++) {
            vector<int> remainingHouses = nums;
            remainingHouses.erase(remainingHouses.begin() + i);
            maxAmount = max(maxAmount, robHelper(remainingHouses));
        }
        return maxAmount;
    }

    int robHelper(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        int maxAmount = 0;
        for (int i = 0; i < nums.size(); i++) {
            int currentAmount = nums[i];
            vector<int> remainingHouses = nums;
            remainingHouses.erase(remainingHouses.begin() + i);
            if (i + 1 < nums.size()) {
                remainingHouses.erase(remainingHouses.begin());
            }
            currentAmount += robHelper(remainingHouses);
            maxAmount = max(maxAmount, currentAmount);
        }
        return maxAmount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of houses. This is because we are trying all possible combinations of stealing from houses.
> - **Space Complexity:** $O(n)$, where $n$ is the number of houses. This is because we are using recursive function calls to try all possible combinations.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible combinations of stealing from houses. The space complexity is relatively low because we are only using a recursive function call stack to try all possible combinations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can solve this problem using dynamic programming. We can break the problem down into two sub-problems: one where we steal from the first house and one where we do not steal from the first house.
- Detailed breakdown of the approach: We can use two arrays to keep track of the maximum amount of money that can be stolen up to each house. One array will be used when we steal from the first house and the other array will be used when we do not steal from the first house.
- Proof of optimality: This approach is optimal because we are only considering the maximum amount of money that can be stolen up to each house, and we are not trying all possible combinations of stealing from houses.

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        return max(robHelper(nums, 0, n - 1), robHelper(nums, 1, n));
    }

    int robHelper(vector<int>& nums, int start, int end) {
        int prev = 0;
        int curr = 0;
        for (int i = start; i < end; i++) {
            int temp = curr;
            curr = max(curr, prev + nums[i]);
            prev = temp;
        }
        return curr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of houses. This is because we are only considering the maximum amount of money that can be stolen up to each house.
> - **Space Complexity:** $O(1)$, where $n$ is the number of houses. This is because we are only using a constant amount of space to keep track of the maximum amount of money that can be stolen up to each house.
> - **Optimality proof:** This approach is optimal because we are only considering the maximum amount of money that can be stolen up to each house, and we are not trying all possible combinations of stealing from houses. The time complexity is linear because we are only iterating over the houses once, and the space complexity is constant because we are only using a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive function calls.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems, using arrays to keep track of the maximum amount of money that can be stolen up to each house.
- Optimization techniques learned: Using dynamic programming to avoid trying all possible combinations of stealing from houses.
- Similar problems to practice: House Robber, House Robber III.

**Mistakes to Avoid:**
- Common implementation errors: Trying all possible combinations of stealing from houses, not using dynamic programming to optimize the solution.
- Edge cases to watch for: When the number of houses is 1, when the number of houses is 2.
- Performance pitfalls: Trying all possible combinations of stealing from houses, not using a constant amount of space to keep track of the maximum amount of money that can be stolen up to each house.
- Testing considerations: Testing the solution with different inputs, such as an array with 1 house, an array with 2 houses, an array with a large number of houses.