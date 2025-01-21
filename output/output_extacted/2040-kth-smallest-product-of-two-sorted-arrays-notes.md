## Kth Smallest Product of Two Sorted Arrays

**Problem Link:** https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description

**Problem Statement:**
- Given two sorted arrays `nums1` and `nums2`, find the kth smallest product of all possible products of two numbers from `nums1` and `nums2`.
- The input arrays are non-empty, and each array contains at most 10^5 elements.
- The elements of the arrays are integers in the range [-10^5, 10^5].
- The value of k is in the range [1, 10^5].

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible products of two numbers from `nums1` and `nums2`, store them in a new array, and then find the kth smallest element in the new array.
- This approach comes to mind first because it directly addresses the problem statement without considering any optimizations.

```cpp
class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        vector<long long> products;
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                products.push_back((long long)nums1[i] * nums2[j]);
            }
        }
        sort(products.begin(), products.end());
        return products[k - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n \cdot m))$, where n and m are the sizes of `nums1` and `nums2`, respectively. This is because we are generating all possible products and then sorting them.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store all the products in a new array.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a time complexity of $O(n \cdot m \cdot log(n \cdot m))$. The space complexity is due to the need to store all the products.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a binary search approach to find the kth smallest product.
- We can use a binary search range from the smallest possible product to the largest possible product.
- For each mid value in the binary search range, we can count the number of products that are less than or equal to mid.
- If the count is greater than or equal to k, we can update the upper bound of the binary search range to mid.
- Otherwise, we can update the lower bound of the binary search range to mid + 1.

```cpp
class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        long long left = (long long)INT_MIN * INT_MIN;
        long long right = (long long)INT_MAX * INT_MAX;
        
        while (left < right) {
            long long mid = left + (right - left) / 2;
            long long count = 0;
            int j = nums2.size() - 1;
            
            for (int i = 0; i < nums1.size(); i++) {
                while (j >= 0 && (long long)nums1[i] * nums2[j] > mid) {
                    j--;
                }
                count += (j + 1);
            }
            
            if (count >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(max\_val))$, where n is the size of `nums1` and max\_val is the maximum possible product.
> - **Space Complexity:** $O(1)$, as we only need a constant amount of space to store the binary search range and the count of products.
> - **Optimality proof:** This approach is optimal because it uses a binary search approach to find the kth smallest product, which reduces the time complexity from $O(n \cdot m \cdot log(n \cdot m))$ to $O(n \cdot log(max\_val))$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of binary search to find the kth smallest product.
- The problem-solving pattern identified is the use of a binary search range to narrow down the possible solutions.
- The optimization technique learned is the use of a count variable to reduce the number of iterations.
- Similar problems to practice include finding the kth smallest element in a sorted array and finding the kth smallest product of three sorted arrays.

**Mistakes to Avoid:**
- A common implementation error is to use a naive approach that generates all possible products and then sorts them.
- An edge case to watch for is when the input arrays are empty or contain only one element.
- A performance pitfall is to use a brute force approach that has a high time complexity.
- A testing consideration is to test the solution with different input sizes and values to ensure that it works correctly.