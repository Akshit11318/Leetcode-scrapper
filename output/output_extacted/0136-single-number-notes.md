## Single Number

**Problem Link:** https://leetcode.com/problems/single-number/description

**Problem Statement:**
- Input format: An array of integers `nums` containing `n` elements.
- Constraints: `1 <= n <= 3 * 10^4`, `0 <= nums[i] <= 10^4`.
- Expected output format: The single number that appears only once in the array.
- Key requirements and edge cases to consider: 
    - All numbers except one appear twice.
    - There is exactly one number that appears once.
- Example test cases with explanations: 
    - Example 1: Input: `nums = [2,2,1]`, Output: `1`. Explanation: `1` appears only once.
    - Example 2: Input: `nums = [4,1,2,1,2]`, Output: `4`. Explanation: `4` appears only once.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array and count the occurrence of each number.
- Step-by-step breakdown of the solution: 
    1. Create a hash map to store the count of each number.
    2. Iterate through the array and update the count of each number in the hash map.
    3. Iterate through the hash map and find the number with a count of 1.
- Why this approach comes to mind first: It's a straightforward solution that directly addresses the problem statement.

```cpp
#include <unordered_map>
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> countMap;
        // Count the occurrence of each number
        for (int num : nums) {
            if (countMap.find(num) != countMap.end()) {
                countMap[num]++;
            } else {
                countMap[num] = 1;
            }
        }
        // Find the number with a count of 1
        for (auto& pair : countMap) {
            if (pair.second == 1) {
                return pair.first;
            }
        }
        // Should not reach here
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we iterate through the array twice: once to count the occurrences and once to find the single number.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements in the array. This is because in the worst-case scenario, all elements are unique, and we store them in the hash map.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the array. The space complexity is also linear because we store each unique element in the hash map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use bitwise operations to find the single number. Specifically, we can use the XOR operation, which has the property that `a ^ a = 0` and `a ^ 0 = a`.
- Detailed breakdown of the approach: 
    1. Initialize a variable `result` to 0.
    2. Iterate through the array and XOR each number with `result`.
    3. After the iteration, `result` will hold the single number.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is better than the brute force approach.

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        // XOR each number with result
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we iterate through the array once.
> - **Space Complexity:** $O(1)$, which means the space required does not grow with the size of the input array. This is because we only use a constant amount of space to store the `result` variable.
> - **Optimality proof:** This is the optimal solution because we cannot do better than linear time complexity for this problem, and we achieve this with constant space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, specifically the XOR operation.
- Problem-solving patterns identified: Using properties of operations to simplify problems.
- Optimization techniques learned: Reducing space complexity by avoiding unnecessary data structures.
- Similar problems to practice: Other problems that involve bitwise operations, such as finding the missing number in an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty array.
- Edge cases to watch for: An array with a single element, an array with all elements being the same.
- Performance pitfalls: Using a data structure that has a high time or space complexity, such as a hash map when a simple variable would suffice.
- Testing considerations: Testing with arrays of different sizes, testing with arrays that have a single element, testing with arrays that have all elements being the same.