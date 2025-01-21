## Combine Two Tables
**Problem Link:** https://leetcode.com/problems/combine-two-tables/description

**Problem Statement:**
- Input format and constraints: The problem involves two tables, `Person` and `Address`, with `Person` having columns `PersonId`, `LastName`, `FirstName`, and `AddressId`, and `Address` having columns `AddressId`, `City`, `State`. The task is to combine these two tables based on the `AddressId` field.
- Expected output format: The resulting table should contain all columns from both tables.
- Key requirements and edge cases to consider: Handling cases where a person does not have a corresponding address.
- Example test cases with explanations: For instance, if a person has an `AddressId` that does not exist in the `Address` table, that person should still be included in the result with `NULL` values for the address columns.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: A straightforward approach would involve iterating through each row of the `Person` table and then searching the `Address` table for a matching `AddressId`.
- Step-by-step breakdown of the solution: 
  1. Iterate over each person in the `Person` table.
  2. For each person, query the `Address` table to find an address with a matching `AddressId`.
  3. If a match is found, combine the person's information with the address information into a new row.
  4. If no match is found, still include the person in the result but with `NULL` values for the address columns.
- Why this approach comes to mind first: It directly addresses the requirement of combining the two tables based on a common field.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Person {
    int PersonId;
    std::string LastName;
    std::string FirstName;
    int AddressId;
};

struct Address {
    int AddressId;
    std::string City;
    std::string State;
};

std::vector<std::tuple<int, std::string, std::string, int, std::string, std::string>> 
combineTables(const std::vector<Person>& persons, const std::vector<Address>& addresses) {
    std::unordered_map<int, Address> addressMap;
    for (const auto& address : addresses) {
        addressMap[address.AddressId] = address;
    }

    std::vector<std::tuple<int, std::string, std::string, int, std::string, std::string>> result;
    for (const auto& person : persons) {
        auto it = addressMap.find(person.AddressId);
        if (it != addressMap.end()) {
            result.push_back(std::make_tuple(
                person.PersonId,
                person.LastName,
                person.FirstName,
                person.AddressId,
                it->second.City,
                it->second.State
            ));
        } else {
            result.push_back(std::make_tuple(
                person.PersonId,
                person.LastName,
                person.FirstName,
                person.AddressId,
                "",
                ""
            ));
        }
    }
    return result;
}

int main() {
    // Example usage
    std::vector<Person> persons = {{1, "Doe", "John", 1}, {2, "Smith", "Jane", 2}};
    std::vector<Address> addresses = {{1, "New York", "NY"}, {2, "Los Angeles", "CA"}};

    auto combined = combineTables(persons, addresses);
    for (const auto& row : combined) {
        std::cout << "PersonId: " << std::get<0>(row) << ", LastName: " << std::get<1>(row)
                  << ", FirstName: " << std::get<2>(row) << ", AddressId: " << std::get<3>(row)
                  << ", City: " << std::get<4>(row) << ", State: " << std::get<5>(row) << std::endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of persons and $m$ is the number of addresses, because for each person, we potentially search through all addresses.
> - **Space Complexity:** $O(n + m)$ for storing the persons and addresses in data structures.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the two datasets, leading to a higher time complexity. The space complexity is due to the storage of the input data.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a database's ability to perform joins efficiently. Since this problem is essentially a `LEFT JOIN` operation between two tables based on `AddressId`, using a database's query language (like SQL) is more efficient than manually iterating over the data.
- Detailed breakdown of the approach: The optimal solution involves using SQL to perform a `LEFT JOIN` between the `Person` and `Address` tables on the `AddressId` field. This ensures that all persons are included in the result, even if there is no matching address.
- Proof of optimality: This approach is optimal because it leverages the database's optimized join algorithms, which are typically more efficient than manual iteration, especially for large datasets.
- Why further optimization is impossible: The `LEFT JOIN` operation is inherently necessary to combine the tables as required, and databases are optimized to perform such operations efficiently.

```sql
SELECT P.PersonId, P.LastName, P.FirstName, P.AddressId, A.City, A.State
FROM Person P
LEFT JOIN Address A
ON P.AddressId = A.AddressId;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$ where $n$ and $m$ are the sizes of the `Person` and `Address` tables, respectively. This is because databases typically use efficient sorting or hashing algorithms for joins.
> - **Space Complexity:** $O(n + m)$ for the result set.
> - **Optimality proof:** The database's join operation is optimized for performance, making this the most efficient approach for combining the tables.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of leveraging built-in database operations for efficiency.
- Problem-solving patterns identified: Recognizing when a problem can be solved more efficiently using existing tools or libraries.
- Optimization techniques learned: Using database queries for complex data operations.
- Similar problems to practice: Other database-related problems involving joins, subqueries, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the use of database operations for data manipulation.
- Edge cases to watch for: Handling cases where data is missing or does not match between tables.
- Performance pitfalls: Manually iterating over large datasets instead of using optimized database operations.
- Testing considerations: Ensuring that database queries are correctly formulated and tested with various input scenarios.