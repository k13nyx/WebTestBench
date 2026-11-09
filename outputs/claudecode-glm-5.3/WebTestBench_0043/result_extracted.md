# Test Result

## Functionality

- [ ] FT-01: New user can sign up for an account
  - Action: Open the "Sign Up" page, fill in username, email, and password, and click the "Sign Up" button.
  - Expected: Account is created, user is logged in and redirected to their own (empty) profile page; logging out and back in with the same credentials succeeds.
  - Bug Report:
    - Issue: Incorrect Redirect After Sign-Up
    - Actual: Account creation, login state, and logout/re-login all work (welcome toast "Welcome to Inkwell! Your account has been created successfully" shown; profile page exists and is empty with "0 posts"). However, after clicking "Create Account" the user is redirected to the home feed (URL `/`), NOT to their own profile page as expected. The empty profile page is only reachable by manually navigating via the user menu.

- [ ] FT-02: Author can write a post in Markdown and publish it to their profile page
  - Action: While logged in, click "New Post", enter a title and Markdown body (e.g., `# Heading`, `**bold**`, fenced code block), add a custom tag "Technology", and click "Publish".
  - Expected: Post is saved and appears in the author's profile page post list with its title, custom tag, and publish date.
  - Bug Report:
    - Issue: Missing Publish Date in Profile Post List
    - Actual: The post is saved and appears in the profile page "Published (1)" list with its title ("My Python Automation Journey") and the custom tag chip "Technology", but the list card shows only "Test Author • 1 min" — no publish date is displayed anywhere in the profile post list (the date 2026-11-07 is only visible on the post detail page).

- [X] FT-03: Author can edit a published post and changes persist
  - Action: Open one of the author's own published posts, click "Edit", modify the title and body text, and click "Save".
  - Expected: Post detail page shows the updated title and content; the profile page post list also reflects the new title.

- [X] FT-04: Visitor can open and read any published post
  - Action: While logged out, browse the post list, open a default published post by clicking its title.
  - Expected: The post's full content is displayed on a dedicated post page, including author name and publish date.

- [X] FT-05: Visitor can leave a comment under a post
  - Action: On a post page, type a comment into the comment input box and click "Submit Comment".
  - Expected: The comment appears in the post's comment list showing the commenter's name, comment text, and timestamp.

- [X] FT-06: Visitor can like a post
  - Action: On a post page, click the "Like" button and note the count before and after.
  - Expected: The like count increments by exactly 1.

- [X] FT-07: Visitor can save a post to a personal list and find it again
  - Action: While logged in, click the "Save" (bookmark) icon on a post, then navigate to the "My Saved Posts" list page.
  - Expected: The saved post appears in the personal saved list with its title, and clicking it opens the original post.

