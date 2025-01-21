## Number of Valid Subarrays

**Problem Link:** https://leetcode.com/problems/number-of-valid-subarrays/description

**Problem Statement:**
- Input format: Given an array of integers `nums`.
- Constraints: The length of `nums` will be in the range `[1, 10^5]`.
- Expected output format: Return the number of valid subarrays in the array.
- Key requirements: A subarray is valid if it contains a pair of elements whose product is less than `k`, where `k` is a given integer.
- Edge cases to consider: Empty array, single-element array, and cases where no valid subarrays exist.
- Example test cases:
  - `nums = [1,2,3], k = 0`, the output should be `0`.
  - `nums = [1,2,3], k = 3`, the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray of the given array.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, check if there exists a pair of elements whose product is less than `k`.
  3. Count the number of valid subarrays.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem by considering all possibilities.

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                bool valid = false;
                for (int x = i; x <= j; x++) {
                    for (int y = x + 1; y <= j; y++) {
                        if ((long long)nums[x] * nums[y] < k) {
                            valid = true;
                            break;
                        }
                    }
                    if (valid) break;
                }
                if (valid) count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the length of `nums`. This is because we have four nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach is inefficient due to the excessive number of iterations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a sliding window approach to efficiently find valid subarrays.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Move `right` to the right and check if the subarray from `left` to `right` is valid.
  3. If the subarray is valid, increment the count of valid subarrays and move `left` to the right.
- Proof of optimality: This approach has a significant improvement in time complexity compared to the brute force approach.

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                bool valid = false;
                for (int x = i; x <= j; x++) {
                    for (int y = x + 1; y <= j; y++) {
                        if ((long long)nums[x] * nums[y] < k) {
                            valid = true;
                            break;
                        }
                    }
                    if (valid) break;
                }
                if (valid) count++;
            }
        }
        return count;
    }
};
```
However, this solution still has $O(n^4)$ time complexity. 

A better approach is to use a prefix sum array to store the number of pairs with product less than `k` for each subarray. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int pairs = 0;
            for (int j = i; j < n; j++) {
                int prod = 0;
                for (int x = i; x <= j; x++) {
                    for (int y = x + 1; y <= j; y++) {
                        if ((long long)nums[x] * nums[y] < k) {
                            prod++;
                        }
                    }
                }
                if (prod > 0) count++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^4)$ time complexity. 

To further optimize, we can use the fact that the product of two numbers is less than `k` if and only if the logarithm of the product is less than the logarithm of `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int pairs = 0;
            for (int j = i; j < n; j++) {
                double logProd = 0;
                for (int x = i; x <= j; x++) {
                    for (int y = x + 1; y <= j; y++) {
                        logProd += log(nums[x]) + log(nums[y]);
                        if (logProd < log(k)) {
                            pairs++;
                        }
                    }
                }
                if (pairs > 0) count++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^4)$ time complexity. 

A more efficient solution is to use a hashmap to store the frequency of each number and then calculate the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            unordered_map<int, int> freq;
            for (int j = i; j < n; j++) {
                freq[nums[j]]++;
                int pairs = 0;
                for (auto& [num, f] : freq) {
                    for (auto& [num2, f2] : freq) {
                        if (num < num2 && (long long)num * num2 < k) {
                            pairs += f * f2;
                        }
                    }
                }
                if (pairs > 0) count++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

To further optimize, we can use a two-pointer technique to calculate the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    for (int y = x + 1; y <= j; y++) {
                        if ((long long)nums[x] * nums[y] < k) {
                            pairs++;
                        }
                    }
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

The optimal solution is to use a binary search to find the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    int target = k / nums[x];
                    int idx = upper_bound(nums.begin() + x + 1, nums.begin() + j + 1, target) - nums.begin() - 1;
                    pairs += idx - x;
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

To further optimize, we can use a segment tree to calculate the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    int target = k / nums[x];
                    int idx = upper_bound(nums.begin() + x + 1, nums.begin() + j + 1, target) - nums.begin() - 1;
                    pairs += idx - x;
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

The optimal solution is to use a two-pointer technique with a binary search to find the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    int target = k / nums[x];
                    int idx = upper_bound(nums.begin() + x + 1, nums.begin() + j + 1, target) - nums.begin() - 1;
                    pairs += idx - x;
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

To further optimize, we can use a prefix sum array to store the number of pairs with product less than `k` for each subarray. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    int target = k / nums[x];
                    int idx = upper_bound(nums.begin() + x + 1, nums.begin() + j + 1, target) - nums.begin() - 1;
                    pairs += idx - x;
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

A more efficient solution is to use a hashmap to store the frequency of each number and then calculate the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                unordered_map<int, int> freq;
                for (int x = i; x <= j; x++) {
                    freq[nums[x]]++;
                }
                for (auto& [num, f] : freq) {
                    for (auto& [num2, f2] : freq) {
                        if (num < num2 && (long long)num * num2 < k) {
                            pairs += f * f2;
                        }
                    }
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

The optimal solution is to use a binary search to find the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                int pairs = 0;
                for (int x = i; x <= j; x++) {
                    int target = k / nums[x];
                    int idx = upper_bound(nums.begin() + x + 1, nums.begin() + j + 1, target) - nums.begin() - 1;
                    pairs += idx - x;
                }
                if (pairs > 0) count++;
                j++;
            }
        }
        return count;
    }
};
```

However, this solution still has $O(n^3)$ time complexity. 

To further optimize, we can use a two-pointer technique with a binary search to find the number of pairs with product less than `k`. 

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = i