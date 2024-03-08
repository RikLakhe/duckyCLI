import argparse

from cli.core.output import save_to_file
from cli.core.search import search_function


def main():
    parser = argparse.ArgumentParser(description="CLI application that interacts with the DuckDuckGo Search API to "
                                                 "fetch relevant information based on user-provided parameters. The "
                                                 "application should output the results to the terminal and write "
                                                 "them to a file for future reference.")

    parser.add_argument("search_query", help="Specify the topic")
    parser.add_argument("--limit", type=int, default=10, help="Specify the limit for search results")
    parser.add_argument("--output-file", default="duckSearch_results.txt", help="Specify the output file path")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    search_query = args.search_query
    limit = args.limit
    output_file = args.output_file

    # Your script logic using the arguments
    search_results = search_function(search_query,limit)
    save_to_file(search_results,"./dump/"+output_file)


if __name__ == "__main__":
    main()
