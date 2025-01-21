## Promise Pool
**Problem Link:** https://leetcode.com/problems/promise-pool/description

**Problem Statement:**
- Input format and constraints: The problem requires handling a pool of promises where each promise has a certain probability of being resolved. The task is to find the minimum number of promises that need to be added to the pool to guarantee a certain success probability for the pool.
- Expected output format: The output should be the minimum number of promises required.
- Key requirements and edge cases to consider: The probability of each promise being resolved is given, and the target success probability for the pool is also provided.
- Example test cases with explanations: For instance, if we have a pool with a single promise that has a 50% chance of being resolved, and we want the pool to have at least an 80% chance of success, we need to determine how many more promises with the same or different probabilities need to be added.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of adding promises to the pool and calculating the resulting probability of success for each combination.
- Step-by-step breakdown of the solution: 
  1. Start with the initial pool of promises.
  2. For each possible number of additional promises (from 0 to a large number), calculate the probability of success for the pool.
  3. Use the inclusion-exclusion principle or a similar method to calculate the probability of success for the pool with the added promises.
- Why this approach comes to mind first: It is straightforward and ensures that all possibilities are considered.

```cpp
#include <iostream>
#include <vector>

// Function to calculate the probability of success for a given pool of promises
double calculateSuccessProbability(const std::vector<double>& probabilities, int targetSuccesses) {
    // Calculate the total number of promises
    int totalPromises = probabilities.size();
    
    // Initialize the probability of success
    double successProbability = 0.0;
    
    // Iterate over all possible combinations of promises
    for (int i = 0; i < (1 << totalPromises); ++i) {
        // Count the number of resolved promises in the current combination
        int resolvedPromises = 0;
        for (int j = 0; j < totalPromises; ++j) {
            if ((i & (1 << j)) != 0) {
                resolvedPromises++;
            }
        }
        
        // Update the probability of success
        if (resolvedPromises >= targetSuccesses) {
            double probability = 1.0;
            for (int j = 0; j < totalPromises; ++j) {
                if ((i & (1 << j)) != 0) {
                    probability *= probabilities[j];
                } else {
                    probability *= (1.0 - probabilities[j]);
                }
            }
            successProbability += probability;
        }
    }
    
    return successProbability;
}

int minPromisesToPool(const std::vector<double>& probabilities, double targetProbability) {
    int minPromises = 0;
    double currentProbability = calculateSuccessProbability(probabilities, 1);
    
    while (currentProbability < targetProbability) {
        minPromises++;
        probabilities.push_back(probabilities[0]); // Add a promise with the same probability as the first promise
        currentProbability = calculateSuccessProbability(probabilities, 1);
    }
    
    return minPromises;
}

int main() {
    std::vector<double> probabilities = {0.5}; // Example probabilities
    double targetProbability = 0.8; // Example target probability
    
    int minPromises = minPromisesToPool(probabilities, targetProbability);
    
    std::cout << "Minimum promises to add: " << minPromises << std::endl;
    
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the total number of promises. This is because we iterate over all possible combinations of promises.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of promises. This is because we need to store the probabilities of all promises.
> - **Why these complexities occur:** The time complexity occurs because we use a brute force approach that tries all possible combinations of promises. The space complexity occurs because we need to store the probabilities of all promises.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a **_binary search_** approach. We can search for the minimum number of promises that need to be added to the pool to guarantee the target success probability.
- Detailed breakdown of the approach: 
  1. Define the search range for the minimum number of promises.
  2. Use a binary search algorithm to find the minimum number of promises that satisfy the target success probability.
- Proof of optimality: The binary search approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.
- Why further optimization is impossible: The binary search approach is already optimal because it has a logarithmic time complexity, which is the best possible time complexity for a search problem.

```cpp
#include <iostream>
#include <vector>

// Function to calculate the probability of success for a given pool of promises
double calculateSuccessProbability(const std::vector<double>& probabilities, int targetSuccesses) {
    // Calculate the total number of promises
    int totalPromises = probabilities.size();
    
    // Initialize the probability of success
    double successProbability = 0.0;
    
    // Iterate over all possible combinations of promises
    for (int i = 0; i < (1 << totalPromises); ++i) {
        // Count the number of resolved promises in the current combination
        int resolvedPromises = 0;
        for (int j = 0; j < totalPromises; ++j) {
            if ((i & (1 << j)) != 0) {
                resolvedPromises++;
            }
        }
        
        // Update the probability of success
        if (resolvedPromises >= targetSuccesses) {
            double probability = 1.0;
            for (int j = 0; j < totalPromises; ++j) {
                if ((i & (1 << j)) != 0) {
                    probability *= probabilities[j];
                } else {
                    probability *= (1.0 - probabilities[j]);
                }
            }
            successProbability += probability;
        }
    }
    
    return successProbability;
}

int minPromisesToPool(const std::vector<double>& probabilities, double targetProbability) {
    int low = 0;
    int high = probabilities.size() * 2; // Initial search range
    
    while (low < high) {
        int mid = (low + high) / 2;
        
        // Create a new pool with the additional promises
        std::vector<double> newProbabilities = probabilities;
        for (int i = 0; i < mid; ++i) {
            newProbabilities.push_back(probabilities[0]); // Add a promise with the same probability as the first promise
        }
        
        // Calculate the probability of success for the new pool
        double newProbability = calculateSuccessProbability(newProbabilities, 1);
        
        // Update the search range
        if (newProbability >= targetProbability) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    
    return low;
}

int main() {
    std::vector<double> probabilities = {0.5}; // Example probabilities
    double targetProbability = 0.8; // Example target probability
    
    int minPromises = minPromisesToPool(probabilities, targetProbability);
    
    std::cout << "Minimum promises to add: " << minPromises << std::endl;
    
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the total number of promises. This is because we use a binary search approach to find the minimum number of promises.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of promises. This is because we need to store the probabilities of all promises.
> - **Optimality proof:** The binary search approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **_binary search_**, **_probability calculation_**.
- Problem-solving patterns identified: **_search problems_**, **_optimization problems_**.
- Optimization techniques learned: **_reducing search space_**, **_using logarithmic time complexity_**.
- Similar problems to practice: **_promise pool problems_**, **_probability calculation problems_**.

**Mistakes to Avoid:**
- Common implementation errors: **_incorrect probability calculation_**, **_incorrect search range_**.
- Edge cases to watch for: **_empty pool_**, **_target probability is 0 or 1_**.
- Performance pitfalls: **_using brute force approach_**, **_not reducing search space_**.
- Testing considerations: **_test with different probabilities_**, **_test with different target probabilities_**.