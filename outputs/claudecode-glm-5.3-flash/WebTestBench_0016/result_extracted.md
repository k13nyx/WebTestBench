# Test Result

## Functionality
- [X] FT-01: Home page displays a "Featured" posts section highlighting one or more designated posts
  - Action: Load the home page
  - Expected: A section labeled "Featured" (or similar) shows at least one post with its title and preview
- [X] FT-02: Home page displays a "Most Recent" posts section listing latest posts in reverse chronological order
  - Action: Load the home page and compare post dates
  - Expected: Posts are listed newest-first, and each shows a date
- [X] FT-03: Each post preview on the home page links to the full article
  - Action: Click a post title/preview on the home page
  - Expected: The full article page opens with the complete post content
- [X] FT-04: Visitors can browse posts by category/topic
  - Action: Click a category name (e.g., "Travel", "Recipes", "Self-Improvement") on the home page or a post
  - Expected: A filtered list appears showing only posts belonging to that category
- [X] FT-05: Visitors can browse posts by series
  - Action: Click a series name (e.g., "Southeast Asia" or "Meal Prep 101")
  - Expected: A list appears showing only posts in that series, ideally in reading order
- [X] FT-06: Visitors can browse posts by date via the archive
  - Action: Click a month/year entry in the archive (e.g., "October 2025")
  - Expected: A list appears showing only posts published in that month/year
- [X] FT-07: Search by a single keyword returns matching posts
  - Action: Enter a keyword that exists in a post (e.g., "ramen") into the search box and submit
  - Expected: Results list shows posts containing that keyword; non-matching posts are excluded
- [X] FT-08: Search by a full phrase returns matching posts
  - Action: Enter a multi-word phrase (e.g., "budget travel tips") and submit
  - Expected: Results show posts containing the phrase; posts without the exact phrase are not shown
- [X] FT-09: Article page displays a comment section where visitors can post a comment
  - Action: Open any article, fill in a comment (e.g., "Great article!") and required fields, then submit
  - Expected: The comment appears in the article's comment list with its text
- [X] FT-10: Article page supports a "like" reaction
  - Action: Click the like button on an article
  - Expected: The like count increases by 1 (e.g., from 0 to 1)
- [ ] FT-11: Article page displays related-post suggestions
  - Action: Open any article and scroll to the related posts area
  - Expected: At least 2 suggested posts are shown, each with a clickable link to its article
  - Bug Report:
    - Issue: Insufficient Related-Post Suggestions (corpus limitation)
    - Actual: The Travel article ("Sunrise Over Angkor Wat") shows 2 related posts (Bangkok, Ha Long Bay) as expected, but the recipe article "The Perfect Homemade Pasta" (/post/perfect-homemade-pasta) shows only 1 related post ("Classic Tiramisu: No-Bake Italian Perfection") in its "You might also enjoy" area — below the expected minimum of 2 suggestions.

## Constraint
- [X] CS-01: Search with no matching keyword shows an empty results state
  - Action: Search for a nonsense string (e.g., "xyzzy123q") and submit
  - Expected: A "no results" message is shown; no unrelated posts are displayed as results
- [X] CS-02: A comment cannot be submitted with empty content
  - Action: On an article, leave the comment field empty and click submit
  - Expected: Submission is blocked with a validation message; no empty comment appears in the list
- [X] CS-03: A single like cannot be double-counted
  - Action: Click the like button repeatedly on the same article
  - Expected: The count increases only once (or toggles), never incrementing by more than 1 per unique visitor
- [X] CS-04: The archive only lists month/year combinations that have published posts
  - Action: Check the archive entries on the home page
  - Expected: Every listed month/year has at least one post; no empty months are shown
- [X] CS-05: Category/series filtering shows only posts that belong to the selected topic
  - Action: Open a category filter and verify each listed post's displayed category
  - Expected: No posts outside the selected category appear in the filtered list

## Interaction
- [X] IX-01: Liking a post gives immediate visual feedback
  - Action: Click the like button on an article
  - Expected: The button changes state (e.g., highlighted/filled) and the count updates immediately without page reload
- [X] IX-02: Submitting a comment gives immediate feedback of success
  - Action: Submit a valid comment on an article
  - Expected: A confirmation message appears (or the new comment is highlighted/marked as posted) without a full page failure

## Content
- [X] CT-01: Default blog posts cover the three themes: travel stories, recipes, and self-improvement guides
  - Action: Browse the home page or category lists
  - Expected: Posts from all three themes exist with relevant titles and content (e.g., a travel story, a recipe with ingredients, a self-improvement guide)
- [X] CT-02: Each post preview shows a title, date, and a short excerpt
  - Action: Inspect the home page post previews
  - Expected: Every preview includes a title, publication date, and a short excerpt (not the full article body)
- [X] CT-03: Related posts are relevant to the current article's topic
  - Action: Open an article about a recipe and inspect its related posts
  - Expected: Suggested posts are related to the same theme (e.g., other recipes), not unrelated posts
