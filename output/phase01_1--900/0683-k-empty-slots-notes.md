## K-Empty Slots
**Problem Link:** https://leetcode.com/problems/k-empty-slots/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `flowers` representing the days on which flowers will bloom, and an integer `k`, find the day on which `k` empty slots will be present between the flowers.
- Expected output format: The day on which `k` empty slots will be present.
- Key requirements and edge cases to consider: 
    - `flowers` array can be empty or contain duplicate values.
    - `k` can be larger than the number of flowers.
- Example test cases with explanations:
    - Example 1: `flowers = [1,3,2], k = 1`, Output: `2`
    - Example 2: `flowers = [1,2,3,4], k = 3`, Output: `-1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating through each flower and checking the number of empty slots between it and the next flower.
- Step-by-step breakdown of the solution:
    1. Sort the `flowers` array to get the order in which the flowers will bloom.
    2. Iterate through each flower in the sorted array.
    3. For each flower, check the number of empty slots between it and the next flower.
    4. If the number of empty slots is greater than or equal to `k`, return the day on which the flower will bloom.
- Why this approach comes to mind first: It's a straightforward approach that checks each flower individually.

```cpp
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        sort(flowers.begin(), flowers.end());
        for (int i = 0; i < flowers.size() - 1; i++) {
            if (flowers[i + 1] - flowers[i] - 1 == k) {
                return flowers[i + 1];
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of flowers, due to the sorting operation.
> - **Space Complexity:** $O(1)$, since we're not using any additional space that scales with input size.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity remains constant since we're only using a small amount of space to store variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each flower individually, we can use a more efficient data structure to keep track of the flowers and their positions.
- Detailed breakdown of the approach:
    1. Create a set to store the positions of the flowers.
    2. Iterate through each flower and add its position to the set.
    3. For each flower, check the number of empty slots between it and the next flower by iterating through the set.
    4. If the number of empty slots is greater than or equal to `k`, return the day on which the flower will bloom.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal since we need to iterate through each flower at least once.
- Why further optimization is impossible: We need to check each flower at least once to determine if there are `k` empty slots between it and the next flower.

```cpp
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        set<int> flowerSet;
        int day = 1;
        for (int flower : flowers) {
            flowerSet.insert(flower);
            auto it = flowerSet.find(flower);
            if (it != flowerSet.begin() && *prev(it) + k + 1 == flower) {
                return day;
            }
            if (next(it) != flowerSet.end() && *next(it) - k - 1 == flower) {
                return day;
            }
            day++;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of flowers, since we're iterating through each flower once.
> - **Space Complexity:** $O(n)$, since we're storing the positions of the flowers in a set.
> - **Optimality proof:** This approach is optimal since we need to iterate through each flower at least once to determine if there are `k` empty slots between it and the next flower.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to keep track of the positions of the flowers and iterating through the set to check for empty slots.
- Problem-solving patterns identified: Using a more efficient data structure to improve the time complexity of the solution.
- Optimization techniques learned: Using a set instead of a brute force approach to reduce the time complexity.
- Similar problems to practice: Problems that involve finding the maximum or minimum value in a set, or problems that involve iterating through a set to find a specific condition.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty `flowers` array or a `k` value that is larger than the number of flowers.
- Edge cases to watch for: Handling duplicate values in the `flowers` array and checking for the case where `k` is larger than the number of flowers.
- Performance pitfalls: Using a brute force approach that has a high time complexity, such as iterating through each flower individually.
- Testing considerations: Testing the solution with different inputs, such as an empty `flowers` array or a `k` value that is larger than the number of flowers.