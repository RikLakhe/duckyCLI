## Project Name: DuckSearch CLI

## Description:
Create a CLI application in Python that interacts with the DuckDuckGo Search API to fetch relevant information based on user-provided parameters. The application should output the results to the terminal and write them to a file for future reference.

### Features:
- Search Functionality: 
  - Accept a search query as a command-line argument. 
  - Use the DuckDuckGo Search API to fetch relevant data for the provided query.
- Output to Terminal:
  - Display the search results in the terminal in a readable format.
- Write to File:
  - Allow the user to specify a filename to write the search results to a text file. 
  - If no filename is provided, use a default filename (e.g., duckSearch_results.txt).
- User-Friendly CLI Interface:
  - Implement a user-friendly CLI interface with clear instructions. 
  - Provide help messages and usage instructions.
- Error Handling:
  - Implement error handling to manage API request failures, invalid input, or other potential issues gracefully. 
  - Display meaningful error messages to the user.
- Code Organization:
  - Organize the code into modular functions and classes for readability and maintainability. 
  - Use a virtual environment to manage dependencies.
- Documentation:
  - Include inline comments for important code segments. 
  - Write a README file explaining how to set up the project, run the application, and any other relevant information.
- Dependencies:
  - requests: Use the requests library to make HTTP requests to the DuckDuckGo Search API.

##### Additional Considerations:
- Respect the DuckDuckGo API usage policies and guidelines.
- Provide clear instructions in the README on how to obtain an API key if needed.

##### Example Usage:
```bash
# Basic Search
python cli/main.py "Python programming"
```

```bash
# Search and Write to File
python cli/main.py "Python programming" --output-file resulttest.txt
```

```bash
# Display Help
python cli/main.py --help
```