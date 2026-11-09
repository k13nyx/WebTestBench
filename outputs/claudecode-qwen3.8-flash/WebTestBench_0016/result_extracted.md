# Test Result

## Functionality
- [X] FT-01: Home page highlights featured and most recent posts
  - Action: Open the home page
  - Expected: Distinct "Featured" and "Most Recent" (or equivalent) sections are visible, each listing posts
  - Note: Verified — a featured hero section ("Stories from the Heart") lists 2 highlighted posts, and a distinct "Recent Stories" section lists 6 more posts. (The featured block is labeled "Stories from the Heart" rather than the literal word "Featured", which is acceptable per "or equivalent"; "Featured Series" also exists.)

- [X] FT-02: Each home page post shows a short preview linking to the full article
  - Action: On the home page, click a post's preview/title/"Read more" link
  - Expected: The browser navigates to that post's full article page, not just the excerpt
  - Note: Clicked the "The Perfect Homemade Pasta" card → URL became /post/perfect-homemade-pasta and the full multi-section article body rendered (ingredients, steps, quote, closing paragraphs), not the excerpt.

- [X] FT-03: Visitors can browse posts by category (topic)
  - Action: From navigation, select the category "Recipes" (and one other category)
  - Expected: A listing page shows only posts assigned to that category
  - Note: /category/recipes → "Recipes · 2 articles" (Pasta, Tiramisu, both 🍳 Recipes). /category/travel → "Travel Stories · 3 articles" (Angkor Wat, Street Food Bangkok, Ha Long Bay, all ✈️ Travel Stories).

- [X] FT-04: Visitors can browse posts by tag
  - Action: Click any tag shown on a post or tag listing
  - Expected: A page appears listing all posts that carry that tag
  - Note: Clicked #Pasta on the article → /search?tag=Pasta → "1 article found tagged with \"Pasta\"" listing The Perfect Homemade Pasta; tag filter chips shown.

- [X] FT-05: Visitors can browse posts by series
  - Action: Open a series page from a post or navigation
  - Expected: All posts belonging to that series are listed, in series order
  - Note: Footer Series → /series → opened "Southeast Asia Adventure" (/series/southeast-asia-adventure): "Series • 3 articles" with posts explicitly numbered 1 (Ha Long Bay, Feb 10), 2 (Street Food Bangkok, Feb 28), 3 (Angkor Wat, Mar 15) in order.

- [ ] FT-06: Archive by month and year works
  - Action: Open the archive and select a month/year entry that has default posts
  - Expected: Posts are grouped by month/year, and selecting one shows only posts published in that period
  - Bug Report:
    - Issue: Non-selectable archive period entries (missing month/year filter interaction)
    - Actual: Grouping exists on /archive (heading "2024" with "March", "February", "January" groups listing the 8 posts), but the month/year entries are NOT selectable: "2024" is a plain `<h2>` and months are plain `<h3>` (cursor: auto; role: null; no anchor/button wrappers; zero buttons in main; no /archive/… sub-routes). The only clickable items are individual post links, so "selecting one shows only posts published in that period" cannot be performed.

- [X] FT-07: Keyword search returns matching posts
  - Action: Enter a single keyword present in a default post's title or body (e.g., "pasta") and submit
  - Expected: Results page lists the post(s) containing that keyword
  - Note: Submitted "pasta" → /search?q=pasta → "1 article found for \"pasta\"" listing The Perfect Homemade Pasta.

- [X] FT-08: Phrase search returns matching posts
  - Action: Enter a multi-word phrase that appears verbatim in a default post and submit
  - Expected: Results include the post containing that exact phrase
  - Note: Submitted "Labor of Love" → /search?q=Labor+of+Love → "1 article found for \"Labor of Love\"" (The Perfect Homemade Pasta, verbatim in its title).

- [ ] FT-09: Visitors can post a comment on an article
  - Action: On an article page, fill the comment form (name + text) and submit
  - Expected: The comment is saved and displayed in the comments list (on reload it persists)
  - Bug Report:
    - Issue: Comment not persisted (in-memory state only)
    - Actual: Submitting "QA Tester / Automated test comment…" was accepted and rendered immediately ("Comment posted!" toast, Comments (1) → Comments (2)). However, after reloading the same article URL, the comment was gone: heading reverted to "Comments (1)" and only the original "HomeChef_Marco" comment remained. The save-persistence half of the expectation fails.

