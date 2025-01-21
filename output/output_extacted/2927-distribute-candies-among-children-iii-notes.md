## Distribute Candies Among Children III
**Problem Link:** https://leetcode.com/problems/distribute-candies-among-children-iii/description

**Problem Statement:**
- Input format: An array of integers `candies` representing the candies each child can have and an integer `num_people` representing the number of children.
- Constraints: `1 <= candies.length <= 100`, `1 <= candies[i] <= 100`, `1 <= num_people <= 100`.
- Expected output format: The number of candies each child can have, represented as an array of integers.
- Key requirements and edge cases to consider: Ensure that the total number of candies distributed does not exceed the total number of candies available.
- Example test cases with explanations:
  - `candies = [1,2,3], num_people = 3` should return `[1,2,3]`.
  - `candies = [30,11,23,4,20], num_people = 3` should return `[11,7,5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Distribute candies to children one by one, starting from the first child, until all candies are distributed or all children have received their fair share.
- Step-by-step breakdown of the solution:
  1. Initialize an array to store the number of candies each child can have.
  2. Iterate through the `candies` array and distribute the candies to the children.
  3. If a child has already received their fair share of candies, move on to the next child.
- Why this approach comes to mind first: It is a straightforward and intuitive way to distribute the candies.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> distributeCandies(std::vector<int>& candies, int num_people) {
    std::vector<int> result(num_people, 0);
    int index = 0;
    for (int candy : candies) {
        result[index % num_people] += candy;
        index++;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of candies, because we are iterating through the `candies` array once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of people, because we need to store the number of candies each child can have.
> - **Why these complexities occur:** The time complexity is linear because we are doing a constant amount of work for each candy, and the space complexity is linear because we need to store the result for each child.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to distribute the candies. We start by giving the first child the first candy, the second child the second candy, and so on.
- Detailed breakdown of the approach:
  1. Initialize an array to store the number of candies each child can have.
  2. Iterate through the `candies` array and distribute the candies to the children using a greedy approach.
- Proof of optimality: This approach is optimal because it ensures that the total number of candies distributed does not exceed the total number of candies available, and it distributes the candies in a fair and efficient manner.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> distributeCandies(std::vector<int>& candies, int num_people) {
    std::vector<int> result(num_people, 0);
    for (int i = 0; i < candies.size(); i++) {
        result[i % num_people] += candies[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of candies, because we are iterating through the `candies` array once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of people, because we need to store the number of candies each child can have.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a minimal amount of space to store the result.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, iteration, and modulo operation.
- Problem-solving patterns identified: Using a greedy approach to distribute resources, iterating through an array, and using modulo to cycle through a list.
- Optimization techniques learned: Using a greedy approach to optimize the distribution of resources.
- Similar problems to practice: Other problems that involve distributing resources, such as coins or items, among a group of people.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the result array, not checking for edge cases, and not using a greedy approach.
- Edge cases to watch for: Empty input array, zero number of people, and negative number of candies.
- Performance pitfalls: Using an inefficient algorithm or data structure, such as a recursive approach or a linked list.
- Testing considerations: Testing with different input sizes, testing with edge cases, and testing with random inputs.