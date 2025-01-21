## Largest Perimeter Triangle

**Problem Link:** https://leetcode.com/problems/largest-perimeter-triangle/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `3 <= nums.length <= 1000`, `1 <= nums[i] <= 10^6`.
- Expected Output: The largest possible perimeter of a triangle with non-zero area, or `0` if no such triangle exists.
- Key Requirements:
  - The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
- Example Test Cases:
  - `nums = [2,2,4,5]`: The largest perimeter is `2 + 2 + 5 = 9`.
  - `nums = [1,2,1]`: No valid triangle exists, so the answer is `0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of three sides to see if they can form a valid triangle.
- We can use a brute force approach by iterating over all possible triples of numbers in the array.

```cpp
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        int n = nums.size();
        int maxPerimeter = 0;
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] < nums[j] + nums[k] && nums[j] < nums[i] + nums[k] && nums[k] < nums[i] + nums[j]) {
                        maxPerimeter = max(maxPerimeter, nums[i] + nums[j] + nums[k]);
                    }
                }
            }
        }
        return maxPerimeter;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ because we have three nested loops iterating over the array.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the maximum perimeter.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible combinations of three sides, resulting in cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to check if the current number and the next two numbers can form a valid triangle.
- Since the array is sorted in descending order, if a valid triangle can be formed, it will have the largest perimeter.
- We can stop checking as soon as we find a valid triangle because it will be the largest one.

```cpp
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        int n = nums.size();
        int maxPerimeter = 0;
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] < nums[i + 1] + nums[i + 2]) {
                maxPerimeter = nums[i] + nums[i + 1] + nums[i + 2];
                break;
            }
        }
        return maxPerimeter;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, and then $O(n)$ for the single loop, resulting in $O(n \log n)$ overall.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the maximum perimeter.
> - **Optimality proof:** This is the optimal approach because we only need to check each number once, and sorting the array allows us to find the largest valid triangle in linear time after sorting.

---

### Final Notes

**Learning Points:**
- The importance of sorting in reducing the search space for valid triangles.
- The key insight that we only need to check the current number and the next two numbers to form a valid triangle.
- The use of a single loop to find the largest valid triangle after sorting.

**Mistakes to Avoid:**
- Not sorting the array before checking for valid triangles.
- Not stopping the search as soon as a valid triangle is found.
- Not considering the constraints of the problem, such as the range of the input numbers.