- [X] FT-10: Visitors can like a post
  - Action: On an article page, click the "Like" reaction button
  - Expected: The like count increases by exactly 1
  - Note: Like button on the pasta post: 456 → 457 (+1 exactly), toast "❤️ Thanks for the love!" appeared.

- [X] FT-11: Article pages show related-post suggestions
  - Action: Open any default article and scroll to the related posts section
  - Expected: At least one related post is suggested; clicking it opens that article
  - Note: Pasta article shows "You might also enjoy" with 1 suggestion (Classic Tiramisu) plus a "More in this category" link; clicking it navigated to /post/classic-tiramisu, which in turn suggests The Perfect Homemade Pasta.

## Constraint
- [X] CS-01: Empty/invalid comments are rejected
  - Action: Submit the comment form with the text (or required name) left blank
  - Expected: Comment is not added; a validation message indicates the required field
  - Note: Clicked "Post Comment" with both fields blank → toast "Please fill in all fields"; comment list stayed at Comments (1); nothing added.

- [X] CS-02: Search with no matches shows a clear no-results state
  - Action: Search for a nonsense string (e.g., "zzqqxx123")
  - Expected: Page shows a "no results found" message; no error page or blank screen
  - Note: /search?q=zzqqxx123 → "0 articles found for \"zzqqxx123\"" + "No articles found matching your criteria." with a "Clear filters" button; page rendered fully, no errors.

- [X] CS-03: Duplicate likes are prevented
  - Action: Click the "Like" button twice in succession on the same article
  - Expected: Count does not increase twice (either blocked or toggled back to original state)
  - Note: Second click toggled 457 → 456, returning to the original state (liked state reverted, button un-highlighted).

- [X] CS-04: Category/tag/series listings contain no foreign posts
  - Action: On the "Travel" category page, inspect every listed post's metadata
  - Expected: No post from another category (e.g., "Recipes") appears in the list
  - Note: /category/travel lists exactly 3 articles — Angkor Wat, Street Food Bangkok, Ha Long Bay — each carrying the "✈️ Travel Stories" category badge; no Recipes or Self Improvement posts present.

## Interaction
- [X] IX-01: Like button gives immediate visual feedback
  - Action: Click the Like button and observe it (before reload)
  - Expected: Button changes state (highlighted/filled icon, updated count) without a full page reload
  - Note: Without any navigation, button class changed from `border bg-background hover:bg-accent` to `bg-primary text-primary-foreground`, the heart SVG gained `fill-current`, and the count updated to 457 in place.

- [X] IX-02: Newly submitted comment appears without losing article context
  - Action: Submit a comment on an article
  - Expected: The comment renders in the list on the same page (or a confirmation message appears); user is not navigated away to a broken page
  - Note: URL stayed /post/perfect-homemade-pasta; the new comment ("QA Tester — Automated test comment…") rendered directly below the existing one, heading updated to "Comments (2)", success toast shown, and the form cleared.

## Content
- [X] CT-01: Default content covers all three instructed themes
  - Action: Browse the home page and category listings
  - Expected: Posts exist for travel stories, detailed recipes, and self-improvement guides; copy/images match each theme (no placeholder/lorem text)
  - Note: Travel (3 posts), Recipes (2), Self Improvement (3) all confirmed with theme-accurate titles, excerpts, and full bodies; images present with descriptive matching alt text (e.g., "Classic Tiramisu: No-Bake Italian Perfection"); no "lorem/ipsum/placeholder" strings detected.

- [X] CT-02: Each article displays complete organizing metadata
  - Action: Open three different default articles
  - Expected: Each shows its category, tag(s), and publish date, and series name where applicable
  - Note: (1) Pasta — 🍳 Recipes, #Italian/#Pasta/#From Scratch/#Comfort Food, March 10, 2024, "Part of: Italian Kitchen Essentials". (2) Tiramisu — 🍳 Recipes, #Italian/#Dessert/#No-Bake/#Coffee, February 20, 2024, "Part of: Italian Kitchen Essentials". (3) Angkor Wat — ✈️ Travel Stories, #Cambodia/#Temples/#Photography/#Southeast Asia, March 15, 2024, "Part of: Southeast Asia Adventure".

- [X] CT-03: Related-post suggestions are topically relevant
  - Action: Open a recipe article and inspect the related posts
  - Expected: Suggested posts share the article's category, tag, or series (not arbitrary posts)
  - Note: Recipe article (Pasta) suggests only "Classic Tiramisu" — same 🍳 Recipes category, shares the #Italian tag, and same "Italian Kitchen Essentials" series; Tiramisu reciprocally suggests Pasta. No off-topic suggestions observed.
