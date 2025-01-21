## Max Sum of a Pair with Equal Sum of Digits

**Problem Link:** https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected output format: The maximum sum of a pair of numbers with an equal sum of digits.
- Key requirements and edge cases to consider: If no such pair exists, return -1.
- Example test cases with explanations: 
    - `nums = [42,24,32,34]`, return `57` because `24 + 33 = 57` and `2+4 = 2+3+3 = 6`.
    - `nums = [100,12]`, return `-1` because no pair exists.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every pair of numbers in the array to see if they have an equal sum of digits.
- Step-by-step breakdown of the solution:
    1. Iterate over the array to consider each number as the first element of a pair.
    2. For each first element, iterate over the rest of the array to consider each number as the second element of a pair.
    3. For each pair, calculate the sum of digits of both numbers and compare them.
    4. If the sums are equal, calculate the sum of the pair and update the maximum sum found so far if necessary.
- Why this approach comes to mind first: It directly addresses the problem by checking all possible pairs, which is a straightforward but inefficient way to solve the problem.

```cpp
#include <vector>
#include <algorithm>

int maxSum(std::vector<int>& nums) {
    int maxSum = -1;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int sum1 = getDigitSum(nums[i]);
            int sum2 = getDigitSum(nums[j]);
            if (sum1 == sum2) {
                maxSum = std::max(maxSum, nums[i] + nums[j]);
            }
        }
    }
    return maxSum;
}

int getDigitSum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of elements in `nums` and $m$ is the maximum number of digits in a number in `nums`. The outer two loops iterate over the array, and the `getDigitSum` function iterates over the digits of a number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and temporary variables.
> - **Why these complexities occur:** The brute force approach checks all pairs of numbers, leading to quadratic time complexity in terms of the number of elements. The calculation of the sum of digits for each number adds a linear factor in terms of the number of digits.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all pairs of numbers, we can group numbers by their sum of digits and then find the maximum sum within each group.
- Detailed breakdown of the approach:
    1. Create a hashmap where the keys are the sums of digits and the values are vectors of numbers with that sum of digits.
    2. Iterate over the array to populate the hashmap.
    3. For each group in the hashmap, find the maximum sum of a pair of numbers.
    4. Update the overall maximum sum if a larger sum is found in any group.
- Proof of optimality: This approach reduces the time complexity by avoiding the need to compare every pair of numbers. It ensures that we consider all possible pairs with an equal sum of digits while minimizing unnecessary comparisons.

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

int maxSum(std::vector<int>& nums) {
    std::unordered_map<int, std::vector<int>> digitSums;
    for (int num : nums) {
        int sum = getDigitSum(num);
        digitSums[sum].push_back(num);
    }
    
    int maxSum = -1;
    for (auto& pair : digitSums) {
        std::vector<int>& numbers = pair.second;
        if (numbers.size() > 1) {
            std::sort(numbers.begin(), numbers.end());
            maxSum = std::max(maxSum, numbers[numbers.size() - 1] + numbers[numbers.size() - 2]);
        }
    }
    return maxSum;
}

int getDigitSum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \log n)$, where $n$ is the number of elements in `nums` and $m$ is the maximum number of digits in a number in `nums`. The initial iteration over the array and the calculation of digit sums take $O(n \cdot m)$ time, and sorting the vectors in the hashmap takes $O(n \log n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, as we store all numbers in the hashmap.
> - **Optimality proof:** This approach minimizes the number of comparisons needed to find the maximum sum of a pair with an equal sum of digits by grouping numbers based on their digit sums and then considering only the largest pairs within each group.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, sorting, and optimization by reducing the number of comparisons.
- Problem-solving patterns identified: Grouping items based on a common property to reduce the search space.
- Optimization techniques learned: Avoiding unnecessary comparisons by leveraging the properties of the data.
- Similar problems to practice: Other problems involving grouping or categorization to optimize solutions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input array or groups with fewer than two elements.
- Edge cases to watch for: Arrays with a single element, arrays with all elements having different sums of digits.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases and large datasets.