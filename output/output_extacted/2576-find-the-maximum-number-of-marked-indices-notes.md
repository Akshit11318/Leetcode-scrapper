## Find the Maximum Number of Marked Indices

**Problem Link:** https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5` and `0 <= nums[i] <= 10^9`.
- Expected output: The maximum number of marked indices.
- Key requirements: Find the maximum number of marked indices such that no two marked indices are closer than `nums[i]` distance.
- Example test cases:
  - Input: `nums = [3, 5, 2, 4]`
  - Output: `2`
  - Explanation: Marked indices are `0` and `2` with distance `2` (index `0` to `2`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of marked indices and calculate the maximum number of marked indices.
- Step-by-step breakdown:
  1. Generate all possible subsets of indices.
  2. For each subset, check if the distance between any two indices is greater than or equal to the value at the smaller index.
  3. If the condition is met, update the maximum number of marked indices.

```cpp
class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        int n = nums.size();
        int maxCount = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> marked;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    marked.push_back(i);
                }
            }
            bool valid = true;
            for (int i = 0; i < marked.size(); i++) {
                for (int j = i + 1; j < marked.size(); j++) {
                    if (marked[j] - marked[i] < nums[marked[i]]) {
                        valid = false;
                        break;
                    }
                }
                if (!valid) break;
            }
            if (valid) {
                maxCount = max(maxCount, (int)marked.size());
            }
        }
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of elements in the input array. This is because we generate all possible subsets of indices and for each subset, we check the distance between any two indices.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we store the marked indices in a vector.
> - **Why these complexities occur:** The brute force approach has exponential time complexity due to generating all possible subsets of indices. The space complexity is linear because we store the marked indices in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Sort the array and use two pointers to find the maximum number of marked indices.
- Detailed breakdown:
  1. Sort the array in ascending order.
  2. Initialize two pointers, `i` and `j`, to the beginning of the array.
  3. Move the `j` pointer to the right until we find an index that is greater than or equal to the value at the `i` index.
  4. If we find such an index, increment the `i` pointer and repeat the process.
  5. The maximum number of marked indices is the number of times we increment the `i` pointer.

```cpp
class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int i = 0, j = n / 2;
        int count = 0;
        while (j < n) {
            if (nums[j] >= nums[i] * 2) {
                count++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the input array. This is because we sort the array using the `sort` function.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the input array. This is because we only use a constant amount of space to store the pointers and the count.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem because we need to sort the array. The space complexity is constant, which is the best possible space complexity because we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two pointers.
- Problem-solving patterns identified: Using two pointers to find the maximum number of marked indices.
- Optimization techniques learned: Sorting the array to reduce the time complexity.
- Similar problems to practice: Problems that involve sorting and using two pointers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundary conditions, not handling the case where the array is empty.
- Edge cases to watch for: The case where the array is empty, the case where the array has only one element.
- Performance pitfalls: Using a brute force approach, not sorting the array.
- Testing considerations: Testing the function with different input sizes, testing the function with different input values.