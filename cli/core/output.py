def save_to_file(results, output_file):
    # Implement your save to file logic here
    print(f"Saving results to {output_file}")
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + '\n')