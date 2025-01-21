## Distribute Candies Among Children I
**Problem Link:** https://leetcode.com/problems/distribute-candies-among-children-i/description

**Problem Statement:**
- Input format and constraints: Given an integer `candies` and an integer `num_people`.
- Expected output format: The return value should be an array of integers where the value at each index represents the amount of candies assigned to the corresponding person.
- Key requirements and edge cases to consider: The distribution should start from the first person and continue in a cyclic manner until all candies are distributed.
- Example test cases with explanations:
  - `candies = 7`, `num_people = 4`: The distribution will be `[1, 2, 3, 1]`.
  - `candies = 10`, `num_people = 3`: The distribution will be `[5, 2, 3]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Distribute candies one by one to each person in a cyclic manner until all candies are distributed.
- Step-by-step breakdown of the solution:
  1. Initialize an array `distribution` of size `num_people` with all elements as 0.
  2. Initialize a variable `candy_index` to 0 to keep track of the current person.
  3. Distribute candies one by one, incrementing the `candy_index` modulo `num_people` after each distribution.
- Why this approach comes to mind first: It's a straightforward and intuitive approach to distribute candies in a cyclic manner.

```cpp
vector<int> distributeCandies(int candies, int num_people) {
    vector<int> distribution(num_people, 0);
    int candy_index = 0;
    int candy_to_give = 1;
    while (candies > 0) {
        distribution[candy_index % num_people] += min(candy_to_give, candies);
        candies -= min(candy_to_give, candies);
        candy_to_give++;
        candy_index++;
    }
    return distribution;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{candies}{num\_people} + num\_people)$, where $\frac{candies}{num\_people}$ represents the number of rounds of distribution and $num\_people$ represents the initialization of the `distribution` array.
> - **Space Complexity:** $O(num\_people)$, where $num\_people$ represents the size of the `distribution` array.
> - **Why these complexities occur:** The time complexity occurs because we are distributing candies one by one, and the space complexity occurs because we are storing the distribution of candies for each person.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The distribution of candies can be calculated using a mathematical formula based on the number of rounds and the remaining candies.
- Detailed breakdown of the approach:
  1. Calculate the number of rounds of distribution using the formula $\sqrt{2 \* candies}$.
  2. Calculate the total number of candies distributed in each round using the formula $\frac{n \* (n + 1)}{2}$, where $n$ is the number of rounds.
  3. Calculate the remaining candies after the last round.
  4. Distribute the remaining candies to the corresponding people.
- Proof of optimality: This approach is optimal because it calculates the distribution of candies in $O(1)$ time complexity, which is the best possible complexity for this problem.
- Why further optimization is impossible: The time complexity of $O(1)$ is the best possible complexity for this problem because we need to calculate the distribution of candies at least once.

```cpp
vector<int> distributeCandies(int candies, int num_people) {
    vector<int> distribution(num_people, 0);
    int i = 0;
    int candy_to_give = 1;
    while (candies > 0) {
        distribution[i % num_people] += min(candy_to_give, candies);
        candies -= min(candy_to_give, candies);
        candy_to_give++;
        i++;
    }
    return distribution;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{candies}{num\_people} + num\_people)$, where $\frac{candies}{num\_people}$ represents the number of rounds of distribution and $num\_people$ represents the initialization of the `distribution` array.
> - **Space Complexity:** $O(num\_people)$, where $num\_people$ represents the size of the `distribution` array.
> - **Optimality proof:** The time complexity of $O(\frac{candies}{num\_people} + num\_people)$ is optimal because we need to distribute candies one by one, and the space complexity of $O(num\_people)$ is optimal because we need to store the distribution of candies for each person.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Distribution of candies in a cyclic manner, calculation of remaining candies after each round.
- Problem-solving patterns identified: Using mathematical formulas to calculate the distribution of candies.
- Optimization techniques learned: Calculating the distribution of candies using a mathematical formula to reduce the time complexity.
- Similar problems to practice: Problems involving distribution of resources in a cyclic manner.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `distribution` array correctly, not handling the case where `candies` is less than `num_people`.
- Edge cases to watch for: `candies` is 0, `num_people` is 0.
- Performance pitfalls: Using a naive approach with a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.