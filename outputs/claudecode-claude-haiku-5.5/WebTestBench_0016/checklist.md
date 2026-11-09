# Test Checklist

## Functionality
- [ ] FT-01: Home page highlights featured posts and lists most recent posts.
  - Action: Open the home page on desktop.
  - Expected: A "Featured" section shows at least one post, and a "Recent" section lists posts newest first, each with a title and preview.
- [ ] FT-02: Post preview links to the full article.
  - Action: Click the "Read more" link or title of any post preview on the home page.
  - Expected: The full article page opens, showing the same post title and complete body text.
- [ ] FT-03: Category browsing shows only posts in that category.
  - Action: Click the "Travel" category in navigation, then click "Recipes" and "Self-Improvement" in turn.
  - Expected: Each category page lists only posts assigned to that category, and every listed post matches the selected category.
- [ ] FT-04: Tag browsing shows only posts with that tag.
  - Action: Click any tag shown on an article page.
  - Expected: A tag page opens listing only posts that carry that tag, and the tag name is shown as the page heading.
- [ ] FT-05: Series page lists its posts in order.
  - Action: Open a series from an article's series label, or from the series listing.
  - Expected: All posts in the series are listed in their series order (e.g., Part 1, Part 2, Part 3), with no posts from other series.
- [ ] FT-06: Archive by month and year lists posts for the selected period.
  - Action: In the "Archive" section, click a month and year that has posts (e.g., the most recent listed month).
  - Expected: Only posts published in that month and year are listed, and each post's date falls within that month.
- [ ] FT-07: Keyword search returns matching posts.
  - Action: Type a single keyword that appears in an existing post's title or body into the search box and press Enter.
  - Expected: Results page lists posts containing that keyword, and the keyword is shown as the search query.
- [ ] FT-08: Exact phrase search returns only posts containing the phrase.
  - Action: Search for an exact multi-word phrase from an existing article, enclosed in quotation marks.
  - Expected: Results include the article containing the exact phrase, and no results lack that phrase.
- [ ] FT-09: Article page displays its metadata.
  - Action: Open any article from the home page.
  - Expected: The page shows the title, publication date, category, tags, and series name (if any), each linking to its respective listing page.
- [ ] FT-10: Like control increases the like count.
  - Action: On any article, click the "Like" control once.
  - Expected: The like count increases by exactly 1 and the control shows a liked state.
- [ ] FT-11: Submitted comment appears in the article's comment list.
  - Action: On any article, enter a name and a comment text in the comment form, then submit.
  - Expected: The comment appears in the comment list with the entered name and text, and the comment count increases by 1.
- [ ] FT-12: Related-post suggestions open the linked articles.
  - Action: On any article, click the first post listed under "Related Posts."
  - Expected: The "Related Posts" section is visible, and the clicked link opens the correct article with a matching title.

## Constraint
- [ ] CS-01: Empty search is blocked.
  - Action: Click the search button or press Enter with the search box empty.
  - Expected: No search is performed, the page does not change, and a message asks the user to enter a keyword.
- [ ] CS-02: Comment cannot be submitted without required fields.
  - Action: On any article, leave the comment text empty (or the name empty) and click the submit button for comments.
  - Expected: The comment is not posted, the comment count is unchanged, and the empty required field is flagged with a validation message.
- [ ] CS-03: One like per visitor, and the liked state persists.
  - Action: On any article, click "Like," then reload the page and click "Like" again.
  - Expected: After reload the article still shows the liked state, and the count is not increased by the second click (the click removes the like or is ignored).
- [ ] CS-04: Comment text is displayed as plain text.
  - Action: On any article, submit a comment containing the text `<b>test</b>`.
  - Expected: The comment displays the literal text `<b>test</b>` and the markup is not rendered as bold text or executed.

## Interaction
- [ ] IX-01: Like control updates without a page reload.
  - Action: On any article, click the "Like" control and observe the control and count.
  - Expected: The control's visual state changes (e.g., filled or highlighted) and the count updates immediately, while the URL and scroll position remain unchanged.
- [ ] IX-02: Comment submission gives confirmation and resets the form.
  - Action: On any article, enter a name and comment, then submit.
  - Expected: A confirmation message appears, the comment form fields are cleared, and the new comment is visible in the list without a page reload.
- [ ] IX-03: Search with no matches shows a clear message.
  - Action: Search for a keyword that does not appear in any post (e.g., "zzqxv").
  - Expected: The results area shows a "No results found" message and no post previews, with no error message or broken layout.

## Content
- [ ] CT-01: Related posts are relevant to the current article.
  - Action: Open any travel, recipe, and self-improvement article, and review its "Related Posts" list.
  - Expected: Each related post shares at least one category or tag with the current article, and none are unrelated topics.