# Test Checklist

## Functionality

- [ ] FT-01: New user can sign up and access an authenticated session
  - Action: Open the home page, click **Sign Up**, complete the registration form with a valid new email, username and password, then submit.
  - Expected: Account is created, the user is logged in, and the header shows the new username (no error message).

- [ ] FT-02: Author can create a post in Markdown and publish it with a custom tag
  - Action: Click **New Post**, enter a title, type Markdown content (e.g. `# Heading`, `**bold**`, `[link](url)`, a fenced ` ```python ` code block), add a custom tag **Technology** in the Custom Tags field, then click **Publish**.
  - Expected: Post is published, the post detail page shows the content rendered from Markdown, and the custom tag **Technology** is displayed on the post.

- [ ] FT-03: Author can edit an existing published post and the update goes live
  - Action: Open an existing post from the author's own account, click **Edit**, change the title and body text, add another custom tag **Reading Notes**, then click **Save / Update**.
  - Expected: Success confirmation is shown; reopening the post shows the new title, new body text, and both **Technology** and **Reading Notes** custom tags.

- [ ] FT-04: Published posts appear on the author's own profile page
  - Action: Sign in as an author, click the username/avatar in the header and open the profile page.
  - Expected: The profile page shows the author's name and lists all posts that this author has published (including the post just created/edited); drafts/unpublished posts are not listed.

- [ ] FT-05: Visitor can open any post from the listing and read the full content
  - Action: While signed out (or in a session not owning the post), open the blog listing and click any post title.
  - Expected: The full post page opens showing the complete title, rendered body content, author name, and publish date — no truncated/unavailable content.

- [ ] FT-06: Visitor can leave a comment under a post
  - Action: On a post's detail page, type text into the **Comment** field and click **Post Comment / Submit**.
  - Expected: The comment appears in the comment list under the post with its text, commenter name and timestamp, and the post's comment count increases by 1.

- [ ] FT-07: Visitor can like a post and the like count is tracked correctly
  - Action: On a post's detail page, note the like count, click the **Like** button once, and reload the page.
  - Expected: Count increases by exactly 1, the button shows a "liked/active" state, and the new count persists after reload; clicking **Like** again removes the like and returns the count to the previous value.

- [ ] FT-08: Visitor can save a post to a personal list and find it again
  - Action: On a post's detail page, click **Save / Bookmark**, then open the personal saved list page (e.g. **My List / Saved**).
  - Expected: The post appears in the saved list with its title and author, and clicking it there opens the same post detail page.

- [ ] FT-09: System automatically extracts core keywords as intelligent tags from the content
  - Action: Publish (or open) a code-related article whose body repeatedly mentions Python and frontend development terms.
  - Expected: The post displays auto-generated intelligent tags (e.g. **Python**, **Frontend Development**) that were not entered manually, and they are derived from the article content.

- [ ] FT-10: Visitor can filter articles by custom tag, by intelligent tag, and by a combined pair
  - Action: In the filter panel, first select custom tag **Technology**; then select intelligent tag **Python** as well, so both are active.
  - Expected: The listing narrows to only articles matching the selected tag(s); with **Technology + Python** selected, results are the intersection (every result has both tags) and no matching article is missing.

- [ ] FT-11: User can save a frequently-used tag group and re-apply it from quick access
  - Action: With **Technology + Python** selected, click **Save as Tag Group**, name it, confirm; clear all filters, then click the saved group in the quick-access area.
  - Expected: The saved group is listed in quick access, and clicking it re-applies exactly the same tag combination, showing the same result set.

- [ ] FT-12: Author can view per-tag metrics in the personal backend and generate a tag popularity report
  - Action: Sign in as author, open the personal backend (dashboard), go to the tag analytics section, view the metrics for a tag, then click **Generate Report**.
  - Expected: For each tag, page views, like counts and comment counts of the articles under it are displayed; the report is generated and shows a tag popularity analysis (ranking/metrics) for the author's tags.

## Constraint

- [ ] CS-01: Signup is blocked for invalid or already-used credentials
  - Action: Try to sign up with (a) empty required fields, (b) a malformed email (e.g. `abc`), (c) an email that already has an account.
  - Expected: Each attempt is rejected with a clear inline error message, no account is created, and no session is started.

- [ ] CS-02: Visitors who are not signed in cannot create, edit or publish posts or open the author backend
  - Action: Sign out, then try to open the post editor / **New Post** page and the author backend dashboard directly.
  - Expected: Access is blocked — the user is redirected to sign in or shown a "please sign in" message, and no post can be created, edited or published.

- [ ] CS-03: An empty comment cannot be submitted
  - Action: On a post's detail page, click **Post Comment / Submit** with an empty comment field (and once with only spaces).
  - Expected: Submission is blocked with a validation message; no comment is added and the comment count does not change.

## Interaction

- [ ] IX-01: Like and Save actions respond immediately with visible state feedback
  - Action: Click **Like** and then **Save / Bookmark** on a post, and observe the buttons without reloading the page.
  - Expected: The Like button instantly changes to a filled/active look with the count updated, the Save button changes to a "saved/active" look, and a confirmation (toast or message) is shown.

- [ ] IX-02: Applied filters are shown as highlighted, removable selections that update results in place
  - Action: Select a custom tag in the filter panel, then remove it by clicking its ✕/deselecting it.
  - Expected: The active tag is visually highlighted while selected, the article list updates without a page reload, and removing it restores the unfiltered list.

## Content

- [ ] CT-01: Post content renders Markdown correctly with no raw syntax visible
  - Action: Open a post written in Markdown containing a heading, bold text, a link and a code block.
  - Expected: Each element is rendered as formatted output (formatted heading, bold text, clickable link, formatted code block); no raw markers such as `#`, `**` or ```` ``` ```` are shown as plain text in the body.

- [ ] CT-02: Tags are labeled correctly, with custom tags distinguished from intelligent tags and relevant to the article
  - Action: View a published article and inspect its displayed tags.
  - Expected: Custom tags (author-added, e.g. **Technology**, **Reading Notes**) and intelligent tags (auto-extracted, e.g. **Python**, **Frontend Development**) are shown separately/labeled differently, and the extracted keywords are clearly related to the article's content.

- [ ] CT-03: Tag analytics display correct, clearly labeled metrics
  - Action: In the author's backend analytics, compare the per-tag page views / likes / comments with the counts shown on the corresponding post pages.
  - Expected: Metrics are labeled "page views", "likes", "comments" (or equivalent) and the values match the counts displayed on the articles; no tag shows blank or placeholder values for articles that have activity.