# Test Checklist

> **Testing data note:** Use the application's default data (pre-existing posts, tags, comments) wherever possible. Only one new account registration is required to test the sign-up flow; all author-side tests use this account. Visitor-side tests can rely on default published posts.

## Functionality
- [ ] FT-01: New user can sign up for an account
  - Action: Open the "Sign Up" page, fill in username, email, and password, and click the "Sign Up" button.
  - Expected: Account is created, user is logged in and redirected to their own (empty) profile page; logging out and back in with the same credentials succeeds.

- [ ] FT-02: Author can write a post in Markdown and publish it to their profile page
  - Action: While logged in, click "New Post", enter a title and Markdown body (e.g., `# Heading`, `**bold**`, fenced code block), add a custom tag "Technology", and click "Publish".
  - Expected: Post is saved and appears in the author's profile page post list with its title, custom tag, and publish date.

- [ ] FT-03: Author can edit a published post and changes persist
  - Action: Open one of the author's own published posts, click "Edit", modify the title and body text, and click "Save".
  - Expected: Post detail page shows the updated title and content; the profile page post list also reflects the new title.

- [ ] FT-04: Visitor can open and read any published post
  - Action: While logged out, browse the post list, open a default published post by clicking its title.
  - Expected: The post's full content is displayed on a dedicated post page, including author name and publish date.

- [ ] FT-05: Visitor can leave a comment under a post
  - Action: On a post page, type a comment into the comment input box and click "Submit Comment".
  - Expected: The comment appears in the post's comment list showing the commenter's name, comment text, and timestamp.

- [ ] FT-06: Visitor can like a post
  - Action: On a post page, click the "Like" button and note the count before and after.
  - Expected: The like count increments by exactly 1.

- [ ] FT-07: Visitor can save a post to a personal list and find it again
  - Action: While logged in, click the "Save" (bookmark) icon on a post, then navigate to the "My Saved Posts" list page.
  - Expected: The saved post appears in the personal saved list with its title, and clicking it opens the original post.

- [ ] FT-08: System automatically generates intelligent tags from post content
  - Action: Publish a post whose body contains Python code (e.g., a fenced ` ```python ` block with `def`/`print`), with no manually added intelligent tags, then open the published post.
  - Expected: The post displays system-generated intelligent tags such as "Python" derived from the code content, shown separately from custom tags.

- [ ] FT-09: Filtering by combined custom + intelligent tags works
  - Action: On the post list, select the custom tag "Technology" and the intelligent tag "Python" together and apply the filter.
  - Expected: Only posts carrying BOTH tags are listed (e.g., "Technology + Python"); posts with only one of the tags are excluded.

- [ ] FT-10: User can save a frequently-used tag group and reapply it
  - Action: Apply a tag combination (e.g., "Technology" + "Python"), click "Save This Tag Group" and name it; then clear filters and reapply the saved group from the saved-groups list.
  - Expected: The named tag group appears in the saved-groups list, and clicking it re-applies the exact same combined filter results without re-selecting tags.

- [ ] FT-11: Author backend shows per-tag views, likes, and comment counts
  - Action: Log in as the author, open the personal dashboard/analytics backend, and locate the per-tag statistics table.
  - Expected: Each tag used by the author's posts shows the aggregated page views, like counts, and comment counts for the posts under that tag.

- [ ] FT-12: Author can generate a tag popularity analysis report
  - Action: In the author dashboard, click "Generate Tag Popularity Report".
  - Expected: A report is produced that ranks/compares tags by their statistics (views, likes, comments), and the numbers shown match the per-tag statistics in the dashboard.

## Constraint
- [ ] CS-01: Post cannot be published with empty required fields
  - Action: In the "New Post" editor, leave the title (or body) empty and click "Publish".
  - Expected: The post is NOT created; a validation message such as "Title is required" is shown next to the empty field.

- [ ] CS-02: Author cannot edit posts owned by another author
  - Action: While logged in, open a post published by a different author.
  - Expected: No "Edit" button is shown on the post page; navigating directly to that post's edit URL is denied with an access-denied message.

- [ ] CS-03: Liking a post twice does not inflate the count
  - Action: While logged in, click the "Like" button on the same post twice in a row and observe the count.
  - Expected: The second click removes the user's like (count returns to the original value) rather than incrementing it again.

## Interaction
- [ ] IX-01: Success toast appears after a post is published
  - Action: Publish a valid post from the editor.
  - Expected: A success toast/notification (e.g., "Post published successfully") appears near the publish button and auto-dismisses, then the user is taken to the published post or profile page.

- [ ] IX-02: Like button state and count update instantly without page reload
  - Action: Click the "Like" (heart) button on a post and observe the button and count.
  - Expected: The heart icon immediately switches to its filled/active state and the count updates in place, with no full page reload required.

## Content
- [ ] CT-01: Markdown content is rendered as formatted rich text
  - Action: Open a post whose body contains Markdown (`# heading`, `**bold**`, a fenced code block, a list) from the default data.
  - Expected: The post page shows a rendered heading, bold text, a syntax-styled code block, and bulleted list — not the raw Markdown syntax characters.

- [ ] CT-02: Intelligent tags are relevant to the post content
  - Action: Inspect the intelligent tags shown on several default posts (e.g., a code-heavy article and a non-technical article).
  - Expected: Each post's intelligent tags are keywords actually reflected in its content (e.g., "Python"/"Frontend Development" only on code-related articles), not random or identical tags across unrelated posts.

- [ ] CT-03: Custom tags and intelligent tags are visually distinguished and correctly labeled
  - Action: Open a post that has both author-added custom tags (e.g., "Technology", "Life", "Reading Notes") and system intelligent tags; also inspect the tag filter UI.
  - Expected: The two tag types are displayed with distinct labels/visual styling (e.g., "Custom" vs "Intelligent" sections or colors) on both the post page and the tag filter panel, with no tag miscategorized.