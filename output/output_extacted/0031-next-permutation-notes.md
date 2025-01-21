## Next Permutation

**Problem Link:** https://leetcode.com/problems/next-permutation/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 100`, `0 <= nums[i] <= 100`.
- Expected Output: Modify the input array `nums` to be the next lexicographically greater permutation. If there is no such permutation, make it the first permutation (i.e., sort the array in ascending order).
- Key Requirements: The solution should handle edge cases, such as when the input array is already the last permutation or is empty.
- Example Test Cases:
  - For `nums = [1, 2, 3]`, the next permutation is `[1, 3, 2]`.
  - For `nums = [3, 2, 1]`, the next permutation is `[1, 2, 3]` since `[3, 2, 1]` is the last permutation.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible permutations of the input array and then finding the next lexicographically greater permutation.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. Sort the permutations in lexicographical order.
  3. Find the current permutation in the sorted list.
  4. If the current permutation is the last one, return the first permutation (i.e., the sorted array). Otherwise, return the next permutation in the list.

```cpp
#include <algorithm>
#include <vector>

void nextPermutation(vector<int>& nums) {
    // Generate all permutations
    sort(nums.begin(), nums.end());
    do {
        // Check if the current permutation is the one we're looking for
        if (isNextPermutation(nums)) {
            return;
        }
    } while (next_permutation(nums.begin(), nums.end()));
    // If we reach here, it means the input was the last permutation
    sort(nums.begin(), nums.end());
}

bool isNextPermutation(vector<int>& nums) {
    // This function should check if the current permutation is the next lexicographically greater permutation
    // However, implementing this correctly in the brute force approach is complex and inefficient
    // It's better to directly find the next permutation using a more efficient algorithm
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of elements in the input array. This is because generating all permutations of an array of $n$ elements results in $n!$ permutations.
> - **Space Complexity:** $O(n)$, for storing the permutations. However, in practice, the space complexity can be much higher due to the need to store all permutations.
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations, which leads to an exponential time complexity. The space complexity is also high because we need to store all these permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: To find the next lexicographically greater permutation, we can use the following steps:
  1. Find the first decreasing element from the right (i.e., the first element that is smaller than the one to its right). If no such element exists, the permutation is the last one.
  2. If such an element is found, find the smallest element to its right that is greater than it.
  3. Swap these two elements.
  4. Reverse the elements to the right of the first decreasing element found in step 1.
- Detailed breakdown:
  - Start from the end of the array and move towards the beginning to find the first decreasing element.
  - Once the decreasing element is found, move towards the end to find the smallest element greater than it.
  - Swap these two elements to ensure the permutation is lexicographically greater.
  - Reverse the elements to the right of the decreasing element to ensure the resulting permutation is the smallest possible one that is lexicographically greater.

```cpp
void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    // Find the first decreasing element from the right
    int i = n - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    
    if (i >= 0) {
        // Find the smallest element to the right that is greater than nums[i]
        int j = n - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    
    // Reverse the elements to the right of i
    reverse(nums.begin() + i + 1, nums.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because in the worst case, we need to traverse the entire array to find the decreasing element and the smallest greater element, and then reverse a portion of the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the indices and temporary swap values.
> - **Optimality proof:** This approach is optimal because it directly constructs the next lexicographically greater permutation without generating all permutations, thus avoiding the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated here is the ability to directly construct the next lexicographically greater permutation without generating all permutations.
- Problem-solving patterns identified include finding the first decreasing element from the right and using it as a pivot to construct the next permutation.
- Optimization techniques learned include avoiding unnecessary computations and using efficient data structures (in this case, the input array itself).

**Mistakes to Avoid:**
- A common mistake is not correctly identifying the first decreasing element or the smallest greater element, leading to incorrect permutations.
- Another mistake is not reversing the correct portion of the array, which can result in an incorrect or non-minimal permutation.
- Performance pitfalls include using inefficient algorithms that generate all permutations or using excessive memory.