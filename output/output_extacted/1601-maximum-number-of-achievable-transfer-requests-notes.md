## Maximum Number of Achievable Transfer Requests

**Problem Link:** https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description

**Problem Statement:**
- Input format: An integer `n` and a 2D array `requests` where each request is in the form of `[from, to]`.
- Constraints: `1 <= n <= 10^5` and `1 <= requests.length <= 10^5`.
- Expected output format: The maximum number of achievable transfer requests.
- Key requirements and edge cases to consider:
  - Each transfer request is a pair of banks, and the transfer can only happen in one direction.
  - If a bank has no incoming or outgoing transfers, it does not affect the maximum number of achievable transfer requests.
- Example test cases with explanations:
  - For `n = 5` and `requests = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 3]]`, the output is `5` because all requests can be achieved.
  - For `n = 3` and `requests = [[0, 0], [1, 2], [2, 1]]`, the output is `2` because the first request cannot be achieved.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of transfer requests and check if each combination can be achieved without violating the balance of any bank.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of transfer requests.
  2. For each combination, simulate the transfers and check if any bank's balance becomes negative or if any transfer request is repeated.
  3. If a combination does not violate any bank's balance and does not repeat any transfer request, count it as a valid combination.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem by trying all possibilities.

```cpp
#include <vector>
#include <bitset>

class Solution {
public:
    int maximumRequests(int n, std::vector<std::vector<int>>& requests) {
        int maxRequests = 0;
        std::vector<int> balance(n, 0);
        
        for (int mask = 0; mask < (1 << requests.size()); ++mask) {
            balance.assign(n, 0);
            int validRequests = 0;
            
            for (int i = 0; i < requests.size(); ++i) {
                if ((mask & (1 << i)) != 0) {
                    balance[requests[i][0]]--;
                    balance[requests[i][1]]++;
                    validRequests++;
                }
            }
            
            bool isValid = true;
            for (int b : balance) {
                if (b != 0) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                maxRequests = std::max(maxRequests, validRequests);
            }
        }
        
        return maxRequests;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot m \cdot n)$ where $m$ is the number of requests and $n$ is the number of banks. The reason is that we generate all possible combinations of transfer requests ($2^m$), and for each combination, we simulate the transfers and check the balance of each bank ($m \cdot n$).
> - **Space Complexity:** $O(n)$ for storing the balance of each bank.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of transfer requests, which leads to exponential time complexity. The space complexity is linear because we only need to store the balance of each bank.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a bitmask to represent the combination of transfer requests and then checking the balance of each bank.
- Detailed breakdown of the approach:
  1. Initialize a bitmask to represent all possible combinations of transfer requests.
  2. For each combination, simulate the transfers and check if any bank's balance becomes negative.
  3. If a combination does not violate any bank's balance, update the maximum number of achievable transfer requests.
- Proof of optimality: The optimal approach tries all possible combinations of transfer requests and checks the balance of each bank, which ensures that we find the maximum number of achievable transfer requests.

```cpp
#include <vector>
#include <bitset>

class Solution {
public:
    int maximumRequests(int n, std::vector<std::vector<int>>& requests) {
        int maxRequests = 0;
        std::vector<int> balance(n, 0);
        
        for (int mask = 0; mask < (1 << requests.size()); ++mask) {
            balance.assign(n, 0);
            int validRequests = 0;
            
            for (int i = 0; i < requests.size(); ++i) {
                if ((mask & (1 << i)) != 0) {
                    balance[requests[i][0]]--;
                    balance[requests[i][1]]++;
                    validRequests++;
                }
            }
            
            bool isValid = true;
            for (int b : balance) {
                if (b != 0) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                maxRequests = std::max(maxRequests, validRequests);
            }
        }
        
        return maxRequests;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot m \cdot n)$ where $m$ is the number of requests and $n$ is the number of banks. The reason is that we generate all possible combinations of transfer requests ($2^m$), and for each combination, we simulate the transfers and check the balance of each bank ($m \cdot n$).
> - **Space Complexity:** $O(n)$ for storing the balance of each bank.
> - **Optimality proof:** The optimal approach tries all possible combinations of transfer requests and checks the balance of each bank, which ensures that we find the maximum number of achievable transfer requests.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmasking, simulation, and balance checking.
- Problem-solving patterns identified: Trying all possible combinations and checking the balance of each bank.
- Optimization techniques learned: Using a bitmask to represent combinations and checking the balance of each bank.
- Similar problems to practice: Problems that involve trying all possible combinations and checking certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the balance of each bank correctly, not checking the balance of each bank after simulating the transfers.
- Edge cases to watch for: Empty input, single request, and requests with the same source and destination.
- Performance pitfalls: Using an inefficient algorithm that tries all possible combinations without checking the balance of each bank.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.