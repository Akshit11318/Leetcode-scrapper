## Deep Object Filter
**Problem Link:** https://leetcode.com/problems/deep-object-filter/description

**Problem Statement:**
- Input format and constraints: The input is a JSON object, and we need to filter it based on the given keys.
- Expected output format: The output should be a filtered JSON object containing only the specified keys.
- Key requirements and edge cases to consider: The JSON object can be nested, and we need to handle arrays and objects recursively.
- Example test cases with explanations: 
    - Input: `{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}` and keys `["a", "c"]`. The output should be `{"a": 1, "c": {"d": 3, "e": 4}}`.
    - Input: `{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}` and keys `["c", "e"]`. The output should be `{"c": {"e": 4}}`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can use a recursive function to traverse the JSON object and filter out the keys that are not specified.
- Step-by-step breakdown of the solution:
    1. Create a recursive function `filterObject` that takes a JSON object and a list of keys as input.
    2. If the input object is an array, iterate over each element and recursively call `filterObject` on each element.
    3. If the input object is an object, iterate over each key-value pair and check if the key is in the list of specified keys.
    4. If the key is specified, add the key-value pair to the filtered object.
    5. If the value is an object or array, recursively call `filterObject` on the value.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large JSON objects.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

// Define a function to filter a JSON object
unordered_map<string, any> filterObject(unordered_map<string, any> obj, vector<string> keys) {
    unordered_map<string, any> filteredObj;
    for (auto& [key, value] : obj) {
        if (find(keys.begin(), keys.end(), key) != keys.end()) {
            if (value.type() == typeid(unordered_map<string, any>)) {
                filteredObj[key] = filterObject(any_cast<unordered_map<string, any>>(value), keys);
            } else if (value.type() == typeid(vector<any>)) {
                vector<any> filteredArray;
                for (any element : any_cast<vector<any>>(value)) {
                    if (element.type() == typeid(unordered_map<string, any>)) {
                        filteredArray.push_back(filterObject(any_cast<unordered_map<string, any>>(element), keys));
                    } else {
                        filteredArray.push_back(element);
                    }
                }
                filteredObj[key] = filteredArray;
            } else {
                filteredObj[key] = value;
            }
        }
    }
    return filteredObj;
}

// Helper function to print the filtered object
void printObject(unordered_map<string, any> obj, int indent = 0) {
    for (auto& [key, value] : obj) {
        for (int i = 0; i < indent; i++) {
            cout << "  ";
        }
        cout << key << ": ";
        if (value.type() == typeid(unordered_map<string, any>)) {
            cout << endl;
            printObject(any_cast<unordered_map<string, any>>(value), indent + 1);
        } else if (value.type() == typeid(vector<any>)) {
            cout << "[" << endl;
            for (any element : any_cast<vector<any>>(value)) {
                if (element.type() == typeid(unordered_map<string, any>)) {
                    printObject(any_cast<unordered_map<string, any>>(element), indent + 1);
                } else {
                    for (int i = 0; i < indent + 1; i++) {
                        cout << "  ";
                    }
                    cout << any_cast<int>(element) << endl;
                }
            }
            for (int i = 0; i < indent; i++) {
                cout << "  ";
            }
            cout << "]" << endl;
        } else {
            cout << any_cast<int>(value) << endl;
        }
    }
}

