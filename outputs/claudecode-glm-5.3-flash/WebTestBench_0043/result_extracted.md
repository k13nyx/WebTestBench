# Test Result

## Functionality
- [X] FT-01: New user can sign up for an account
  - Action: Open the sign-up page, enter a username/email and password, click the "Sign Up" button
  - Expected: Account is created, user is logged in, and a profile page exists for the new user

- [X] FT-02: Author can write a post in Markdown
  - Action: Open the post editor, enter a title and Markdown content (e.g., `# Heading`, `**bold**`, a code block), save as draft
  - Expected: The post is saved with the Markdown source intact and appears in the author's post list

- [X] FT-03: Author can edit an existing post
  - Action: Open one of the author's own published posts, click "Edit", change the title or body, and save
  - Expected: The post displays the updated title/content after saving

- [ ] FT-04: Publishing a post makes it appear on the author's profile page
  - Action: Click "Publish" on a draft post, then open the author's public profile page
  - Expected: The published post (title and timestamp) is listed on the author's profile page
  - Bug Report:
    - Issue: Missing element (timestamp) on profile listing
    - Actual: After publishing via the editor's "Published" checkbox + "Save Changes" (no dedicated "Publish" button exists on the draft view), the post IS listed on the profile's "Published (1)" tab with title and custom tag, but the profile card shows only "QA Tester • 1 min" (read time) — no publish date/timestamp is displayed. The date (2026-11-08) appears only on the post detail page, not on the profile listing.

- [X] FT-05: A visitor can open and read any published post
  - Action: While logged out (or as another user), open a published post from a profile or post list
  - Expected: The full post renders as formatted content (headings, bold, code blocks visible)

- [X] FT-06: A visitor can leave a comment under a post
  - Action: On a published post, type a comment (e.g., "Great article!") in the comment box and submit it
  - Expected: The comment appears in the comment section under the post with commenter name and time

- [X] FT-07: A visitor can like a post
  - Action: Click the "Like" button on a published post
  - Expected: The like count increases by 1 and the button shows a liked/active state

- [X] FT-08: A user can save a post to a personal list
  - Action: Click "Save"/"Bookmark" on a post, then open the personal saved list page
  - Expected: The post appears in the user's saved list and can be reopened from there

- [X] FT-09: Author can add custom tags when publishing
  - Action: In the publish/editor view, add a custom tag such as "Technology" or "Life", then publish
  - Expected: The custom tag is shown on the published post and on the post's list entry

- [ ] FT-10: System automatically extracts intelligent tags from content
  - Action: Publish a post whose body repeatedly mentions "Python" and "Frontend Development"
  - Expected: An auto-generated intelligent tag (e.g., "Python", "Frontend Development") appears on the post without manual entry, separate from custom tags
  - Bug Report:
    - Issue: Intelligent tags generated but never displayed on the published post
    - Actual: The system DID auto-extract intelligent tags (stored as `autoTags: ["Python","TypeScript","Tutorial","Productivity","Design"]`, visible in the editor's "Intelligent Tags (auto-detected)" section), but the published post page displays ONLY the custom tag chip "Technology". No intelligent tag chip (e.g., "Python") appears anywhere on the published post view or its list card, so the auto-generated tag never "appears on the post".

- [X] FT-11: Visitors can filter posts by combined tags
  - Action: On the tag filter view, select a custom tag "Technology" AND an intelligent tag "Python" together
  - Expected: Only posts having BOTH tags are listed; posts with only one of the tags are excluded

- [X] FT-12: User can save a frequently-used tag group for quick access
  - Action: After selecting a tag combination (e.g., "Technology + Python"), click "Save Tag Group", give it a name, then reload the page
  - Expected: The named tag group is persisted and clicking it re-applies the same tag filter instantly

- [X] FT-13: Author backend shows per-tag statistics for their articles
  - Action: Open the author's personal backend/dashboard and view the per-tag statistics section
  - Expected: For each tag, page views, like counts, and comment counts of that author's articles under the tag are displayed

- [X] FT-14: Author can generate a tag popularity analysis report
  - Action: In the backend, click "Generate Tag Popularity Report"
  - Expected: A report is displayed comparing tags by popularity metrics (e.g., views/likes/comments per tag)

## Constraint
- [X] CS-01: Publishing is blocked when required fields are empty
  - Action: Attempt to publish a post with an empty title or empty content
  - Expected: Publication is rejected and a validation error (e.g., "Title is required") is shown; no post is created

- [X] CS-02: Duplicate account sign-up is prevented
  - Action: Attempt to sign up again with an email/username that already exists
  - Expected: Sign-up fails with an error message such as "Account already exists"; no second account is created

- [X] CS-03: Only the author can edit their own post
  - Action: As a visitor or another user, open someone else's published post
  - Expected: No "Edit" button/control is available and the post cannot be modified

## Interaction
- [X] IX-01: Editor shows live Markdown preview
  - Action: While typing Markdown (e.g., `# Title`, a list, `code`) in the editor, observe the preview pane
  - Expected: The preview updates in real time showing rendered heading, list, and code formatting

- [X] IX-02: Liking gives immediate visual feedback
  - Action: Click "Like" on a post, then click it again
  - Expected: The first click turns the button active and increments the count; the second click un-likes (count returns to previous value and state clears)

## Content
- [ ] CT-01: Intelligent tags are relevant to post content
  - Action: Open a published code-related article and inspect its auto-generated intelligent tags
  - Expected: Displayed intelligent tags (e.g., "Python", "Frontend Development") match the article's actual topic; no irrelevant or empty tag placeholders are shown
  - Bug Report:
    - Issue: Intelligent tags not rendered on the article page; detected tag list partially irrelevant
    - Actual: Opening the published code-related article (/post/post-1794102071730), no intelligent tags are displayed at all — only the custom tag "Technology" is shown (same root cause as FT-10). The auto-detected list that does exist (visible only in the editor) contains "Python" (relevant) but also generic, content-unsupported suggestions such as "TypeScript", "Tutorial", "Productivity", and "Design" that are not mentioned in the article body, so the extraction is only partially content-relevant.
