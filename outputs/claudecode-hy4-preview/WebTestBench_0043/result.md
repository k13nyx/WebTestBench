I've completed all checklist items. Here are the results:

# Test Result

## Functionality

- [X] FT-01: New user can sign up and access an authenticated session
  - Action: Open the home page, click **Sign Up**, complete the registration form with a valid new email, username and password, then submit.
  - Expected: Account is created, the user is logged in, and the header shows the new username (no error message).

- [X] FT-02: Author can create a post in Markdown and publish it with a custom tag
  - Action: Click **New Post**, enter a title, type Markdown content (e.g. `# Heading`, `**bold**`, `[link](url)`, a fenced ` ```python ` code block), add a custom tag **Technology** in the Custom Tags field, then click **Publish**.
  - Expected: Post is published, the post detail page shows the content rendered from Markdown, and the custom tag **Technology** is displayed on the post.

- [X] FT-03: Author can edit an existing published post and the update goes live
  - Action: Open an existing post from the author's own account, click **Edit**, change the title and body text, add another custom tag **Reading Notes**, then click **Save / Update**.
  - Expected: Success confirmation is shown; reopening the post shows the new title, new body text, and both **Technology** and **Reading Notes** custom tags.

- [X] FT-04: Published posts appear on the author's own profile page
  - Action: Sign in as an author, click the username/avatar in the header and open the profile page.
  - Expected: The profile page shows the author's name and lists all posts that this author has published (including the post just created/edited); drafts/unpublished posts are not listed.

- [X] FT-05: Visitor can open any post from the listing and read the full content
  - Action: While signed out (or in a session not owning the post), open the blog listing and click any post title.
  - Expected: The full post page opens showing the complete title, rendered body content, author name, and publish date — no truncated/unavailable content.

- [X] FT-06: Visitor can leave a comment under a post
  - Action: On a post's detail page, type text into the **Comment** field and click **Post Comment / Submit**.
  - Expected: The comment appears in the comment list under the post with its text, commenter name and timestamp, and the post's comment count increases by 1.

- [X] FT-07: Visitor can like a post and the like count is tracked correctly
  - Action: On a post's detail page, note the like count, click the **Like** button once, and reload the page.
  - Expected: Count increases by exactly 1, the button shows a "liked/active" state, and the new count persists after reload; clicking **Like** again removes the like and returns the count to the previous value.

- [X] FT-08: Visitor can save a post to a personal list and find it again
  - Action: On a post's detail page, click **Save / Bookmark**, then open the personal saved list page (e.g. **My List / Saved**).
  - Expected: The post appears in the saved list with its title and author, and clicking it there opens the same post detail page.

- [ ] FT-09: System automatically extracts core keywords as intelligent tags from the content
  - Action: Publish (or open) a code-related article whose body repeatedly mentions Python and frontend development terms.
  - Expected: The post displays auto-generated intelligent tags (e.g. **Python**, **Frontend Development**) that were not entered manually, and they are derived from the article content.
  - Bug Report:
    - Issue: Intelligent tags extracted but never rendered on the post
    - Actual: Keyword extraction does work internally — the editor shows "Intelligent Tags (auto-detected) / Suggested based on content: Python, TypeScript, DevOps, Tutorial, Design" and the published post is stored with `autoTags: ["Python"]`. However, neither the post detail page nor the listing card renders `autoTags`. On `/post/post-1794076469485` the only tags shown at the top of the article are the custom tags **Technology** and **Reading Notes**; a text search for an element whose text is exactly "Python" returns no tag element anywhere in the article. Visiting readers therefore never see the promised auto-generated intelligent tags.

- [ ] FT-10: Visitor can filter articles by custom tag, by intelligent tag, and by a combined pair
  - Action: In the filter panel, first select custom tag **Technology**; then select intelligent tag **Python** as well, so both are active.
  - Expected: The listing narrows to only articles matching the selected tag(s); with **Technology + Python** selected, results are the intersection (every result has both tags) and no matching article is missing.
  - Bug Report:
    - Issue: Incorrect "No posts match the selected tags." empty-state text when a filter combination matches exactly one article
    - Actual: The AND/intersection logic itself works — selecting custom tag **Technology** gives "Filtered Stories (3)" (post-1794076469485, post-1794076701480, post-3, all carrying `Technology`), and adding the intelligent tag **Python** narrows to "Filtered Stories (2)" (post-1794076469485 + post-1794076701480), i.e. the correct intersection of the two dimensions. But when a filter combination matches exactly one article (e.g. **Technology + Python** before the second Python article existed, or the intelligent tag **Python** alone), the page simultaneously renders the matching article in the featured slot, the heading "Filtered Stories (1)", and an empty-state paragraph "No posts match the selected tags." — telling the reader there are no results while a result is displayed.

- [X] FT-11: User can save a frequently-used tag group and re-apply it from quick access
  - Action: With **Technology + Python** selected, click **Save as Tag Group**, name it, confirm; clear all filters, then click the saved group in the quick-access area.
  - Expected: The saved group is listed in quick access, and clicking it re-applies exactly the same tag combination, showing the same result set.

- [ ] FT-12: Author can view per-tag metrics in the personal backend and generate a tag popularity report
  - Action: Sign in as author, open the personal backend (dashboard), go to the tag analytics section, view the metrics for a tag, then click **Generate Report**.
  - Expected: For each tag, page views, like counts and comment counts of the articles under it are displayed; the report is generated and shows a tag popularity analysis (ranking/metrics) for the author's tags.
  - Bug Report:
    - Issue: No "Generate Report" action exists; page-views metric is never populated
    - Actual: The author backend is the **Analytics** tab of the profile page (`/profile/user-1794076436766`). It renders a static card titled "Tag Popularity Report" with totals (Total Tags 3, Total Views 0, Total Likes 2, Total Comments 2) and a ranking: #1 Technology (2 posts, 0/1/1), #2 Python (2 posts, 0/1/1), #3 Reading Notes (1 post, 0/0/0). There is **no** "Generate Report" button or any other control in the panel (button query returns an empty list), so the required action cannot be performed. Additionally, the page-views metric is always 0: the post record for `/post/post-1794076701480` kept `views: 0` after three separate page visits (publish redirect, edit redirect, and a full reload), and post detail pages display no view counter at all, so the views column is blank/placeholder even for articles that have likes and comments.

## Constraint

- [ ] CS-01: Signup is blocked for invalid or already-used credentials
  - Action: Try to sign up with (a) empty required fields, (b) a malformed email (e.g. `abc`), (c) an email that already has an account.
  - Expected: Each attempt is rejected with a clear inline error message, no account is created, and no session is started.
  - Bug Report:
    - Issue: No validation feedback for malformed email; no inline message for empty fields
    - Actual: (a) With all three fields empty the "Create Account" button is `disabled`, so submission is prevented — but no inline or explanatory error message is displayed. (b) With name "Test User", email `abc` and password `testpass123` the button becomes **enabled**, and clicking it silently does nothing: the URL stays `/signup`, no error text appears anywhere in the document body, no toast is rendered in the notifications region, `blog_current_user` remains `null`, and no user is added. The attempt is silently ignored rather than "rejected with a clear inline error message". (c) Using the already-registered `sarah@example.com` correctly shows the toast "Sign up failed — An account with this email already exists." and creates no account/session.

- [ ] CS-02: Visitors who are not signed in cannot create, edit or publish posts or open the author backend
  - Action: Sign out, then try to open the post editor / **New Post** page and the author backend dashboard directly.
  - Expected: Access is blocked — the user is redirected to sign in or shown a "please sign in" message, and no post can be created, edited or published.
  - Bug Report:
    - Issue: /write renders a blank page for signed-out visitors with no redirect or sign-in prompt
    - Actual: After signing out, opening `http://localhost:6043/write` directly leaves the URL at `/write` but renders an **empty `<main>`** — no editor, no redirect to `/login`, and no "please sign in" message (only the footer is on the page). By contrast, `/edit/post-1794076469485` correctly redirects to `/login`, and the author backend (the Analytics tab) is correctly hidden from visitors — another author's public `/profile/user-2` shows only "Posts by Marcus Webb" with no Analytics tab. So creation is blocked in effect, but the "New Post" route fails to give any redirect or message.

- [X] CS-03: An empty comment cannot be submitted
  - Action: On a post's detail page, click **Post Comment / Submit** with an empty comment field (and once with only spaces).
  - Expected: Submission is blocked with a validation message; no comment is added and the comment count does not change.

## Interaction

- [ ] IX-01: Like and Save actions respond immediately with visible state feedback
  - Action: Click **Like** and then **Save / Bookmark** on a post, and observe the buttons without reloading the page.
  - Expected: The Like button instantly changes to a filled/active look with the count updated, the Save button changes to a "saved/active" look, and a confirmation (toast or message) is shown.
  - Bug Report:
    - Issue: No confirmation (toast/message) after Like or Save
    - Actual: Both buttons do update instantly and correctly without a reload — the Like button switched from `0` to `1` with its icon becoming `lucide-heart h-4 w-4 fill-current animate-heart-beat` on a `bg-primary/10 text-primary` background, and the Save button immediately changed its label to "Unsave" with the `lucide-bookmark-check` icon and `bg-accent/10 text-accent` styling. However, no toast or any other confirmation message appeared: the notifications region stayed empty after both clicks (verified again 400 ms after clicking "Create Account"-style actions in the same session showed toasts do work, e.g. "Post published!", "Post updated!", "Sign up failed").

- [X] IX-02: Applied filters are shown as highlighted, removable selections that update results in place
  - Action: Select a custom tag in the filter panel, then remove it by clicking its ✕/deselecting it.
  - Expected: The active tag is visually highlighted while selected, the article list updates without a page reload, and removing it restores the unfiltered list.

## Content

- [X] CT-01: Post content renders Markdown correctly with no raw syntax visible
  - Action: Open a post written in Markdown containing a heading, bold text, a link and a code block.
  - Expected: Each element is rendered as formatted output (formatted heading, bold text, clickable link, formatted code block); no raw markers such as `#`, `**` or ```` ``` ```` are shown as plain text in the body.

- [ ] CT-02: Tags are labeled correctly, with custom tags distinguished from intelligent tags and relevant to the article
  - Action: View a published article and inspect its displayed tags.
  - Expected: Custom tags (author-added, e.g. **Technology**, **Reading Notes**) and intelligent tags (auto-extracted, e.g. **Python**, **Frontend Development**) are shown separately/labeled differently, and the extracted keywords are clearly related to the article's content.
  - Bug Report:
    - Issue: Intelligent tags missing from article view; the two tag types are never shown together or labeled differently on a post
    - Actual: On the article page the tag row contains only the author's custom tags (`Technology`, `Reading Notes`), rendered with identical `bg-secondary text-secondary-foreground` badges and no section labels; the auto-extracted keyword **Python** is absent entirely, so nothing distinguishes custom from intelligent tags for a reader. (The two categories are only separated inside the editor — "Custom Tags" vs. "Intelligent Tags (auto-detected)" — and in the filter dialog, which does list **Python** under "Intelligent Tags".) The extracted keyword that is produced is relevant to the content (`Python`, from an article about Python/frontend development), but a visitor never sees it.

- [ ] CT-03: Tag analytics display correct, clearly labeled metrics
  - Action: In the author's backend analytics, compare the per-tag page views / likes / comments with the counts shown on the corresponding post pages.
  - Expected: Metrics are labeled "page views", "likes", "comments" (or equivalent) and the values match the counts displayed on the articles; no tag shows blank or placeholder values for articles that have activity.
  - Bug Report:
    - Issue: Metric values are unlabeled (icons only) and the page-views metric is always 0
    - Actual: Likes and comments do reconcile correctly — the Analytics tab shows Technology: 2 posts, likes 1, comments 1; Python: 2 posts, likes 1, comments 1; Reading Notes: 1 post, likes 0, comments 0, which matches the post pages (`/post/post-1794076701480` = like count 1, "Comments (1)"; `/post/post-1794076469485` = like count 0, "Comments (0)"). However, each per-tag metric is rendered as `<span>[icon]0</span>` with no text label, `title`, or `aria-label` (a query for `[title]`/`[aria-label]` inside the analytics panel returns nothing), so nothing says "page views / likes / comments". And the page-views value is blank/placeholder: it shows 0 for every tag even though the articles under them have likes and comments, because view counts are never recorded (`views: 0` persisted across three visits) and post pages show no view counter to compare against.