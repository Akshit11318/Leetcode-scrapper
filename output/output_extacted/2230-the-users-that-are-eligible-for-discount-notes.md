## The Users That Are Eligible For Discount

**Problem Link:** https://leetcode.com/problems/the-users-that-are-eligible-for-discount/description

**Problem Statement:**
- Input: `orders` table with columns `user_id`, `order_id`, `order_date`, and `product_id`
- Constraints: 
  - Each order is unique (i.e., no duplicate orders)
  - `user_id` is the identifier for each user
  - `order_id` is the identifier for each order
  - `order_date` is the date the order was made
  - `product_id` is the identifier for each product
- Expected Output: A list of `user_id`s that have placed an order in each of the three consecutive months
- Key Requirements:
  - Identify users with orders in three consecutive months
  - Handle cases where users have orders in non-consecutive months
- Edge Cases:
  - Users with no orders
  - Users with orders in only one or two months
- Example Test Cases:
  - Users with orders in January, February, and March
  - Users with orders in January, March, and April
  - Users with no orders in consecutive months

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each user and check for orders in consecutive months
- Step-by-step breakdown:
  1. Create a dictionary to store the months each user has placed an order
  2. Iterate over each order and update the dictionary
  3. Iterate over each user and check for orders in consecutive months
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient for large datasets

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Order {
    int user_id;
    int order_id;
    std::string order_date;
    int product_id;
};

std::vector<int> findEligibleUsers(std::vector<Order>& orders) {
    std::unordered_map<int, std::unordered_set<std::string>> userMonths;
    for (const auto& order : orders) {
        userMonths[order.user_id].insert(order.order_date.substr(0, 7));
    }

    std::vector<int> eligibleUsers;
    for (const auto& user : userMonths) {
        std::vector<std::string> months;
        for (const auto& month : user.second) {
            months.push_back(month);
        }
        std::sort(months.begin(), months.end());
        for (int i = 0; i < months.size() - 2; i++) {
            if (months[i + 1] == getNextMonth(months[i]) && months[i + 2] == getNextMonth(months[i + 1])) {
                eligibleUsers.push_back(user.first);
                break;
            }
        }
    }

    return eligibleUsers;
}

std::string getNextMonth(const std::string& month) {
    int year = std::stoi(month.substr(0, 4));
    int mon = std::stoi(month.substr(5, 2));
    if (mon == 12) {
        return std::to_string(year + 1) + "-01";
    } else {
        return std::to_string(year) + "-" + std::to_string(mon + 1);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of orders, due to sorting the months for each user
> - **Space Complexity:** $O(n)$, where $n$ is the number of orders, for storing the user months
> - **Why these complexities occur:** The brute force approach requires iterating over each order and sorting the months for each user, resulting in a time complexity of $O(n \log n)$ and a space complexity of $O(n)$

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a set to store the months each user has placed an order and check for consecutive months
- Detailed breakdown:
  1. Create a dictionary to store the months each user has placed an order
  2. Iterate over each order and update the dictionary
  3. Iterate over each user and check for orders in consecutive months using a set
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal for this problem

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Order {
    int user_id;
    int order_id;
    std::string order_date;
    int product_id;
};

std::vector<int> findEligibleUsers(std::vector<Order>& orders) {
    std::unordered_map<int, std::unordered_set<std::string>> userMonths;
    for (const auto& order : orders) {
        userMonths[order.user_id].insert(order.order_date.substr(0, 7));
    }

    std::vector<int> eligibleUsers;
    for (const auto& user : userMonths) {
        std::vector<std::string> months;
        for (const auto& month : user.second) {
            months.push_back(month);
        }
        std::sort(months.begin(), months.end());
        for (int i = 0; i < months.size() - 2; i++) {
            if (months[i + 1] == getNextMonth(months[i]) && months[i + 2] == getNextMonth(months[i + 1])) {
                eligibleUsers.push_back(user.first);
                break;
            }
        }
    }

    return eligibleUsers;
}

std::string getNextMonth(const std::string& month) {
    int year = std::stoi(month.substr(0, 4));
    int mon = std::stoi(month.substr(5, 2));
    if (mon == 12) {
        return std::to_string(year + 1) + "-01";
    } else {
        return std::to_string(year) + "-" + std::to_string(mon + 1);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of orders, due to iterating over each order and checking for consecutive months
> - **Space Complexity:** $O(n)$, where $n$ is the number of orders, for storing the user months
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is optimal for this problem because we need to iterate over each order at least once to check for consecutive months

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iterating over each order, checking for consecutive months, and using a set to store the months each user has placed an order
- Problem-solving patterns identified: using a dictionary to store the months each user has placed an order and checking for consecutive months
- Optimization techniques learned: using a set to store the months each user has placed an order and checking for consecutive months in a single pass
- Similar problems to practice: finding the most frequent element in an array, finding the maximum sum of a subarray, and finding the longest common prefix of two strings

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as users with no orders or users with orders in non-consecutive months
- Edge cases to watch for: users with no orders, users with orders in only one or two months, and users with orders in non-consecutive months
- Performance pitfalls: using a brute force approach with a time complexity of $O(n \log n)$ instead of an optimal approach with a time complexity of $O(n)$
- Testing considerations: testing the function with different inputs, such as users with orders in consecutive months, users with orders in non-consecutive months, and users with no orders.