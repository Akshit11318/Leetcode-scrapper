## Web Crawler
**Problem Link:** https://leetcode.com/problems/web-crawler/description

**Problem Statement:**
- Given a `url`, a `HtmlParser`, and a `startUrl`, crawl all the pages and return all the urls that have the same domain as the `startUrl`.
- The `HtmlParser` interface has a method `getUrls(String url)` which returns a list of urls that are present in the given `url`.
- The `startUrl` is the url from which the crawling starts.
- The task is to return a list of all urls that are present in the same domain as the `startUrl`.
- Example test cases:
  - `startUrl = "http://news.yahoo.com/news/topics/"`, the output should be all the urls that have the domain "yahoo.com".
  - `startUrl = "https://www.example.com/"`, the output should be all the urls that have the domain "example.com".

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to start from the `startUrl` and crawl all the pages by following the links.
- We will use a `set` to keep track of the visited urls to avoid revisiting them.
- We will also use a `queue` to keep track of the urls that need to be crawled.

```cpp
class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        set<string> visited;
        queue<string> q;
        q.push(startUrl);
        visited.insert(startUrl);
        vector<string> res;
        
        while (!q.empty()) {
            string url = q.front();
            q.pop();
            if (getDomain(url) == getDomain(startUrl)) {
                res.push_back(url);
            }
            for (string nextUrl : htmlParser.getUrls(url)) {
                if (visited.find(nextUrl) == visited.end()) {
                    q.push(nextUrl);
                    visited.insert(nextUrl);
                }
            }
        }
        
        return res;
    }
    
    string getDomain(string url) {
        int start = url.find("://");
        start = url.find("/", start + 3);
        return url.substr(0, start);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$ where $N$ is the number of urls and $M$ is the average number of links in a url. This is because we are crawling all the pages and following all the links.
> - **Space Complexity:** $O(N)$ where $N$ is the number of urls. This is because we are storing all the visited urls in a `set`.
> - **Why these complexities occur:** These complexities occur because we are using a `set` to keep track of the visited urls and a `queue` to keep track of the urls that need to be crawled.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `set` to keep track of the visited urls and a `queue` to keep track of the urls that need to be crawled.
- We will also use a `domain` variable to store the domain of the `startUrl`.
- We will use a `getDomain` function to extract the domain from a given url.

```cpp
class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        set<string> visited;
        queue<string> q;
        q.push(startUrl);
        visited.insert(startUrl);
        vector<string> res;
        string domain = getDomain(startUrl);
        
        while (!q.empty()) {
            string url = q.front();
            q.pop();
            if (getDomain(url) == domain) {
                res.push_back(url);
            }
            for (string nextUrl : htmlParser.getUrls(url)) {
                if (visited.find(nextUrl) == visited.end() && getDomain(nextUrl) == domain) {
                    q.push(nextUrl);
                    visited.insert(nextUrl);
                }
            }
        }
        
        return res;
    }
    
    string getDomain(string url) {
        int start = url.find("://");
        start = url.find("/", start + 3);
        return url.substr(0, start);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$ where $N$ is the number of urls and $M$ is the average number of links in a url. This is because we are crawling all the pages and following all the links.
> - **Space Complexity:** $O(N)$ where $N$ is the number of urls. This is because we are storing all the visited urls in a `set`.
> - **Optimality proof:** This is the optimal solution because we are only crawling the pages that are in the same domain as the `startUrl`, which reduces the number of pages that need to be crawled.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: crawling, using a `set` to keep track of visited urls, using a `queue` to keep track of urls that need to be crawled.
- Problem-solving patterns identified: using a `getDomain` function to extract the domain from a given url.
- Optimization techniques learned: only crawling the pages that are in the same domain as the `startUrl`.
- Similar problems to practice: crawling a graph, finding all the connected components in a graph.

**Mistakes to Avoid:**
- Not using a `set` to keep track of visited urls, which can lead to revisiting the same url multiple times.
- Not using a `queue` to keep track of urls that need to be crawled, which can lead to missing some urls.
- Not using a `getDomain` function to extract the domain from a given url, which can lead to incorrect results.