## Count Number of Distinct Integers After Reverse Operations

**Problem Link:** https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 10^5$, $0 \leq nums[i] \leq 10^9$.
- Expected output format: The number of distinct integers after applying reverse operations.
- Key requirements and edge cases to consider: Handling leading zeros when reversing numbers, identifying distinct integers after reversal.
- Example test cases with explanations:
  - `nums = [1, 13, 10, 1207]`: Reversing these numbers gives `[1, 31, 01, 7021]`. After removing leading zeros, we have `[1, 31, 1, 7021]`, which contains 3 distinct integers.
  - `nums = [2, 2, 2]`: Reversing these numbers gives `[2, 2, 2]`, which contains 1 distinct integer.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each number in the input array, reverse it and store the reversed numbers in a new array or data structure.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set or hash table to store unique reversed integers.
  2. Iterate through each number in the input array.
  3. Reverse the current number and remove any leading zeros.
  4. Add the reversed number to the set.
  5. After iterating through all numbers, return the size of the set, which represents the number of distinct integers after reverse operations.

```cpp
#include <iostream>
#include <unordered_set>
#include <string>

int countDistinctIntegers(int* nums, int numsSize) {
    std::unordered_set<int> uniqueIntegers;
    for (int i = 0; i < numsSize; ++i) {
        std::string str = std::to_string(nums[i]);
        std::string reversedStr = std::string(str.rbegin(), str.rend());
        // Remove leading zeros
        while (!reversedStr.empty() && reversedStr[0] == '0') {
            reversedStr.erase(reversedStr.begin());
        }
        if (reversedStr.empty()) {
            reversedStr = "0"; // Handle the case where the reversed string becomes empty
        }
        uniqueIntegers.insert(std::stoi(reversedStr));
    }
    return uniqueIntegers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of integers in the input array, and $m$ is the average number of digits in the integers. This is because for each integer, we are reversing it, which takes $O(m)$ time.
> - **Space Complexity:** $O(n \cdot m)$, as in the worst case, we might store all reversed integers in the set, each of which could have up to $m$ digits.
> - **Why these complexities occur:** The time complexity is dominated by the operation of reversing each integer and then converting it back to an integer to store in the set. The space complexity is due to the storage of these reversed integers in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, as the problem inherently requires examining each number, reversing it, and checking for uniqueness.
- Detailed breakdown of the approach: Same steps as the brute force approach but with optimizations in implementation, such as using `std::string` to handle leading zeros and reversing the string efficiently.
- Proof of optimality: This approach is optimal because it must examine each number at least once to reverse it and check for uniqueness, making it a linear time complexity operation with respect to the input size and the size of the numbers.
- Why further optimization is impossible: Further optimization is not possible because the problem requires checking each number and its reverse, which already achieves a linear time complexity with respect to the input size.

```cpp
#include <iostream>
#include <unordered_set>
#include <string>

int countDistinctIntegers(int* nums, int numsSize) {
    std::unordered_set<int> uniqueIntegers;
    for (int i = 0; i < numsSize; ++i) {
        std::string str = std::to_string(nums[i]);
        std::string reversedStr = std::string(str.rbegin(), str.rend());
        // Remove leading zeros
        while (!reversedStr.empty() && reversedStr[0] == '0') {
            reversedStr.erase(reversedStr.begin());
        }
        if (reversedStr.empty()) {
            reversedStr = "0"; // Handle the case where the reversed string becomes empty
        }
        uniqueIntegers.insert(std::stoi(reversedStr));
        // Also add the original number to the set
        uniqueIntegers.insert(nums[i]);
    }
    return uniqueIntegers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of integers and $m$ is the average number of digits in the integers.
> - **Space Complexity:** $O(n \cdot m)$, for storing the unique integers in the set.
> - **Optimality proof:** This solution is optimal because it checks each number and its reverse exactly once, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reversing numbers, handling leading zeros, using sets for uniqueness.
- Problem-solving patterns identified: Checking each element and its transformation for uniqueness.
- Optimization techniques learned: Using `std::string` for efficient string manipulation.
- Similar problems to practice: Problems involving string manipulation, uniqueness, and transformations.

**Mistakes to Avoid:**
- Not handling leading zeros properly when reversing numbers.
- Not using a set or similar data structure to efficiently keep track of unique integers.
- Not considering the case where the reversed string becomes empty.
- Not testing the solution with a variety of inputs, including edge cases like zero and numbers with leading zeros.