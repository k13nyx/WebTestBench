# Test Checklist

## Functionality
- [ ] FT-01: New user can sign up for an account.
  - Action: Open the sign-up form, fill in username, email, and password, and submit.
  - Expected: The account is created and the user gains access to the site as a signed-in author (e.g., reaches their profile/dashboard).

- [ ] FT-02: Author can write a post in Markdown and publish it to their profile page.
  - Action: Open the post editor, enter a title and Markdown body (e.g., `# Title`, `**bold**`, a list), click "Publish".
  - Expected: The post is published and listed on the author's own profile page with the entered title.

- [ ] FT-03: Author can edit their own published post.
  - Action: Open an own published post, click "Edit", modify the title/body, save the changes.
  - Expected: The updated content is saved and displayed on the post page (still present after reload).

- [ ] FT-04: Visitor can open a post, read it, and leave a comment.
  - Action: As a visitor, open a published post from the article list, read it, type text into the comment box, and submit.
  - Expected: The full post content is displayed, and the new comment appears under the post.

- [ ] FT-05: Visitor can like a post.
  - Action: Click the "Like" button on a post.
  - Expected: The like count increases by 1, and the like is retained after page reload.

- [ ] FT-06: User can save a post to a personal list and find it again.
  - Action: Click the "Save"/bookmark button on a post, then open the personal saved list.
  - Expected: The post appears in the saved list and can be opened from there.

- [ ] FT-07: Author can add custom tags when publishing a post.
  - Action: In the publish flow, add custom tags (e.g., "Technology", "Life", "Reading Notes") and publish.
  - Expected: The custom tags are saved and shown on the post page.

- [ ] FT-08: System automatically generates intelligent tags from article content.
  - Action: Publish or open a content-rich article (e.g., a code-related post) without manually adding intelligent tags, then view its tags.
  - Expected: System-generated intelligent tags are displayed automatically alongside the author's custom tags.

- [ ] FT-09: Articles can be filtered by custom tag and by intelligent tag (dual dimensions).
  - Action: On the article list (using existing default articles/tags), apply a custom tag filter (e.g., "Technology"), clear it, then apply an intelligent tag filter (e.g., "Python").
  - Expected: Each filter lists only articles carrying the selected tag of that tag type.

- [ ] FT-10: Combined tag search works across both tag dimensions.
  - Action: Select a tag combination spanning both dimensions, e.g., "Technology + Python".
  - Expected: Only articles matching ALL selected tags (both Technology and Python) are listed.

- [ ] FT-11: User can save a frequently-used tag group and reuse it for quick access.
  - Action: Apply "Technology + Python", save this combination as a tag group, clear all filters, then re-apply the saved group.
  - Expected: The group appears in the saved tag groups, and one click filters the article list by the full tag combination.

- [ ] FT-12: Author can view per-tag article statistics in the personal backend.
  - Action: Open the personal backend's tag statistics view and inspect the data for one tag.
  - Expected: For each tag, the page views, like counts, and comment counts of its articles are displayed.

- [ ] FT-13: Author can generate a tag popularity analysis report.
  - Action: In the tag analytics area of the personal backend, trigger the generate-report action.
  - Expected: A tag popularity analysis report is produced summarizing/ranking tags by their views, likes, and comments.

## Constraint
- [ ] CS-01: Sign-up rejects invalid input.
  - Action: Submit the sign-up form with empty required fields; then with an already-registered username/email.
  - Expected: Both attempts are rejected with an error message, and no duplicate account is created.

- [ ] CS-02: A post cannot be published with an empty title or empty body.
  - Action: In the editor, leave the title or the body empty and click "Publish".
  - Expected: Publishing is blocked with a validation message, and no incomplete post appears on the profile page.

- [ ] CS-03: Users cannot edit or delete other authors' posts.
  - Action: While signed in as user B, open a post authored by user A.
  - Expected: No Edit/Delete controls are available for that post; any direct modification attempt is denied.

## Interaction
- [ ] IX-01: Like and Save controls provide immediate state feedback.
  - Action: Click "Like" and "Save" on a post, then click each button a second time.
  - Expected: Each control visually switches to its active (liked/saved) state on the first click and back to its inactive state on the second click.

- [ ] IX-02: Publishing a post provides success feedback.
  - Action: Click "Publish" after filling in a valid title and body.
  - Expected: A success confirmation (message/toast) is displayed.

## Content
- [ ] CT-01: Markdown content is rendered as formatted elements, not raw syntax.
  - Action: Open a post containing headings, bold text, lists, links, and code blocks (use an existing default post).
  - Expected: Headings, bold text, list items, links, and code blocks render as formatted HTML elements; no raw Markdown characters (e.g., `#`, `**`) are visible.

- [ ] CT-02: Intelligent tags are relevant to the article's content.
  - Action: Compare an article's auto-generated intelligent tags with its actual content (e.g., a code-related article).
  - Expected: Tags are content-relevant core keywords (e.g., "Python", "Frontend Development" for code articles), not generic or unrelated words.