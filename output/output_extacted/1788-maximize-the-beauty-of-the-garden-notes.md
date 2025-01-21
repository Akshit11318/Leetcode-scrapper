## Maximize the Beauty of the Garden

**Problem Link:** https://leetcode.com/problems/maximize-the-beauty-of-the-garden/description

**Problem Statement:**
- Input: An array of integers `flowers` where `flowers[i]` represents the beauty of the `i-th` flower, and an integer `newFlowers` representing the number of new flowers to be planted, and an integer `maxBeauty` representing the maximum beauty that can be added to each flower.
- Expected output: The maximum beauty of the garden after planting the new flowers.
- Key requirements and edge cases to consider: 
    - The beauty of the garden is the sum of the beauty of all flowers.
    - Each new flower can be planted at any position in the garden.
    - The beauty of each flower cannot exceed `maxBeauty`.
- Example test cases with explanations: 
    - For `flowers = [1, 2, 3, 4], newFlowers = 2, maxBeauty = 5`, the maximum beauty of the garden can be achieved by planting two new flowers with beauty 5 at the beginning of the garden, resulting in a total beauty of 1 + 2 + 3 + 4 + 5 + 5 = 20.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of planting new flowers and calculate the total beauty for each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of planting new flowers.
    2. For each combination, calculate the total beauty of the garden.
    3. Update the maximum beauty if the current beauty is greater.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxBeauty(std::vector<int>& flowers, int newFlowers, int maxBeauty) {
    int n = flowers.size();
    int totalBeauty = 0;
    for (int i = 0; i < n; i++) {
        totalBeauty += flowers[i];
    }
    std::vector<int> newFlowersBeauty(newFlowers, maxBeauty);
    std::vector<int> combinedFlowers;
    combinedFlowers.reserve(n + newFlowers);
    combinedFlowers.insert(combinedFlowers.end(), flowers.begin(), flowers.end());
    combinedFlowers.insert(combinedFlowers.end(), newFlowersBeauty.begin(), newFlowersBeauty.end());
    std::sort(combinedFlowers.begin(), combinedFlowers.end());
    int maxTotalBeauty = 0;
    do {
        int currentTotalBeauty = 0;
        for (int i = 0; i < combinedFlowers.size(); i++) {
            currentTotalBeauty += combinedFlowers[i];
        }
        maxTotalBeauty = std::max(maxTotalBeauty, currentTotalBeauty);
    } while (std::next_permutation(combinedFlowers.begin(), combinedFlowers.end()));
    return maxTotalBeauty;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + newFlowers)!)$, where n is the number of flowers. This is because we are generating all permutations of the combined flowers.
> - **Space Complexity:** $O(n + newFlowers)$, where n is the number of flowers. This is because we need to store the combined flowers.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of planting new flowers, resulting in a high time complexity. The space complexity is high because we need to store all the flowers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum beauty of the garden can be achieved by planting new flowers with the maximum beauty and sorting the flowers in descending order.
- Detailed breakdown of the approach:
    1. Sort the flowers in descending order.
    2. Plant new flowers with the maximum beauty and add them to the sorted flowers.
    3. Calculate the total beauty of the garden.
- Proof of optimality: The maximum beauty of the garden is achieved when the new flowers are planted with the maximum beauty and the flowers are sorted in descending order.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maximumBeauty(std::vector<int>& flowers, int newFlowers, int maxBeauty) {
    int n = flowers.size();
    std::sort(flowers.rbegin(), flowers.rend());
    for (int i = 0; i < n; i++) {
        if (flowers[i] < maxBeauty) {
            flowers[i] = maxBeauty;
            newFlowers--;
            if (newFlowers == 0) {
                break;
            }
        }
    }
    if (newFlowers > 0) {
        flowers.insert(flowers.end(), newFlowers, maxBeauty);
    }
    int totalBeauty = 0;
    for (int i = 0; i < flowers.size(); i++) {
        totalBeauty += flowers[i];
    }
    return totalBeauty;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n log n + newFlowers)$, where n is the number of flowers. This is because we are sorting the flowers and adding new flowers.
> - **Space Complexity:** $O(n + newFlowers)$, where n is the number of flowers. This is because we need to store the flowers.
> - **Optimality proof:** The optimal approach achieves the maximum beauty of the garden by planting new flowers with the maximum beauty and sorting the flowers in descending order.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm.
- Problem-solving patterns identified: Maximization problem, greedy approach.
- Optimization techniques learned: Sorting, greedy algorithm.
- Similar problems to practice: Other maximization problems, greedy algorithm problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect sorting, incorrect calculation of total beauty.
- Edge cases to watch for: Empty input, zero new flowers, maximum beauty less than the beauty of existing flowers.
- Performance pitfalls: High time complexity, high space complexity.
- Testing considerations: Test with different inputs, test with edge cases.