int main() {
    // Example usage
    unordered_map<string, any> obj = {
        {"a", 1},
        {"b", 2},
        {"c", unordered_map<string, any>{{"d", 3}, {"e", 4}}},
        {"f", vector<any>{5, 6, unordered_map<string, any>{{"g", 7}, {"h", 8}}}}
    };
    vector<string> keys = {"a", "c", "e"};
    unordered_map<string, any> filteredObj = filterObject(obj, keys);
    printObject(filteredObj);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of key-value pairs in the JSON object and $m$ is the maximum depth of the object.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the filtered object.
> - **Why these complexities occur:** The time complexity is due to the recursive function calls, and the space complexity is due to the storage of the filtered object.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a recursive function with memoization to avoid redundant computations.
- Detailed breakdown of the approach:
    1. Create a recursive function `filterObject` that takes a JSON object and a list of keys as input.
    2. Use a memoization table to store the filtered objects for each sub-object.
    3. If the input object is an array, iterate over each element and recursively call `filterObject` on each element.
    4. If the input object is an object, iterate over each key-value pair and check if the key is in the list of specified keys.
    5. If the key is specified, add the key-value pair to the filtered object.
    6. If the value is an object or array, recursively call `filterObject` on the value and store the result in the memoization table.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$, where $n$ is the number of key-value pairs in the JSON object, as we avoid redundant computations using memoization.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

// Define a function to filter a JSON object
unordered_map<string, any> filterObject(unordered_map<string, any> obj, vector<string> keys, unordered_map<string, any>& memo) {
    if (memo.find("obj") != memo.end()) {
        return memo["obj"];
    }
    unordered_map<string, any> filteredObj;
    for (auto& [key, value] : obj) {
        if (find(keys.begin(), keys.end(), key) != keys.end()) {
            if (value.type() == typeid(unordered_map<string, any>)) {
                filteredObj[key] = filterObject(any_cast<unordered_map<string, any>>(value), keys, memo);
            } else if (value.type() == typeid(vector<any>)) {
                vector<any> filteredArray;
                for (any element : any_cast<vector<any>>(value)) {
                    if (element.type() == typeid(unordered_map<string, any>)) {
                        filteredArray.push_back(filterObject(any_cast<unordered_map<string, any>>(element), keys, memo));
                    } else {
                        filteredArray.push_back(element);
                    }
                }
                filteredObj[key] = filteredArray;
            } else {
                filteredObj[key] = value;
            }
        }
    }
    memo["obj"] = filteredObj;
    return filteredObj;
}

// Helper function to print the filtered object
void printObject(unordered_map<string, any> obj, int indent = 0) {
    for (auto& [key, value] : obj) {
        for (int i = 0; i < indent; i++) {
            cout << "  ";
        }
        cout << key << ": ";
        if (value.type() == typeid(unordered_map<string, any>)) {
            cout << endl;
            printObject(any_cast<unordered_map<string, any>>(value), indent + 1);
        } else if (value.type() == typeid(vector<any>)) {
            cout << "[" << endl;
            for (any element : any_cast<vector<any>>(value)) {
                if (element.type() == typeid(unordered_map<string, any>)) {
                    printObject(any_cast<unordered_map<string, any>>(element), indent + 1);
                } else {
                    for (int i = 0; i < indent + 1; i++) {
                        cout << "  ";
                    }
                    cout << any_cast<int>(element) << endl;
                }
            }
            for (int i = 0; i < indent; i++) {
                cout << "  ";
            }
            cout << "]" << endl;
        } else {
            cout << any_cast<int>(value) << endl;
        }
    }
}

int main() {
    // Example usage
    unordered_map<string, any> obj = {
        {"a", 1},
        {"b", 2},
        {"c", unordered_map<string, any>{{"d", 3}, {"e", 4}}},
        {"f", vector<any>{5, 6, unordered_map<string, any>{{"g", 7}, {"h", 8}}}}
    };
    vector<string> keys = {"a", "c", "e"};
    unordered_map<string, any> memo;
    unordered_map<string, any> filteredObj = filterObject(obj, keys, memo);
    printObject(filteredObj);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of key-value pairs in the JSON object.
> - **Space Complexity:** $O(n)$, as we need to store the filtered object and the memoization table.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$, as we avoid redundant computations using memoization.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive functions, memoization, and JSON object manipulation.
- Problem-solving patterns identified: Using memoization to avoid redundant computations and improving the time complexity of the solution.
- Optimization techniques learned: Using memoization to optimize the solution and reducing the time complexity.
- Similar problems to practice: JSON object filtering, recursive functions, and memoization.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty JSON objects or arrays, and not checking for key existence in the memoization table.
- Edge cases to watch for: Handling nested JSON objects and arrays, and checking for key existence in the memoization table.
- Performance pitfalls: Not using memoization, which can lead to redundant computations and a higher time complexity.
- Testing considerations: Testing the solution with different JSON objects, including nested objects and arrays, and checking for correct output and performance.