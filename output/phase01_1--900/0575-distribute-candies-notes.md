## Distribute Candies

**Problem Link:** https://leetcode.com/problems/distribute-candies/description

**Problem Statement:**
- Input: An array of candies of different types represented by integers, and the number of sisters `n`.
- Constraints: $2 \leq n \leq 100$, $1 \leq candies.length \leq 100$, $1 \leq candies[i] \leq 1000$.
- Expected Output: A boolean indicating whether it's possible to distribute the candies equally among the sisters.
- Key Requirements: The distribution should ensure each sister gets at least one candy of a unique type.
- Edge Cases: When the number of unique candies is less than the number of sisters.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try and distribute the candies in a way that each sister gets at least one unique candy type. 
- Step-by-step breakdown involves iterating through the array of candies, trying to assign each unique candy to a sister.
- This approach comes to mind first because it directly addresses the requirement of distributing unique candies.

```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

bool canDistributeCandiesBrute(vector<int>& candies) {
    unordered_set<int> uniqueCandies;
    for (int candy : candies) {
        uniqueCandies.insert(candy);
    }
    return uniqueCandies.size() >= candies.size() / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of candies, because we're doing a single pass through the array of candies to find unique types.
> - **Space Complexity:** $O(n)$, as in the worst case, every candy could be of a unique type, requiring storage for each.
> - **Why these complexities occur:** The time complexity is linear because we're iterating through the candies once, and the space complexity is also linear because we're storing each unique candy in a set.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is realizing we only need to count the number of unique candies and compare it to half the number of sisters.
- Detailed breakdown involves using a set to store unique candies, which automatically eliminates duplicates.
- Proof of optimality: This is the most efficient way because we're only iterating through the candies once and using a data structure that allows for constant time complexity operations (insertion and lookup in a set).

```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

bool distributeCandies(vector<int>& candies) {
    unordered_set<int> uniqueCandies;
    for (int candy : candies) {
        uniqueCandies.insert(candy);
    }
    return uniqueCandies.size() >= candies.size() / 2 + candies.size() % 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of candies.
> - **Space Complexity:** $O(n)$, as we're storing unique candies in a set.
> - **Optimality proof:** This is optimal because we're doing a single pass through the data and using a set for efficient storage and lookup of unique candies.

---

### Final Notes

**Learning Points:**
- The importance of using sets for storing unique elements.
- How to optimize solutions by focusing on the key requirements of the problem.
- Understanding that sometimes, the optimal solution involves a simple, direct approach.

**Mistakes to Avoid:**
- Overcomplicating the solution by trying to distribute candies individually instead of focusing on the count of unique candies.
- Not considering the use of a set for efficient storage and lookup of unique elements.
- Forgetting to account for the case where the number of candies is odd, requiring an adjustment to the comparison.