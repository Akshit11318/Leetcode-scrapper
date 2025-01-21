## Distribute Candies to People
**Problem Link:** https://leetcode.com/problems/distribute-candies-to-people/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers as input: `n` representing the number of people and `candies` representing the total number of candies to be distributed.
- Expected output format: The function should return a vector of integers, where each integer represents the number of candies given to the corresponding person.
- Key requirements and edge cases to consider: The distribution should start from the first person and continue in a circular manner, with each person receiving one more candy than the previous person in each round until all candies are distributed.
- Example test cases with explanations: For example, given `n = 4` and `candies = 7`, the output should be `[1,2,3,1]` because in the first round, the first person gets 1 candy, the second person gets 2 candies, and the third person gets 3 candies. Then, in the second round, only the fourth person gets 1 candy, as there are not enough candies for another full round.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The straightforward approach is to simulate the distribution process round by round, keeping track of the candies given to each person.
- Step-by-step breakdown of the solution:
  1. Initialize a vector `result` of size `n` with all elements as 0 to keep track of the candies given to each person.
  2. Initialize a variable `i` to 0 to represent the current person and a variable `candies_to_give` to 1 to represent the number of candies to give in the current round.
  3. Loop until all candies are distributed (`candies > 0`).
  4. In each iteration, give `candies_to_give` candies to the current person (`result[i] += candies_to_give`), subtract these candies from the total (`candies -= candies_to_give`), and move to the next person (`i = (i + 1) % n`).
  5. Increment `candies_to_give` for the next round (`candies_to_give++`).
- Why this approach comes to mind first: It directly simulates the problem's description, making it intuitive but potentially inefficient due to the looping and conditional checks.

```cpp
vector<int> distributeCandies(int n, int candies) {
    vector<int> result(n, 0);
    int i = 0, candies_to_give = 1;
    while (candies > 0) {
        if (candies_to_give > candies) {
            result[i] += candies;
            break;
        }
        result[i] += candies_to_give;
        candies -= candies_to_give;
        i = (i + 1) % n;
        candies_to_give++;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{candies}{n} + n)$ because in the worst case, we might have to distribute candies for $\frac{candies}{n}$ rounds, and each round involves $n$ people. However, since `candies_to_give` increases by 1 each time, the actual number of rounds is less.
> - **Space Complexity:** $O(n)$ for storing the result vector.
> - **Why these complexities occur:** The time complexity is due to the loop that continues until all candies are distributed, and the space complexity is due to the storage needed for the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the distribution process, we can calculate the number of full rounds and the remaining candies. Then, distribute the candies for the full rounds and the remaining candies separately.
- Detailed breakdown of the approach:
  1. Calculate the total number of candies that can be distributed in full rounds (`total_candies_in_full_rounds = (n * (n + 1)) / 2`).
  2. Determine the number of full rounds (`full_rounds = total_candies_in_full_rounds / n`).
  3. Calculate the remaining candies after full rounds (`remaining_candies = candies - full_rounds * n`).
  4. Initialize the result vector with the sum of the first `n` natural numbers multiplied by the number of full rounds (`result[i] = (i + 1) * full_rounds` for each `i`).
  5. Distribute the remaining candies by adding 1 to each person in the sequence until all remaining candies are distributed.
- Proof of optimality: This approach reduces the time complexity by avoiding the need to simulate each round of distribution, making it more efficient for large inputs.
- Why further optimization is impossible: The problem inherently requires distributing candies in a specific pattern, and any solution must at least calculate the distribution for each person, making the time complexity at least $O(n)$.

```cpp
vector<int> distributeCandies(int n, int candies) {
    vector<int> result(n, 0);
    int full_rounds = 0;
    int total_candies_in_full_rounds = (n * (n + 1)) / 2;
    while (candies >= total_candies_in_full_rounds) {
        candies -= total_candies_in_full_rounds;
        full_rounds++;
        for (int i = 0; i < n; i++) {
            result[i] += (i + 1);
        }
    }
    int i = 0;
    while (candies > 0) {
        int give = min(i + 1, candies);
        result[i] += give;
        candies -= give;
        i = (i + 1) % n;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + \sqrt{candies})$ because the while loop runs for at most $\sqrt{candies}$ iterations (due to the increase in `total_candies_in_full_rounds`), and then we distribute the remaining candies, which takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(n)$ for the result vector.
> - **Optimality proof:** The time complexity is optimized by reducing the number of iterations needed to distribute the candies, making it more efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, optimization by reducing unnecessary iterations, and calculation of distribution patterns.
- Problem-solving patterns identified: Breaking down the problem into manageable parts (full rounds and remaining candies) and solving each part separately.
- Optimization techniques learned: Avoiding unnecessary iterations and calculating distributions directly.
- Similar problems to practice: Other distribution or allocation problems that require optimizing the distribution process.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of full rounds or remaining candies, and not handling the distribution of remaining candies correctly.
- Edge cases to watch for: When `candies` is less than `n`, and when `candies` is exactly divisible by `n`.
- Performance pitfalls: Using a brute force approach for large inputs, which can lead to significant performance issues.
- Testing considerations: Test with various inputs, including edge cases, to ensure the solution works correctly and efficiently.