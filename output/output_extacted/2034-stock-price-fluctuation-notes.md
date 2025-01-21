## Stock Price Fluctuation
**Problem Link:** https://leetcode.com/problems/stock-price-fluctuation/description

**Problem Statement:**
- Input format and constraints: Given a list of `timestamp` and `price` pairs representing the stock price at different times, the goal is to create a data structure that can efficiently handle the following operations:
  - `StockPriceFluctuation()`: Initialize the data structure.
  - `void update(int timestamp, int price)`: Update the stock price at a given `timestamp`.
  - `int current()`: Return the current stock price.
  - `int maximum()`: Return the maximum stock price so far.
  - `int minimum()`: Return the minimum stock price so far.
- Expected output format: The output should be the result of the respective operations.
- Key requirements and edge cases to consider: 
  - Handle duplicate `timestamp` values by updating the price for that `timestamp`.
  - Ensure efficient retrieval of current, maximum, and minimum prices.
- Example test cases with explanations:
  - `StockPriceFluctuation stock; stock.update(1, 10); stock.update(2, 20); stock.current();` should return `20`.
  - `StockPriceFluctuation stock; stock.update(1, 10); stock.update(2, 20); stock.maximum();` should return `20`.
  - `StockPriceFluctuation stock; stock.update(1, 10); stock.update(2, 20); stock.minimum();` should return `10`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use a simple list or array to store the `timestamp` and `price` pairs, and then iterate through the list to find the current, maximum, and minimum prices.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store `timestamp` and `price` pairs.
  2. For the `update` operation, append the new `timestamp` and `price` pair to the list.
  3. For the `current` operation, return the `price` of the last `timestamp` pair in the list.
  4. For the `maximum` and `minimum` operations, iterate through the list to find the maximum and minimum prices.
- Why this approach comes to mind first: It is the most straightforward way to store and retrieve data, but it is inefficient for large datasets.

```cpp
class StockPriceFluctuation {
public:
    vector<pair<int, int>> prices;
    int currentTimestamp = 0;

    StockPriceFluctuation() {}

    void update(int timestamp, int price) {
        bool found = false;
        for (auto& p : prices) {
            if (p.first == timestamp) {
                p.second = price;
                found = true;
                break;
            }
        }
        if (!found) {
            prices.push_back({timestamp, price});
        }
        currentTimestamp = max(currentTimestamp, timestamp);
    }

    int current() {
        for (auto& p : prices) {
            if (p.first == currentTimestamp) {
                return p.second;
            }
        }
        return -1; // Handle the case where no price is found
    }

    int maximum() {
        int maxPrice = INT_MIN;
        for (auto& p : prices) {
            maxPrice = max(maxPrice, p.second);
        }
        return maxPrice;
    }

    int minimum() {
        int minPrice = INT_MAX;
        for (auto& p : prices) {
            minPrice = min(minPrice, p.second);
        }
        return minPrice;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `update`, `current`, `maximum`, and `minimum` operations, where $n$ is the number of `timestamp` and `price` pairs.
> - **Space Complexity:** $O(n)$ for storing the `timestamp` and `price` pairs.
> - **Why these complexities occur:** The brute force approach involves iterating through the list of `timestamp` and `price` pairs for each operation, resulting in linear time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a combination of a `map` to store `timestamp` and `price` pairs, and two `multiset`s to keep track of the maximum and minimum prices.
- Detailed breakdown of the approach:
  1. Initialize an empty `map` to store `timestamp` and `price` pairs, and two empty `multiset`s to store prices.
  2. For the `update` operation, update the `price` in the `map` and insert or erase prices from the `multiset`s as necessary.
  3. For the `current` operation, return the `price` of the maximum `timestamp` in the `map`.
  4. For the `maximum` and `minimum` operations, return the maximum and minimum prices from the `multiset`s.
- Proof of optimality: This approach ensures efficient retrieval of current, maximum, and minimum prices, with an average time complexity of $O(log n)$ for `update`, `current`, `maximum`, and `minimum` operations.

```cpp
class StockPriceFluctuation {
public:
    map<int, int> prices;
    multiset<int> maxPrices;
    multiset<int> minPrices;
    int currentTimestamp = 0;

    StockPriceFluctuation() {}

    void update(int timestamp, int price) {
        if (prices.find(timestamp) != prices.end()) {
            maxPrices.erase(maxPrices.find(prices[timestamp]));
            minPrices.erase(minPrices.find(prices[timestamp]));
        }
        prices[timestamp] = price;
        maxPrices.insert(price);
        minPrices.insert(price);
        currentTimestamp = max(currentTimestamp, timestamp);
    }

    int current() {
        return prices[currentTimestamp];
    }

    int maximum() {
        return *maxPrices.rbegin();
    }

    int minimum() {
        return *minPrices.begin();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$ for `update`, `current`, `maximum`, and `minimum` operations, where $n$ is the number of `timestamp` and `price` pairs.
> - **Space Complexity:** $O(n)$ for storing the `timestamp` and `price` pairs, and the prices in the `multiset`s.
> - **Optimality proof:** The optimal approach ensures efficient retrieval of current, maximum, and minimum prices, with an average time complexity of $O(log n)$, making it the best possible solution for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `map` and `multiset` data structures to optimize the solution.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using efficient data structures to solve them.
- Optimization techniques learned: Using `multiset`s to keep track of maximum and minimum prices, and updating the `map` and `multiset`s efficiently.
- Similar problems to practice: Problems involving efficient retrieval of maximum and minimum values, such as finding the maximum and minimum values in a sliding window.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle duplicate `timestamp` values, and not updating the `multiset`s correctly.
- Edge cases to watch for: Handling the case where no price is found, and ensuring that the `multiset`s are updated correctly.
- Performance pitfalls: Using inefficient data structures, such as iterating through a list to find the maximum and minimum prices.
- Testing considerations: Testing the solution with different input scenarios, including duplicate `timestamp` values and edge cases.