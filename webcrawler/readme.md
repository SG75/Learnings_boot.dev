# Web Crawler

This is a Node.js application that crawls a given base URL, fetches HTML content, extracts URLs from it, and generates a report on the number of inbound links to each page.

## Features

- Crawls web pages starting from a base URL
- Normalizes URLs
- Extracts URLs from HTML content
- Recursively follows and processes links within the same domain
- Generates a report of pages sorted by the number of inbound links

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/webcrawler.git
    ```

2. Navigate to the project directory:

    ```bash
    cd webcrawler
    ```

3. Install the dependencies:

    ```bash
    npm install
    ```

## Usage

1. Run the crawler with a base URL:

    ```bash
    node main.js <baseURL>
    ```

    Replace `<baseURL>` with the URL you want to start crawling from.

2. Example:

    ```bash
    node main.js https://example.com
    ```

## Testing

The application includes tests for URL normalization and HTML parsing. To run the tests, use the following command:

```bash
npm test
