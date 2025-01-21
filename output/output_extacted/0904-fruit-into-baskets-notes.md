## Fruit Into Baskets

**Problem Link:** https://leetcode.com/problems/fruit-into-baskets/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of integers representing the types of fruits in a row, where each integer corresponds to a specific fruit type.
- Expected output format: The function should return the maximum number of fruits that can be collected into baskets, with a constraint of at most two different types of fruits in the baskets.
- Key requirements and edge cases to consider: The function should handle cases where there is only one type of fruit, or where there are more than two types of fruits in the list.
- Example test cases with explanations:
  - Example 1: Input: `[1,2,1]`, Output: `3`, Explanation: We can collect all fruits in one go.
  - Example 2: Input: `[0,1,2,2]`, Output: `3`, Explanation: We can collect the first two fruits and the last fruit.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of fruits and calculate the maximum number of fruits that can be collected.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of fruits.
  2. For each combination, check if it satisfies the constraint of having at most two different types of fruits.
  3. If it satisfies the constraint, calculate the number of fruits in the combination.
  4. Keep track of the maximum number of fruits found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int totalFruit(std::vector<int>& fruits) {
    int n = fruits.size();
    int maxFruits = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            std::vector<int> fruitTypes;
            for (int k = i; k <= j; k++) {
                if (std::find(fruitTypes.begin(), fruitTypes.end(), fruits[k]) == fruitTypes.end()) {
                    fruitTypes.push_back(fruits[k]);
                }
                if (fruitTypes.size() > 2) {
                    break;
                }
            }
            if (fruitTypes.size() <= 2) {
                maxFruits = std::max(maxFruits, j - i + 1);
            }
        }
    }
    return maxFruits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of fruits. This is because we have three nested loops: two for generating all possible combinations of fruits, and one for checking the constraint.
> - **Space Complexity:** $O(n)$, where $n$ is the number of fruits. This is because we need to store all possible combinations of fruits.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible combinations of fruits, which is not necessary. The space complexity is also high because we need to store all possible combinations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to solve this problem. The sliding window will represent the current combination of fruits.
- Detailed breakdown of the approach:
  1. Initialize the sliding window to the first fruit.
  2. Expand the sliding window to the right by adding one fruit at a time.
  3. If the number of different types of fruits in the sliding window exceeds 2, shrink the sliding window from the left by removing one fruit at a time.
  4. Keep track of the maximum number of fruits in the sliding window.
- Proof of optimality: This approach is optimal because it only considers the necessary combinations of fruits and does not generate all possible combinations.

```cpp
#include <vector>
#include <unordered_map>

int totalFruit(std::vector<int>& fruits) {
    int n = fruits.size();
    int maxFruits = 0;
    int left = 0;
    std::unordered_map<int, int> fruitCount;
    for (int right = 0; right < n; right++) {
        fruitCount[fruits[right]]++;
        while (fruitCount.size() > 2) {
            fruitCount[fruits[left]]--;
            if (fruitCount[fruits[left]] == 0) {
                fruitCount.erase(fruits[left]);
            }
            left++;
        }
        maxFruits = std::max(maxFruits, right - left + 1);
    }
    return maxFruits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of fruits. This is because we only iterate through the list of fruits once.
> - **Space Complexity:** $O(1)$, where $n$ is the number of fruits. This is because we only need to store the count of each type of fruit in the sliding window, and the number of types is at most 2.
> - **Optimality proof:** This approach is optimal because it only considers the necessary combinations of fruits and does not generate all possible combinations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, hash map for efficient lookup.
- Problem-solving patterns identified: Using a sliding window to reduce the problem size.
- Optimization techniques learned: Avoiding unnecessary iterations and using efficient data structures.
- Similar problems to practice: Other problems that can be solved using the sliding window approach, such as `Minimum Window Substring` and `Longest Substring Without Repeating Characters`.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the edge cases, such as an empty list of fruits.
- Edge cases to watch for: Handling cases where there is only one type of fruit, or where there are more than two types of fruits in the list.
- Performance pitfalls: Using inefficient data structures or algorithms, such as generating all possible combinations of fruits.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.