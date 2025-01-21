## Largest Unique Number

**Problem Link:** https://leetcode.com/problems/largest-unique-number/description

**Problem Statement:**
- Input format and constraints: The problem requires finding the largest unique number in an array of integers. The array contains both positive and negative integers, and the goal is to identify the largest number that appears only once in the array.
- Expected output format: The function should return the largest unique number. If no unique number exists, the function should return `-1`.
- Key requirements and edge cases to consider:
  - Handling empty arrays
  - Handling arrays with duplicate elements
  - Handling arrays with negative numbers
- Example test cases with explanations:
  - Example 1: Input `nums = [5,7,3,9,4,5,6]`, Output `9`. Explanation: `9` is the largest number that appears only once in the array.
  - Example 2: Input `nums = [9,9,8,8]`, Output `-1`. Explanation: No number appears only once in the array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach to solving this problem is to iterate over the array, count the occurrences of each number, and keep track of the maximum unique number encountered.
- Step-by-step breakdown of the solution:
  1. Initialize an empty map to store the count of each number.
  2. Iterate over the array and update the count of each number in the map.
  3. Initialize a variable to store the maximum unique number.
  4. Iterate over the map and update the maximum unique number if a number with a count of 1 is found.
  5. Return the maximum unique number. If no unique number exists, return `-1`.

```cpp
#include <iostream>
#include <unordered_map>

int largestUniqueNumber(int* nums, int numsSize) {
    // Create a map to store the count of each number
    std::unordered_map<int, int> countMap;
    
    // Count the occurrences of each number
    for (int i = 0; i < numsSize; i++) {
        if (countMap.find(nums[i]) != countMap.end()) {
            countMap[nums[i]]++;
        } else {
            countMap[nums[i]] = 1;
        }
    }
    
    // Initialize the maximum unique number
    int maxUniqueNum = -1;
    
    // Find the maximum unique number
    for (auto& pair : countMap) {
        if (pair.second == 1 && pair.first > maxUniqueNum) {
            maxUniqueNum = pair.first;
        }
    }
    
    return maxUniqueNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the array twice: once to count the occurrences of each number and once to find the maximum unique number.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because in the worst case, we need to store every number in the map.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the array. The space complexity is linear because we need to store every unique number in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a single pass over the array and a map to store the count of each number. This allows us to find the maximum unique number in a single pass.
- Detailed breakdown of the approach:
  1. Initialize an empty map to store the count of each number.
  2. Initialize a variable to store the maximum unique number.
  3. Iterate over the array and update the count of each number in the map. If a number has a count of 1, update the maximum unique number.
  4. Return the maximum unique number. If no unique number exists, return `-1`.

```cpp
#include <iostream>
#include <unordered_map>

int largestUniqueNumber(int* nums, int numsSize) {
    // Create a map to store the count of each number
    std::unordered_map<int, int> countMap;
    
    // Initialize the maximum unique number
    int maxUniqueNum = -1;
    
    // Count the occurrences of each number and find the maximum unique number
    for (int i = 0; i < numsSize; i++) {
        if (countMap.find(nums[i]) != countMap.end()) {
            countMap[nums[i]]++;
        } else {
            countMap[nums[i]] = 1;
        }
        
        // Update the maximum unique number
        if (countMap[nums[i]] == 1 && nums[i] > maxUniqueNum) {
            maxUniqueNum = nums[i];
        }
    }
    
    return maxUniqueNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because in the worst case, we need to store every unique number in the map.
> - **Optimality proof:** This solution is optimal because we only iterate over the array once and use a map to store the count of each number. This allows us to find the maximum unique number in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of maps to store the count of each number and the importance of iterating over the array only once to achieve optimal time complexity.
- Problem-solving patterns identified: The problem requires identifying the maximum unique number in an array, which involves counting the occurrences of each number and finding the maximum number with a count of 1.
- Optimization techniques learned: The problem demonstrates the use of a single pass over the array and a map to store the count of each number to achieve optimal time complexity.
- Similar problems to practice: Other problems that involve finding the maximum or minimum value in an array, such as finding the maximum sum of a subarray or the minimum number of operations to make an array sorted.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the map or the maximum unique number variable, not updating the count of each number correctly, or not returning the correct value.
- Edge cases to watch for: Empty arrays, arrays with duplicate elements, and arrays with negative numbers.
- Performance pitfalls: Iterating over the array multiple times or using a data structure with high time complexity, such as a linked list.
- Testing considerations: Test the function with different input arrays, including empty arrays, arrays with duplicate elements, and arrays with negative numbers.