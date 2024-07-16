// console.log("Maha Ganapathi");
import { crawlPage } from "./crawl.js";
import { printReport } from "./report.js";

function main() {
  // Get the command-line arguments, excluding the first two default arguments
  const args = process.argv.slice(2);

  // Check the number of arguments
  if (args.length < 1) {
    console.error("Error: Not enough arguments provided.");
    process.exit(1);
  } else if (args.length > 1) {
    console.error("Error: Too many arguments provided.");
    process.exit(1);
  }

  // If exactly one argument is provided, it's the baseURL
  const baseURL = args[0];
  //   console.log(`Crawler is starting at baseURL: ${baseURL}`);
  //   crawlPage(baseURL);
  crawlPage(baseURL)
    .then((pages) => {
      printReport(pages);
    })
    .catch((error) => {
      console.error("Error during crawling:", error);
    });
}

main();
