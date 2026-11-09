# Test Checklist

## Functionality
- [ ] FT-01: Search articles by keyword or phrase
  - Action: Enter a search term into the search bar and press Enter or click the Search button.
  - Expected: Search results page displays only the articles containing the query in their title, summary, or body.
- [ ] FT-02: Browse articles by category
  - Action: Click on a category name (e.g., "Travel", "Recipes", or "Self-Improvement") in the navigation or post metadata.
  - Expected: Page navigates to the category listing displaying all articles assigned to that category.
- [ ] FT-03: Browse articles by series
  - Action: Click on a series title link from a post or the series menu.
  - Expected: Page displays the series overview listing all articles belonging to that series in sequential order.
- [ ] FT-04: Filter articles by date archive
  - Action: Select a specific month and year from the date archive list.
  - Expected: Page updates to display only articles published during the selected month and year.
- [ ] FT-05: Filter articles by tag
  - Action: Click on a tag link on any article card or article page.
  - Expected: Page loads a filtered list of all articles associated with that specific tag.
- [ ] FT-06: Navigate from post preview to full article
  - Action: Click the article title or "Read More" link on a home page post preview card.
  - Expected: Browser navigates directly to the full article page showing the complete content.
- [ ] FT-07: Submit a comment on an article
  - Action: Enter valid text into the comment form on an article page and click "Submit Comment".
  - Expected: Comment is submitted successfully and appears in the article's comment list.
- [ ] FT-08: Add a "Like" reaction to an article
  - Action: Click the "Like" button on an article page.
  - Expected: The like counter increments by 1.
- [ ] FT-09: Navigate via related-post suggestions
  - Action: Click on an article card in the "Related Posts" section at the bottom of an article.
  - Expected: Browser navigates to the selected related article page.

## Constraint
- [ ] CS-01: Prevent empty comment submission
  - Action: Click the "Submit Comment" button while the comment input field is blank.
  - Expected: Submission is blocked and a required field validation message is displayed.
- [ ] CS-02: Prevent duplicate "Like" reaction in the same session
  - Action: Click the "Like" button a second time on an already-liked article.
  - Expected: The like count does not increment further (or toggles off), preventing multiple likes from the same user.
- [ ] CS-03: Search query with no matching articles
  - Action: Enter a non-existent search term (e.g., "zzxxqq99") and submit the search.
  - Expected: Results page displays a clear "No articles found" message without crashing or displaying empty broken cards.

## Interaction
- [ ] IX-01: Post preview card hover state
  - Action: Hover the mouse cursor over a post card on the home page.
  - Expected: Card exhibits a visible interactive state change (such as elevation shadow, border highlight, or title color shift) and cursor changes to a pointer.
- [ ] IX-02: Visual toggle of the "Like" reaction button
  - Action: Click the "Like" button on an article page.
  - Expected: The like button icon immediately changes visual state (e.g., fills with color or highlights) to reflect the active liked state.

## Content
- [ ] CT-01: Home page featured posts display
  - Action: View the top section of the home page.
  - Expected: A designated "Featured Posts" section is clearly displayed highlighting selected spotlight articles.
- [ ] CT-02: Home page most recent posts feed
  - Action: Inspect the recent posts feed on the home page.
  - Expected: Articles are arranged in reverse chronological order, each showing a title, date, thumbnail, and a short text excerpt.
- [ ] CT-03: Archive navigation by month and year
  - Action: Locate the archive widget/section on the home page.
  - Expected: Archive lists distinct past months and years grouped with corresponding article counts.
- [ ] CT-04: Topic coverage for default blog content
  - Action: Inspect the default categories and published articles across the site.
  - Expected: Articles and taxonomy cover travel stories, detailed recipes, and self-improvement guides.
- [ ] CT-05: Article page layout and metadata completeness
  - Action: Open any single article page.
  - Expected: Page displays full body text, publication date, category, tags, series name (if applicable), reaction button, comments section, and related posts.