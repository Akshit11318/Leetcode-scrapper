## Convert JSON String to Object
**Problem Link:** https://leetcode.com/problems/convert-json-string-to-object/description

**Problem Statement:**
- Input format and constraints: The input is a JSON string that needs to be converted into a JavaScript object.
- Expected output format: The output should be a JavaScript object.
- Key requirements and edge cases to consider: Handling nested JSON structures, arrays, and potential errors in the JSON string.
- Example test cases with explanations: 
    - Input: `"{"name": "John", "age": 30, "city": "New York"}"` 
    - Output: `{name: "John", age: 30, city: "New York"}`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One might think to manually parse the JSON string by iterating through each character and constructing the object based on the syntax of JSON. This involves identifying keys, values, and the structure (arrays, objects).
- Step-by-step breakdown of the solution:
    1. Initialize an empty object to store the result.
    2. Iterate through the JSON string to identify keys and values.
    3. Use conditional statements to handle different types of values (strings, numbers, booleans, arrays, objects).
    4. Recursively handle nested structures.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem without relying on external libraries or functions.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Function to convert JSON string to object
std::unordered_map<std::string, std::string> convertJSON(const std::string& jsonString) {
    std::unordered_map<std::string, std::string> result;
    size_t start = 1; // Start after the first '{'
    size_t end = jsonString.size() - 1; // End before the last '}'
    
    while (start < end) {
        size_t keyStart = start;
        size_t keyEnd = jsonString.find(':', start);
        std::string key = jsonString.substr(keyStart, keyEnd - keyStart);
        
        size_t valueStart = keyEnd + 1;
        size_t valueEnd = jsonString.find(',', valueStart);
        if (valueEnd == std::string::npos) {
            valueEnd = end;
        }
        std::string value = jsonString.substr(valueStart, valueEnd - valueStart);
        
        // Remove quotes from key and value
        key.erase(0, key.find_first_not_of('"'));
        key.erase(key.find_last_not_of('"') + 1);
        value.erase(0, value.find_first_not_of('"'));
        value.erase(value.find_last_not_of('"') + 1);
        
        result[key] = value;
        start = valueEnd + 1;
    }
    
    return result;
}

int main() {
    std::string jsonString = "{\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}";
    std::unordered_map<std::string, std::string> result = convertJSON(jsonString);
    
    for (const auto& pair : result) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the JSON string, because we are scanning the string once.
> - **Space Complexity:** $O(n)$, for storing the resulting object and temporary strings.
> - **Why these complexities occur:** The brute force approach involves scanning the entire string and creating a new object with potentially the same number of elements as the input string.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize existing JSON parsing libraries that are optimized and well-tested.
- Detailed breakdown of the approach: 
    1. Choose a suitable JSON library (e.g., `json` library in C++).
    2. Use the library's functions to parse the JSON string into a C++ object (e.g., `json` object).
    3. Access and manipulate the object as needed.
- Proof of optimality: This approach is optimal because it leverages the efficiency and optimizations of a dedicated JSON parsing library, which is typically more efficient than a custom, brute-force implementation.

```cpp
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    std::string jsonString = "{\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}";
    json jsonObject = json::parse(jsonString);
    
    std::cout << jsonObject.dump(4) << std::endl;
    
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the JSON string, due to the parsing process.
> - **Space Complexity:** $O(n)$, for storing the parsed JSON object.
> - **Optimality proof:** The use of a specialized library for JSON parsing ensures that the solution is as efficient as possible, leveraging the library's optimizations and handling of edge cases.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Parsing, recursion for nested structures, and the importance of leveraging existing libraries for complex tasks.
- Problem-solving patterns identified: The value of breaking down complex problems into manageable parts and recognizing when to use existing solutions.
- Optimization techniques learned: Using specialized libraries can significantly improve performance and reliability.
- Similar problems to practice: Other parsing tasks, such as XML or CSV parsing, and working with different data formats.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as malformed input or unexpected nesting levels.
- Edge cases to watch for: Empty strings, single-element arrays, and deeply nested structures.
- Performance pitfalls: Implementing a custom parser without considering efficiency or scalability.
- Testing considerations: Thoroughly testing with a variety of inputs, including edge cases and large datasets.