# LeetCode Problem Analyzer CLI

```
  _                  _      _____                                             
 | |                | |    / ____|                                            
 | |      ___   ___ | |_  | (___    ___  _ __  __ _  _ __   _ __    ___  _ __ 
 | |     / _ \ / _ \| __|  \___ \  / __|| '__|/ _` || '_ \ | '_ \  / _ \| '__|
 | |____|  __/|  __/| |_   ____) || (__ | |  | (_| || |_) || |_) ||  __/| |   
 |______|\___| \___| \__| |_____/  \___||_|   \__,_|| .__/ | .__/  \___||_|   
                                                   | |    | |                
                                                   |_|    |_| 
```

Welcome to the **LeetCode Problem Analyzer CLI**! This tool helps you analyze LeetCode problems programmatically and generates insightful notes for problem-solving.

---

## 🚀 Features

- **Problem Range Selection**: Process problems by specifying a range (e.g., `1-100`).
- **Custom Model Support**: Use different models for analysis (default: `llama-3.3-70b-versatile`).
- **Output Directory**: Save generated notes to a specific folder (default: `./notes`).
- **Sleep Customization**: Set delay between problem analysis requests to prevent rate-limiting.
- **Logging**: Track progress and errors during execution.

---

## 🛠️ Usage

### Prerequisites
- Python 3.8+
- Required packages: `argparse`, `pathlib`, `logging`, and others as per `requirements.txt`.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/leetcode-analyzer-cli.git
   cd leetcode-analyzer-cli
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Command-Line Options
```
Usage:
  python app.py --range <RANGE> --api-key <API_KEY> [OPTIONS]

Required Arguments:
  --range RANGE            Specify the range of problems (e.g., 1-100).
  --api-key API_KEY        Your API key for accessing the Groq API.

Optional Arguments:
  --output-dir OUTPUT_DIR  Directory to save the output (default: ./notes).
  --model MODEL            Specify the model to use (default: llama-3.3-70b-versatile).
  --sleep SLEEP            Delay between requests in seconds (default: 30). Use -1 for no sleep.
```

#### Example
Run the application for problems `1-10` using your API key:
```bash
python app.py --range 1-10 --api-key YOUR_API_KEY --output-dir ./results
```

---

## 📂 Directory Structure
```
leetcode-scrapper/
├── app.py               # Main application file
├── leetcode_analyzer.py # Analyzer logic (imported in app.py)
├── notes/               # Default output directory
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 👨‍💻 Authors

- **Akshit** ([akshit11318](https://github.com/akshit11318))
- **Rohan** ([roh4n-code](https://github.com/roh4n-code))

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ❤️ Contributions

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a Pull Request.

---

## 🔗 Links

- [LeetCode](https://leetcode.com/)
- [GitHub Repository](https://github.com/akshit11318/leetcode-scrapper)
