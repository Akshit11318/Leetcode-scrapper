## Tuple with Same Product
**Problem Link:** https://leetcode.com/problems/tuple-with-same-product/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected output format: The number of tuples `(a, b, c, d)` such that `a * b = c * d` where `a`, `b`, `c`, and `d` are distinct elements in the array.
- Key requirements and edge cases to consider: Handling duplicate products, ensuring distinct elements in tuples, and optimizing for performance.
- Example test cases with explanations:
  - For `nums = [2, 3, 4, 6]`, the output should be `8` because there are `8` tuples satisfying the condition: `(2, 6, 3, 4)`, `(2, 6, 4, 3)`, `(3, 4, 2, 6)`, `(3, 4, 6, 2)`, `(4, 3, 2, 6)`, `(4, 3, 6, 2)`, `(2, 4, 3, 6)`, `(2, 4, 6, 3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible combinations of four distinct numbers in the array and check if the product of the first two numbers equals the product of the last two numbers.
- Step-by-step breakdown of the solution:
  1. Generate all possible tuples of four distinct numbers from the array.
  2. For each tuple, calculate the product of the first two numbers and the product of the last two numbers.
  3. If the two products are equal, increment the count of valid tuples.
- Why this approach comes to mind first: It directly addresses the problem statement by exhaustively checking all possible combinations.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int tupleSameProduct(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int a = 0; a < n; ++a) {
        for (int b = a + 1; b < n; ++b) {
            for (int c = 0; c < n; ++c) {
                for (int d = c + 1; d < n; ++d) {
                    if (a != c && a != d && b != c && b != d) {
                        if (nums[a] * nums[b] == nums[c] * nums[d]) {
                            count++;
                        }
                    }
                }
            }
        }
    }
    return count * 8; // Each valid tuple is counted 8 times due to permutations
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of elements in the array. This is because we have four nested loops iterating over the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The brute force approach involves checking all possible combinations of four elements, leading to a high time complexity. However, it uses minimal extra space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all tuples and checking their products, we can store the products of pairs of numbers and their counts. Then, for each pair, we can find how many other pairs have the same product.
- Detailed breakdown of the approach:
  1. Create a map to store the products of pairs and their counts.
  2. Iterate through the array to generate all pairs of numbers and calculate their products.
  3. For each product, increment its count in the map.
  4. After counting all products, iterate through the map and for each product count, calculate the number of tuples that can be formed with this product. This involves combinatorics, specifically using the formula for combinations to find how many ways we can select two pairs from the count of pairs for a given product.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to generate all possible tuples and instead focuses on the products of pairs, which is a more efficient way to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int tupleSameProduct(vector<int>& nums) {
    unordered_map<int, int> productCount;
    int n = nums.size();
    for (int a = 0; a < n; ++a) {
        for (int b = a + 1; b < n; ++b) {
            int product = nums[a] * nums[b];
            productCount[product]++;
        }
    }
    int count = 0;
    for (auto& pair : productCount) {
        int countOfProduct = pair.second;
        // Calculate the number of ways to choose two pairs from countOfProduct pairs
        // This is a combination problem, choosing 2 pairs out of countOfProduct pairs
        // The formula for combinations is nC2 = n * (n - 1) / 2
        if (countOfProduct > 1) {
            count += countOfProduct * (countOfProduct - 1) / 2 * 8;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have two nested loops iterating over the array to generate pairs and their products.
> - **Space Complexity:** $O(n^2)$, because in the worst case, we might store every pair's product in the map.
> - **Optimality proof:** This approach is optimal because it reduces the problem to counting the occurrences of each product and then calculates the combinations of these counts, which is more efficient than generating all possible tuples.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of reducing the problem space by focusing on critical characteristics (in this case, the products of pairs).
- Problem-solving patterns identified: Using maps to count occurrences and then applying combinatorial formulas to calculate the final result.
- Optimization techniques learned: Avoiding brute force by identifying a more efficient representation of the problem (products of pairs instead of tuples).
- Similar problems to practice: Other problems involving combinatorics and optimization, such as finding combinations or permutations under certain constraints.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating combinations or failing to account for all possible pairs and their products.
- Edge cases to watch for: Handling cases where the input array is small or where there are many duplicate products.
- Performance pitfalls: Failing to optimize the solution, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input sizes and scenarios to ensure correctness and performance.