# Test Checklist

## Functionality
- [ ] FT-01: New user can sign up for an account
  - Action: Open the sign-up page, enter a username/email and password, click the "Sign Up" button
  - Expected: Account is created, user is logged in, and a profile page exists for the new user
- [ ] FT-02: Author can write a post in Markdown
  - Action: Open the post editor, enter a title and Markdown content (e.g., `# Heading`, `**bold**`, a code block), save as draft
  - Expected: The post is saved with the Markdown source intact and appears in the author's post list
- [ ] FT-03: Author can edit an existing post
  - Action: Open one of the author's own published posts, click "Edit", change the title or body, and save
  - Expected: The post displays the updated title/content after saving
- [ ] FT-04: Publishing a post makes it appear on the author's profile page
  - Action: Click "Publish" on a draft post, then open the author's public profile page
  - Expected: The published post (title and timestamp) is listed on the author's profile page
- [ ] FT-05: A visitor can open and read any published post
  - Action: While logged out (or as another user), open a published post from a profile or post list
  - Expected: The full post renders as formatted content (headings, bold, code blocks visible)
- [ ] FT-06: A visitor can leave a comment under a post
  - Action: On a published post, type a comment (e.g., "Great article!") in the comment box and submit it
  - Expected: The comment appears in the comment section under the post with commenter name and time
- [ ] FT-07: A visitor can like a post
  - Action: Click the "Like" button on a published post
  - Expected: The like count increases by 1 and the button shows a liked/active state
- [ ] FT-08: A user can save a post to a personal list
  - Action: Click "Save"/"Bookmark" on a post, then open the personal saved list page
  - Expected: The post appears in the user's saved list and can be reopened from there
- [ ] FT-09: Author can add custom tags when publishing
  - Action: In the publish/editor view, add a custom tag such as "Technology" or "Life", then publish
  - Expected: The custom tag is shown on the published post and on the post's list entry
- [ ] FT-10: System automatically extracts intelligent tags from content
  - Action: Publish a post whose body repeatedly mentions "Python" and "Frontend Development"
  - Expected: An auto-generated intelligent tag (e.g., "Python", "Frontend Development") appears on the post without manual entry, separate from custom tags
- [ ] FT-11: Visitors can filter posts by combined tags
  - Action: On the tag filter view, select a custom tag "Technology" AND an intelligent tag "Python" together
  - Expected: Only posts having BOTH tags are listed; posts with only one of the tags are excluded
- [ ] FT-12: User can save a frequently-used tag group for quick access
  - Action: After selecting a tag combination (e.g., "Technology + Python"), click "Save Tag Group", give it a name, then reload the page
  - Expected: The named tag group is persisted and clicking it re-applies the same tag filter instantly
- [ ] FT-13: Author backend shows per-tag statistics for their articles
  - Action: Open the author's personal backend/dashboard and view the per-tag statistics section
  - Expected: For each tag, page views, like counts, and comment counts of that author's articles under the tag are displayed
- [ ] FT-14: Author can generate a tag popularity analysis report
  - Action: In the backend, click "Generate Tag Popularity Report"
  - Expected: A report is displayed comparing tags by popularity metrics (e.g., views/likes/comments per tag)

## Constraint
- [ ] CS-01: Publishing is blocked when required fields are empty
  - Action: Attempt to publish a post with an empty title or empty content
  - Expected: Publication is rejected and a validation error (e.g., "Title is required") is shown; no post is created
- [ ] CS-02: Duplicate account sign-up is prevented
  - Action: Attempt to sign up again with an email/username that already exists
  - Expected: Sign-up fails with an error message such as "Account already exists"; no second account is created
- [ ] CS-03: Only the author can edit their own post
  - Action: As a visitor or another user, open someone else's published post
  - Expected: No "Edit" button/control is available and the post cannot be modified

## Interaction
- [ ] IX-01: Editor shows live Markdown preview
  - Action: While typing Markdown (e.g., `# Title`, a list, `code`) in the editor, observe the preview pane
  - Expected: The preview updates in real time showing rendered heading, list, and code formatting
- [ ] IX-02: Liking gives immediate visual feedback
  - Action: Click "Like" on a post, then click it again
  - Expected: The first click turns the button active and increments the count; the second click un-likes (count returns to previous value and state clears)

## Content
- [ ] CT-01: Intelligent tags are relevant to post content
  - Action: Open a published code-related article and inspect its auto-generated intelligent tags
  - Expected: Displayed intelligent tags (e.g., "Python", "Frontend Development") match the article's actual topic; no irrelevant or empty tag placeholders are shown