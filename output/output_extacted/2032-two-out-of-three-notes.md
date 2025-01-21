## Two Out of Three
**Problem Link:** https://leetcode.com/problems/two-out-of-three/description

**Problem Statement:**
- Input format and constraints: The problem takes three arrays of integers as input: `nums1`, `nums2`, and `nums3`. The constraints are that the length of each array can be up to $10^4$ and the integers are within the range $1 \leq nums[i] \leq 10^4$.
- Expected output format: The output should be a vector of unique integers that appear in at least two of the input arrays.
- Key requirements and edge cases to consider: The solution should handle cases where there are duplicate integers within an array, and it should also handle cases where an integer appears in all three arrays or in exactly two arrays.
- Example test cases with explanations:
    - For example, given `nums1 = [1, 1, 3, 2]`, `nums2 = [2, 3]`, and `nums3 = [3]`, the output should be `[3, 2]` because `3` and `2` are the only integers that appear in at least two of the arrays.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each integer in each array and check if it exists in the other two arrays. This involves using nested loops to compare each element of one array with all elements of the other two arrays.
- Step-by-step breakdown of the solution:
    1. Initialize an empty set to store unique integers that appear in at least two arrays.
    2. Iterate through each array, and for each integer in the array, check its presence in the other two arrays.
    3. If an integer is found in at least two arrays, add it to the set.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement by comparing each integer across the arrays.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
    unordered_set<int> result;
    for (int num : nums1) {
        if (find(nums2.begin(), nums2.end(), num) != nums2.end() || find(nums3.begin(), nums3.end(), num) != nums3.end()) {
            result.insert(num);
        }
    }
    for (int num : nums2) {
        if (find(nums1.begin(), nums1.end(), num) != nums1.end() || find(nums3.begin(), nums3.end(), num) != nums3.end()) {
            result.insert(num);
        }
    }
    for (int num : nums3) {
        if (find(nums1.begin(), nums1.end(), num) != nums1.end() || find(nums2.begin(), nums2.end(), num) != nums2.end()) {
            result.insert(num);
        }
    }
    vector<int> finalResult(result.begin(), result.end());
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the maximum length of the input arrays. This is because in the worst case, for each element in one array, we might end up searching through all elements of the other two arrays.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of unique integers across all arrays. This is because we store unique integers that appear in at least two arrays in a set.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loop structure, and the space complexity is linear because we only store unique integers in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each integer across arrays directly, we can use an `unordered_map` to store the count of each integer across all arrays. This allows us to efficiently identify integers that appear in at least two arrays.
- Detailed breakdown of the approach:
    1. Initialize an `unordered_map` to store the count of each integer across all arrays.
    2. Iterate through each array and update the count of each integer in the map.
    3. After counting, iterate through the map and add integers that appear in at least two arrays to the result set.
- Proof of optimality: This approach is optimal because it only requires a single pass through each array to count the occurrences of each integer, reducing the time complexity significantly compared to the brute force approach.
- Why further optimization is impossible: This approach has a linear time complexity with respect to the total number of elements across all arrays, which is the minimum required to examine each element at least once.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
    unordered_map<int, int> countMap;
    unordered_set<int> result;
    
    for (int num : nums1) countMap[num]++;
    for (int num : nums2) countMap[num]++;
    for (int num : nums3) countMap[num]++;
    
    for (auto& pair : countMap) {
        if (pair.second >= 2) {
            result.insert(pair.first);
        }
    }
    
    vector<int> finalResult(result.begin(), result.end());
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of elements across all arrays. This is because we make a single pass through each array.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of unique integers across all arrays. This is because we store the count of each integer in a map and unique integers that appear in at least two arrays in a set.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best possible for this problem since we must examine each element at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of using data structures like `unordered_map` and `unordered_set` for efficient counting and storage of unique elements.
- Problem-solving patterns identified: The strategy of counting occurrences of elements and then filtering based on a condition.
- Optimization techniques learned: Reducing time complexity by minimizing the number of passes through the data and using efficient data structures.
- Similar problems to practice: Problems involving counting, filtering, and efficient use of data structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of data structures, not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with duplicate elements, and integers that appear in all three arrays.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input scenarios, including edge cases.