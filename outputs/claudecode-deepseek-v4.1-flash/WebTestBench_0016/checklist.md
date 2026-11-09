# Test Checklist

## Functionality
- [ ] FT-01: Visitors can browse posts filtered by category.
  - Action: Click a category link (e.g., "Travel") in the category list.
  - Expected: Only posts assigned to that category are listed.
- [ ] FT-02: Visitors can browse posts filtered by tag.
  - Action: Click a tag link (e.g., "Recipes") on a post or tag list.
  - Expected: Only posts carrying that tag are listed.
- [ ] FT-03: Visitors can browse posts grouped by series.
  - Action: Click a series name/link.
  - Expected: All posts belonging to that series are listed in the intended reading order.
- [ ] FT-04: Visitors can browse posts by date using the archive.
  - Action: Click a month/year entry in the archive (e.g., "October 2026").
  - Expected: Only posts published in that month and year are listed.
- [ ] FT-05: Visitors can search by keyword or phrase.
  - Action: Enter a keyword/phrase in the search field and submit.
  - Expected: Posts whose title or body match the query are listed.
- [ ] FT-06: Home page highlights featured posts.
  - Action: Load the home page.
  - Expected: A clearly labeled "Featured" area displays featured posts.
- [ ] FT-07: Home page shows the most recent posts.
  - Action: Load the home page.
  - Expected: A "Recent" area lists posts ordered newest first.
- [ ] FT-08: Each preview links to its full article.
  - Action: Click a post title or "Read more" link on any preview.
  - Expected: The full article page for that post opens.
- [ ] FT-09: Visitors can submit a comment on an article.
  - Action: Enter a comment on an article page and submit.
  - Expected: The comment appears in the article's comment list.
- [ ] FT-10: Visitors can like an article.
  - Action: Click the "Like" control on an article page.
  - Expected: The like is registered and the count reflects the action.
- [ ] FT-11: Article pages show related-post suggestions.
  - Action: Open any article page and scroll to the suggestions.
  - Expected: A "Related posts" section lists links to other posts.

## Constraint
- [ ] CS-01: Comments cannot be submitted empty.
  - Action: Submit the comment form with no text entered.
  - Expected: Submission is blocked with a validation message; no empty comment is added.
- [ ] CS-02: Search handles queries with no matches gracefully.
  - Action: Search for a random string (e.g., "zxqw123").
  - Expected: A "no results found" message is shown; no posts are listed.
- [ ] CS-03: A like cannot be duplicated by repeated clicks.
  - Action: Click "Like" multiple times on the same article.
  - Expected: The like is only counted once (or toggles off/on consistently), never inflating the count.

## Interaction
- [ ] IX-01: Confirmation feedback appears after a comment is submitted.
  - Action: Submit a valid comment.
  - Expected: A success message (e.g., toast/notice) is displayed.
- [ ] IX-02: Like control reflects its active state visually.
  - Action: Click "Like" on an article.
  - Expected: The control visibly changes state (e.g., filled icon/color) and the count updates immediately.

## Content
- [ ] CT-01: Article content matches the blog's theme.
  - Action: Review the default posts on the home/listing pages.
  - Expected: All posts are about travel stories, recipes, or self-improvement guides.
- [ ] CT-02: Every post preview shows a short excerpt.
  - Action: Review post previews on the home/listing pages.
  - Expected: Each preview displays a brief summary of the article, not the full text or empty space.
- [ ] CT-03: Archive entries are labeled with month and year.
  - Action: Review the archive section on the home page.
  - Expected: Each archive link shows a valid month name and year (e.g., "October 2026").
- [ ] CT-04: Related-post suggestions are relevant to the open article.
  - Action: Open an article and review the "Related posts" section.
  - Expected: Suggested posts share a topic, category, tag, or series with the current article.