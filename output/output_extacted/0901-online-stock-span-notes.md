## Online Stock Span
**Problem Link:** [https://leetcode.com/problems/online-stock-span/description](https://leetcode.com/problems/online-stock-span/description)

**Problem Statement:**
- Input format and constraints: The problem involves designing a class `StockSpanner` that has a method `next` which takes an integer `price` as input and returns the number of consecutive days (including the current day) where the stock price was less than or equal to the current day's price.
- Expected output format: The output should be an integer representing the number of consecutive days.
- Key requirements and edge cases to consider: The class should handle multiple calls to the `next` method, and each call should return the correct number of consecutive days based on the current and previous stock prices.
- Example test cases with explanations:
  - Example 1: `StockSpanner stockSpanner; stockSpanner.next(100); stockSpanner.next(80); stockSpanner.next(60); stockSpanner.next(70); stockSpanner.next(60);` should return `[1, 1, 1, 2, 1]`.
  - Example 2: `StockSpanner stockSpanner; stockSpanner.next(7); stockSpanner.next(7); stockSpanner.next(7);` should return `[1, 2, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to keep track of all the previous prices and then for each new price, iterate through all the previous prices to find the number of consecutive days where the price was less than or equal to the current price.
- Step-by-step breakdown of the solution:
  1. Create a vector to store all the previous prices.
  2. When `next` method is called, iterate through the vector of previous prices to find the number of consecutive days where the price was less than or equal to the current price.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
class StockSpanner {
public:
    vector<int> prices;
    StockSpanner() {}
    
    int next(int price) {
        int count = 1;
        for (int i = prices.size() - 1; i >= 0; i--) {
            if (prices[i] <= price) {
                count++;
            } else {
                break;
            }
        }
        prices.push_back(price);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of times the `next` method is called. This is because in the worst case, we are iterating through all the previous prices for each new price.
> - **Space Complexity:** $O(n)$, where $n$ is the number of times the `next` method is called. This is because we are storing all the previous prices in a vector.
> - **Why these complexities occur:** The brute force approach involves iterating through all the previous prices for each new price, which results in a linear time complexity. The space complexity is also linear because we are storing all the previous prices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the prices and their corresponding spans. When a new price is added, we pop all the prices from the stack that are less than or equal to the new price and update the span of the new price accordingly.
- Detailed breakdown of the approach:
  1. Create a stack to store pairs of prices and their corresponding spans.
  2. When the `next` method is called, pop all the prices from the stack that are less than or equal to the new price and update the span of the new price accordingly.
  3. Push the new price and its span onto the stack.
- Proof of optimality: This approach is optimal because it only requires a single pass through the stack for each new price, resulting in a time complexity of $O(1)$ amortized.

```cpp
class StockSpanner {
public:
    stack<pair<int, int>> stack;
    StockSpanner() {}
    
    int next(int price) {
        int span = 1;
        while (!stack.empty() && stack.top().first <= price) {
            span += stack.top().second;
            stack.pop();
        }
        stack.push({price, span});
        return span;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ amortized, where $n$ is the number of times the `next` method is called. This is because we are only pushing and popping elements from the stack, and each element is pushed and popped at most once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of times the `next` method is called. This is because in the worst case, we are storing all the prices in the stack.
> - **Optimality proof:** The optimal approach has a time complexity of $O(1)$ amortized, which is the best possible time complexity for this problem. The space complexity is also optimal because we are only storing the necessary information in the stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a stack to keep track of prices and their corresponding spans.
- Problem-solving patterns identified: The use of a stack to solve problems that involve keeping track of a sequence of elements.
- Optimization techniques learned: The use of a stack to reduce the time complexity of a problem.
- Similar problems to practice: Problems that involve keeping track of a sequence of elements, such as the `Daily Temperatures` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the stack is empty before popping an element.
- Edge cases to watch for: The case where the input price is less than or equal to the price at the top of the stack.
- Performance pitfalls: Using a vector instead of a stack to store the prices and their corresponding spans.
- Testing considerations: Testing the `next` method with different input prices and verifying that the output is correct.