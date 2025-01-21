## Hand of Straights
**Problem Link:** https://leetcode.com/problems/hand-of-straights/description

**Problem Statement:**
- Input format: An array of integers `hand` and an integer `W`.
- Constraints: `1 <= hand.length <= 1000`, `0 <= hand[i] <= 1000`, `1 <= W <= hand.length`.
- Expected output format: A boolean indicating whether the hand can be divided into `W` groups of consecutive integers.
- Key requirements and edge cases to consider: Handling duplicate cards, ensuring groups are consecutive, and verifying the number of groups matches `W`.
- Example test cases with explanations:
  - Input: `hand = [1,2,3,6,2,3,4,7,8], W = 3`, Output: `True`, Explanation: We can divide the hand into `W = 3` groups of consecutive integers: `[1,2,3]`, `[2,3,4]`, and `[6,7,8]`.
  - Input: `hand = [1,2,3,4,5], W = 4`, Output: `False`, Explanation: We cannot divide the hand into `W = 4` groups of consecutive integers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of consecutive integers to form groups.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of consecutive integers from the hand.
  2. For each combination, check if it can be divided into `W` groups.
  3. If a valid division is found, return `True`.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
#include <vector>
#include <algorithm>

bool isNStraightHand(std::vector<int>& hand, int W) {
    std::sort(hand.begin(), hand.end());
    int n = hand.size();
    for (int i = 0; i < n; i++) {
        std::vector<bool> visited(n, false);
        visited[i] = true;
        int groups = 1;
        int current = hand[i];
        for (int j = i + 1; j < n; j++) {
            if (!visited[j] && hand[j] == current + 1) {
                visited[j] = true;
                current = hand[j];
                groups++;
            }
            if (groups == W) break;
        }
        if (groups == W) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cards in the hand. This is because we iterate over the hand for each card.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cards in the hand. This is because we use a visited array to keep track of visited cards.
> - **Why these complexities occur:** The brute force approach involves checking all possible combinations of consecutive integers, resulting in quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a hashmap to store the frequency of each card and then iterating over the hand to form groups.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the frequency of each card.
  2. Iterate over the hand to form groups of consecutive integers.
  3. For each group, decrement the frequency of each card in the group.
  4. If a card has a frequency of 0, it cannot be used to form a group.
- Proof of optimality: This approach ensures that we consider all possible combinations of consecutive integers while minimizing the number of iterations.

```cpp
#include <vector>
#include <unordered_map>

bool isNStraightHand(std::vector<int>& hand, int W) {
    if (hand.size() % W != 0) return false;
    std::sort(hand.begin(), hand.end());
    std::unordered_map<int, int> count;
    for (int num : hand) count[num]++;
    for (int num : hand) {
        if (count[num] == 0) continue;
        int current = num;
        for (int i = 0; i < W; i++) {
            if (count[current] == 0) return false;
            count[current]--;
            current++;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of cards in the hand. This is because we sort the hand and then iterate over it.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cards in the hand. This is because we use a hashmap to store the frequency of each card.
> - **Optimality proof:** This approach ensures that we consider all possible combinations of consecutive integers while minimizing the number of iterations, resulting in a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store frequency, iterating over the hand to form groups, and minimizing iterations.
- Problem-solving patterns identified: Considering all possible combinations, using a hashmap to store frequency, and minimizing iterations.
- Optimization techniques learned: Using a hashmap to store frequency, iterating over the hand to form groups, and minimizing iterations.
- Similar problems to practice: Other problems involving forming groups or combinations, such as `Partition Equal Subset Sum` or `Partition to K Equal Sum Subsets`.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible combinations, not minimizing iterations, or not using a hashmap to store frequency.
- Edge cases to watch for: Handling duplicate cards, ensuring groups are consecutive, and verifying the number of groups matches `W`.
- Performance pitfalls: Not using a hashmap to store frequency, not iterating over the hand to form groups, or not minimizing iterations.
- Testing considerations: Testing with different inputs, such as different hand sizes, different values of `W`, and different combinations of cards.