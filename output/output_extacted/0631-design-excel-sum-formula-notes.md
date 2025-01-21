## Design Excel Sum Formula

**Problem Link:** https://leetcode.com/problems/design-excel-sum-formula/description

**Problem Statement:**
- Input format and constraints: The input will be a string representing a cell reference in the format "A1", "B2", etc. The Excel sheet has a maximum of 26 columns and 26 rows.
- Expected output format: The output will be the sum of the values in the cells referenced by the input string.
- Key requirements and edge cases to consider: The input string can contain multiple cell references separated by commas, and the references can be in the format "A1" or "A1:B2".
- Example test cases with explanations: 
    - Input: "A1"
    - Output: 0 (since the cell A1 has no value)
    - Input: "A1,B2"
    - Output: 0 (since neither cell A1 nor B2 has a value)
    - Input: "A1:B2"
    - Output: 0 (since neither cell A1 nor B2 has a value)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves parsing the input string to extract the cell references, then iterating over each reference to calculate the sum.
- Step-by-step breakdown of the solution:
    1. Parse the input string to extract the cell references.
    2. For each reference, check if it is a single cell or a range of cells.
    3. If it is a single cell, get its value and add it to the sum.
    4. If it is a range of cells, get the values of all cells in the range and add them to the sum.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large input strings.

```cpp
class Excel {
public:
    void set(int row, int col, int val) {
        // set the value of the cell at row and col
        cells[row][col] = val;
    }
    
    int get(int row, int col) {
        // get the value of the cell at row and col
        return cells[row][col];
    }
    
    int sum(int row, int col, string str) {
        // parse the input string to extract the cell references
        vector<string> refs;
        string ref;
        for (char c : str) {
            if (c == ',') {
                refs.push_back(ref);
                ref.clear();
            } else {
                ref += c;
            }
        }
        refs.push_back(ref);
        
        int sum = 0;
        for (string ref : refs) {
            // check if the reference is a single cell or a range of cells
            if (ref.find(':') != string::npos) {
                // it is a range of cells
                int startRow, startCol, endRow, endCol;
                // parse the start and end cell references
                startRow = ref[0] - 'A' + 1;
                startCol = ref[1] - '0';
                endRow = ref[3] - 'A' + 1;
                endCol = ref[4] - '0';
                // get the values of all cells in the range and add them to the sum
                for (int i = startRow; i <= endRow; i++) {
                    for (int j = startCol; j <= endCol; j++) {
                        sum += get(i, j);
                    }
                }
            } else {
                // it is a single cell
                int row = ref[0] - 'A' + 1;
                int col = ref[1] - '0';
                // get the value of the cell and add it to the sum
                sum += get(row, col);
            }
        }
        return sum;
    }
    
private:
    int cells[27][27]; // assuming a maximum of 26 columns and 26 rows
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where n is the number of cell references and m is the maximum number of cells in a range.
> - **Space Complexity:** $O(1)$, since we only use a fixed amount of space to store the cells.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each cell reference and each cell in the range. The space complexity occurs because we only use a fixed amount of space to store the cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map<string, int>` to store the values of the cells, where the key is the cell reference and the value is the cell value.
- Detailed breakdown of the approach:
    1. Parse the input string to extract the cell references.
    2. For each reference, check if it is a single cell or a range of cells.
    3. If it is a single cell, get its value from the map and add it to the sum.
    4. If it is a range of cells, get the values of all cells in the range from the map and add them to the sum.
- Proof of optimality: This approach is optimal because we only iterate over each cell reference and each cell in the range once, and we use a map to store the cell values, which allows us to look up the values in constant time.

```cpp
class Excel {
public:
    void set(int row, int col, int val) {
        // set the value of the cell at row and col
        string ref = string(1, 'A' + row - 1) + to_string(col);
        cells[ref] = val;
    }
    
    int get(int row, int col) {
        // get the value of the cell at row and col
        string ref = string(1, 'A' + row - 1) + to_string(col);
        return cells[ref];
    }
    
    int sum(int row, int col, string str) {
        // parse the input string to extract the cell references
        vector<string> refs;
        string ref;
        for (char c : str) {
            if (c == ',') {
                refs.push_back(ref);
                ref.clear();
            } else {
                ref += c;
            }
        }
        refs.push_back(ref);
        
        int sum = 0;
        for (string ref : refs) {
            // check if the reference is a single cell or a range of cells
            if (ref.find(':') != string::npos) {
                // it is a range of cells
                string startRef = ref.substr(0, ref.find(':'));
                string endRef = ref.substr(ref.find(':') + 1);
                int startRow = startRef[0] - 'A' + 1;
                int startCol = stoi(startRef.substr(1));
                int endRow = endRef[0] - 'A' + 1;
                int endCol = stoi(endRef.substr(1));
                // get the values of all cells in the range and add them to the sum
                for (int i = startRow; i <= endRow; i++) {
                    for (int j = startCol; j <= endCol; j++) {
                        string cellRef = string(1, 'A' + i - 1) + to_string(j);
                        sum += cells[cellRef];
                    }
                }
            } else {
                // it is a single cell
                sum += cells[ref];
            }
        }
        return sum;
    }
    
private:
    unordered_map<string, int> cells; // store the values of the cells
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where n is the number of cell references and m is the maximum number of cells in a range.
> - **Space Complexity:** $O(n)$, where n is the number of cells.
> - **Optimality proof:** This approach is optimal because we only iterate over each cell reference and each cell in the range once, and we use a map to store the cell values, which allows us to look up the values in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: parsing input strings, iterating over cell references, using maps to store cell values.
- Problem-solving patterns identified: breaking down complex problems into simpler sub-problems, using data structures to store and look up values efficiently.
- Optimization techniques learned: using maps to store cell values, iterating over cell references and cells in the range only once.
- Similar problems to practice: other problems that involve parsing input strings, iterating over data structures, and using optimization techniques to improve performance.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling invalid input, not using data structures efficiently.
- Edge cases to watch for: empty input strings, invalid cell references, ranges of cells that are not rectangular.
- Performance pitfalls: iterating over cell references and cells in the range multiple times, not using maps to store cell values.
- Testing considerations: testing with different input strings, testing with different cell references and ranges, testing with invalid input.