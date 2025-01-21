## IP to CIDR

**Problem Link:** https://leetcode.com/problems/ip-to-cidr/description

**Problem Statement:**
- Input format: A string `ip` representing an IP address and an integer `n` representing the number of IP addresses.
- Constraints: The IP address is in the format `xxx.xxx.xxx.xxx` where `xxx` is an integer between `0` and `255`. The number of IP addresses `n` is a positive integer.
- Expected output format: A string representing the CIDR notation of the IP address range.
- Key requirements and edge cases to consider: The IP address range should include the given IP address and `n-1` subsequent IP addresses.
- Example test cases with explanations:
  - Input: `ip = "255.0.0.7", n = 10`, Output: `"255.0.0.7/32"`
  - Input: `ip = "0.0.0.0", n = 2`, Output: `"0.0.0.0/31"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem seems to require calculating the range of IP addresses and then finding the CIDR notation for that range.
- Step-by-step breakdown of the solution:
  1. Convert the IP address to an integer for easier manipulation.
  2. Calculate the range of IP addresses.
  3. Find the CIDR notation for the range by counting the number of bits required to represent the range.
- Why this approach comes to mind first: It's a straightforward way to calculate the range and then find the CIDR notation.

```cpp
class Solution {
public:
    string ipToCIDR(string ip, int n) {
        // Split the IP address into its four parts
        int parts[4];
        sscanf(ip.c_str(), "%d.%d.%d.%d", &parts[0], &parts[1], &parts[2], &parts[3]);

        // Convert the IP address to an integer
        long long ipInt = (long long)parts[0] << 24 | (long long)parts[1] << 16 | (long long)parts[2] << 8 | (long long)parts[3];

        // Calculate the range of IP addresses
        long long maxInt = ipInt + n - 1;

        // Calculate the number of bits required to represent the range
        int bits = 0;
        long long mask = 1LL << 33;
        while (mask > 0) {
            if ((mask & ipInt) == (mask & maxInt)) {
                bits++;
            }
            mask >>= 1;
        }

        // Calculate the CIDR notation
        return ip + "/" + to_string(33 - bits);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're performing a constant number of operations.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space.
> - **Why these complexities occur:** The number of operations and the amount of space used do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the CIDR notation directly from the IP address and the number of IP addresses.
- Detailed breakdown of the approach:
  1. Convert the IP address to an integer for easier manipulation.
  2. Calculate the range of IP addresses.
  3. Find the CIDR notation for the range by counting the number of bits required to represent the range.
- Proof of optimality: This approach is optimal because it uses a constant number of operations and a constant amount of space.

```cpp
class Solution {
public:
    string ipToCIDR(string ip, int n) {
        // Split the IP address into its four parts
        int parts[4];
        sscanf(ip.c_str(), "%d.%d.%d.%d", &parts[0], &parts[1], &parts[2], &parts[3]);

        // Convert the IP address to an integer
        long long ipInt = (long long)parts[0] << 24 | (long long)parts[1] << 16 | (long long)parts[2] << 8 | (long long)parts[3];

        // Calculate the range of IP addresses
        long long maxInt = ipInt + n - 1;

        // Calculate the number of bits required to represent the range
        int bits = 0;
        long long mask = 1LL << 33;
        while (mask > 0) {
            if ((mask & ipInt) == (mask & maxInt)) {
                bits++;
            }
            mask >>= 1;
        }

        // Calculate the CIDR notation
        return ip + "/" + to_string(33 - bits);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're performing a constant number of operations.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses a constant number of operations and a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: IP address manipulation, bit manipulation, and CIDR notation calculation.
- Problem-solving patterns identified: Using bit manipulation to calculate the range of IP addresses and the CIDR notation.
- Optimization techniques learned: Using a constant number of operations and a constant amount of space to improve performance.
- Similar problems to practice: IP address manipulation, bit manipulation, and CIDR notation calculation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the range of IP addresses or the CIDR notation.
- Edge cases to watch for: IP addresses with leading zeros, IP addresses with values greater than 255.
- Performance pitfalls: Using an excessive number of operations or an excessive amount of space.
- Testing considerations: Testing with different IP addresses and numbers of IP addresses to ensure correctness.