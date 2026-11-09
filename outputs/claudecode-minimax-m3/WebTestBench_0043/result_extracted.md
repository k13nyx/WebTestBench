# Test Result

## Functionality

- [X] FT-01: User can sign up for a new account
  - Action: Navigate to the sign-up page and complete registration with valid credentials (e.g., username, email, password).
  - Expected: A new user account is created and the user is logged in/redirected to their profile.

- [X] FT-02: Author can write and edit a post in Markdown
  - Action: Create a new post with a title and Markdown body content (including headings, lists, code blocks); open the existing post and modify its content.
  - Expected: Markdown content is accepted as input, saved, and reloaded with the updated content on subsequent visits.

- [X] FT-03: Author can publish a post to their profile page
  - Action: Click the "Publish" button on a finished post draft.
  - Expected: The post becomes publicly visible on the author's profile page and is accessible via a direct post URL.

- [ ] FT-04: Visitor can open and read any published post
  - Action: Open a published post URL as an unauthenticated visitor.
  - Expected: The post page loads showing the title, author, body content, and metadata (views, likes, comments count).
  - Bug Report:
    - Issue: Missing Metadata (view / like counters not rendered on the public post page)
    - Actual: Signed out and opened `http://localhost:6043/post/post-1` and `http://localhost:6043/post/post-1794053959009`. The page renders the title ("The Art of Writing Clean Code"), the author link ("Marcus Webb" / "QA Tester" → /profile/...), the date + read time, the rendered Markdown body, the tag chips and the comments count ("Comments (2)" / "Comments (1)"). However the action bar for an anonymous visitor contains only "Share" — no like button and no like count at all — and no view count is rendered anywhere in the app (a DOM scan of the article found no element containing "view"/eye counter). The backend `views` field is also never incremented: `post-1.views` stayed at142 and the new post stayed at 0 after repeated visits.

- [X] FT-05: Visitor can leave a comment under a post
  - Action: Submit a comment with valid text in the comment form under any published post.
  - Expected: The comment is added and visible in the post's comment list.

- [X] FT-06: User can like a post
  - Action: Click the "Like" button on any published post.
  - Expected: The like is registered and the post's like count increases by one for the current user.

- [X] FT-07: User can save a post to a personal list
  - Action: Click the "Save" button on any published post; then open the personal saved-list page.
  - Expected: The saved post appears in the user's personal list for later retrieval.

- [X] FT-08: Author can add custom tags when publishing
  - Action: While publishing a post, add custom tags (e.g., "Technology", "Life", "Reading Notes") in the tags field.
  - Expected: The custom tags are saved and displayed alongside the post.

- [ ] FT-09: System auto-extracts intelligent tags from post content
  - Action: Publish a post whose body clearly relates to a topic (e.g., a Python/frontend code article).
  - Expected: The system automatically generates intelligent tags (e.g., "Python", "Frontend Development") that appear on the post in addition to the custom tags.
  - Bug Report:
    - Issue: Generated tags not surfaced on the published post (Intelligent tags hidden from readers)
    - Actual: The system does extract tags — the editor's "Intelligent Tags (auto-detected)" panel suggested `Python / TypeScript / Frontend Development / Machine Learning / DevOps` and the stored post object contains `autoTags: ["Python","TypeScript","Frontend Development","Machine Learning","DevOps"]`. But on the published post page only the custom chips are rendered: a DOM scan of `<article>` returned exactly `["Technology","Reading Notes"]` (the custom tags) — no intelligent tag appears "in addition to the custom tags", either for the author or for an anonymous visitor. The intelligent tags are only visible inside the edit screen.

- [X] FT-10: Visitor can filter posts by tags (custom and intelligent)
  - Action: Open the article list and select a single tag (either custom or intelligent) as a filter.
  - Expected: Only posts associated with the selected tag are displayed.

- [X] FT-11: Visitor can perform combined tag search (e.g., "Technology + Python")
  - Action: Apply a combined filter selecting both a custom tag (e.g., "Technology") and an intelligent tag (e.g., "Python") simultaneously.
  - Expected: The system returns only posts that match both selected tags.

- [X] FT-12: User can save frequently-used tag groups for quick access
  - Action: Create a tag group containing a set of tags (e.g., "Technology + Python") and save it; later access the saved tag group from the filter area.
  - Expected: The saved tag group is persisted and can be applied with one click to filter posts.

- [X] FT-13: Author can view tag analytics in personal backend (stats + popularity report)
  - Action: Open the author's personal backend and navigate to the tag analytics section; trigger the generation of a tag popularity analysis report.
  - Expected: The backend displays page views, like counts, and comment counts aggregated per tag, and an analysis report is produced.

## Constraint

- [X] CS-01: Post cannot be published without required fields
  - Action: Try to publish a post with an empty title or empty content.
  - Expected: Publishing is blocked and a validation message indicates which required field is missing.

- [X] CS-02: Empty comment cannot be submitted
  - Action: Click "Submit" on the comment form with an empty (or whitespace-only) comment body.
  - Expected: Submission is blocked and the user is prompted to enter comment content.

- [X] CS-03: Combined tag filter uses AND logic across custom and intelligent tags
  - Action: Apply a combined filter "Technology + Python" against the default article set, including posts that have only "Technology" and posts that have only "Python".
  - Expected: Only posts carrying BOTH "Technology" AND "Python" appear; posts with only one of the tags are excluded.

## Interaction

- [X] IX-01: Liking a post immediately updates the like count visually
  - Action: Click the "Like" button on a post and observe the displayed like count without refreshing the page.
  - Expected: The like count increments by one and the like button reflects the liked state (e.g., filled/highlighted) without requiring a page reload.

- [X] IX-02: New comment appears immediately after submission
  - Action: Submit a comment under a post and observe the comment list without refreshing.
  - Expected: The newly posted comment is appended to the comment list and visible right after submission.

## Content

- [X] CT-01: Markdown content renders correctly in published posts
  - Action: Publish a post containing Markdown elements (headings `#`, bullet lists, fenced code blocks, bold/italic text) and view the published post.
  - Expected: The Markdown is rendered as formatted HTML (visible headings, lists, syntax-highlighted code, styled text) — no raw Markdown symbols (`#`, `*`, ```) are shown to visitors.

- [ ] CT-02: Intelligent tags are semantically relevant to the post content
  - Action: Publish two default test posts — one discussing Python programming, one discussing daily life reflections — and inspect the auto-generated intelligent tags on each.
  - Expected: Each post's intelligent tags match its topic (e.g., "Python"/"Programming" for the code post; "Life"/"Reflection" for the life post); no obviously irrelevant tags appear.
  - Bug Report:
    - Issue: Tag extraction returns a fixed/unrelated tag pool instead of content-derived keywords
    - Actual: The code post ("Python Frontend Development Guide") received `Python, TypeScript, Frontend Development, Machine Learning, DevOps` — Python and Frontend Development are correct, but "Machine Learning" is irrelevant to the article. The daily-life post ("Small Joys of Ordinary Mornings") received `TypeScript, Tutorial, Design, Life, Project` — only "Life" matches the topic; "TypeScript", "Tutorial", "Design" and "Project" are obviously irrelevant, and no "Reflection"-type tag was produced. The 15 values offered in the Intelligent Tags filter are the same pool for every article, so tags appear to be sampled from a fixed list rather than extracted from the content.
