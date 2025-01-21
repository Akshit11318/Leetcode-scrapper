## Final Prices with a Special Discount in a Shop

**Problem Link:** https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description

**Problem Statement:**
- Input format: an array of integers `prices` where `prices[i]` is the price of the item at index `i`.
- Constraints: `1 <= prices.length <= 500`, `1 <= prices[i] <= 10^3`.
- Expected output format: an array of integers representing the final prices after applying the special discount.
- Key requirements and edge cases to consider: 
    - If an item's price is greater than or equal to the price of the next item, apply a discount equal to the price of the next item.
    - The discount is only applied if the next item's price is less than or equal to the current item's price.
- Example test cases with explanations:
    - Input: `prices = [8, 4, 6, 2, 3]`, Output: `[4, 4, 4, 2, 3]`
    - Input: `prices = [1, 2, 3, 4, 5]`, Output: `[1, 2, 3, 4, 5]`
    - Input: `prices = [10, 1, 1, 6]`, Output: `[9, 1, 1, 6]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array and for each element, check the remaining elements to find a price that is less than or equal to the current price.
- Step-by-step breakdown of the solution:
    1. Initialize an empty array `finalPrices` to store the final prices.
    2. Iterate through the `prices` array.
    3. For each element, iterate through the remaining elements in the array.
    4. If a price is found that is less than or equal to the current price, apply the discount and break the inner loop.
    5. Add the final price (after applying the discount) to the `finalPrices` array.

```cpp
#include <vector>
using namespace std;

vector<int> finalPrices(vector<int>& prices) {
    vector<int> finalPrices;
    for (int i = 0; i < prices.size(); i++) {
        bool discountApplied = false;
        for (int j = i + 1; j < prices.size(); j++) {
            if (prices[j] <= prices[i]) {
                finalPrices.push_back(prices[i] - prices[j]);
                discountApplied = true;
                break;
            }
        }
        if (!discountApplied) {
            finalPrices.push_back(prices[i]);
        }
    }
    return finalPrices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the `prices` array. This is because we have a nested loop structure.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the `prices` array. This is because we are storing the final prices in a new array.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loop structure, which results in a lot of redundant comparisons. The space complexity is linear because we are storing the final prices in a new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a stack to keep track of the indices of the elements that have not been processed yet.
- Detailed breakdown of the approach:
    1. Initialize an empty stack `stack` to store the indices of the elements.
    2. Initialize a vector `finalPrices` to store the final prices.
    3. Iterate through the `prices` array and push the indices onto the stack.
    4. For each element, check if the stack is not empty and the top element of the stack is greater than or equal to the current element.
    5. If the condition is met, pop the top element from the stack and apply the discount.
    6. Repeat steps 4-5 until the stack is empty or the top element is less than the current element.
    7. Add the final price (after applying the discount) to the `finalPrices` array.

```cpp
#include <vector>
#include <stack>
using namespace std;

vector<int> finalPrices(vector<int>& prices) {
    vector<int> finalPrices(prices.size());
    stack<int> stack;
    for (int i = 0; i < prices.size(); i++) {
        while (!stack.empty() && prices[stack.top()] >= prices[i]) {
            finalPrices[stack.top()] = prices[stack.top()] - prices[i];
            stack.pop();
        }
        stack.push(i);
    }
    for (int i = 0; i < prices.size(); i++) {
        if (finalPrices[i] == 0) {
            finalPrices[i] = prices[i];
        }
    }
    return finalPrices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the `prices` array. This is because each element is pushed and popped from the stack exactly once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the `prices` array. This is because we are using a stack to store the indices of the elements.
> - **Optimality proof:** The optimal approach has a linear time complexity because we are using a stack to keep track of the indices of the elements, which allows us to avoid redundant comparisons. The space complexity is also linear because we are storing the final prices in a new array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: stack data structure, iteration, and conditional statements.
- Problem-solving patterns identified: using a stack to keep track of indices, applying discounts based on conditions.
- Optimization techniques learned: avoiding redundant comparisons by using a stack.
- Similar problems to practice: problems involving stacks, iteration, and conditional statements.

**Mistakes to Avoid:**
- Common implementation errors: incorrect use of stack operations, incorrect application of discounts.
- Edge cases to watch for: empty input array, array with single element.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: test cases with different input sizes, test cases with edge cases.