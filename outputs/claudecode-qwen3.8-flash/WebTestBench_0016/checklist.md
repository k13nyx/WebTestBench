# Test Checklist

## Functionality
- [ ] FT-01: Home page highlights featured and most recent posts
  - Action: Open the home page
  - Expected: Distinct "Featured" and "Most Recent" (or equivalent) sections are visible, each listing posts

- [ ] FT-02: Each home page post shows a short preview linking to the full article
  - Action: On the home page, click a post's preview/title/"Read more" link
  - Expected: The browser navigates to that post's full article page, not just the excerpt

- [ ] FT-03: Visitors can browse posts by category (topic)
  - Action: From navigation, select the category "Recipes" (and one other category)
  - Expected: A listing page shows only posts assigned to that category

- [ ] FT-04: Visitors can browse posts by tag
  - Action: Click any tag shown on a post or tag listing
  - Expected: A page appears listing all posts that carry that tag

- [ ] FT-05: Visitors can browse posts by series
  - Action: Open a series page from a post or navigation
  - Expected: All posts belonging to that series are listed, in series order

- [ ] FT-06: Archive by month and year works
  - Action: Open the archive and select a month/year entry that has default posts
  - Expected: Posts are grouped by month/year, and selecting one shows only posts published in that period

- [ ] FT-07: Keyword search returns matching posts
  - Action: Enter a single keyword present in a default post's title or body (e.g., "pasta") and submit
  - Expected: Results page lists the post(s) containing that keyword

- [ ] FT-08: Phrase search returns matching posts
  - Action: Enter a multi-word phrase that appears verbatim in a default post and submit
  - Expected: Results include the post containing that exact phrase

- [ ] FT-09: Visitors can post a comment on an article
  - Action: On an article page, fill the comment form (name + text) and submit
  - Expected: The comment is saved and displayed in the comments list (on reload it persists)

- [ ] FT-10: Visitors can like a post
  - Action: On an article page, click the "Like" reaction button
  - Expected: The like count increases by exactly 1

- [ ] FT-11: Article pages show related-post suggestions
  - Action: Open any default article and scroll to the related posts section
  - Expected: At least one related post is suggested; clicking it opens that article

## Constraint
- [ ] CS-01: Empty/invalid comments are rejected
  - Action: Submit the comment form with the text (or required name) left blank
  - Expected: Comment is not added; a validation message indicates the required field

- [ ] CS-02: Search with no matches shows a clear no-results state
  - Action: Search for a nonsense string (e.g., "zzqqxx123")
  - Expected: Page shows a "no results found" message; no error page or blank screen

- [ ] CS-03: Duplicate likes are prevented
  - Action: Click the "Like" button twice in succession on the same article
  - Expected: Count does not increase twice (either blocked or toggled back to original state)

- [ ] CS-04: Category/tag/series listings contain no foreign posts
  - Action: On the "Travel" category page, inspect every listed post's metadata
  - Expected: No post from another category (e.g., "Recipes") appears in the list

## Interaction
- [ ] IX-01: Like button gives immediate visual feedback
  - Action: Click the Like button and observe it (before reload)
  - Expected: Button changes state (highlighted/filled icon, updated count) without a full page reload

- [ ] IX-02: Newly submitted comment appears without losing article context
  - Action: Submit a comment on an article
  - Expected: The comment renders in the list on the same page (or a confirmation message appears); user is not navigated away to a broken page

## Content
- [ ] CT-01: Default content covers all three instructed themes
  - Action: Browse the home page and category listings
  - Expected: Posts exist for travel stories, detailed recipes, and self-improvement guides; copy/images match each theme (no placeholder/lorem text)

- [ ] CT-02: Each article displays complete organizing metadata
  - Action: Open three different default articles
  - Expected: Each shows its category, tag(s), and publish date, and series name where applicable

- [ ] CT-03: Related-post suggestions are topically relevant
  - Action: Open a recipe article and inspect the related posts
  - Expected: Suggested posts share the article's category, tag, or series (not arbitrary posts)