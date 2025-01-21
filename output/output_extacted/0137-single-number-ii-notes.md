## Single Number II
**Problem Link:** https://leetcode.com/problems/single-number-ii/description

**Problem Statement:**
- Input: An array of integers where every element appears three times except for one, which appears only once.
- Constraints: The array is non-empty and contains at least one element.
- Expected Output: The integer that appears only once.
- Key Requirements: Find the single number in the array.
- Edge Cases: Empty array, array with all elements appearing three times, array with more than one single number (this case is not possible according to the problem statement).
- Example Test Cases:
  - Input: `[2,2,3,2]`, Output: `3`
  - Input: `[0,1,0,1,0,1,100]`, Output: `100`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to count the occurrences of each number and find the one that appears only once.
- This approach involves iterating over the array and using a data structure (like a hash map) to store the counts of each number.
- This approach comes to mind first because it directly addresses the problem statement by counting occurrences.

```cpp
#include <iostream>
#include <unordered_map>

int singleNumber(int* nums, int numsSize) {
    std::unordered_map<int, int> countMap;
    for (int i = 0; i < numsSize; i++) {
        if (countMap.find(nums[i]) != countMap.end()) {
            countMap[nums[i]]++;
        } else {
            countMap[nums[i]] = 1;
        }
    }
    for (auto& pair : countMap) {
        if (pair.second == 1) {
            return pair.first;
        }
    }
    // Should not reach here according to the problem statement
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are scanning the array once to count the occurrences and then scanning the hash map to find the single number.
> - **Space Complexity:** $O(n)$, because in the worst case, every element in the array could be unique, requiring space in the hash map for each one.
> - **Why these complexities occur:** These complexities occur because we are using a hash map to store the counts of each number, which allows for efficient lookup and insertion but requires additional space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use bit manipulation to find the single number. Since every number except one appears three times, we can use two bits to track the counts of each bit position (0, 1, and 2 appearances).
- We use two integers, `ones` and `twos`, to track the bits that have appeared once and twice, respectively. We update these integers based on the bits of the current number.
- This approach is optimal because it uses constant space and has a linear time complexity.
- Proof of optimality: This approach is optimal because it uses the minimum amount of space (two integers) and has the minimum time complexity ($O(n)$) required to solve the problem.

```cpp
int singleNumber(int* nums, int numsSize) {
    int ones = 0, twos = 0;
    for (int i = 0; i < numsSize; i++) {
        twos |= ones & nums[i];
        ones ^= nums[i];
        int threes = ones & twos;
        ones &= ~threes;
        twos &= ~threes;
    }
    return ones;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are scanning the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the `ones` and `twos` integers.
> - **Optimality proof:** This is the optimal solution because it uses the minimum amount of space and has the minimum time complexity required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, tracking counts of appearances.
- Problem-solving patterns identified: Using two bits to track counts of appearances, updating counts based on bit positions.
- Optimization techniques learned: Using constant space, minimizing time complexity.
- Similar problems to practice: Single Number, Single Number III.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the `ones` and `twos` integers, not handling the case where a bit appears three times.
- Edge cases to watch for: Empty array, array with all elements appearing three times.
- Performance pitfalls: Using excessive space, having a high time complexity.
- Testing considerations: Test with arrays of different sizes, test with arrays containing different numbers of unique elements.