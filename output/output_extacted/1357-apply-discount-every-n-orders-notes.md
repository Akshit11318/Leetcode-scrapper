## Apply Discount Every N Orders
**Problem Link:** https://leetcode.com/problems/apply-discount-every-n-orders/description

**Problem Statement:**
- Input format and constraints: The problem involves designing a system to apply discounts to every N orders. The input includes a list of orders and the frequency at which the discount should be applied (N).
- Expected output format: The output should be the final state of the system after applying the discount to the specified orders.
- Key requirements and edge cases to consider: Handling cases where the number of orders is less than N, ensuring the discount is applied correctly, and managing the order queue efficiently.
- Example test cases with explanations:
  - Test case 1: Applying a discount every 3 orders to a list of 6 orders.
  - Test case 2: Applying a discount every 5 orders to a list of 10 orders.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the list of orders and apply the discount to every Nth order.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the final state of orders.
  2. Iterate through each order in the input list.
  3. For every Nth order, apply the discount.
  4. Add the order (with discount applied if applicable) to the final list.
- Why this approach comes to mind first: It directly addresses the requirement of applying a discount to every Nth order by iterating through the list and checking each order's position.

```cpp
class Cashier {
public:
    Cashier(int n, vector<int>& products, vector<int>& discounts) {
        this->n = n;
        this->products = products;
        this->discounts = discounts;
    }

    double applyDiscount(int orderNumber) {
        if (orderNumber % n == 0) {
            // Apply discount
            double discount = discounts[orderNumber % n - 1];
            return products[orderNumber % n - 1] * (1 - discount / 100);
        } else {
            // No discount
            return products[orderNumber % n];
        }
    }

private:
    int n;
    vector<int> products;
    vector<int> discounts;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where m is the number of orders. This is because we are iterating through each order once.
> - **Space Complexity:** $O(m)$, for storing the final state of orders.
> - **Why these complexities occur:** The brute force approach involves a linear scan of the input orders, resulting in a time complexity of $O(m)$. The space complexity is also $O(m)$ because in the worst case, we might need to store all orders.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Realizing that the discount application is based solely on the order number's position in a sequence that repeats every N orders. This allows for a more direct calculation without needing to iterate through all previous orders.
- Detailed breakdown of the approach:
  1. Determine if the current order number is a multiple of N (i.e., it's an order where the discount should be applied).
  2. If it is, calculate the discount based on the order number's position within the repeating sequence.
- Proof of optimality: This approach is optimal because it minimizes the number of operations needed to determine whether a discount should be applied and calculates the discount directly without unnecessary iterations.
- Why further optimization is impossible: The approach already operates in constant time for each order, making it as efficient as possible for this problem.

```cpp
class Cashier {
public:
    Cashier(int n, vector<int>& products, vector<int>& discounts) : n(n), products(products), discounts(discounts), order(0) {}

    double applyDiscount(int product) {
        order++;
        if (order % n == 0) {
            // Apply discount
            int index = (order / n) - 1;
            if(index < discounts.size()) {
                return products[product - 1] * (1 - discounts[index] / 100);
            }
        }
        // No discount
        return products[product - 1];
    }

private:
    int n;
    vector<int> products;
    vector<int> discounts;
    int order;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are performing a constant number of operations for each order.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the necessary variables.
> - **Optimality proof:** The optimal approach achieves constant time complexity for applying discounts, making it the most efficient solution possible for this problem.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the problem's requirements and identifying patterns that can lead to more efficient solutions.
- Problem-solving patterns identified: Recognizing that the problem involves a repeating sequence and exploiting this to simplify the solution.
- Optimization techniques learned: Minimizing the number of operations and avoiding unnecessary iterations.
- Similar problems to practice: Problems involving sequences, patterns, and efficient iteration.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the order number or misapplying the discount.
- Edge cases to watch for: Handling cases where the number of orders is less than N or ensuring the discount is applied correctly at the start of each sequence.
- Performance pitfalls: Failing to recognize the repeating pattern and thus iterating unnecessarily through all orders.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.