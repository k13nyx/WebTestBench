# Test Checklist

## Functionality
- [ ] FT-01: Publish a new article
  - Action: Open the create/publish article screen; enter a title, body text, and select article type (Travel / Recipe / Self-improvement); click "Publish".
  - Expected: A new article is created and appears in the blog with a success confirmation shown.

- [ ] FT-02: Assign categories to an article
  - Action: When creating/editing an article, select one or more categories.
  - Expected: The article is associated with the selected categories and appears under them when browsing.

- [ ] FT-03: Assign tags to an article
  - Action: Add one or more tags to an article.
  - Expected: The tags are saved, listed on the article, and the article is filterable by those tags.

- [ ] FT-04: Assign a series to an article
  - Action: Assign the article to a series (select a series name).
  - Expected: The article is grouped under that series and shown in the series listing.

- [ ] FT-05: Browse articles by category/topic
  - Action: Click a category name/topic link from navigation or sidebar.
  - Expected: Only articles belonging to that category/topic are displayed.

- [ ] FT-06: Browse articles by series
  - Action: Click a series name/link.
  - Expected: All articles in that series are listed.

- [ ] FT-07: Browse articles by date
  - Action: Select a date filter (e.g., a specific month/year).
  - Expected: Only articles published within that date range are shown.

- [ ] FT-08: Search articles by keyword or phrase
  - Action: Enter a keyword or phrase in the search box and submit.
  - Expected: Articles matching the keyword/phrase are returned; non-matching articles are excluded.

- [ ] FT-09: Home page highlights featured and most recent posts
  - Action: Open the home page.
  - Expected: A "Featured" section and a "Most Recent" section are both visible, each with post previews.

- [ ] FT-10: View archive grouped by month and year
  - Action: Open the archive view.
  - Expected: Posts are grouped and listed by month and year.

- [ ] FT-11: Post preview links to full article
  - Action: On home/archive/category view, click a post's preview or title.
  - Expected: The full article page for that post opens.

- [ ] FT-12: Submit a comment on an article
  - Action: On an article page, enter text in the comment box and click "Submit"/"Post Comment".
  - Expected: The comment is accepted and added to the article.

- [ ] FT-13: Like/react to an article
  - Action: On an article page, click the "Like" button.
  - Expected: The like/reaction count increases by one.

## Constraint
- [ ] CS-01: Cannot publish with empty required fields
  - Action: Open the publish form; leave title or body empty; click "Publish".
  - Expected: Publish is blocked and an error indicates the required fields are missing.

- [ ] CS-02: Cannot submit an empty comment
  - Action: On an article page, submit the comment form with empty text.
  - Expected: Submission is blocked and a validation message indicates comment text is required.

## Interaction
- [ ] IX-01: Comment appears immediately after posting
  - Action: Submit a valid comment on an article page.
  - Expected: The new comment appears in the comment list without a full page reload.

- [ ] IX-02: Like updates count and state instantly
  - Action: Click the "Like" button on an article.
  - Expected: The reaction count and button visual state update immediately (no reload).

## Content
- [ ] CT-01: Post previews show relevant content
  - Action: Inspect a post preview on home/archive/category views.
  - Expected: Each preview shows a relevant title, a short excerpt of the article, and a link to the full post.

- [ ] CT-02: Articles match declared themes
  - Action: Browse articles and review displayed content.
  - Expected: Articles reflect the declared themes (travel stories, recipes, self-improvement) and are on-topic.

- [ ] CT-03: Archive/category/tag labels are correct
  - Action: Open archive, category, and tag listings.
  - Expected: Each listing shows correct names and the associated posts, with no mismatched or placeholder labels.