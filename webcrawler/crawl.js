import { JSDOM } from "jsdom";
import fetch from "node-fetch";

function normalizeURL(url) {
  try {
    // Ensure the URL starts with http or https
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      throw new Error("Invalid protocol");
    }

    // Create a URL object from the input URL string
    const urlObj = new URL(url);

    // Normalize the hostname by removing the protocol (http or https)
    const hostname = urlObj.hostname;

    // Normalize the pathname by ensuring it doesn't end with a slash
    let pathname = urlObj.pathname;
    if (pathname.endsWith("/")) {
      pathname = pathname.slice(0, -1);
    }

    // Construct the normalized URL
    const normalizedURL = `${hostname}${pathname}`;

    return normalizedURL;
  } catch (error) {
    // Handle invalid URLs
    console.error("Invalid URL:", url);
    return null;
  }
}

function getURLsFromHTML(html, baseURL) {
  const urls = [];
  const dom = new JSDOM(html);
  const anchors = dom.window.document.querySelectorAll("a");

  for (const anchor of anchors) {
    if (anchor.hasAttribute("href")) {
      let href = anchor.getAttribute("href");

      try {
        // convert any relative URLs to absolute URLs
        href = new URL(href, baseURL).href;
        urls.push(href);
      } catch (err) {
        console.log(`${err.message}: ${href}`);
      }
    }
  }

  return urls;
}

// async function crawlPage(currentURL) {
//   try {
//     const response = await fetch(currentURL);

//     // Check if the response status code is 400 or higher
//     if (!response.ok) {
//       console.error(`Error fetching page: ${response.status}`);
//       return;
//     }

//     // Check if the content-type header is not text/html
//     const contentType = response.headers.get("content-type");
//     if (!contentType || !contentType.includes("text/html")) {
//       console.error("Non HTML content-type:", contentType);
//       return;
//     }

//     // Print the HTML body as a string
//     const html = await response.text();
//     console.log(html);
//   } catch (error) {
//     console.error("Error fetching the URL:", error.message);
//   }
// }

async function fetchAndParse(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      console.error(`Error fetching page: ${response.status}`);
      return null;
    }
    const contentType = response.headers.get("content-type");
    if (!contentType || !contentType.includes("text/html")) {
      console.error("Non HTML content-type:", contentType);
      return null;
    }
    return await response.text();
  } catch (error) {
    console.error("Error fetching the URL:", error.message);
    return null;
  }
}

async function crawlPage(baseURL, currentURL = baseURL, pages = {}) {
  const baseDomain = new URL(baseURL).hostname;
  const currentDomain = new URL(currentURL).hostname;
  if (baseDomain !== currentDomain) {
    return pages;
  }
  const normalizedURL = normalizeURL(currentURL);
  if (pages[normalizedURL]) {
    pages[normalizedURL]++;
    return pages;
  }
  pages[normalizedURL] = 1;
  const html = await fetchAndParse(currentURL);
  if (!html) {
    return pages;
  }
  const urls = getURLsFromHTML(html, baseURL);
  for (const url of urls) {
    pages = await crawlPage(baseURL, url, pages);
  }
  return pages;
}

export { normalizeURL, getURLsFromHTML, crawlPage };
