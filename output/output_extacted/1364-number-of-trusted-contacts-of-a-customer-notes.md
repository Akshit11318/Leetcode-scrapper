## Number of Trusted Contacts of a Customer
**Problem Link:** https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/description

**Problem Statement:**
- Input: A table `Calls` containing customer interactions with `id`, `customer_id`, `call_date`, `call_type` (either 'inbound' or 'outbound'), and `customer_id_of_caller` (the `customer_id` of the other party in the call).
- Expected output: For each customer, calculate the number of trusted contacts. A trusted contact is defined as another customer who has made an 'inbound' call to the customer and received an 'outbound' call from the customer.
- Key requirements and edge cases to consider: 
    - A customer can have multiple trusted contacts.
    - The same customer can appear in both the `customer_id` and `customer_id_of_caller` columns.
    - The date of the call does not affect the definition of a trusted contact.
- Example test cases with explanations:
    - A customer with only 'outbound' calls has no trusted contacts.
    - A customer with only 'inbound' calls has no trusted contacts if they have not made an 'outbound' call to any of the callers.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each customer's calls to check for 'inbound' calls and then verify if there's a corresponding 'outbound' call to the same customer.
- Step-by-step breakdown of the solution:
    1. For each customer, iterate over all their calls.
    2. For each 'inbound' call, check if there exists an 'outbound' call to the same `customer_id_of_caller`.
    3. Count the distinct `customer_id_of_caller` for which both conditions are met.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

struct Call {
    int id;
    int customer_id;
    std::string call_date;
    std::string call_type;
    int customer_id_of_caller;
};

std::unordered_map<int, int> countTrustedContacts(const std::vector<Call>& calls) {
    std::unordered_map<int, int> trustedContactsCount;
    for (const auto& call : calls) {
        if (call.call_type == "inbound") {
            int inboundCaller = call.customer_id_of_caller;
            bool foundOutbound = false;
            for (const auto& otherCall : calls) {
                if (otherCall.customer_id == call.customer_id &&
                    otherCall.call_type == "outbound" &&
                    otherCall.customer_id_of_caller == inboundCaller) {
                    foundOutbound = true;
                    break;
                }
            }
            if (foundOutbound && trustedContactsCount.find(call.customer_id) == trustedContactsCount.end()) {
                trustedContactsCount[call.customer_id] = 1;
            } else if (foundOutbound) {
                trustedContactsCount[call.customer_id]++;
            }
        }
    }
    return trustedContactsCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of calls, due to the nested loop structure.
> - **Space Complexity:** $O(n)$ for storing the count of trusted contacts for each customer.
> - **Why these complexities occur:** The brute force approach involves checking every call against every other call, leading to quadratic time complexity. The space complexity is linear because we store the count of trusted contacts for each unique customer.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Utilize an unordered map to store the `customer_id` and their corresponding 'inbound' and 'outbound' calls. This allows for efficient lookups and reduces the time complexity.
- Detailed breakdown of the approach:
    1. Create two unordered maps: one for 'inbound' calls and one for 'outbound' calls, where each key is a `customer_id` and the value is an unordered set of `customer_id_of_caller`.
    2. Iterate over the calls, populating the 'inbound' and 'outbound' maps.
    3. For each customer, intersect their 'inbound' and 'outbound' sets to find trusted contacts.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Call {
    int id;
    int customer_id;
    std::string call_date;
    std::string call_type;
    int customer_id_of_caller;
};

std::unordered_map<int, int> countTrustedContacts(const std::vector<Call>& calls) {
    std::unordered_map<int, std::unordered_set<int>> inboundCalls;
    std::unordered_map<int, std::unordered_set<int>> outboundCalls;

    for (const auto& call : calls) {
        if (call.call_type == "inbound") {
            inboundCalls[call.customer_id].insert(call.customer_id_of_caller);
        } else if (call.call_type == "outbound") {
            outboundCalls[call.customer_id].insert(call.customer_id_of_caller);
        }
    }

    std::unordered_map<int, int> trustedContactsCount;
    for (const auto& customerInbound : inboundCalls) {
        int customerId = customerInbound.first;
        if (outboundCalls.find(customerId) != outboundCalls.end()) {
            std::unordered_set<int> intersection;
            for (int caller : customerInbound.second) {
                if (outboundCalls[customerId].find(caller) != outboundCalls[customerId].end()) {
                    intersection.insert(caller);
                }
            }
            trustedContactsCount[customerId] = intersection.size();
        }
    }
    return trustedContactsCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of calls, because we make a single pass through the calls and use constant time operations for insertions and lookups in the unordered maps and sets.
> - **Space Complexity:** $O(n)$ for storing the 'inbound' and 'outbound' calls in the unordered maps and sets.
> - **Optimality proof:** This approach is optimal because it achieves linear time complexity by avoiding nested loops and using data structures that allow for constant time operations.

---

### Final Notes

**Learning Points:**
- Utilizing unordered maps and sets for efficient lookups and storage.
- Reducing time complexity by avoiding nested loops and using single pass algorithms.
- Understanding how to apply data structures to solve real-world problems efficiently.

**Mistakes to Avoid:**
- Not considering the use of more efficient data structures.
- Failing to recognize opportunities to reduce time complexity.
- Not validating the input and handling edge cases properly.
- Not commenting the code clearly for readability and maintainability.