## Number of Unique Flavors After Sharing K Candies
**Problem Link:** https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/description

**Problem Statement:**
- Input format and constraints: Given a list of candies with their respective flavors, and an integer `k`, determine the number of unique flavors that can be obtained after sharing `k` candies.
- Expected output format: The number of unique flavors after sharing `k` candies.
- Key requirements and edge cases to consider:
  - If `k` is greater than or equal to the total number of candies, all candies can be shared, resulting in all flavors being unique.
  - If `k` is 0, no candies can be shared, resulting in the same number of unique flavors as before.
- Example test cases with explanations:
  - Input: `candies = [1, 2, 2, 3, 4, 4]`, `k = 2`
    Output: `4`
    Explanation: Share candies with flavors 2 and 4, resulting in unique flavors 1, 2, 3, and 4.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over all possible combinations of candies that can be shared, and calculate the number of unique flavors for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of candies that can be shared.
  2. For each combination, remove the shared candies from the list.
  3. Calculate the number of unique flavors in the remaining list.
  4. Keep track of the maximum number of unique flavors found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it has a high time complexity due to the generation of all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int numUniqueFlavors(std::vector<int>& candies, int k) {
    int maxUnique = 0;
    for (int i = 0; i < (1 << candies.size()); i++) {
        std::vector<int> remainingCandies = candies;
        int sharedCandies = 0;
        for (int j = 0; j < candies.size(); j++) {
            if ((i & (1 << j)) != 0) {
                remainingCandies.erase(remainingCandies.begin() + j);
                sharedCandies++;
                j--;
            }
        }
        if (sharedCandies == k) {
            std::unordered_set<int> uniqueFlavors(remainingCandies.begin(), remainingCandies.end());
            maxUnique = std::max(maxUnique, static_cast<int>(uniqueFlavors.size()));
        }
    }
    return maxUnique;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of candies. This is because we generate all possible combinations of candies, and for each combination, we iterate over the list of candies to remove the shared ones.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candies. This is because we store the remaining candies in a separate list.
> - **Why these complexities occur:** The high time complexity is due to the generation of all possible combinations of candies, and the space complexity is due to the storage of the remaining candies.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the frequency of each flavor, and then iterate over the flavors to calculate the number of unique flavors after sharing `k` candies.
- Detailed breakdown of the approach:
  1. Create a hash map to store the frequency of each flavor.
  2. Iterate over the list of candies and update the frequency of each flavor in the hash map.
  3. Initialize a variable to store the number of unique flavors after sharing `k` candies.
  4. Iterate over the hash map and for each flavor, if its frequency is greater than 1, subtract the minimum between its frequency and `k` from `k`, and increment the number of unique flavors.
  5. If `k` is still greater than 0, increment the number of unique flavors by the number of flavors with a frequency of 1 that can be shared.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the number of candies, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int numUniqueFlavors(std::vector<int>& candies, int k) {
    std::unordered_map<int, int> flavorFrequency;
    for (int candy : candies) {
        flavorFrequency[candy]++;
    }
    int uniqueFlavors = 0;
    for (auto& pair : flavorFrequency) {
        if (pair.second > 1) {
            k -= std::min(pair.second, k);
            uniqueFlavors++;
        }
    }
    if (k > 0) {
        for (auto& pair : flavorFrequency) {
            if (pair.second == 1) {
                k--;
                uniqueFlavors++;
                if (k == 0) {
                    break;
                }
            }
        }
    }
    return uniqueFlavors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of candies. This is because we iterate over the list of candies to update the frequency of each flavor, and then iterate over the hash map to calculate the number of unique flavors.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candies. This is because we store the frequency of each flavor in a hash map.
> - **Optimality proof:** This approach has the best possible time complexity for this problem, as we only need to iterate over the list of candies and the hash map once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, frequency counting, and iterative approaches.
- Problem-solving patterns identified: Using hash maps to store frequency information and iterating over the map to calculate the result.
- Optimization techniques learned: Reducing the time complexity by using a hash map to store frequency information and iterating over the map only once.
- Similar problems to practice: Problems involving frequency counting, hash maps, and iterative approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty list of candies or a negative value of `k`.
- Edge cases to watch for: Handling cases where `k` is greater than or equal to the total number of candies, or where `k` is 0.
- Performance pitfalls: Using a brute force approach with a high time complexity, or not optimizing the solution by using a hash map to store frequency information.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure its correctness and performance.