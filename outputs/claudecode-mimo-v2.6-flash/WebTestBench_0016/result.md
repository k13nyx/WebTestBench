All checklist items have been executed. Here are the complete test results:

# Test Result

## Functionality
- [X] FT-01: Browse posts by category (topic)
  - Action: From the home page or navigation, select a category (e.g., "Travel").
  - Expected: A listing page opens showing only posts in that category, and each listed post can be opened.
  - Actual: Clicked "Travel Stories" in nav → /category/travel showed "3 articles", all ✈️ Travel Stories (Sunrise Over Angkor Wat, Street Food Adventures in Bangkok, Ha Long Bay by Kayak); clicking a listed post opened its full article.

- [X] FT-02: Browse posts by tag
  - Action: On a post or tag cloud/list, click a tag (e.g., "recipes").
  - Expected: A page opens showing all posts carrying that tag, and each listed post can be opened.
  - Actual: Clicked "#Thailand" on an article → /search?tag=Thailand showed '1 article found tagged with "Thailand"' (Street Food Adventures in Bangkok), listed as a link to the full post. Home tag cloud also provides tag links (e.g., "Southeast Asia (3)").

- [X] FT-03: Browse posts by series
  - Action: Select a series from the site navigation or a post's series indicator.
  - Expected: A page opens listing the posts belonging to that series in order, and each post can be opened.
  - Actual: Clicked "Part of: Southeast Asia Adventure" → /series/southeast-asia-adventure listed 3 articles numbered in order (1. Ha Long Bay by Kayak, 2. Street Food Adventures in Bangkok, 3. Sunrise Over Angkor Wat), each a link to its full post.

- [ ] FT-04: Browse posts via archive by month and year
  - Action: In the archive, click a specific month/year entry (e.g., "March 2026").
  - Expected: A page opens listing posts published in that month, and each post can be opened.
  - Bug Report:
    - Issue: Non-interactive Archive Entries (month/year headings are not clickable)
    - Actual: On /archive, "2024", "March", "February", "January" are plain H2/H3 headings with no href, no click handler, and cursor: auto — clicking them does nothing and no month-filtered page exists. The archive is a single grouped page listing all 8 articles; only individual post links are clickable, so the prescribed action cannot be performed.

- [X] FT-05: Search posts by keyword
  - Action: Enter a single keyword present in a known post (e.g., "pasta") into the search box and submit.
  - Expected: A results page opens listing posts containing that keyword, and selecting a result opens the full article.
  - Actual: Entered "pasta" in /search → '1 article found for "pasta"' (The Perfect Homemade Pasta); clicking the result opened /post/perfect-homemade-pasta with full content.

- [X] FT-06: Search posts by phrase
  - Action: Enter an exact multi-word phrase from a known post (e.g., "slow morning routine") into the search box and submit.
  - Expected: Results include posts containing that phrase, and selecting a result opens the full article.
  - Actual: The example phrase "slow morning routine" returns '0 articles found' (phrase does not exist in any post), so an exact phrase from a known post was used: "watching the gods wake up" (Angkor Wat article blockquote) → '1 article found for "watching the gods wake up"' (/post/sunrise-over-angkor-wat); clicking it opened the full article. Phrase search works.

- [X] FT-07: Open full article from a post preview
  - Action: On the home page, click the title/"read more" link of any post preview.
  - Expected: The full article page for that post opens with the complete content.
  - Actual: Clicked the hero preview card ("Sunrise Over Angkor Wat") on the home page → /post/sunrise-over-angkor-wat opened with full body, headings, list, and blockquote.

- [X] FT-08: Submit a comment on an article
  - Action: On an article page, enter comment text in the comment form and submit it.
  - Expected: The comment is accepted and displayed in the article's comment list.
  - Actual: Filled name "QATester" + comment text, clicked "Post Comment" → toast "Comment posted! Thanks for joining the conversation.", heading changed "Comments (2)" → "Comments (3)", and the new comment (QATester, Nov 8, 2026, full text) appeared in the list.

- [X] FT-09: Like an article
  - Action: On an article page, click the like control.
  - Expected: The like is registered and the displayed like count reflects the like.
  - Actual: Clicked like button → count changed 234 → 235 with toast "❤️ Thanks for the love! Your appreciation means the world."

- [X] FT-10: Navigate to a related post
  - Action: On an article page, click one of the suggested related posts.
  - Expected: The clicked related article opens in full.
  - Actual: In "You might also enjoy", clicked "Street Food Adventures in Bangkok" → /post/street-food-bangkok opened with full article content.

## Constraint
- [X] CS-01: Comment cannot be submitted empty
  - Action: Leave the comment box empty (or spaces only) and attempt to submit.
  - Expected: Submission is blocked with a validation message, and no empty comment appears in the list.
  - Actual: With name filled and comment box empty, clicked "Post Comment" → toast validation message "Please fill in all fields"; heading remained "Comments (3)" and no empty comment was added.

