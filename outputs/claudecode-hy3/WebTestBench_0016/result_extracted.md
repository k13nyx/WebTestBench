# Test Result

## Functionality

- [ ] FT-01: Publish a new article
  - Action: Open the create/publish article screen; enter a title, body text, and select article type (Travel / Recipe / Self-improvement); click "Publish".
  - Expected: A new article is created and appears in the blog with a success confirmation shown.
  - Bug Report:
    - Issue: Missing Feature / No Authoring UI
    - Actual: No create/publish screen exists. There is no "Publish"/"New Post" link anywhere in the navigation or UI, and all candidate routes return a 404 ("Oops! Page not found"): /new, /write, /admin, /create, /publish.

- [ ] FT-02: Assign categories to an article
  - Action: When creating/editing an article, select one or more categories.
  - Expected: The article is associated with the selected categories and appears under them when browsing.
  - Bug Report:
    - Issue: Missing Feature / No Authoring UI
    - Actual: There is no create/edit article interface (see FT-01), so categories cannot be assigned to an article. Category browsing exists on the read side, but assignment is not possible.

- [ ] FT-03: Assign tags to an article
  - Action: Add one or more tags to an article.
  - Expected: The tags are saved, listed on the article, and the article is filterable by those tags.
  - Bug Report:
    - Issue: Missing Feature / No Authoring UI
    - Actual: No create/edit article interface exists, so tags cannot be added to articles. Tag filtering works on the read side, but assignment is not possible.

- [ ] FT-04: Assign a series to an article
  - Action: Assign the article to a series (select a series name).
  - Expected: The article is grouped under that series and shown in the series listing.
  - Bug Report:
    - Issue: Missing Feature / No Authoring UI
    - Actual: No create/edit article interface exists, so an article cannot be assigned to a series. Series listings work on the read side, but assignment is not possible.

- [X] FT-05: Browse articles by category/topic
  - Action: Click a category name/topic link from navigation or sidebar.
  - Expected: Only articles belonging to that category/topic are displayed.
  - (Verified: /category/travel shows only 3 Travel Stories articles, all correctly tagged Travel.)

- [X] FT-06: Browse articles by series
  - Action: Click a series name/link.
  - Expected: All articles in that series are listed.
  - (Verified: /series/southeast-asia-adventure lists all 3 articles of that series.)

- [ ] FT-07: Browse articles by date
  - Action: Select a date filter (e.g., a specific month/year).
  - Expected: Only articles published within that date range are shown.
  - Bug Report:
    - Issue: Missing Feature / No Date Filter Control
    - Actual: There is no interactive date-filter control. The Archive page (/archive) only statically groups posts under year/month headings (2024 > March/February/January) and the Search page offers only a keyword box and tag filters — no month/year selector. It is impossible to "select a date filter" to restrict to a specific range.

- [X] FT-08: Search articles by keyword or phrase
  - Action: Enter a keyword or phrase in the search box and submit.
  - Expected: Articles matching the keyword/phrase are returned; non-matching articles are excluded.
  - (Verified: searching "pasta" returns "1 article found for pasta" — only "The Perfect Homemade Pasta", all others excluded.)

- [X] FT-09: Home page highlights featured and most recent posts
  - Action: Open the home page.
  - Expected: A "Featured" section and a "Most Recent" section are both visible, each with post previews.
  - (Verified: Home page highlights featured posts in the top hero "Stories from the Heart" area with 2 post previews, and a clearly labeled "Recent Stories" section with 6 post previews. Note: the top hero is not literally titled "Featured", but it functions as the featured/highlighted area.)

- [X] FT-10: View archive grouped by month and year
  - Action: Open the archive view.
  - Expected: Posts are grouped and listed by month and year.
  - (Verified: /archive groups under "2024" → "March", "February", "January", each listing its posts with dates.)

- [X] FT-11: Post preview links to full article
  - Action: On home/archive/category view, click a post's preview or title.
  - Expected: The full article page for that post opens.
  - (Verified: Clicking the home-page preview for "Sunrise Over Angkor Wat" navigated to /post/sunrise-over-angkor-wat and opened the full article.)

- [X] FT-12: Submit a comment on an article
  - Action: On an article page, enter text in the comment box and click "Submit"/"Post Comment".
  - Expected: The comment is accepted and added to the article.
  - (Verified: Filling name + comment and clicking "Post Comment" showed "Comment posted!" and the comment count went from 2 to 3.)

- [X] FT-13: Like/react to an article
  - Action: On an article page, click the "Like" button.
  - Expected: The like/reaction count increases by one.
  - (Verified: Clicking the like button increased the count from 234 to 235 and showed "Thanks for the love!".)

## Constraint

- [ ] CS-01: Cannot publish with empty required fields
  - Action: Open the publish form; leave title or body empty; click "Publish".
  - Expected: Publish is blocked and an error indicates the required fields are missing.
  - Bug Report:
    - Issue: Missing Feature / No Publish Form
    - Actual: There is no publish form in the application (all authoring routes 404), so the empty-required-field validation cannot exist or be exercised.

- [X] CS-02: Cannot submit an empty comment
  - Action: On an article page, submit the comment form with empty text.
  - Expected: Submission is blocked and a validation message indicates comment text is required.
  - (Verified: Clicking "Post Comment" with both fields empty showed notification "Please fill in all fields" and the comment count remained unchanged.)

## Interaction

- [X] IX-01: Comment appears immediately after posting
  - Action: Submit a valid comment on an article page.
  - Expected: The new comment appears in the comment list without a full page reload.
  - (Verified: After posting, the new comment "QA Tester — Great article..." appeared in the list and the count became "Comments (3)" with no full-page reload; URL stayed /post/sunrise-over-angkor-wat.)

- [X] IX-02: Like updates count and state instantly
  - Action: Click the "Like" button on an article.
  - Expected: The reaction count and button visual state update immediately (no reload).
  - (Verified: Count updated 234 → 235 instantly, button became active, "Thanks for the love!" toast appeared, no reload.)

## Content

- [X] CT-01: Post previews show relevant content
  - Action: Inspect a post preview on home/archive/category views.
  - Expected: Each preview shows a relevant title, a short excerpt of the article, and a link to the full post.
  - (Verified: Every preview (home, category, archive, series) shows a title, a short excerpt paragraph, and is wrapped in a link to the full /post/... page.)

- [X] CT-02: Articles match declared themes
  - Action: Browse articles and review displayed content.
  - Expected: Articles reflect the declared themes (travel stories, recipes, self-improvement) and are on-topic.
  - (Verified: Travel posts describe trips (Angkor Wat, Bangkok, Ha Long Bay); Recipe posts describe dishes (Pasta, Tiramisu); Self-Improvement posts describe habits (5 AM Club, Digital Minimalism, Journaling) — all on-topic.)

- [X] CT-03: Archive/category/tag labels are correct
  - Action: Open archive, category, and tag listings.
  - Expected: Each listing shows correct names and the associated posts, with no mismatched or placeholder labels.
  - (Verified: Archive labeled "2024" with correct months; /category/travel shows "Travel Stories — 3 articles" with only travel posts; /search?tag=Italian shows '2 articles found tagged with "Italian"' with the two Italian recipe posts — all labels correct, no placeholders.)
