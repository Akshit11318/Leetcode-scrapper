## Random Pick Index

**Problem Link:** [https://leetcode.com/problems/random-pick-index/description](https://leetcode.com/problems/random-pick-index/description)

**Problem Statement:**
- Given an array of integers `nums`, implement a solution that returns a random index of a given target number.
- The input format is an array of integers `nums` and a target number `target`.
- The expected output format is a random index of the target number in the array.
- Key requirements include handling duplicate numbers and ensuring each index has an equal probability of being returned.
- Edge cases to consider include an empty input array, a target number not present in the array, and duplicate target numbers.

**Example Test Cases:**
- `nums = [1, 2, 3, 3, 3]`, `target = 3`: A random index among 2, 3, 4 should be returned.
- `nums = [1, 2, 3, 3, 3]`, `target = 1`: Index 0 should be returned.
- `nums = []`, `target = 1`: An error or empty result should be returned.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array to find all indices of the target number.
- Then, we can use a random number generator to select one of these indices.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
class Solution {
public:
    vector<int> indices;
    Solution(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                indices.push_back(i);
            }
        }
    }
    
    int pick(int target) {
        vector<int> indicesOfTarget;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                indicesOfTarget.push_back(i);
            }
        }
        int randomIndex = rand() % indicesOfTarget.size();
        return indicesOfTarget[randomIndex];
    }
private:
    vector<int> nums;
    int target;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we are scanning the array in the `pick` method for every query.
> - **Space Complexity:** $O(n)$, because in the worst case, all elements in the array could be the target number, and we store all their indices.
> - **Why these complexities occur:** These complexities occur because the brute force approach involves scanning the entire array for every query and storing all indices of the target number.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to store the indices of each number in the array during the initialization phase.
- Then, when a query is made, we can directly access the stored indices of the target number and select a random one.
- This approach is optimal because it minimizes the time complexity of the query operation.

```cpp
class Solution {
public:
    unordered_map<int, vector<int>> indices;
    Solution(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        vector<int>& indicesOfTarget = indices[target];
        int randomIndex = rand() % indicesOfTarget.size();
        return indicesOfTarget[randomIndex];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `pick` method, because we are directly accessing the stored indices of the target number and selecting a random one.
> - **Space Complexity:** $O(n)$, because in the worst case, all elements in the array could be unique, and we store all their indices.
> - **Optimality proof:** This is the optimal solution because we cannot achieve a better time complexity for the query operation than $O(1)$, and the space complexity is necessary to store the indices of all numbers.

### Final Notes

**Learning Points:**
- The importance of pre-processing and storing relevant data to reduce query time complexity.
- The use of `unordered_map` for efficient storage and retrieval of indices.
- The application of random number generation to select a random index.

**Mistakes to Avoid:**
- Not considering the query operation's time complexity and optimizing it.
- Not handling edge cases such as an empty input array or a target number not present in the array.
- Not ensuring each index has an equal probability of being returned.