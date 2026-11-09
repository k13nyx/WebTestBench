# Test Checklist

## Functionality
- [ ] FT-01: User can sign up for a new account
  - Action: Navigate to the sign-up page and complete registration with valid credentials (e.g., username, email, password).
  - Expected: A new user account is created and the user is logged in/redirected to their profile.

- [ ] FT-02: Author can write and edit a post in Markdown
  - Action: Create a new post with a title and Markdown body content (including headings, lists, code blocks); open the existing post and modify its content.
  - Expected: Markdown content is accepted as input, saved, and reloaded with the updated content on subsequent visits.

- [ ] FT-03: Author can publish a post to their profile page
  - Action: Click the "Publish" button on a finished post draft.
  - Expected: The post becomes publicly visible on the author's profile page and is accessible via a direct post URL.

- [ ] FT-04: Visitor can open and read any published post
  - Action: Open a published post URL as an unauthenticated visitor.
  - Expected: The post page loads showing the title, author, body content, and metadata (views, likes, comments count).

- [ ] FT-05: Visitor can leave a comment under a post
  - Action: Submit a comment with valid text in the comment form under any published post.
  - Expected: The comment is added and visible in the post's comment list.

- [ ] FT-06: User can like a post
  - Action: Click the "Like" button on any published post.
  - Expected: The like is registered and the post's like count increases by one for the current user.

- [ ] FT-07: User can save a post to a personal list
  - Action: Click the "Save" button on any published post; then open the personal saved-list page.
  - Expected: The saved post appears in the user's personal list for later retrieval.

- [ ] FT-08: Author can add custom tags when publishing
  - Action: While publishing a post, add custom tags (e.g., "Technology", "Life", "Reading Notes") in the tags field.
  - Expected: The custom tags are saved and displayed alongside the post.

- [ ] FT-09: System auto-extracts intelligent tags from post content
  - Action: Publish a post whose body clearly relates to a topic (e.g., a Python/frontend code article).
  - Expected: The system automatically generates intelligent tags (e.g., "Python", "Frontend Development") that appear on the post in addition to the custom tags.

- [ ] FT-10: Visitor can filter posts by tags (custom and intelligent)
  - Action: Open the article list and select a single tag (either custom or intelligent) as a filter.
  - Expected: Only posts associated with the selected tag are displayed.

- [ ] FT-11: Visitor can perform combined tag search (e.g., "Technology + Python")
  - Action: Apply a combined filter selecting both a custom tag (e.g., "Technology") and an intelligent tag (e.g., "Python") simultaneously.
  - Expected: The system returns only posts that match both selected tags.

- [ ] FT-12: User can save frequently-used tag groups for quick access
  - Action: Create a tag group containing a set of tags (e.g., "Technology + Python") and save it; later access the saved tag group from the filter area.
  - Expected: The saved tag group is persisted and can be applied with one click to filter posts.

- [ ] FT-13: Author can view tag analytics in personal backend (stats + popularity report)
  - Action: Open the author's personal backend and navigate to the tag analytics section; trigger the generation of a tag popularity analysis report.
  - Expected: The backend displays page views, like counts, and comment counts aggregated per tag, and an analysis report is produced.

## Constraint
- [ ] CS-01: Post cannot be published without required fields
  - Action: Try to publish a post with an empty title or empty content.
  - Expected: Publishing is blocked and a validation message indicates which required field is missing.

- [ ] CS-02: Empty comment cannot be submitted
  - Action: Click "Submit" on the comment form with an empty (or whitespace-only) comment body.
  - Expected: Submission is blocked and the user is prompted to enter comment content.

- [ ] CS-03: Combined tag filter uses AND logic across custom and intelligent tags
  - Action: Apply a combined filter "Technology + Python" against the default article set, including posts that have only "Technology" and posts that have only "Python".
  - Expected: Only posts carrying BOTH "Technology" AND "Python" appear; posts with only one of the tags are excluded.

## Interaction
- [ ] IX-01: Liking a post immediately updates the like count visually
  - Action: Click the "Like" button on a post and observe the displayed like count without refreshing the page.
  - Expected: The like count increments by one and the like button reflects the liked state (e.g., filled/highlighted) without requiring a page reload.

- [ ] IX-02: New comment appears immediately after submission
  - Action: Submit a comment under a post and observe the comment list without refreshing.
  - Expected: The newly posted comment is appended to the comment list and visible right after submission.

## Content
- [ ] CT-01: Markdown content renders correctly in published posts
  - Action: Publish a post containing Markdown elements (headings `#`, bullet lists, fenced code blocks, bold/italic text) and view the published post.
  - Expected: The Markdown is rendered as formatted HTML (visible headings, lists, syntax-highlighted code, styled text) — no raw Markdown symbols (`#`, `*`, ```) are shown to visitors.

- [ ] CT-02: Intelligent tags are semantically relevant to the post content
  - Action: Publish two default test posts — one discussing Python programming, one discussing daily life reflections — and inspect the auto-generated intelligent tags on each.
  - Expected: Each post's intelligent tags match its topic (e.g., "Python"/"Programming" for the code post; "Life"/"Reflection" for the life post); no obviously irrelevant tags appear.