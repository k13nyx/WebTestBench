# Test Checklist

## Functionality
- [ ] FT-01: Home page highlights featured and most recent posts
  - Action: Open the blog home page and inspect the "Featured" section and the "Recent Posts" section.
  - Expected: Both sections are visible and each lists at least one post with title and preview text; featured posts are visually distinguished from recent posts.

- [ ] FT-02: Each post preview links to the full article
  - Action: On the home page (or any post list), click a post's title or "Read more" link shown under its short preview.
  - Expected: The browser navigates to that post's dedicated article page displaying the full post content, not just the preview.

- [ ] FT-03: Visitor can browse posts by category (topic)
  - Action: Click a category link (e.g., "Recipes") from the navigation menu or a post's category label.
  - Expected: A category listing page opens showing all posts assigned to that category, each with title and preview.

- [ ] FT-04: Visitor can browse posts by series
  - Action: Click a series link (e.g., "Europe Trip 2025") shown on a post or in navigation.
  - Expected: A series page opens listing all posts in that series, ordered logically (e.g., by part number or publish date).

- [ ] FT-05: Visitor can browse the archive by month and year
  - Action: Open the archive page and click a specific month/year entry (e.g., "October 2026").
  - Expected: The archive view lists exactly the posts published in that month/year, each linking to its full article.

- [ ] FT-06: Visitor can search posts by keyword
  - Action: Type a keyword that exists in post content (e.g., "pasta") into the search box and press Enter or click the search button.
  - Expected: A search results page opens listing every post containing that keyword, each result linking to the full article.

- [ ] FT-07: Visitor can search posts by an exact phrase
  - Action: Type a multi-word phrase from an article (e.g., "morning routine") into the search box and submit.
  - Expected: Results include posts containing that exact phrase; posts containing only one of the words but not the phrase are not presented as phrase matches.

- [ ] FT-08: Visitor can submit a comment on an article
  - Action: Open any article page, fill in the comment form (name, email, comment text) with valid data, and click the "Post Comment"/"Submit" button.
  - Expected: The comment is successfully saved and displayed in the article's comment section.

- [ ] FT-09: Visitor can like an article
  - Action: Open any article page and click the "Like" button/reaction control.
  - Expected: The like is recorded; the button reflects the visitor's liked state (e.g., filled/highlighted) after the action.

- [ ] FT-10: Article page shows related-post suggestions
  - Action: Open any article page and locate the "Related Posts" / "You might also like" section.
  - Expected: At least one other post is suggested via a clickable link that navigates to that article, with suggestions sharing the article's category, tags, or series.

- [ ] FT-11: Every post is organized with category, tags, and series metadata
  - Action: Open several articles and inspect their metadata labels.
  - Expected: Each post displays at least one category and one or more tags as clickable links; series is shown when the post belongs to one.

## Constraint
- [ ] CS-01: Comment cannot be submitted with empty required fields
  - Action: On an article page, leave the comment text (or name) field empty and click "Post Comment".
  - Expected: The comment is not submitted; a validation message (e.g., "Comment cannot be empty") is shown and no empty comment appears in the comment list.

- [ ] CS-02: Search with no matching results shows a graceful empty state
  - Action: Search for a nonsense string (e.g., "zzqxv123") in the search box.
  - Expected: A results page or message stating "No results found" is displayed; the page does not crash, and no unrelated posts are listed.

- [ ] CS-03: Empty search query returns no arbitrary results
  - Action: Leave the search box empty and press Enter or click the search button.
  - Expected: No search is executed (or all-posts listing is shown with a prompt to enter a keyword); random or incorrect filtering does not occur.

- [ ] CS-04: Category listing contains only posts of that category
  - Action: Open a category page (e.g., "Travel") and check every listed post's category label.
  - Expected: All listed posts carry that category; no posts from other categories (e.g., Recipes) appear in the list.

## Interaction
- [ ] IX-01: Like count increments immediately upon clicking "Like"
  - Action: Note the current like count on an article, click "Like", and observe the counter.
  - Expected: The displayed like count increases by exactly 1 without a full page reload.

- [ ] IX-02: Newly submitted comment appears in the comment list immediately
  - Action: Submit a valid comment on an article and observe the comment section.
  - Expected: The new comment (with entered name/text and submission timestamp) appears at the top/bottom of the comment list without needing a manual page refresh.

- [ ] IX-03: Archive month/year navigation updates the post list
  - Action: On the archive page, click one month/year entry, then a different one.
  - Expected: The post list updates each time to reflect only the newly selected month/year, with the selected period indicated as active.

## Content
- [ ] CT-01: All blog content matches the stated themes: travel stories, recipes, self-improvement
  - Action: Review the posts on the home page, category pages, and archive listings.
  - Expected: Every post title, preview, and full article relates to travel, recipes/cooking, or self-improvement; no off-topic placeholder content (e.g., lorem ipsum or unrelated sample posts) exists.

- [ ] CT-02: Preview text is a genuine short excerpt of the full article
  - Action: Compare a post's preview on the home/list page with the beginning of its full article page.
  - Expected: The preview corresponds to the same article (correct title and matching content excerpt), not a mismatched or generic blurb.

- [ ] CT-03: Archive month/year entries match actual post publish dates
  - Action: Open an article, note its publish date, and verify the corresponding month/year entry in the archive contains that article.
  - Expected: Every published article appears under the archive entry matching its displayed publish date, and no archive entry lists posts from a different month/year.