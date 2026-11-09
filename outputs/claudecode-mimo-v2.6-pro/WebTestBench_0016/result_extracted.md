# Test Result

## Functionality
- [ ] FT-01: Home page displays a featured posts section.
  - Action: Open the home page and locate the featured posts area.
  - Expected: A "Featured" section is visible listing at least one featured post by title.
  - Bug Report:
    - Issue: Missing Featured Posts Section (Missing Element)
    - Actual: No "Featured" section listing featured posts exists on the home page. The only heading containing "Featured" is "Featured Series", which lists series cards ("Southeast Asia Adventure", "Italian Kitchen Essentials", "Morning Rituals") rather than posts. The hero area lists two posts ("Sunrise Over Angkor Wat: A Journey Through Time", "The Perfect Homemade Pasta: A Labor of Love") under the heading "Stories from the Heart" with no "Featured" label anywhere in the DOM.

- [X] FT-02: Home page displays the most recent posts, newest first.
  - Action: View the recent posts section on the home page.
  - Expected: Posts are listed with publish dates sorted from newest to oldest.

- [X] FT-03: A post preview links to the full article.
  - Action: Click the title/preview of any post on the home page.
  - Expected: The full article page for that post opens, showing its complete content.

- [X] FT-04: Visitors can browse posts by category (topic).
  - Action: Click a category label (e.g., "Travel") on a post or in the navigation.
  - Expected: A listing page opens showing only posts in that category.

- [X] FT-05: Visitors can browse posts by tag.
  - Action: Click a tag label on a post.
  - Expected: A listing page opens showing only posts carrying that tag.

- [X] FT-06: Visitors can browse posts by series.
  - Action: Click a series name on a post or in the navigation.
  - Expected: A series page opens listing all posts of that series in part order.

- [ ] FT-07: Archive groups posts by month and year and supports browsing by date.
  - Action: Open the archive section, then click one month entry (e.g., "November 2026").
  - Expected: Archive entries are labeled by month and year; clicking an entry lists only posts published in that month.
  - Bug Report:
    - Issue: Non-Clickable Month Entries / Missing Month-and-Year Labels (Unresponsive Navigation)
    - Actual: The archive groups posts under a "2024" heading with plain month headings "March", "February", "January" — entries are labeled with the month name only (no "March 2024"-style month-and-year label). The month entries are non-clickable H3 text elements (cursor: auto, no href, no onclick, no link/button role anywhere for months), so clicking a month entry to list only that month's posts is impossible.

- [X] FT-08: Search works for both keywords and phrases.
  - Action: In the search box, submit a single keyword from an existing post title, then a multi-word phrase from an existing post's content.
  - Expected: In both cases the matching post appears in the search results.

- [ ] FT-09: Visitors can submit a comment on an article page.
  - Action: Open any article, enter text in the comment form, and submit it.
  - Expected: The comment is accepted and appears in the article's comment list (still present after page reload).
  - Bug Report:
    - Issue: Comment Not Persisted Across Page Reload (Data Loss)
    - Actual: The comment is accepted and appears immediately ("Comments (3)" containing "QA test comment - what a beautiful sunrise story!" from "QA Tester"), but after a page reload the list resets to "Comments (2)" and the submitted comment and author name are no longer present.

- [X] FT-10: Visitors can like a post.
  - Action: Click the "Like" button on an article page.
  - Expected: The like count for that post increases by exactly one.

- [X] FT-11: Article pages suggest related posts.
  - Action: Open an article page and view the "Related Posts" section.
  - Expected: At least one other post is suggested, and clicking it opens its full article page.

## Constraint
- [X] CS-01: An empty comment cannot be submitted.
  - Action: Click the submit button on the comment form with the comment field left blank.
  - Expected: Submission is blocked with a validation message; no empty comment is added to the list.

- [X] CS-02: A search with no matches must not return unrelated posts.
  - Action: Search for a random non-existent string (e.g., "zzzqqqxyz123").
  - Expected: A "no results" message is shown and no posts are listed.

- [X] CS-03: A visitor cannot like the same post more than once.
  - Action: Click the "Like" button twice in a row on the same article.
  - Expected: The count never reflects two likes from one visitor (second click unlikes or is ignored).

## Interaction
- [X] IX-01: Comment submission gives immediate visual confirmation.
  - Action: Submit a valid comment on an article page.
  - Expected: A success confirmation (message or toast) is displayed and the comment list updates without a page reload.

- [X] IX-02: The Like button changes visual state when clicked.
  - Action: Click the "Like" button on an article page.
  - Expected: The button immediately switches to an active/liked appearance (e.g., filled or highlighted icon).

## Content
- [X] CT-01: Each post preview shows title, short excerpt, and publish date.
  - Action: Inspect any post preview on the home page or a listing page.
  - Expected: The preview displays the post title, a short excerpt from the article, and its publish date.

- [X] CT-02: The article page shows complete post information.
  - Action: Open any full article page.
  - Expected: It shows the title, publish date, full body content, and the post's category, tags, and series labels.

- [X] CT-03: Related-post suggestions are topically relevant.
  - Action: Compare each suggested related post with the currently open article.
  - Expected: Every suggested post shares at least one category, tag, or series with the current article.

- [X] CT-04: All displayed content matches the blog's themes.
  - Action: Review posts across featured, recent, and category listings.
  - Expected: All posts are travel stories, recipes, or self-improvement guides; no off-topic content appears.