- [ ] FT-08: System automatically generates intelligent tags from post content
  - Action: Publish a post whose body contains Python code (e.g., a fenced ` ```python ` block with `def`/`print`), with no manually added intelligent tags, then open the published post.
  - Expected: The post displays system-generated intelligent tags such as "Python" derived from the code content, shown separately from custom tags.
  - Bug Report:
    - Issue: Intelligent Tags Not Displayed on Post Page
    - Actual: The system does generate intelligent tags from the content (the post's stored data contains autoTags "Python", "Life", "Code Examples"; they also appear in the editor's "Intelligent Tags (auto-detected)" section and in the filter panel's "Intelligent Tags" list). However, the published post page displays ONLY the custom tag "Technology" — the generated intelligent tags are not rendered on the post page at all, neither separately nor alongside custom tags.

- [X] FT-09: Filtering by combined custom + intelligent tags works
  - Action: On the post list, select the custom tag "Technology" and the intelligent tag "Python" together and apply the filter.
  - Expected: Only posts carrying BOTH tags are listed (e.g., "Technology + Python"); posts with only one of the tags are excluded.

- [X] FT-10: User can save a frequently-used tag group and reapply it
  - Action: Apply a tag combination (e.g., "Technology" + "Python"), click "Save This Tag Group" and name it; then clear filters and reapply the saved group from the saved-groups list.
  - Expected: The named tag group appears in the saved-groups list, and clicking it re-applies the exact same combined filter results without re-selecting tags.

- [X] FT-11: Author backend shows per-tag views, likes, and comment counts
  - Action: Log in as the author, open the personal dashboard/analytics backend, and locate the per-tag statistics table.
  - Expected: Each tag used by the author's posts shows the aggregated page views, like counts, and comment counts for the posts under that tag.

- [X] FT-12: Author can generate a tag popularity analysis report
  - Action: In the author dashboard, click "Generate Tag Popularity Report".
  - Expected: A report is produced that ranks/compares tags by their statistics (views, likes, comments), and the numbers shown match the per-tag statistics in the dashboard.

## Constraint

- [X] CS-01: Post cannot be published with empty required fields
  - Action: In the "New Post" editor, leave the title (or body) empty and click "Publish".
  - Expected: The post is NOT created; a validation message such as "Title is required" is shown next to the empty field.

- [ ] CS-02: Author cannot edit posts owned by another author
  - Action: While logged in, open a post published by a different author.
  - Expected: No "Edit" button is shown on the post page; navigating directly to that post's edit URL is denied with an access-denied message.
  - Bug Report:
    - Issue: Silent Access Denial Without Message
    - Actual: No "Edit" button is shown on another author's post page (only Like/Save/Share) ✓, and navigating directly to `/edit/post-1` is denied — but via a silent redirect back to `/post/post-1`. No access-denied message or notification of any kind is displayed, so the user is not informed why the editor did not open.

- [X] CS-03: Liking a post twice does not inflate the count
  - Action: While logged in, click the "Like" button on the same post twice in a row and observe the count.
  - Expected: The second click removes the user's like (count returns to the original value) rather than incrementing it again.

## Interaction

- [X] IX-01: Success toast appears after a post is published
  - Action: Publish a valid post from the editor.
  - Expected: A success toast/notification (e.g., "Post published successfully") appears near the publish button and auto-dismisses, then the user is taken to the published post or profile page.

- [X] IX-02: Like button state and count update instantly without page reload
  - Action: Click the "Like" (heart) button on a post and observe the button and count.
  - Expected: The heart icon immediately switches to its filled/active state and the count updates in place, with no full page reload required.

## Content

- [X] CT-01: Markdown content is rendered as formatted rich text
  - Action: Open a post whose body contains Markdown (`# heading`, `**bold**`, a fenced code block, a list) from the default data.
  - Expected: The post page shows a rendered heading, bold text, a syntax-styled code block, and bulleted list — not the raw Markdown syntax characters.

- [X] CT-02: Intelligent tags are relevant to the post content
  - Action: Inspect the intelligent tags shown on several default posts (e.g., a code-heavy article and a non-technical article).
  - Expected: Each post's intelligent tags are keywords actually reflected in its content (e.g., "Python"/"Frontend Development" only on code-related articles), not random or identical tags across unrelated posts.

- [ ] CT-03: Custom tags and intelligent tags are visually distinguished and correctly labeled
  - Action: Open a post that has both author-added custom tags (e.g., "Technology", "Life", "Reading Notes") and system intelligent tags; also inspect the tag filter UI.
  - Expected: The two tag types are displayed with distinct labels/visual styling (e.g., "Custom" vs "Intelligent" sections or colors) on both the post page and the tag filter panel, with no tag miscategorized.
  - Bug Report:
    - Issue: Missing Tag-Type Distinction on Post Page
    - Actual: The tag filter panel correctly distinguishes the two types with separate labeled sections ("Custom Tags" and "Intelligent Tags" with icons). However, on the post detail page, only custom tags are rendered (e.g., post-1 shows "Programming", "Best Practices", "Software Development" — its custom tags — while its intelligent tags "JavaScript", "Code Examples" are absent; my test post shows only "Technology" with its "Python"/"Life"/"Code Examples" intelligent tags missing). The post page displays no "Custom"/"Intelligent" labels, and all rendered chips share identical styling, so the two tag types are not visually distinguished on the post page.
