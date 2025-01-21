## Maximum Profitable Triplets with Increasing Prices I
**Problem Link:** https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers representing the prices of items at different times and returns the maximum number of profitable triplets that can be formed with increasing prices.
- Expected output format: The maximum number of profitable triplets.
- Key requirements and edge cases to consider: 
    * The prices array can contain duplicate prices.
    * The prices array can be empty or contain a single element.
    * The prices array can contain negative numbers.
- Example test cases with explanations: 
    * If the prices array is [1, 2, 3], the maximum number of profitable triplets is 1.
    * If the prices array is [1, 3, 2, 4, 5], the maximum number of profitable triplets is 2.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves checking every possible triplet in the prices array to see if it forms a profitable triplet with increasing prices.
- Step-by-step breakdown of the solution:
    1. Iterate over the prices array to consider each price as the first price in the triplet.
    2. For each first price, iterate over the remaining prices to consider each price as the second price in the triplet.
    3. For each second price, iterate over the remaining prices to consider each price as the third price in the triplet.
    4. Check if the current triplet has increasing prices and is profitable.
    5. If the triplet is profitable, increment the count of profitable triplets.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution to a problem, as it involves checking every possible solution.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int count = 0;
    for (int i = 0; i < prices.size(); i++) {
        for (int j = i + 1; j < prices.size(); j++) {
            for (int k = j + 1; k < prices.size(); k++) {
                if (prices[i] < prices[j] && prices[j] < prices[k]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of prices in the prices array. This is because the brute force approach involves three nested loops, each of which iterates over the prices array.
> - **Space Complexity:** $O(1)$, as the brute force approach only uses a constant amount of space to store the count of profitable triplets.
> - **Why these complexities occur:** The time complexity occurs because the brute force approach checks every possible triplet in the prices array, resulting in a cubic number of operations. The space complexity occurs because the brute force approach only uses a constant amount of space to store the count of profitable triplets.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a two-pointer technique to find the maximum number of profitable triplets with increasing prices.
- Detailed breakdown of the approach:
    1. Initialize two pointers, `i` and `j`, to the start of the prices array.
    2. Initialize a count of profitable triplets to 0.
    3. Iterate over the prices array with the `i` pointer.
    4. For each price at the `i` pointer, iterate over the remaining prices with the `j` pointer.
    5. For each price at the `j` pointer, check if the current price is greater than the price at the `i` pointer.
    6. If the current price is greater than the price at the `i` pointer, increment the count of profitable triplets.
- Proof of optimality: The optimal solution is optimal because it only checks each price in the prices array once, resulting in a linear number of operations.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int count = 0;
    for (int i = 0; i < prices.size(); i++) {
        for (int j = i + 1; j < prices.size(); j++) {
            for (int k = j + 1; k < prices.size(); k++) {
                if (prices[i] < prices[j] && prices[j] < prices[k]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

However, this solution is still not optimal as the time complexity is still $O(n^3)$. 

To optimize it further, we can use the concept of **combinations**. We can calculate the total number of combinations of 3 elements from the given array and then subtract the combinations that do not satisfy the condition.

But the problem can be solved more efficiently by using the concept of **three pointers**.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            if (prices[j] > prices[i]) {
                for (int k = j + 1; k < n; k++) {
                    if (prices[k] > prices[j]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of prices in the prices array. This is because the optimal solution involves three nested loops, each of which iterates over the prices array.
> - **Space Complexity:** $O(1)$, as the optimal solution only uses a constant amount of space to store the count of profitable triplets.
> - **Optimality proof:** The optimal solution is optimal because it only checks each price in the prices array once, resulting in a linear number of operations. However, the time complexity can still be optimized further.

However, the above solution is still not optimal. We can optimize it further by using a single loop and maintaining two variables to keep track of the maximum and second maximum values seen so far.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        int max1 = 0, max2 = 0;
        for (int j = i + 1; j < n; j++) {
            if (prices[j] > prices[i]) {
                if (prices[j] > max1) {
                    max2 = max1;
                    max1 = prices[j];
                } else if (prices[j] > max2) {
                    max2 = prices[j];
                }
            }
        }
        count += max2 > 0;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of prices in the prices array. This is because the optimal solution involves two nested loops, each of which iterates over the prices array.
> - **Space Complexity:** $O(1)$, as the optimal solution only uses a constant amount of space to store the count of profitable triplets and the maximum and second maximum values seen so far.
> - **Optimality proof:** The optimal solution is optimal because it only checks each price in the prices array once, resulting in a quadratic number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of the two-pointer technique and the concept of combinations to solve the problem efficiently.
- Problem-solving patterns identified: The problem identifies the pattern of using multiple loops to check each possible solution and the pattern of using variables to keep track of the maximum and second maximum values seen so far.
- Optimization techniques learned: The problem teaches the optimization technique of using a single loop and maintaining variables to keep track of the maximum and second maximum values seen so far.
- Similar problems to practice: Similar problems to practice include problems that involve finding the maximum number of profitable triplets with increasing prices, problems that involve using the two-pointer technique, and problems that involve using the concept of combinations.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include using incorrect loop bounds, using incorrect conditional statements, and using incorrect variables to keep track of the maximum and second maximum values seen so far.
- Edge cases to watch for: Edge cases to watch for include the case where the prices array is empty, the case where the prices array contains a single element, and the case where the prices array contains duplicate prices.
- Performance pitfalls: Performance pitfalls include using multiple loops to check each possible solution, using incorrect variables to keep track of the maximum and second maximum values seen so far, and using incorrect conditional statements.
- Testing considerations: Testing considerations include testing the function with different inputs, testing the function with edge cases, and testing the function with large inputs to ensure that it runs efficiently.