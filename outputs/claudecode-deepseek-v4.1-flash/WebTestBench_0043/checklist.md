# Test Checklist

## Functionality
- [ ] FT-01: New user can sign up and access their profile
  - Action: Go to the sign-up page, enter valid credentials, and submit.
  - Expected: Account is created; user lands on their own profile page; profile shows the user's name/empty post list.

- [ ] FT-02: Author can write a post in Markdown with a rendered preview
  - Action: Open "new post", type a title and Markdown body (e.g., a heading and a code block), and toggle preview.
  - Expected: Markdown is rendered correctly (headings, code blocks) in the preview pane.

- [ ] FT-03: Author can edit an existing post
  - Action: Open one of the author's own posts, click "Edit", change the content, and save.
  - Expected: Editor opens pre-filled with current content; changes persist and are shown on the post.

- [ ] FT-04: Author can publish a post to their profile page
  - Action: From the editor, click "Publish".
  - Expected: Post becomes publicly visible and appears in the post list on the author's profile page.

- [ ] FT-05: A visitor can open and read any published post
  - Action: As a logged-out visitor, click a published post from a profile or list.
  - Expected: Full post content (title, rendered body, author) is displayed.

- [ ] FT-06: A visitor can leave a comment under a post
  - Action: On a post page, enter a comment and submit.
  - Expected: Comment is saved and displayed under the post, attributed to the visitor.

- [ ] FT-07: A user can like a post
  - Action: Click the "Like" button on a post.
  - Expected: Like is registered and the like count increases for that post.

- [ ] FT-08: A user can save a post to a personal list and find it again
  - Action: Click "Save" on a post, then open the personal saved list.
  - Expected: The post appears in the saved list and opens correctly from there.

- [ ] FT-09: Author can add custom tags when publishing
  - Action: In the editor, add custom tags (e.g., "Technology", "Life", "Reading Notes") and publish.
  - Expected: The post displays exactly the custom tags entered by the author.

- [ ] FT-10: System auto-generates intelligent tags from post content
  - Action: Publish a code-related post and view it.
  - Expected: System-generated tags (e.g., "Python", "Frontend Development") are shown alongside custom tags, without author input.

- [ ] FT-11: Visitor can filter articles by custom and intelligent tags, including combined search
  - Action: Filter by a custom tag (e.g., "Technology"), then by an intelligent tag (e.g., "Python"), then apply both together.
  - Expected: Each filtered view shows only matching posts; combined search returns posts matching both tags.

- [ ] FT-12: User can save a frequently-used tag group for quick access
  - Action: Select a tag combination (e.g., "Technology + Python") and click "Save tag group"; reload the site and apply it.
  - Expected: The tag group is stored and reapplies the same combined filter in one action.

- [ ] FT-13: Author backend shows per-tag metrics for articles
  - Action: Open the author backend, select a tag, and view its articles.
  - Expected: Each article lists its page views, like count, and comment count.

- [ ] FT-14: Author can generate a tag popularity analysis report
  - Action: In the backend, trigger "Generate tag popularity report".
  - Expected: A report ranks tags (e.g., by usage/engagement) and is displayed to the author.

## Constraint
- [ ] CS-01: A post cannot be published with missing required fields
  - Action: Attempt to publish with an empty title or empty body.
  - Expected: Publish is blocked and a validation message indicates the missing field(s).

- [ ] CS-02: Only the author can edit their own posts
  - Action: As a non-author (visitor or another user), open a post and look for edit controls; attempt to reach the edit action.
  - Expected: No edit controls are shown to non-authors, and editing another user's post is not permitted.

## Interaction
- [ ] IX-01: Clear feedback is shown after publishing
  - Action: Click "Publish" on a valid post.
  - Expected: A success confirmation appears (e.g., toast/message) and the user is taken to the published post or profile showing it.

- [ ] IX-02: Like button reflects state change immediately
  - Action: Click the "Like" button on a post, then click it again.
  - Expected: Button visual state toggles (liked/unliked) and the like count updates instantly on each click.

## Content
- [ ] CT-01: Intelligent tags are relevant to the article content
  - Action: Open a post about code/frontend topics and inspect its intelligent tags.
  - Expected: Extracted tags are directly related to the content (e.g., "Python", "Frontend Development"), not random or unrelated terms.

- [ ] CT-02: Analytics and report data match actual post activity
  - Action: Compare a post's page views, likes, and comments with the numbers shown in the backend per-tag view and the popularity report.
  - Expected: Displayed metrics and report values match the actual recorded activity for that post and tag.