## Maximum Beauty of an Array After Applying Operation
**Problem Link:** https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description

**Problem Statement:**
- Input format and constraints: The problem involves an array of integers and a series of operations where we can either multiply an element by -1 or add 1 to all elements. The goal is to maximize the beauty of the array, which is calculated as the sum of the absolute values of its elements minus the minimum absolute value.
- Expected output format: The maximum beauty of the array after applying the operations.
- Key requirements and edge cases to consider: Handling arrays with negative numbers, zeros, and positive numbers, and considering the impact of the operations on these values.
- Example test cases with explanations: 
    - For the array [1, -2, 3, -4, 5], the maximum beauty can be achieved by not changing the array, resulting in a beauty of |1| + |-2| + |3| + |-4| + |5| - min(|1|, |-2|, |3|, |-4|, |5|) = 1 + 2 + 3 + 4 + 5 - 1 = 14.
    - For the array [-1, -2, -3, -4, -5], the maximum beauty can be achieved by multiplying all elements by -1 and then not changing the array, resulting in a beauty of |1| + |2| + |3| + |4| + |5| - min(|1|, |2|, |3|, |4|, |5|) = 1 + 2 + 3 + 4 + 5 - 1 = 14.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of operations (multiplying by -1 and adding 1) to all elements and calculate the beauty of the array after each combination.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of operations for each element.
    2. For each combination, apply the operations to the array.
    3. Calculate the beauty of the array after applying the operations.
    4. Keep track of the maximum beauty found.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

int maxBeauty(std::vector<int>& nums) {
    int maxBeauty = INT_MIN;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        std::vector<int> temp = nums;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i))) {
                temp[i] *= -1;
            }
        }
        int minAbs = INT_MAX;
        int sumAbs = 0;
        for (int num : temp) {
            int absNum = std::abs(num);
            minAbs = std::min(minAbs, absNum);
            sumAbs += absNum;
        }
        maxBeauty = std::max(maxBeauty, sumAbs - minAbs);
    }
    return maxBeauty;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate $2^n$ combinations and for each combination, we iterate over the array.
> - **Space Complexity:** $O(n)$, for storing the temporary array.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of operations, which leads to exponential time complexity. The space complexity is linear due to the temporary array used to store the modified elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves understanding that to maximize the beauty of the array, we should aim to have as many positive numbers as possible and minimize the minimum absolute value. Since we can add 1 to all elements, we should first make all negative numbers positive by multiplying them by -1 if necessary, and then consider adding 1 to all elements to minimize the minimum absolute value.
- Detailed breakdown of the approach: 
    1. Count the number of negative numbers in the array.
    2. If there are any negative numbers, multiply them by -1 to make them positive.
    3. Calculate the minimum absolute value in the array.
    4. If adding 1 to all elements would increase the beauty (i.e., the minimum absolute value is less than the number of elements), add 1 to all elements and recalculate the beauty.
- Proof of optimality: This approach is optimal because it ensures that we have as many positive numbers as possible and minimizes the minimum absolute value, thus maximizing the beauty of the array.

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int maxBeauty(std::vector<int>& nums) {
    int minAbs = INT_MAX;
    int sumAbs = 0;
    for (int& num : nums) {
        num = std::abs(num);
        minAbs = std::min(minAbs, num);
        sumAbs += num;
    }
    return sumAbs - minAbs;
}
```

However, to fully optimize, we need to consider adding 1 to all elements to minimize the minimum absolute value. Here's the optimized code:

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int maxBeauty(std::vector<int>& nums) {
    int minAbs = INT_MAX;
    int sumAbs = 0;
    for (int& num : nums) {
        num = std::abs(num);
        minAbs = std::min(minAbs, num);
        sumAbs += num;
    }
    int add = std::min(minAbs, (int)nums.size());
    return sumAbs + add - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the array once to calculate the sum and minimum of absolute values.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store the sum and minimum of absolute values.
> - **Optimality proof:** This approach is optimal because it ensures that we have as many positive numbers as possible and minimizes the minimum absolute value, thus maximizing the beauty of the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, absolute value calculation, and minimization.
- Problem-solving patterns identified: Understanding the problem requirements, identifying key insights, and optimizing the solution.
- Optimization techniques learned: Minimizing the minimum absolute value and considering the impact of operations on the array.
- Similar problems to practice: Other optimization problems involving arrays and operations.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the impact of operations on the array, not minimizing the minimum absolute value.
- Edge cases to watch for: Empty arrays, arrays with all negative numbers, arrays with all positive numbers.
- Performance pitfalls: Using inefficient algorithms or data structures.
- Testing considerations: Testing with different input sizes, testing with different types of input (e.g., all negative, all positive).