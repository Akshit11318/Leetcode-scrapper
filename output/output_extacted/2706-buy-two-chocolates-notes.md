## Buy Two Chocolates

**Problem Link:** https://leetcode.com/problems/buy-two-chocolates/description

**Problem Statement:**
- Input format and constraints: The problem asks for the minimum cost to buy two chocolates from a list of prices where each price is a positive integer.
- Expected output format: The minimum cost.
- Key requirements and edge cases to consider: The list must contain at least two prices, and the prices are distinct.
- Example test cases with explanations:
  - Example 1: Input: `prices = [1,2,3,4,5]`, Output: `3`, Explanation: Buy chocolates with prices 1 and 2.
  - Example 2: Input: `prices = [10,20,30,40,50]`, Output: `30`, Explanation: Buy chocolates with prices 10 and 20.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the list of prices and then select the first two prices to get the minimum cost.
- Step-by-step breakdown of the solution: 
  1. Sort the list of prices in ascending order.
  2. Select the first two prices from the sorted list.
  3. Calculate the minimum cost by adding the two selected prices.
- Why this approach comes to mind first: The simplest way to find the minimum cost is to sort the prices and pick the two smallest ones.

```cpp
#include <algorithm>
#include <vector>

int minCost(std::vector<int>& prices) {
    // Input validation
    if (prices.size() < 2) {
        throw std::invalid_argument("The list must contain at least two prices.");
    }

    // Sort the list of prices in ascending order
    std::sort(prices.begin(), prices.end());

    // Select the first two prices from the sorted list
    int minCost = prices[0] + prices[1];

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of prices. This is due to the sorting operation.
> - **Space Complexity:** $O(1)$, assuming the sorting algorithm used is in-place. Otherwise, it could be $O(n)$ for the auxiliary array used in sorting.
> - **Why these complexities occur:** The sorting operation dominates the time complexity. The space complexity depends on the sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since we only need the two smallest prices, we can find them in a single pass through the list without sorting.
- Detailed breakdown of the approach: 
  1. Initialize two variables to store the minimum and second minimum prices.
  2. Iterate through the list of prices to find the minimum and second minimum prices.
  3. Calculate the minimum cost by adding the minimum and second minimum prices.
- Proof of optimality: This approach has a linear time complexity, which is optimal for finding the two smallest elements in an unsorted list.
- Why further optimization is impossible: We must examine each price at least once to find the two smallest ones, so the time complexity cannot be less than linear.

```cpp
#include <vector>
#include <climits>

int minCost(std::vector<int>& prices) {
    // Input validation
    if (prices.size() < 2) {
        throw std::invalid_argument("The list must contain at least two prices.");
    }

    // Initialize variables to store the minimum and second minimum prices
    int minPrice = INT_MAX;
    int secondMinPrice = INT_MAX;

    // Iterate through the list of prices to find the minimum and second minimum prices
    for (int price : prices) {
        if (price < minPrice) {
            secondMinPrice = minPrice;
            minPrice = price;
        } else if (price < secondMinPrice) {
            secondMinPrice = price;
        }
    }

    // Calculate the minimum cost by adding the minimum and second minimum prices
    int minCost = minPrice + secondMinPrice;

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of prices. This is because we make a single pass through the list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and second minimum prices.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best we can do for finding the two smallest elements in an unsorted list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the minimum and second minimum elements in an unsorted list.
- Problem-solving patterns identified: Using a single pass through the list to find the required elements.
- Optimization techniques learned: Avoiding unnecessary sorting operations when only a subset of the sorted list is needed.
- Similar problems to practice: Finding the kth smallest element in an unsorted list, finding the maximum and second maximum elements in an unsorted list.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty list or a list with less than two elements.
- Edge cases to watch for: Lists with duplicate elements, lists with negative numbers.
- Performance pitfalls: Using sorting operations when they are not necessary.
- Testing considerations: Test the function with lists of different sizes, including edge cases.