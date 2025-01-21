## Design a Text Editor
**Problem Link:** https://leetcode.com/problems/design-a-text-editor/description

**Problem Statement:**
- Input format and constraints: The text editor supports the following operations: 
  - `TextEditor()`: Initializes the object with an empty text editor.
  - `void addText(string text)`: Appends `text` to the end of the current text.
  - `int deleteText(int k)`: Deletes `k` characters from the end of the current text, returning the number of characters actually deleted.
  - `string cursorLeft(int k)`: Moves the cursor `k` characters to the left and returns the last `min(10, len)` characters of the text, where `len` is the length of the current text.
  - `string cursorRight(int k)`: Moves the cursor `k` characters to the right and returns the last `min(10, len)` characters of the text.
- Expected output format: The output should be the result of the operations performed on the text editor.
- Key requirements and edge cases to consider: Handling edge cases such as deleting more characters than the current text length, moving the cursor beyond the text boundaries, and appending text.
- Example test cases with explanations:
  - `TextEditor()`: Initializes an empty text editor.
  - `addText("hello")`: Appends "hello" to the text editor, resulting in "hello".
  - `deleteText(3)`: Deletes 3 characters from the end of the text, resulting in "he".
  - `cursorLeft(1)`: Moves the cursor 1 character to the left and returns the last 2 characters, resulting in "he".
  - `cursorRight(1)`: Moves the cursor 1 character to the right and returns the last 2 characters, resulting in "he".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a string to store the current text and an integer to represent the cursor position.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the text and a cursor position at 0.
  2. For the `addText` operation, append the given text to the end of the current text and move the cursor to the end of the text.
  3. For the `deleteText` operation, delete the specified number of characters from the end of the text and update the cursor position accordingly.
  4. For the `cursorLeft` operation, move the cursor to the left by the specified number of characters and return the last 10 characters of the text.
  5. For the `cursorRight` operation, move the cursor to the right by the specified number of characters and return the last 10 characters of the text.
- Why this approach comes to mind first: It is a straightforward implementation that directly addresses the problem requirements.

```cpp
class TextEditor {
public:
    string text;
    int cursor;

    TextEditor() {
        text = "";
        cursor = 0;
    }

    void addText(string s) {
        text += s;
        cursor = text.size();
    }

    int deleteText(int k) {
        int del = min(k, (int)text.size() - cursor);
        text.erase(cursor - del, del);
        cursor -= del;
        return del;
    }

    string cursorLeft(int k) {
        cursor = max(0, cursor - k);
        return text.substr(max(0, cursor - 10), min(10, (int)text.size() - cursor + 10));
    }

    string cursorRight(int k) {
        cursor = min((int)text.size(), cursor + k);
        return text.substr(max(0, cursor - 10), min(10, (int)text.size() - cursor + 10));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the length of the text and $k$ is the number of characters to delete or move the cursor.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the text.
> - **Why these complexities occur:** The time complexity occurs due to the string operations such as appending, deleting, and substring extraction. The space complexity occurs due to the storage of the text.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a doubly-linked list to store the text and a pointer to represent the cursor position.
- Detailed breakdown of the approach:
  1. Initialize a doubly-linked list to store the text and a pointer to represent the cursor position.
  2. For the `addText` operation, append the given text to the end of the doubly-linked list and move the cursor to the end of the list.
  3. For the `deleteText` operation, delete the specified number of nodes from the end of the doubly-linked list and update the cursor position accordingly.
  4. For the `cursorLeft` operation, move the cursor to the left by the specified number of nodes and return the last 10 characters of the list.
  5. For the `cursorRight` operation, move the cursor to the right by the specified number of nodes and return the last 10 characters of the list.
- Why further optimization is impossible: The doubly-linked list allows for efficient insertion and deletion of nodes, and the pointer allows for efficient movement of the cursor.

```cpp
class TextEditor {
public:
    struct Node {
        char data;
        Node* next;
        Node* prev;
    };

    Node* head;
    Node* cursor;

    TextEditor() {
        head = nullptr;
        cursor = nullptr;
    }

    void addText(string s) {
        Node* node = new Node();
        node->data = s[0];
        node->next = nullptr;
        node->prev = cursor;
        if (cursor) cursor->next = node;
        else head = node;
        cursor = node;
        for (int i = 1; i < s.size(); i++) {
            Node* newNode = new Node();
            newNode->data = s[i];
            newNode->next = nullptr;
            newNode->prev = cursor;
            cursor->next = newNode;
            cursor = newNode;
        }
    }

    int deleteText(int k) {
        int del = 0;
        while (cursor && k > 0) {
            Node* temp = cursor;
            cursor = cursor->prev;
            if (cursor) cursor->next = nullptr;
            else head = nullptr;
            delete temp;
            del++;
            k--;
        }
        return del;
    }

    string cursorLeft(int k) {
        while (cursor && k > 0) {
            cursor = cursor->prev;
            k--;
        }
        string res = "";
        Node* temp = cursor;
        for (int i = 0; i < 10 && temp; i++) {
            res += temp->data;
            temp = temp->prev;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    string cursorRight(int k) {
        while (cursor && cursor->next && k > 0) {
            cursor = cursor->next;
            k--;
        }
        string res = "";
        Node* temp = cursor;
        for (int i = 0; i < 10 && temp; i++) {
            res += temp->data;
            temp = temp->prev;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of characters to delete or move the cursor.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the text.
> - **Optimality proof:** The doubly-linked list allows for efficient insertion and deletion of nodes, and the pointer allows for efficient movement of the cursor. This results in a time complexity of $O(k)$, which is optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Doubly-linked lists, pointers, and string manipulation.
- Problem-solving patterns identified: Using a doubly-linked list to store the text and a pointer to represent the cursor position.
- Optimization techniques learned: Using a doubly-linked list to reduce the time complexity of insertion and deletion operations.
- Similar problems to practice: Implementing a stack or queue using a doubly-linked list, or solving problems that involve manipulating strings or linked lists.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as deleting more characters than the current text length, or moving the cursor beyond the text boundaries.
- Edge cases to watch for: Handling cases where the text is empty, or where the cursor is at the beginning or end of the text.
- Performance pitfalls: Using a singly-linked list instead of a doubly-linked list, which can result in a higher time complexity for insertion and deletion operations.
- Testing considerations: Testing the implementation with different input cases, such as adding and deleting text, and moving the cursor to different positions.