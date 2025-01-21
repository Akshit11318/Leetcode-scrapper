## How Many Apples Can You Put into the Basket
**Problem Link:** https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of integers `arr` representing the weights of apples and an integer `k` representing the maximum capacity of the basket. 
- Expected output format: The function should return the maximum number of apples that can be put into the basket without exceeding its capacity.
- Key requirements and edge cases to consider: The function should handle cases where the input list is empty, the capacity of the basket is zero, or the weights of the apples are negative.
- Example test cases with explanations: For example, given `arr = [1, 2, 3, 4, 5]` and `k = 7`, the function should return `2` because we can put the apples with weights `1` and `2` into the basket without exceeding its capacity.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible combinations of apples and checking if their total weight exceeds the capacity of the basket.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of apples.
  2. For each combination, calculate the total weight.
  3. If the total weight does not exceed the capacity of the basket, update the maximum number of apples that can be put into the basket.
- Why this approach comes to mind first: This approach is straightforward and ensures that we consider all possible combinations of apples.

```cpp
#include <vector>
#include <algorithm>

int maxNumberOfApples(std::vector<int>& arr, int k) {
    std::sort(arr.begin(), arr.end());
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (k >= arr[i]) {
            k -= arr[i];
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of apples.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the count and the remaining capacity.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves sorting the apples by their weights and then iterating over the sorted list to add the apples to the basket until its capacity is exceeded.
- Detailed breakdown of the approach: 
  1. Sort the apples by their weights in ascending order.
  2. Initialize a variable to keep track of the remaining capacity of the basket.
  3. Iterate over the sorted list of apples and add each apple to the basket if its weight does not exceed the remaining capacity.
- Proof of optimality: This approach is optimal because it ensures that we add the maximum number of apples to the basket by always choosing the lightest apple that does not exceed the remaining capacity.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$ due to the sorting operation, which is the best we can achieve for this problem because we must consider all apples.

```cpp
#include <vector>
#include <algorithm>

int maxNumberOfApples(std::vector<int>& arr, int k) {
    std::sort(arr.begin(), arr.end());
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (k >= arr[i]) {
            k -= arr[i];
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of apples.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the count and the remaining capacity.
> - **Optimality proof:** This approach is optimal because it ensures that we add the maximum number of apples to the basket by always choosing the lightest apple that does not exceed the remaining capacity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm.
- Problem-solving patterns identified: Using a greedy approach to solve optimization problems.
- Optimization techniques learned: Sorting the input data to make it easier to solve the problem.
- Similar problems to practice: Other optimization problems that can be solved using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the input list is empty or if the capacity of the basket is zero.
- Edge cases to watch for: Handling cases where the weights of the apples are negative or where the capacity of the basket is zero.
- Performance pitfalls: Using a brute force approach that generates all possible combinations of apples, which can lead to a high time complexity.
- Testing considerations: Testing the function with different input scenarios, including edge cases and large input sizes.