- [X] CS-02: Filtered and search views contain only matching posts
  - Action: Open a category, tag, series, or archive view, and run a keyword search; inspect the listed items.
  - Expected: Every listed post matches the selected category/tag/series/month or search query; no unrelated post appears.
  - Actual: /category/travel = 3/3 travel posts; /category/recipes = 2/2 recipes; /category/self-improvement = 3/3 self-improvement; tag "Thailand" = only Bangkok post; series "Southeast Asia Adventure" = 3 SE-Asia posts; archive groups match dates (Mar 15/10/5, Feb 28/20/15/10, Jan 25); searches "pasta" and "watching the gods wake up" each returned only the matching post. No unrelated posts found anywhere.

- [X] CS-03: Repeated like clicks do not inflate the count
  - Action: Click the like control on the same article multiple time in one visit.
  - Expected: The count increases by at most 1 for the visit, regardless of how many times it is clicked.
  - Actual: On one visit: 234 → click → 235 → click → 234 (toggle) → 5 rapid further clicks all stayed at 234. Count never exceeded 235, i.e., a maximum increase of 1 for the visit.

## Interaction
- [X] IX-01: Like control gives immediate feedback
  - Action: Click the like control on an article page.
  - Expected: The like count/button state updates immediately after the click, without needing a manual page refresh.
  - Actual: Count updated 234 → 235 synchronously after the click with a toast notification; no refresh was performed.

- [X] IX-02: Post previews show clickable affordance on hover
  - Action: Hover over a post preview's title or "read more" link on the home page.
  - Expected: A visible hover state (e.g., highlight/underline) indicates the element is clickable and leads to the full article.
  - Actual: Hovering the hero preview card's title/link applied a visible hover state — the card's image changed to transform: matrix(1.05, 0, 0, 1.05, 0, 0) (1.05× zoom) versus transform: none on the non-hovered card, and cursor: pointer confirms clickability. (Note: the title text itself gets no underline/color change; feedback is via card image zoom.)

## Content
- [ ] CT-01: Home page shows featured and most recent posts
  - Action: Open the home page.
  - Expected: A "Featured" section and a "Most Recent"/latest-posts section are both present and populated with posts.
  - Bug Report:
    - Issue: Missing "Featured" Posts Section
    - Actual: The home page has a populated recent-posts section ("Recent Stories", 6 posts) and an unlabeled hero with 2 highlighted posts under the heading "Stories from the Heart", but no section is identified as "Featured". The only element containing "Featured" is the "Featured Series" heading, whose section is populated with 3 series cards (Southeast Asia Adventure, Italian Kitchen Essentials, Morning Rituals), not posts. A full text search of the page (including hidden nodes) found "Featured" only in "Featured Series".

- [X] CT-02: Each post preview contains complete preview information
  - Action: Inspect any post preview card on the home page or listing pages.
  - Expected: It shows the post title, a short excerpt, the publication date, its category, and a link to the full article.
  - Actual: Hero card "Sunrise Over Angkor Wat": title (h2), excerpt ("Waking up at 4 AM seemed impossible…"), date "Mar 15, 2024", category "✈️ Travel Stories", and the whole card wraps a link to /post/sunrise-over-angkor-wat. Listing cards likewise show title, excerpt, date, category badge, and link.

- [X] CT-03: Article page shows full content and organizing metadata
  - Action: Open any full article.
  - Expected: The full body content is displayed along with title, publication date, category, tags, and series (if part of one).
  - Actual: /post/sunrise-over-angkor-wat: h1 title, "March 15, 2024", category link "✈️ Travel Stories", series link "Part of: Southeast Asia Adventure", tags #Cambodia/#Temples/#Photography/#Southeast Asia, and full multi-section body (H2/H3, list, blockquote). Also verified on /post/perfect-homemade-pasta and /post/5am-club-experiment.

- [X] CT-04: Related-post suggestions are present and relevant
  - Action: Scroll to the related-posts area of an article page.
  - Expected: Suggestions are shown, and each relates to the current article's topic/category/tag/series.
  - Actual: "You might also enjoy" section present on all article pages: Angkor Wat (Travel) → Street Food Bangkok + Ha Long Bay (both Travel); Pasta (Recipes) → Tiramisu (Recipes); 5 AM Club (Self Improvement) → Journaling + Digital Minimalism (both Self Improvement, sharing Lifestyle/Morning Routine themes).

- [X] CT-05: Content matches the blog's themes
  - Action: Browse home page, category listings, and several articles across categories.
  - Expected: Posts cover the three themes — travel stories, recipes, and self-improvement guides — and any images shown are relevant to their post's topic.
  - Actual: Home page and category listings cover all three themes: Travel (Angkor Wat, Bangkok street food, Ha Long Bay), Recipes (homemade pasta, tiramisu), Self Improvement (5 AM Club, Digital Minimalism, Journaling). Full articles opened across all three categories match their themes, and image alt attributes are topic-relevant (e.g., alt="Sunrise Over Angkor Wat: A Journey Through Time", alt="The Perfect Homemade Pasta: A Labor of Love").

**Summary: 17 PASS / 3 FAIL** — FT-04 (archive month/year entries are not clickable), CT-01 (no "Featured" posts section on the home page).