import sys
import json
import csv
import requests

if len(sys.argv) < 2:
    print("Error: Input file not provided.")
    sys.exit(1)

input_file = sys.argv[1]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    with open(input_file, 'r') as input_file_handle:
        reader = csv.DictReader(input_file_handle)

        with open('output.csv', 'w', newline='') as output_file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            with open('errors.log', 'w') as errors_file:
                for row in reader:
                    url = row['url']

                    try:
                        response = requests.head(url,
                                                 headers=headers,
                                                 timeout=5,
                                                 allow_redirects=True)
                        if response.status_code == 200:
                            writer.writerow(row)
                        else:
                            error_msg = f"Error for URL {url}: Status Code {response.status_code}"
                            errors_file.write(json.dumps({"url": url,
                                                          "status_code": response.status_code,
                                                          "error_msg": error_msg}) + "\n")
                    except (requests.exceptions.RequestException,
                            ValueError) as e:
                        error_msg = f"Error for URL {url}: {str(e)}"
                        errors_file.write(json.dumps({"url": url,
                                                      "status_code": "999",
                                                      "error_msg": error_msg}) + "\n")

    print("Done! Output written to output.csv and errors logged to errors.log")
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)
