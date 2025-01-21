## Product of the Last K Numbers
**Problem Link:** https://leetcode.com/problems/product-of-the-last-k-numbers/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 40000`, `1 <= nums[i] <= 2^31 - 1`.
- Expected output format: The product of the last `k` numbers.
- Key requirements and edge cases to consider: Handle cases where `k` is greater than the number of elements in `nums`, and cases where `nums` contains zeros.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4], k = 2`, output should be `12`.
  - `nums = [5, 10, 15], k = 1`, output should be `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the product of the last `k` numbers by iterating over the array and multiplying the last `k` elements.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `product` to `1`.
  2. Iterate over the last `k` elements of the array.
  3. Multiply each element with the `product`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class ProductOfNumbers {
public:
    vector<int> nums;
    ProductOfNumbers() {
        nums = vector<int>();
    }
    
    void add(int num) {
        nums.push_back(num);
    }
    
    int getProduct(int k) {
        long long product = 1;
        for (int i = nums.size() - k; i < nums.size(); i++) {
            product *= nums[i];
        }
        return product;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of elements to consider for the product. This is because we are iterating over the last `k` elements of the array.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are storing all the elements in the array.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the last `k` elements of the array, and the space complexity occurs because we are storing all the elements in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the product of the last `k` numbers every time, we can store the prefix products of the array.
- Detailed breakdown of the approach:
  1. Initialize an array `prefix` to store the prefix products of the array.
  2. When adding a new number, update the `prefix` array by multiplying the new number with the last element of the `prefix` array.
  3. When getting the product of the last `k` numbers, divide the last element of the `prefix` array by the element at index `n - k - 1`, where `n` is the number of elements in the array.
- Proof of optimality: This approach has a time complexity of $O(1)$ for getting the product of the last `k` numbers, which is optimal.
- Why further optimization is impossible: We need to store the prefix products of the array to get the product of the last `k` numbers in $O(1)$ time, and storing the prefix products requires $O(n)$ space.

```cpp
class ProductOfNumbers {
public:
    vector<int> prefix;
    ProductOfNumbers() {
        prefix = vector<int>();
    }
    
    void add(int num) {
        if (prefix.empty()) {
            prefix.push_back(num);
        } else {
            if (num == 0) {
                prefix = vector<int>();
            } else {
                prefix.push_back(prefix.back() * num);
            }
        }
    }
    
    int getProduct(int k) {
        if (k > prefix.size()) {
            return 0;
        }
        if (k == prefix.size()) {
            return prefix.back();
        }
        return prefix.back() / prefix[prefix.size() - k - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $k$ is the number of elements to consider for the product. This is because we are storing the prefix products of the array and can get the product of the last `k` numbers in constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are storing the prefix products of the array.
> - **Optimality proof:** The time complexity is optimal because we can get the product of the last `k` numbers in constant time, and the space complexity is necessary to store the prefix products of the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix products, dynamic programming.
- Problem-solving patterns identified: Using prefix products to solve problems involving products of arrays.
- Optimization techniques learned: Storing prefix products to reduce time complexity.
- Similar problems to practice: Problems involving products of arrays, such as finding the maximum product of a subarray.

**Mistakes to Avoid:**
- Common implementation errors: Not handling cases where `k` is greater than the number of elements in the array, not handling cases where the array contains zeros.
- Edge cases to watch for: Cases where `k` is greater than the number of elements in the array, cases where the array contains zeros.
- Performance pitfalls: Not using prefix products to reduce time complexity.
- Testing considerations: Test cases where `k` is greater than the number of elements in the array, test cases where the array contains zeros.