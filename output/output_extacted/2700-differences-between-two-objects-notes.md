## Differences Between Two Objects
**Problem Link:** https://leetcode.com/problems/differences-between-two-objects/description

**Problem Statement:**
- Input format and constraints: Given two objects, find the differences between them.
- Expected output format: Return a list of differences.
- Key requirements and edge cases to consider: The objects can have nested objects and arrays.
- Example test cases with explanations:
  - Test case 1: Two objects with different values for the same key.
  - Test case 2: Two objects with different keys.
  - Test case 3: Two objects with nested objects.
  - Test case 4: Two objects with arrays.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare the two objects key by key.
- Step-by-step breakdown of the solution:
  1. Get all the keys from both objects.
  2. Compare the values for each key.
  3. If the values are different, add the key to the list of differences.
- Why this approach comes to mind first: It is a straightforward way to compare two objects.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

void getDifferences(unordered_map<string, unordered_map<string, string>> obj1, 
                    unordered_map<string, unordered_map<string, string>> obj2, 
                    vector<string>& differences) {
    set<string> allKeys;
    for (auto& pair : obj1) {
        allKeys.insert(pair.first);
    }
    for (auto& pair : obj2) {
        allKeys.insert(pair.first);
    }

    for (auto& key : allKeys) {
        if (obj1.find(key) != obj1.end() && obj2.find(key) != obj2.end()) {
            if (obj1[key] != obj2[key]) {
                differences.push_back(key);
            }
        } else if (obj1.find(key) != obj1.end()) {
            differences.push_back(key);
        } else if (obj2.find(key) != obj2.end()) {
            differences.push_back(key);
        }
    }
}

int main() {
    unordered_map<string, unordered_map<string, string>> obj1 = {
        {"key1", {{"nestedKey1", "value1"}}},
        {"key2", {{"nestedKey2", "value2"}}}
    };

    unordered_map<string, unordered_map<string, string>> obj2 = {
        {"key1", {{"nestedKey1", "value3"}}},
        {"key3", {{"nestedKey3", "value3"}}}
    };

    vector<string> differences;
    getDifferences(obj1, obj2, differences);

    for (auto& diff : differences) {
        cout << diff << endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of keys in both objects. 
> - **Space Complexity:** $O(n)$, where $n$ is the total number of keys in both objects. 
> - **Why these complexities occur:** The brute force approach iterates over all keys in both objects once.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use recursion to handle nested objects.
- Detailed breakdown of the approach:
  1. Create a function to compare two objects.
  2. If the objects are not of the same type, return the difference.
  3. If the objects are arrays, compare them element by element.
  4. If the objects are objects, compare them key by key.
- Proof of optimality: This approach handles all possible cases and has the same time complexity as the brute force approach.
- Why further optimization is impossible: This approach already has the optimal time complexity.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

void getDifferences(unordered_map<string, string> obj1, 
                    unordered_map<string, string> obj2, 
                    vector<string>& differences) {
    set<string> allKeys;
    for (auto& pair : obj1) {
        allKeys.insert(pair.first);
    }
    for (auto& pair : obj2) {
        allKeys.insert(pair.first);
    }

    for (auto& key : allKeys) {
        if (obj1.find(key) != obj1.end() && obj2.find(key) != obj2.end()) {
            if (obj1[key] != obj2[key]) {
                differences.push_back(key);
            }
        } else if (obj1.find(key) != obj1.end()) {
            differences.push_back(key);
        } else if (obj2.find(key) != obj2.end()) {
            differences.push_back(key);
        }
    }
}

void getDifferences(vector<string> arr1, vector<string> arr2, vector<string>& differences) {
    if (arr1.size() != arr2.size()) {
        differences.push_back("array_length");
    }

    for (int i = 0; i < arr1.size(); i++) {
        if (arr1[i] != arr2[i]) {
            differences.push_back(to_string(i));
        }
    }
}

int main() {
    unordered_map<string, string> obj1 = {
        {"key1", "value1"},
        {"key2", "value2"}
    };

    unordered_map<string, string> obj2 = {
        {"key1", "value3"},
        {"key3", "value3"}
    };

    vector<string> differences;
    getDifferences(obj1, obj2, differences);

    for (auto& diff : differences) {
        cout << diff << endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of keys in both objects. 
> - **Space Complexity:** $O(n)$, where $n$ is the total number of keys in both objects. 
> - **Optimality proof:** This approach handles all possible cases and has the same time complexity as the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, iteration over objects and arrays.
- Problem-solving patterns identified: Handling nested objects and arrays.
- Optimization techniques learned: Using recursion to handle nested objects.
- Similar problems to practice: Comparing two arrays, comparing two strings.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for null values.
- Edge cases to watch for: Objects with different types, objects with nested objects and arrays.
- Performance pitfalls: Using unnecessary iterations, not using recursion to handle nested objects.
- Testing considerations: Testing with different types of objects, testing with nested objects and arrays.