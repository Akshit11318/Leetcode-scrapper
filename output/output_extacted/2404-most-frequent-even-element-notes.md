## Most Frequent Even Element
**Problem Link:** https://leetcode.com/problems/most-frequent-even-element/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums`, where `1 <= nums.length <= 1000` and `1 <= nums[i] <= 1000`.
- Expected output format: The function should return the most frequent even element in the array. If there is a tie, return the smallest one.
- Key requirements and edge cases to consider: Handle cases where there are no even elements, or where the array is empty.
- Example test cases with explanations:
  - Input: `nums = [1,2,2,3,4]`
    - Output: `2`
    - Explanation: The even elements in the array are `2` and `4`. `2` appears twice, which is more than `4`. If there were multiple even elements with the same highest frequency, we would return the smallest one.
  - Input: `nums = [0,1,2,2,4]`
    - Output: `2`
    - Explanation: The even elements in the array are `0`, `2`, and `4`. `2` appears twice, which is more than `0` and `4`. 

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the occurrences of each even number in the array and keep track of the one with the highest count. In case of a tie, store the smallest number.
- Step-by-step breakdown of the solution:
  1. Initialize an empty map to store the count of each even number.
  2. Iterate through the array to count the occurrences of each even number.
  3. Keep track of the maximum count and the corresponding smallest even number.
- Why this approach comes to mind first: It directly addresses the problem statement by counting occurrences and handling ties.

```cpp
#include <iostream>
#include <unordered_map>

int mostFrequentEven(int* nums, int numsSize) {
    if (numsSize == 0) return -1; // Edge case: empty array

    std::unordered_map<int, int> countMap;
    int maxCount = 0;
    int result = INT_MAX; // Initialize result as the maximum possible integer value

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) { // Check if the number is even
            if (countMap.find(nums[i]) != countMap.end()) {
                countMap[nums[i]]++;
            } else {
                countMap[nums[i]] = 1;
            }

            if (countMap[nums[i]] > maxCount) {
                maxCount = countMap[nums[i]];
                result = nums[i];
            } else if (countMap[nums[i]] == maxCount && nums[i] < result) {
                result = nums[i];
            }
        }
    }

    return (maxCount == 0) ? -1 : result; // Return -1 if no even elements are found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the map.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the array once. The space complexity is also linear because, in the worst case, we store every element in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but ensuring that we minimize the number of operations and memory usage by directly updating the maximum count and result as we iterate through the array.
- Detailed breakdown of the approach: Similar to the brute force, but with a focus on minimizing unnecessary operations and ensuring that we handle all edge cases efficiently.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, minimizing the time complexity, and it uses a map to store counts, which allows for efficient lookup and update of counts.

```cpp
#include <iostream>
#include <unordered_map>
#include <climits>

int mostFrequentEven(int* nums, int numsSize) {
    if (numsSize == 0) return -1; // Edge case: empty array

    std::unordered_map<int, int> countMap;
    int maxCount = 0;
    int result = INT_MAX; // Initialize result as the maximum possible integer value

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) { // Check if the number is even
            countMap[nums[i]]++;
            if (countMap[nums[i]] > maxCount) {
                maxCount = countMap[nums[i]];
                result = nums[i];
            } else if (countMap[nums[i]] == maxCount && nums[i] < result) {
                result = nums[i];
            }
        }
    }

    return (maxCount == 0) ? -1 : result; // Return -1 if no even elements are found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the map.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity for this problem by only requiring a single pass through the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing (using an unordered map to store counts), iteration, and conditional logic for handling ties and edge cases.
- Problem-solving patterns identified: The use of a map to efficiently count occurrences and the importance of handling edge cases.
- Optimization techniques learned: Minimizing the number of operations by directly updating the maximum count and result as we iterate through the array.
- Similar problems to practice: Other problems involving counting occurrences, handling ties, and optimizing solutions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like an empty array), not initializing variables properly, and not checking for ties correctly.
- Edge cases to watch for: Empty arrays, arrays with no even elements, and arrays with multiple even elements having the same highest frequency.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time or space complexities than necessary.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure it behaves as expected.