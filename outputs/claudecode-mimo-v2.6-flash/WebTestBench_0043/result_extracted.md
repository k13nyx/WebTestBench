# Test Result

## Functionality
- [X] FT-01: New visitor can sign up with valid credentials and access authoring features.
  - Action: Open the Sign up page, enter a unique email/username and a password, submit the form.
  - Expected: Account is created, the user is logged in, and the "New post"/profile option becomes available.
- [X] FT-02: Author can write a post in Markdown, publish it, and find it on their profile page.
  - Action: Click "New post", enter a title and a Markdown body (e.g., `# Heading` and `- bullet`), add custom tag "Technology", click "Publish"; then open the own profile page and the post.
  - Expected: The post is listed on the profile; opening it shows the title and the Markdown rendered as a formatted heading and bullet list (not raw syntax).
- [X] FT-03: Author can edit a published post and the changes become visible to visitors.
  - Action: Open an existing published post in edit mode, change the title and body, save; then open the same post as a logged-out visitor.
  - Expected: The post detail shows the updated title and body.
- [X] FT-04: Any visitor can open a post from the listing and read the full article.
  - Action: While logged out, click a post title on the home/article listing page.
  - Expected: The post detail page opens showing the full content, author name, publish date, and the post's tags.
- [X] FT-05: Visitor can leave a comment that appears under the post.
  - Action: On a post detail page, type a comment in the comment box and submit it.
  - Expected: The new comment is listed under the post with its text and the commenter's name.
- [X] FT-06: Visitor can like a post and the like is recorded permanently.
  - Action: Click the "Like" button on a post, note the count, then reload the page.
  - Expected: After reload the count still includes the like and the button still shows the post as liked.
- [X] FT-07: User can save a post to a personal list and find it again from there.
  - Action: Click "Save" on a post; then open the personal saved-posts list.
  - Expected: The post appears in the saved list, and opening it navigates to the post detail page.
- [X] FT-08: Author's custom tags appear on the published post.
  - Action: Publish a post with custom tags "Technology" and "Reading Notes"; open the post detail.
  - Expected: Both custom tags are displayed on the post.
- [ ] FT-09: System automatically generates intelligent tags from the article content.
  - Action: Publish an article whose content discusses Python (without adding "Python" as a custom tag); open the post's tag area.
  - Expected: An intelligent tag such as "Python" is generated from the content and shown together with the post's tags.
  - Bug Report:
    - Issue: Intelligent tags generated but never displayed on the post
    - Actual: The editor's "Intelligent Tags (auto-detected)" correctly detected "Python, Backend Development, Code Examples" (stored in `autoTags`, visible in Analytics/filters), but the post detail tag area and listing/profile cards show only the custom tags "Technology, Reading Notes" — no intelligent tag such as "Python" is shown together with the post's tags.
- [X] FT-10: Visitor can filter articles by a single custom tag and by a single intelligent tag.
  - Action: On the article listing, select the custom tag "Technology" and observe results; clear it, then select the intelligent tag "Python" and observe results.
  - Expected: The first result set contains only posts with the "Technology" tag; the second contains only posts with the "Python" tag.
- [X] FT-11: Combined tag search returns only posts matching all selected tags.
  - Action: Select both "Technology" and "Python" in the tag filters simultaneously.
  - Expected: The listing shows only posts that have both tags (e.g., "Technology + Python").
- [X] FT-12: User can save a frequently-used tag group and apply it for quick access.
  - Action: With "Technology" + "Python" selected, save the tag group; later open the saved tag groups list and select it.
  - Expected: The saved group is listed; selecting it activates both tags as filters in one step and shows the matching posts.
- [X] FT-13: Author can view per-tag statistics and generate a tag popularity analysis report in their backend.
  - Action: Open the personal backend, select a tag that has existing activity, view its stats; then generate the tag popularity report.
  - Expected: Stats show page views, like counts, and comment counts for articles under that tag; the report opens listing tags ranked by popularity with figures consistent with those stats.

## Constraint
- [ ] CS-01: Sign-up form rejects invalid or duplicate registrations.
  - Action: Submit the sign-up form with empty required fields; then submit again with an email/username that is already registered.
  - Expected: Neither submission creates an account; each attempt shows an error message identifying the missing or duplicate field.
  - Bug Report:
    - Issue: Missing validation error message on empty-field submission
    - Actual: With empty fields the "Create Account" button stays disabled and no error message identifying the missing fields ever appears (pressing Enter also produces no feedback); only the duplicate-email attempt shows an error ("Sign up failed - An account with this email already exists.").
- [X] CS-02: Post cannot be published with empty required fields.
  - Action: In the post editor, leave the title empty (or leave the body empty) and click "Publish".
  - Expected: The post is not published; an error message prompts for the missing title/content.
- [ ] CS-03: Empty comment cannot be submitted.
  - Action: Leave the comment box empty and click the submit comment button.
  - Expected: No comment is added; a prompt or error indicates the comment cannot be empty.
  - Bug Report:
    - Issue: No validation prompt for empty comment
    - Actual: No comment is added, but no prompt or error appears either — the "Post Comment" button is silently disabled while the box is empty, and pressing Enter in the empty box produces no message.

## Interaction
- [X] IX-01: Publishing a post gives immediate success feedback.
  - Action: Fill in a valid post and click "Publish".
  - Expected: A success confirmation (e.g., "Post published" message) appears immediately, and the new post is visible on the author's profile without further manual refresh.
- [X] IX-02: Like button responds immediately to clicks.
  - Action: Click "Like" on a post, then click it again.
  - Expected: On the first click the count increments and the button switches to the liked state instantly; on the second click the like is removed and the count decrements.

## Content
- [ ] CT-01: Post listing and profile display accurate, relevant information for each article.
  - Action: Compare items on the home listing and an author's profile page against the actual published posts.
  - Expected: Each item shows the correct title, a readable excerpt from the article, the author name, and the exact custom/intelligent tags of that post; no unrelated items appear.
  - Bug Report:
    - Issue: Incorrect/incomplete tag display on listing and profile cards
    - Actual: Titles, excerpts, and author names are correct with no unrelated items, but tags are not exact: cards show only the first 2 custom tags (e.g., "The Future of Human-AI Collaboration" card hides its "Technology" tag shown on its detail page; "Clean Code" hides "Software Development"; "Creativity" hides "Process"), and intelligent tags (e.g., Python/Backend Development/Code Examples) are never displayed on any listing or profile card.
- [X] CT-02: Auto-generated intelligent tags are relevant to the article's content.
  - Action: Review the intelligent tags on several posts, especially a code/technology article (e.g., one about Python).
  - Expected: Each intelligent tag matches the article's topic (e.g., a Python-focused article yields a "Python"-related keyword, not unrelated topics).
