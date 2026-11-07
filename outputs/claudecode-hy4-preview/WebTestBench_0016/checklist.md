# Test Checklist

## Functionality
- [ ] FT-01: Home page highlights featured posts in a distinct section
  - Action: Open the home page and locate the "Featured" / "Featured Posts" section.
  - Expected: The section is present and contains at least one post, each with a title, a short description, and a working link.

- [ ] FT-02: Home page lists most recent posts in reverse-chronological order
  - Action: On the home page, locate the "Recent Posts" / "Latest" list and read the publication dates from top to bottom.
  - Expected: Multiple posts are listed with dates in newest-to-oldest order (no older post appears above a newer one).

- [ ] FT-03: Each listing entry shows a short preview that links to the full article
  - Action: On the home page (or any listing page), click a post's title or "Read more" link.
  - Expected: The listing displayed a 1–3 sentence excerpt per post, and clicking opens that post's full article page showing the complete body text.

- [ ] FT-04: Visitors can browse posts by topic/category
  - Action: Click a category link (e.g., "Travel", "Recipes", "Self-Improvement") in the navigation or on a post.
  - Expected: A listing page opens whose heading shows the selected category and which contains only posts assigned to it; every listed post displays that same category.

- [ ] FT-05: Visitors can browse posts by tag
  - Action: Click any tag link shown on a post or in the tag list.
  - Expected: A listing page opens showing only posts carrying that tag, and the selected tag is displayed on each result.

- [ ] FT-06: Visitors can browse posts by series
  - Action: Open the series navigation, select a series, then open one of its posts.
  - Expected: The series page lists all posts belonging to that series in sequence (e.g., Part 1, Part 2) with working links, and each article page indicates the series it belongs to.

- [ ] FT-07: Archive lets visitors browse posts by year and month
  - Action: Open the "Archive" page and select a month under a year (e.g., "March 2025").
  - Expected: Only posts published in that month and year are listed, each showing its publication date; months are grouped under their year.

- [ ] FT-08: Search by a single keyword returns matching posts
  - Action: Type one word that appears in an existing post's title or body into the search field and submit.
  - Expected: A results page lists the matching post(s) with title and preview linking to the full article; posts without that word are excluded.

- [ ] FT-09: Search by a multi-word phrase returns matching posts
  - Action: Enter an exact multi-word phrase taken from an existing post into the search field and submit.
  - Expected: The post containing that exact phrase appears in the results, and posts containing only one of the words are ranked below or excluded.

- [ ] FT-10: Visitors can post a comment on an article
  - Action: On an article page, fill in the comment form (name, email, comment text) and click "Post Comment" / "Submit".
  - Expected: The submitted comment appears in the article's comment list with the entered name, comment text, and a date; the form is cleared.

- [ ] FT-11: Visitors can "like" an article
  - Action: On an article page, click the "Like" reaction control and read the like count.
  - Expected: The like count increases by exactly 1 and the control switches to a liked/active state.

- [ ] FT-12: Article page suggests related posts
  - Action: Scroll to the bottom of an article page and inspect the "Related Posts" / "You may also like" section.
  - Expected: At least two different posts are suggested with title and link, the current post is not among them, and each link opens its own article page.

## Constraint
- [ ] CS-01: Search with no matches shows an explicit empty-state message
  - Action: Enter a nonsense term (e.g., "zzzqqqx") in the search field and submit.
  - Expected: A "No results" / "No posts found" message is displayed; the page is not blank, does not error, and does not list unrelated posts.

- [ ] CS-02: Empty required comment fields are rejected
  - Action: On an article page, click "Post Comment" / "Submit" with the name and comment fields left empty.
  - Expected: A validation message is shown, the comment is not added to the comment list, and the comment count is unchanged.

- [ ] CS-03: A like is counted only once per visitor
  - Action: On an article page, note the like count, click "Like", then click the like control two more times.
  - Expected: After the first click the count is original + 1; further clicks do not inflate the count (either it stays at +1 or returns to the original when toggled off).

## Interaction
- [ ] IX-01: Like control responds immediately without leaving the article
  - Action: Click the "Like" control on an article page and observe the control and page.
  - Expected: The control visually changes to the liked state right away, and the page does not navigate away or reload.

- [ ] IX-02: A submitted comment appears immediately and the form resets
  - Action: Submit a valid comment and observe the comment list and the form.
  - Expected: The new comment is added to the list without a full page reload, and all form fields return to empty.

## Content
- [ ] CT-01: All posts match the blog's stated themes
  - Action: Review titles and previews of posts on the home page, category pages, and article pages.
  - Expected: Every post belongs to travel stories, recipes, or self-improvement guides; no off-topic, dummy, or "Lorem ipsum" content is present.

- [ ] CT-02: Every post preview and article page shows complete, non-placeholder metadata
  - Action: Inspect three previews on listing pages and three article pages.
  - Expected: Each shows a non-empty title, author, publication date, and category/tag labels; no "Untitled", "Coming soon", or empty values are displayed.

- [ ] CT-03: All post images render and are relevant to their post
  - Action: Open the home page, a listing page, and two article pages; check every image/icon.
  - Expected: All images load without broken-image icons, and each image relates to its post's travel/recipe/self-improvement topic.