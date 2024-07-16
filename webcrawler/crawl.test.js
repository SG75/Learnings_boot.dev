import { test, expect } from "@jest/globals";
// import { normalizeURL } from "./crawl.js";

import { normalizeURL, getURLsFromHTML } from "./crawl.js";

test("normalizeURL removes the protocol and trailing slash", () => {
  expect(normalizeURL("https://blog.boot.dev/path/")).toBe(
    "blog.boot.dev/path"
  );
  expect(normalizeURL("https://blog.boot.dev/path")).toBe("blog.boot.dev/path");
  expect(normalizeURL("http://blog.boot.dev/path/")).toBe("blog.boot.dev/path");
  expect(normalizeURL("http://blog.boot.dev/path")).toBe("blog.boot.dev/path");
});

test("normalizeURL handles URLs without trailing slashes correctly", () => {
  expect(normalizeURL("https://blog.boot.dev/anotherpath")).toBe(
    "blog.boot.dev/anotherpath"
  );
  expect(normalizeURL("http://blog.boot.dev/anotherpath")).toBe(
    "blog.boot.dev/anotherpath"
  );
});

test("normalizeURL returns null for invalid URLs", () => {
  expect(normalizeURL("not a url")).toBeNull();
  expect(normalizeURL("htp://missing-t-in-http.com")).toBeNull();
  expect(normalizeURL("")).toBeNull();
});

test("normalizeURL works with complex paths", () => {
  expect(normalizeURL("https://blog.boot.dev/path/to/resource/")).toBe(
    "blog.boot.dev/path/to/resource"
  );
  expect(normalizeURL("http://blog.boot.dev/path/to/resource")).toBe(
    "blog.boot.dev/path/to/resource"
  );
});

test("normalizeURL works with query parameters and fragments", () => {
  expect(normalizeURL("https://blog.boot.dev/path/?query=1")).toBe(
    "blog.boot.dev/path"
  );
  expect(normalizeURL("http://blog.boot.dev/path/#fragment")).toBe(
    "blog.boot.dev/path"
  );
});

test("getURLsFromHTML absolute", () => {
  const inputURL = "https://blog.boot.dev";
  const inputBody =
    '<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>';
  const actual = getURLsFromHTML(inputBody, inputURL);
  const expected = ["https://blog.boot.dev/"];
  expect(actual).toEqual(expected);
});

test("getURLsFromHTML relative", () => {
  const inputURL = "https://blog.boot.dev";
  const inputBody =
    '<html><body><a href="/path/one"><span>Boot.dev></span></a></body></html>';
  const actual = getURLsFromHTML(inputBody, inputURL);
  const expected = ["https://blog.boot.dev/path/one"];
  expect(actual).toEqual(expected);
});

test("getURLsFromHTML both", () => {
  const inputURL = "https://blog.boot.dev";
  const inputBody =
    '<html><body><a href="/path/one"><span>Boot.dev></span></a><a href="https://other.com/path/one"><span>Boot.dev></span></a></body></html>';
  const actual = getURLsFromHTML(inputBody, inputURL);
  const expected = [
    "https://blog.boot.dev/path/one",
    "https://other.com/path/one",
  ];
  expect(actual).toEqual(expected);
});
