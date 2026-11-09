# Test Checklist

## Functionality
- [ ] FT-01: Browse posts by category (topic)
  - Action: From the home page or navigation, select a category (e.g., "Travel").
  - Expected: A listing page opens showing only posts in that category, and each listed post can be opened.
- [ ] FT-02: Browse posts by tag
  - Action: On a post or tag cloud/list, click a tag (e.g., "recipes").
  - Expected: A page opens showing all posts carrying that tag, and each listed post can be opened.
- [ ] FT-03: Browse posts by series
  - Action: Select a series from the site navigation or a post's series indicator.
  - Expected: A page opens listing the posts belonging to that series in order, and each post can be opened.
- [ ] FT-04: Browse posts via archive by month and year
  - Action: In the archive, click a specific month/year entry (e.g., "March 2026").
  - Expected: A page opens listing posts published in that month, and each post can be opened.
- [ ] FT-05: Search posts by keyword
  - Action: Enter a single keyword present in a known post (e.g., "pasta") into the search box and submit.
  - Expected: A results page opens listing posts containing that keyword, and selecting a result opens the full article.
- [ ] FT-06: Search posts by phrase
  - Action: Enter an exact multi-word phrase from a known post (e.g., "slow morning routine") into the search box and submit.
  - Expected: Results include posts containing that phrase, and selecting a result opens the full article.
- [ ] FT-07: Open full article from a post preview
  - Action: On the home page, click the title/"read more" link of any post preview.
  - Expected: The full article page for that post opens with the complete content.
- [ ] FT-08: Submit a comment on an article
  - Action: On an article page, enter comment text in the comment form and submit it.
  - Expected: The comment is accepted and displayed in the article's comment list.
- [ ] FT-09: Like an article
  - Action: On an article page, click the like control.
  - Expected: The like is registered and the displayed like count reflects the like.
- [ ] FT-10: Navigate to a related post
  - Action: On an article page, click one of the suggested related posts.
  - Expected: The clicked related article opens in full.

## Constraint
- [ ] CS-01: Comment cannot be submitted empty
  - Action: Leave the comment box empty (or spaces only) and attempt to submit.
  - Expected: Submission is blocked with a validation message, and no empty comment appears in the list.
- [ ] CS-02: Filtered and search views contain only matching posts
  - Action: Open a category, tag, series, or archive view, and run a keyword search; inspect the listed items.
  - Expected: Every listed post matches the selected category/tag/series/month or search query; no unrelated post appears.
- [ ] CS-03: Repeated like clicks do not inflate the count
  - Action: Click the like control on the same article multiple times in one visit.
  - Expected: The count increases by at most 1 for the visit, regardless of how many times it is clicked.

## Interaction
- [ ] IX-01: Like control gives immediate feedback
  - Action: Click the like control on an article page.
  - Expected: The like count/button state updates immediately after the click, without needing a manual page refresh.
- [ ] IX-02: Post previews show clickable affordance on hover
  - Action: Hover over a post preview's title or "read more" link on the home page.
  - Expected: A visible hover state (e.g., highlight/underline) indicates the element is clickable and leads to the full article.

## Content
- [ ] CT-01: Home page shows featured and most recent posts
  - Action: Open the home page.
  - Expected: A "Featured" section and a "Most Recent"/latest-posts section are both present and populated with posts.
- [ ] CT-02: Each post preview contains complete preview information
  - Action: Inspect any post preview card on the home page or listing pages.
  - Expected: It shows the post title, a short excerpt, the publication date, its category, and a link to the full article.
- [ ] CT-03: Article page shows full content and organizing metadata
  - Action: Open any full article.
  - Expected: The full body content is displayed along with title, publication date, category, tags, and series (if part of one).
- [ ] CT-04: Related-post suggestions are present and relevant
  - Action: Scroll to the related-posts area of an article page.
  - Expected: Suggestions are shown, and each relates to the current article's topic/category/tag/series.
- [ ] CT-05: Content matches the blog's themes
  - Action: Browse home page, category listings, and several articles across categories.
  - Expected: Posts cover the three themes — travel stories, recipes, and self-improvement guides — and any images shown are relevant to their post's topic.