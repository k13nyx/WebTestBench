# Test Checklist

## Functionality
- [ ] FT-01: Home page displays a featured posts section.
  - Action: Open the home page and locate the featured posts area.
  - Expected: A "Featured" section is visible listing at least one featured post by title.

- [ ] FT-02: Home page displays the most recent posts, newest first.
  - Action: View the recent posts section on the home page.
  - Expected: Posts are listed with publish dates sorted from newest to oldest.

- [ ] FT-03: A post preview links to the full article.
  - Action: Click the title/preview of any post on the home page.
  - Expected: The full article page for that post opens, showing its complete content.

- [ ] FT-04: Visitors can browse posts by category (topic).
  - Action: Click a category label (e.g., "Travel") on a post or in the navigation.
  - Expected: A listing page opens showing only posts in that category.

- [ ] FT-05: Visitors can browse posts by tag.
  - Action: Click a tag label on a post.
  - Expected: A listing page opens showing only posts carrying that tag.

- [ ] FT-06: Visitors can browse posts by series.
  - Action: Click a series name on a post or in the navigation.
  - Expected: A series page opens listing all posts of that series in part order.

- [ ] FT-07: Archive groups posts by month and year and supports browsing by date.
  - Action: Open the archive section, then click one month entry (e.g., "November 2026").
  - Expected: Archive entries are labeled by month and year; clicking an entry lists only posts published in that month.

- [ ] FT-08: Search works for both keywords and phrases.
  - Action: In the search box, submit a single keyword from an existing post title, then a multi-word phrase from an existing post's content.
  - Expected: In both cases the matching post appears in the search results.

- [ ] FT-09: Visitors can submit a comment on an article page.
  - Action: Open any article, enter text in the comment form, and submit it.
  - Expected: The comment is accepted and appears in the article's comment list (still present after page reload).

- [ ] FT-10: Visitors can like a post.
  - Action: Click the "Like" button on an article page.
  - Expected: The like count for that post increases by exactly one.

- [ ] FT-11: Article pages suggest related posts.
  - Action: Open an article page and view the "Related Posts" section.
  - Expected: At least one other post is suggested, and clicking it opens its full article page.

## Constraint
- [ ] CS-01: An empty comment cannot be submitted.
  - Action: Click the submit button on the comment form with the comment field left blank.
  - Expected: Submission is blocked with a validation message; no empty comment is added to the list.

- [ ] CS-02: A search with no matches must not return unrelated posts.
  - Action: Search for a random non-existent string (e.g., "zzzqqqxyz123").
  - Expected: A "no results" message is shown and no posts are listed.

- [ ] CS-03: A visitor cannot like the same post more than once.
  - Action: Click the "Like" button twice in a row on the same article.
  - Expected: The count never reflects two likes from one visitor (second click unlikes or is ignored).

## Interaction
- [ ] IX-01: Comment submission gives immediate visual confirmation.
  - Action: Submit a valid comment on an article page.
  - Expected: A success confirmation (message or toast) is displayed and the comment list updates without a page reload.

- [ ] IX-02: The Like button changes visual state when clicked.
  - Action: Click the "Like" button on an article page.
  - Expected: The button immediately switches to an active/liked appearance (e.g., filled or highlighted icon).

## Content
- [ ] CT-01: Each post preview shows title, short excerpt, and publish date.
  - Action: Inspect any post preview on the home page or a listing page.
  - Expected: The preview displays the post title, a short excerpt from the article, and its publish date.

- [ ] CT-02: The article page shows complete post information.
  - Action: Open any full article page.
  - Expected: It shows the title, publish date, full body content, and the post's category, tags, and series labels.

- [ ] CT-03: Related-post suggestions are topically relevant.
  - Action: Compare each suggested related post with the currently open article.
  - Expected: Every suggested post shares at least one category, tag, or series with the current article.

- [ ] CT-04: All displayed content matches the blog's themes.
  - Action: Review posts across featured, recent, and category listings.
  - Expected: All posts are travel stories, recipes, or self-improvement guides; no off-topic content appears.