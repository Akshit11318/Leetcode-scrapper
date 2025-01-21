## Arrange Table by Gender

**Problem Link:** https://leetcode.com/problems/arrange-table-by-gender/description

**Problem Statement:**
- Input: A table with `id`, `name`, and `gender` columns, and a number `special` representing a special customer.
- Expected output: The table rearranged so that customers of the same gender are seated together, and the special customer is seated as close as possible to the front.
- Key requirements:
  - Customers of the same gender must be seated together.
  - The special customer must be seated as close as possible to the front.
- Example test cases:
  - Table with customers of different genders and a special customer.
  - Table with customers of the same gender and no special customer.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to sort the table by `gender` and then by `id`.
- However, this approach does not guarantee that the special customer is seated as close as possible to the front.
- To achieve this, we need to separate the special customer from the rest of the table and insert them at the beginning of the sorted table.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Customer {
    int id;
    string name;
    char gender;
};

bool compareCustomers(Customer a, Customer b) {
    if (a.gender == b.gender) {
        return a.id < b.id;
    }
    return a.gender < b.gender;
}

vector<Customer> arrangeTableByGender(vector<Customer>& table, int special) {
    // Separate the special customer from the rest of the table
    Customer specialCustomer;
    vector<Customer> otherCustomers;
    for (Customer customer : table) {
        if (customer.id == special) {
            specialCustomer = customer;
        } else {
            otherCustomers.push_back(customer);
        }
    }

    // Sort the other customers by gender and then by id
    sort(otherCustomers.begin(), otherCustomers.end(), compareCustomers);

    // Insert the special customer at the beginning of the sorted table
    vector<Customer> result;
    result.push_back(specialCustomer);
    result.insert(result.end(), otherCustomers.begin(), otherCustomers.end());

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of customers in the table, due to the sorting operation.
> - **Space Complexity:** $O(n)$, as we need to store the sorted table.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to the need to store the sorted table.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass through the table to separate the customers by gender and insert the special customer at the beginning.
- We can use two vectors to store the male and female customers separately.
- After separating the customers, we can concatenate the two vectors and insert the special customer at the beginning.

```cpp
vector<Customer> arrangeTableByGender(vector<Customer>& table, int special) {
    vector<Customer> maleCustomers;
    vector<Customer> femaleCustomers;
    Customer specialCustomer;

    // Separate the customers by gender and find the special customer
    for (Customer customer : table) {
        if (customer.id == special) {
            specialCustomer = customer;
        } else if (customer.gender == 'M') {
            maleCustomers.push_back(customer);
        } else {
            femaleCustomers.push_back(customer);
        }
    }

    // Sort the male and female customers by id
    sort(maleCustomers.begin(), maleCustomers.end(), [](Customer a, Customer b) { return a.id < b.id; });
    sort(femaleCustomers.begin(), femaleCustomers.end(), [](Customer a, Customer b) { return a.id < b.id; });

    // Concatenate the male and female customers and insert the special customer at the beginning
    vector<Customer> result;
    result.push_back(specialCustomer);
    result.insert(result.end(), maleCustomers.begin(), maleCustomers.end());
    result.insert(result.end(), femaleCustomers.begin(), femaleCustomers.end());

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of customers in the table, due to the sorting operations.
> - **Space Complexity:** $O(n)$, as we need to store the separated customers and the final result.
> - **Optimality proof:** This approach is optimal because it uses a single pass through the table to separate the customers and insert the special customer, and then sorts the customers by id.

---

### Final Notes

**Learning Points:**
- The importance of separating the special customer from the rest of the table to ensure they are seated as close as possible to the front.
- The use of two vectors to store the male and female customers separately to simplify the sorting process.
- The concatenation of the male and female customers to form the final result.

**Mistakes to Avoid:**
- Not separating the special customer from the rest of the table, resulting in incorrect seating.
- Not sorting the male and female customers by id, resulting in incorrect ordering.
- Not concatenating the male and female customers correctly, resulting in incorrect final result.