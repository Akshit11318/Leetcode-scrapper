## Airplane Seat Assignment Probability

**Problem Link:** https://leetcode.com/problems/airplane-seat-assignment-probability/description

**Problem Statement:**
- Input format and constraints: The input will be an integer `n`, representing the number of passengers.
- Expected output format: The output should be the probability that the last passenger gets their original seat.
- Key requirements and edge cases to consider: The probability should be calculated for a scenario where each passenger randomly chooses a seat.
- Example test cases with explanations: For example, if there is only one passenger, the probability is 1.0. If there are two passengers, the probability is 0.5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the process of passengers randomly choosing seats and calculate the probability based on multiple simulations.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of times the last passenger gets their original seat.
  2. Run multiple simulations.
  3. In each simulation, simulate the process of passengers randomly choosing seats.
  4. Check if the last passenger gets their original seat and update the counter accordingly.
  5. Calculate the probability by dividing the counter by the total number of simulations.
- Why this approach comes to mind first: It is a straightforward and intuitive way to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

double airplaneSeatAssignmentProbabilityBruteForce(int n, int simulations = 1000000) {
    int count = 0;
    srand(time(0));
    for (int i = 0; i < simulations; i++) {
        std::vector<bool> seats(n, false);
        for (int j = 0; j < n - 1; j++) {
            int randomSeat;
            do {
                randomSeat = rand() % n;
            } while (seats[randomSeat]);
            seats[randomSeat] = true;
        }
        if (!seats[n - 1]) {
            count++;
        }
    }
    return static_cast<double>(count) / simulations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times simulations)$, where $n$ is the number of passengers and $simulations$ is the number of simulations.
> - **Space Complexity:** $O(n)$, for the vector of seats.
> - **Why these complexities occur:** The time complexity is high because we are simulating the process for each passenger and for multiple simulations. The space complexity is due to the vector of seats.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: If the first passenger does not choose the last seat, then the last passenger will always get their original seat. If the first passenger chooses the last seat, then the last passenger will never get their original seat. Therefore, the probability is simply the probability that the first passenger does not choose the last seat, which is $\frac{n-1}{n}$.
- Detailed breakdown of the approach:
  1. Calculate the probability that the first passenger does not choose the last seat.
- Proof of optimality: This approach is optimal because it directly calculates the probability without the need for simulations.
- Why further optimization is impossible: This approach has a time complexity of $O(1)$, which is the best possible time complexity.

```cpp
double airplaneSeatAssignmentProbabilityOptimal(int n) {
    return static_cast<double>(n - 1) / n;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the calculation is constant time.
> - **Space Complexity:** $O(1)$, because no additional space is used.
> - **Optimality proof:** This approach is optimal because it directly calculates the probability without the need for simulations, resulting in the best possible time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Probability calculation, simulation, and optimization.
- Problem-solving patterns identified: Identifying key insights that lead to optimal solutions.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary simulations.
- Similar problems to practice: Other probability calculation problems, such as coin flipping or dice rolling.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating probabilities or not considering edge cases.
- Edge cases to watch for: Handling cases where $n$ is 1 or 0.
- Performance pitfalls: Using simulations when a direct calculation is possible.
- Testing considerations: Testing for different values of $n$ and checking for correctness.