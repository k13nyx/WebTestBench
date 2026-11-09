I have all the data needed. Let me finalize the report.

# Test Result

## Functionality
- [X] FT-01: View featured and most recent posts on home page
  - Action: Open the home page and scroll to the top posts sections.
  - Expected: A "Featured" section and a "Recent Posts" section both display at least one post each.

- [X] FT-02: Open a full article from its preview
  - Action: From any post preview on the home, category, tag, or archive page, click the "Read more" / title link.
  - Expected: The corresponding full article page loads with the complete content.

- [X] FT-03: Browse posts by category
  - Action: Click a category link (e.g., "Travel", "Recipes", "Self-Improvement") from the navigation or a post.
  - Expected: A listing page shows all posts that belong to that category.

- [X] FT-04: Browse posts by tag
  - Action: Click a tag label shown on a post preview or article.
  - Expected: A listing page shows all posts that share that tag.

- [X] FT-05: Browse posts by series
  - Action: Click a series link from an article or navigation.
  - Expected: A listing page shows all posts that are part of that series, ordered.

- [X] FT-06: Browse archive by month and year
  - Action: Open the archive page and click a specific month-year entry.
  - Expected: A listing page shows all posts published in that month-year.

- [X] FT-07: Search posts by keyword or phrase
  - Action: Enter a keyword/phrase from a default post into the search box and submit.
  - Expected: Results page lists the matching posts (title or content match).

- [X] FT-08: Submit a comment on an article
  - Action: On an article page, fill in the comment form with a name and comment text, then submit.
  - Expected: The new comment appears in the comments list on that article.

- [X] FT-09: Like an article
  - Action: On an article page, click the "Like" button.
  - Expected: The like is registered and the like count increments by one.

- [X] FT-10: View related post suggestions on an article
  - Action: Open any article and scroll to the "Related Posts" area.
  - Expected: At least one related post is listed and links to another article.

## Constraint
- [ ] CS-01: Empty search query is rejected
  - Action: Submit the search box with no text or only whitespace.
  - Expected: Search does not run; user sees a validation message ("Please enter a search term" or similar), no results page.
  - Bug Report:
    - Issue: Missing Validation / Unrestricted Empty Search
    - Actual: Empty search silently runs without any validation. The /search page on first load shows "8 articles found" (all posts). When whitespace (" ") is entered and submitted, the URL changes to /search?q=+++ and the page shows "0 articles found for ' '" with "No articles found matching your criteria." No validation message or error toast is displayed. Expected: blocked submission with a "Please enter a search term" message.

- [X] CS-02: Comment form requires name and message
  - Action: Submit the comment form with the name field empty, or the comment field empty.
  - Expected: Submission is blocked and a required-field message is shown for the missing field.

- [X] CS-03: Archive lists only months/years that contain posts
  - Action: Open the archive page.
  - Expected: Every listed month-year has at least one post; clicking it returns one or more posts (no empty list).

- [X] CS-04: Like count cannot exceed one per user action
  - Action: Click the "Like" button twice in quick succession.
  - Expected: The count increases by one (not two) per legitimate action, OR the second click is ignored/detected as duplicate — never an uncontrolled double count.

## Interaction
- [X] IX-01: Successful comment submission shows confirmation
  - Action: Submit a valid comment.
  - Expected: A confirmation message/toast ("Comment posted", "Thank you") is shown and then clears; the comment appears in the list.

- [X] IX-02: Like button reflects updated state immediately
  - Action: Click "Like" on an article.
  - Expected: The like count and button state (e.g., filled/active icon) update without requiring a page reload.

- [X] IX-03: Related-post click navigates to that article
  - Action: Click a post in the "Related Posts" section of an article.
  - Expected: The browser navigates to that related article's full page.

## Content
- [X] CT-01: Post previews include title, excerpt, and link
  - Action: View the home, category, tag, series, or archive listing page.
  - Expected: Every preview card shows a title, a short excerpt, and a clickable link to the full article.

- [X] CT-02: Categories cover the three stated topics
  - Action: Inspect the categories list in navigation or archive.
  - Expected: Categories for "Travel", "Recipes", and "Self-Improvement" (or equivalent themed labels) are present, and default posts are filed under them.

- [X] CT-03: Search results match the entered keyword/phrase
  - Action: Enter a unique keyword from a default post's title or body and run the search.
  - Expected: The matching post appears in the results; non-matching posts are not shown for that unique keyword.