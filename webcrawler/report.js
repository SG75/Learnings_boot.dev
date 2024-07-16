// Function to sort pages by the number of inbound links
function sortPagesByInboundLinks(pages) {
  // Convert pages object to an array of [url, count] pairs
  const pageEntries = Object.entries(pages);
  // Sort the array by the count in descending order
  pageEntries.sort((a, b) => b[1] - a[1]);
  return pageEntries;
}

// Function to print the report
function printReport(pages) {
  console.log("Report starting...");

  // Sort pages
  const sortedPages = sortPagesByInboundLinks(pages);

  // Print each page in a formatted way
  for (const [url, count] of sortedPages) {
    console.log(`Found ${count} internal links to ${url}`);
  }
}

export { printReport };
