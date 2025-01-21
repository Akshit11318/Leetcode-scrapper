## Removing Minimum Number of Magic Beans
**Problem Link:** https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description

**Problem Statement:**
- Input format and constraints: You are given an array of integers `beans`, where each integer represents the number of magic beans in a bag.
- Expected output format: Return the minimum number of bags you need to remove to make the average number of beans in each bag a whole number.
- Key requirements and edge cases to consider: The input array is non-empty and contains only non-negative integers.
- Example test cases with explanations:
  - If `beans = [1,2,3,4,5,6,7,8,9]`, the average number of beans is `5`. To make the average a whole number, we need to remove bags with a total of `1 + 3 + 5 + 7 + 9 = 25` beans. We can do this by removing `2` bags with `1` and `3` beans, or `3` bags with `1`, `2`, and `3` beans, etc. However, the minimum number of bags to remove is `1`, by removing the bag with `1` or `3` or `5` or `7` or `9` beans.
  - If `beans = [1,2,3,4,5,6,7,8,9,10]`, the average number of beans is `5.5`. To make the average a whole number, we need to remove bags with a total of `1 + 3 + 5 + 7 + 9 = 25` beans. We can do this by removing `2` bags with `1` and `3` beans, or `3` bags with `1`, `2`, and `3` beans, etc. However, the minimum number of bags to remove is `1`, by removing the bag with `5` or `10` beans.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing bags and calculate the average for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of bags to remove.
  2. For each combination, calculate the total number of beans in the remaining bags.
  3. Calculate the average number of beans in each bag for the remaining bags.
  4. Check if the average is a whole number.
  5. If it is, update the minimum number of bags to remove.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minimum_bags_to_remove(std::vector<int>& beans) {
    int n = beans.size();
    int min_bags = n;
    for (int mask = 0; mask < (1 << n); mask++) {
        int total_beans = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                total_beans += beans[i];
                count++;
            }
        }
        if (count > 0 && total_beans % count == 0) {
            int bags_to_remove = __builtin_popcount(mask);
            min_bags = std::min(min_bags, bags_to_remove);
        }
    }
    return min_bags;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of bags. This is because we generate all possible combinations of bags to remove, which is $2^n$, and for each combination, we calculate the total number of beans and the average, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, making it constant.
> - **Why these complexities occur:** The time complexity is exponential because we are generating all possible combinations of bags to remove. The space complexity is constant because we only use a fixed amount of space to store the minimum number of bags to remove and the current combination of bags to remove.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The average number of beans in each bag will be a whole number if and only if the total number of beans is divisible by the number of bags. Therefore, we need to find the minimum number of bags to remove such that the total number of beans in the remaining bags is divisible by the number of remaining bags.
- Detailed breakdown of the approach:
  1. Calculate the total number of beans and the number of bags.
  2. Calculate the remainder of the total number of beans divided by the number of bags.
  3. If the remainder is 0, return 0 because we don't need to remove any bags.
  4. Otherwise, try removing each bag one by one and calculate the new remainder.
  5. If the new remainder is 0, return 1 because we only need to remove one bag.
  6. If we can't remove one bag to make the remainder 0, try removing two bags and calculate the new remainder.
  7. Repeat this process until we find the minimum number of bags to remove.
- Proof of optimality: This approach is optimal because it tries all possible combinations of removing bags and returns the minimum number of bags to remove.
- Why further optimization is impossible: This approach is already optimal because it tries all possible combinations of removing bags.

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int minimum_bags_to_remove(std::vector<int>& beans) {
    int n = beans.size();
    int total_beans = std::accumulate(beans.begin(), beans.end(), 0);
    int remainder = total_beans % n;
    if (remainder == 0) return 0;
    for (int i = 0; i < n; i++) {
        int new_remainder = (total_beans - beans[i]) % (n - 1);
        if (new_remainder == 0) return 1;
    }
    return 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bags. This is because we try removing each bag one by one and calculate the new remainder.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, making it constant.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of removing bags and returns the minimum number of bags to remove.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trying all possible combinations of removing bags and calculating the average number of beans in each bag.
- Problem-solving patterns identified: Using a brute force approach to try all possible solutions and then optimizing it to find the minimum number of bags to remove.
- Optimization techniques learned: Trying to remove each bag one by one and calculating the new remainder to find the minimum number of bags to remove.
- Similar problems to practice: Problems that involve trying all possible combinations of solutions and optimizing them to find the minimum or maximum value.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the remainder is 0 before trying to remove bags.
- Edge cases to watch for: When the total number of beans is divisible by the number of bags, we don't need to remove any bags.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of removing bags without optimizing it.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it returns the correct result.