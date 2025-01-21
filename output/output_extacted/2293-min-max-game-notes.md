## Min-Max Game
**Problem Link:** [https://leetcode.com/problems/min-max-game/description](https://leetcode.com/problems/min-max-game/description)

**Problem Statement:**
- The input is a 1D array `nums` of length `n`, where `n` is a power of 2.
- The task is to simulate a Min-Max game where pairs of elements from the array are compared in each round. 
- In the first round, the minimum and maximum of each pair are compared.
- In subsequent rounds, the minimum of the maximum values from the previous round and the maximum of the minimum values from the previous round are compared.
- The game continues until only one element remains.
- The expected output is the final remaining element.

**Example Test Cases:**
- For `nums = [1,3,5,2,4,8,6,7]`, the output should be `13`.
- For `nums = [1,1,1,1]`, the output should be `1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to simulate the game round by round, comparing pairs of elements and selecting the minimum and maximum values for the next round.
- This approach involves recursively dividing the array into pairs, comparing the elements in each pair, and selecting the minimum and maximum values.

```cpp
class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        vector<int> nextRound;
        for (int i = 0; i < nums.size(); i += 2) {
            nextRound.push_back(min(nums[i], nums[i+1]));
            nextRound.push_back(max(nums[i], nums[i+1]));
        }
        return minMaxGame(nextRound);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the input array. This is because we recursively divide the array into pairs and compare the elements in each pair.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we create a new array `nextRound` to store the results of each round.
> - **Why these complexities occur:** The time complexity occurs because we recursively divide the array into pairs and compare the elements in each pair. The space complexity occurs because we create a new array `nextRound` to store the results of each round.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to observe the pattern of the game and realize that the final remaining element is always the same, regardless of the order in which the pairs are compared.
- We can prove this by induction. In the first round, the minimum and maximum values are compared. In subsequent rounds, the minimum of the maximum values from the previous round and the maximum of the minimum values from the previous round are compared.
- Since the order of comparison does not affect the final result, we can simplify the game by comparing the minimum and maximum values of each pair in a specific order.

```cpp
class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        int n = nums.size();
        for (int len = n / 2; len > 0; len /= 2) {
            vector<int> nextRound;
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    if (j % 2 == 0) {
                        nextRound.push_back(min(nums[i + j], nums[i + j + len]));
                    } else {
                        nextRound.push_back(max(nums[i + j], nums[i + j + len]));
                    }
                }
            }
            nums = nextRound;
        }
        return nums[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the input array. This is because we iterate over the array and compare the elements in each pair.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we create a new array `nextRound` to store the results of each round.
> - **Optimality proof:** The optimality of this solution can be proven by showing that it has the same time complexity as the brute force approach, but with a more efficient implementation.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of recursion and dynamic programming to solve a complex problem.
- The problem-solving pattern identified in this problem is the use of a divide-and-conquer approach to solve a problem that can be broken down into smaller sub-problems.
- The optimization technique learned in this problem is the use of a specific order of comparison to simplify the game and reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error in this problem is to forget to update the `nums` array after each round.
- An edge case to watch for is when the input array has only one element.
- A performance pitfall to avoid is to use a naive recursive approach that has a high time complexity.