## Maximum Element After Decreasing and Rearranging

**Problem Link:** https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `1 <= nums[i] <= 10^4`.
- Expected Output: The maximum element in the array after decreasing and rearranging.
- Key Requirements:
  - Decrease and rearrange elements in the array to maximize the value of the smallest element.
  - The goal is to make all elements as large as possible.

**Example Test Cases:**
- Input: `nums = [2,2,1,2,1]`
  - Explanation: Rearrange to `[1,2,2,2,1]` to make the smallest element as large as possible.
  - Output: `2`
- Input: `nums = [100, 1, 1000]`
  - Explanation: Rearrange to `[1, 100, 1000]`, but since we aim to maximize the smallest element, we can only have a maximum of `2` because we can't make all elements greater than `2` due to the constraints of the given numbers.
  - Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves sorting the array and then trying to maximize the smallest element by rearranging the numbers.
- This approach involves checking every possible permutation of the array, which is impractical for large inputs.

```cpp
#include <algorithm>
using namespace std;

int maximumElementAfterDecrementingAndRearranging(vector<int>& nums) {
    // Sort the array in ascending order
    sort(nums.begin(), nums.end());
    
    // Initialize the smallest element
    int smallest = 1;
    
    // Iterate through the sorted array
    for (int i = 0; i < nums.size(); i++) {
        // If the current element is greater than the smallest + 1, set it to smallest + 1
        if (nums[i] > smallest) {
            nums[i] = smallest;
        }
        // Increment the smallest element
        smallest++;
    }
    
    // Return the smallest element as the maximum after rearranging
    return smallest - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$ if we consider the sorting algorithm used by `std::sort` in C++ does not allocate additional space that scales with input size $n$.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant because we are modifying the input array in-place.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to realize that to maximize the smallest element, we need to make all elements as small as possible to allow for the smallest element to be as large as possible.
- We can achieve this by sorting the array and then iterating through it, ensuring each element is as small as possible to maximize the smallest element.

```cpp
int maximumElementAfterDecrementingAndRearranging(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    nums[0] = 0;
    for (int i = 1; i < nums.size(); i++) {
        nums[i] = min(nums[i], nums[i-1] + 1);
    }
    return nums.back();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(1)$ as we are modifying the input array in-place.
> - **Optimality proof:** This approach is optimal because it ensures that every element in the array is as small as possible, thus maximizing the value of the smallest element. No further optimization is possible because any attempt to increase the value of an element would necessarily decrease the value of another element, given the constraints of the problem.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they impact the solution.
- The use of sorting to simplify the problem and make it more manageable.
- The concept of maximizing the smallest element by minimizing all other elements.

**Mistakes to Avoid:**
- Overcomplicating the problem by considering unnecessary permutations or combinations.
- Failing to recognize the importance of sorting in simplifying the problem.
- Not considering the constraints of the problem when designing the solution.

**Similar Problems to Practice:**
- Problems involving array manipulation and optimization.
- Problems that require maximizing or minimizing certain elements under given constraints.
- Problems that involve sorting and rearranging elements to achieve a specific goal.