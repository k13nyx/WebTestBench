I've completed the full test run. Here is the checklist report.

# Test Result

## Functionality

- [X] FT-01: Visitor can register a new account via sign-up form
  - Action: Click "Sign up", fill in username/email and password, submit.
  - Expected: Account is created, user is signed in, and a profile page is shown for the new user.
  - Note: Account created (toast "Welcome to Inkwell! / Your account has been created successfully."), user auto-signed-in (nav shows "Saved", "Write", avatar). Sign-up redirects to the home feed rather than the profile; the new user's profile page does exist and renders correctly (name "QA Tester", "Joined 2026-11-07", 0 posts, tabs Published/Drafts/Analytics) at /profile/user-1794059178561.

- [X] FT-02: Author can create a post with Markdown content and a title
  - Action: From the author dashboard click "New Post", enter a title and body containing Markdown syntax (e.g. `# Heading`, `**bold**`, a list), save.
  - Expected: The post is saved and its title and body appear in the author's post list.
  - Note: "Write New Post" → title/body/custom tag filled → "Publish" produced toast "Post published! Your post is now live." The post appears in the author's profile list (Published (2)) with title + body excerpt.

- [X] FT-03: Markdown syntax is rendered as formatted content on the post page
  - Action: Open a post whose body contains Markdown headings, bold text, and lists.
  - Expected: The post page shows rendered headings/bold/lists, not raw `#`, `**`, or `-` characters.
  - Note: Post page DOM contains `<h1>Updated Introduction</h1>`, `<strong>Python</strong>`, `<strong>Frontend Development</strong>` and a real `<ul>/<li>` list — no raw Markdown characters in the rendered body.

- [X] FT-04: Author can edit an existing post and save the changes
  - Action: In the author dashboard open an existing post, click "Edit", change the title and body, save, then reopen the post.
  - Expected: The updated title and body are shown; the previous version is no longer displayed.
  - Note: Editor (pencil link → /edit/post-1794059202691) → title/body changed → "Save Changes" → toast "Post updated!"; reopening the post shows the new title "Python Frontend Notes Updated" and the new body. Minor defect: the dashboard post list still renders the *pre-edit* body excerpt (stale `excerpt` field).

- [X] FT-05: Published post appears on the author's public profile page
  - Action: Publish a post, then open the author's public profile page.
  - Expected: The post title appears in the profile's post list and opens the correct post when clicked.
  - Note: Profile shows "2 posts" and both titles; clicking "Python Frontend Notes Updated" opened /post/post-1794059202691 with the matching content.

- [X] FT-06: A visitor can open a post detail page and read the full content
  - Action: From a profile or article list, click any post title.
  - Expected: A detail page shows the post title, author, full body, and its like/comment counts.
  - Note: Detail page shows title, author + date + read time, full body, like-count button and "Comments (n)" heading.

- [X] FT-07: A visitor can leave a comment under a post
  - Action: Open a post, type text into the comment box, submit.
  - Expected: The comment (with author name and timestamp) appears in the comment list under the post and the comment count increases by 1.
  - Note: "Comments (0)" → "Comments (1)"; comment rendered with author "QA Tester", date 2026-11-07 and the submitted text.

- [X] FT-08: A visitor can like a post and the like count updates
  - Action: Open a post, click the "Like" button, then reload the post.
  - Expected: Like count increases by 1 and the like state is retained after reload.
  - Note: Count went 0 → 1 with the button switching to the active style (`bg-primary/10 text-primary`); after a full page reload the count stayed 1.

- [X] FT-09: A visitor can save a post to a personal saved list and remove it
  - Action: Open a post, click "Save"; open the "Saved" / bookmarks page; then click "Remove" on that post.
  - Expected: The post appears in the saved list while saved, disappears after removal, and the post's save state is reflected on the post page.
  - Note: "Save" → "Unsave"; /saved showed "Saved Posts — 1 post saved for later" with the post card; the card's remove control reduced it to "0 posts saved for later" / "No saved posts yet"; the post page's button reverted to "Save".

- [X] FT-10: Author can view per-tag analytics (views, likes, comments) in the backend
  - Action: Sign in as an author, open the backend analytics section, and view the tag statistics table.
  - Expected: Each tag used by that author's posts is listed with page views, like count, and comment count values.
  - Note: The "Analytics" tab on the author's own profile lists all 7 of the author's tags (Technology, Design, Python, Testing, Best Practices, Productivity, Reading Notes), each with three icon/value columns for views, likes and comments. Caveat: the view column is always 0 because views are never incremented (see CT-03).

- [X] FT-11: Author can generate a tag popularity analysis report
  - Action: In the backend analytics section click the button to generate a tag popularity report.
  - Expected: A report is displayed ranking/summarising tags by popularity (e.g. view/like/comment totals and ordering), using the author's own posts.
  - Note: The report ("Tag Popularity Report" with Total Tags / Total Views / Total Likes / Total Comments and a ranked list #1–#7) renders automatically on opening the Analytics tab — there is no separate "generate report" button. Ranking is by post count, not by engagement (Design has 1 like/1 comment yet ranks below Technology and above Python which has 0/0).

- [X] FT-12: Visitors can filter articles by custom tag and by intelligent tag
  - Action: On the article list page select a custom tag (e.g. "Technology") and separately select an intelligent tag (e.g. "Python"), and apply the filter each time.
  - Expected: Only posts carrying the selected custom tag are listed for the first case, and only posts whose extracted keywords include the intelligent tag are listed for the second.
  - Note: Custom "Technology" → "Filtered Stories (3)": both of the author's posts + seeded post-3 (the only other post with that custom tag). Intelligent "Python" → exactly 1 post ("Python Frontend Notes Updated"); posts tagged only with the word Technology (Weekend Garden Journal) or with other auto tags (post-1/post-2/post-3) were excluded. Caveat: when only one post matches, the list block still renders "No posts match the selected tags." under a "Filtered Stories (1)" heading (see CT-04).

## Constraint

- [X] CS-01: Sign-up rejects duplicate usernames and invalid input
  - Action: Attempt to sign up with a username that already exists, and separately with an empty password or mismatched password confirmation.
  - Expected: Each attempt is blocked with a visible validation error and no account is created.
  - Note: The form has no username field (Full Name / Email / Password) and no password-confirmation field; email is the unique account identifier. Signing up with the existing email was rejected with the visible toast "Sign up failed — An account with this email already exists." and no account created. An invalid password ("abc") or an empty password disables "Create Account" and the unmet rules ("At least 8 characters", "Contains a number") lose their green check mark. Caveat: display name is not unique-checked — "QA Tester" + a new email created a second account named "QA Tester".

- [X] CS-02: A post cannot be published without a title and body
  - Action: In the new/edit post form clear the title (and separately the body) and attempt to save/publish.
  - Expected: Submission is blocked with an error message and no post is created or published.
  - Note: Empty form → toast "Title required / Please add a title for your post."; title only → toast "Content required / Please write some content for your post."; in both cases the app stayed on /write and no post was created.

- [ ] CS-03: A user cannot like the same post twice
  - Action: Click the "Like" button twice on the same post (same signed-in account).
  - Expected: The count increases only once and the button shows the already-liked state.
  - Bug Report:
    - Issue: Like button toggles off (implements "unlike") on the second click instead of being idempotent.
    - Actual: First click: count 0 → 1, button becomes active (`bg-primary/10 text-primary`). Second click on the same account: count 1 → 0 and the button reverts to the inactive style, i.e. the count no longer "increases only once" and the already-liked state is not retained (an accidental double-click silently unlikes the post).

- [ ] CS-04: Comments require a signed-in account and non-empty text
  - Action: While signed out, open a post and try to comment; then while signed in, submit an empty comment box.
  - Expected: Signed-out users are prompted to sign in/login, and the empty comment is rejected with a validation message.
  - Bug Report:
    - Issue: Missing validation feedback for an empty comment (silent rejection).
    - Actual: The signed-out half passes — the comment box is replaced by "Join the conversation" with "Sign In" / "Sign Up" links. The signed-in half fails: with an empty (or whitespace-only) comment the "Post Comment" button is simply disabled and pressing Enter in the box produces no message — no validation error, toast or inline text is displayed, so the user gets no explanation of why the comment cannot be posted.

- [ ] CS-05: Intelligent tags are generated from content, not from the author's custom tags
  - Action: Publish a post with content discussing Python and frontend development, adding only a custom tag such as "Technology"; then view the post's tag list.
  - Expected: The post shows the author's custom tag plus automatically extracted intelligent tags such as "Python" / "Frontend Development" derived from the body text.
  - Bug Report:
    - Issue: Intelligent tags are not displayed on the post and are not reliably derived from the body text.
    - Actual: The published post's tag list (post detail header) shows only the custom tag "Technology" — none of the intelligent tags are shown to readers. The editor's "Intelligent Tags (auto-detected)" for that post are Python, Testing, Best Practices, Productivity, Reading Notes: "Frontend Development", although present in the body, was not extracted, while "Productivity" and "Reading Notes" do not appear in the body at all.

- [X] CS-06: Combined tag search requires tags from both dimensions and matches posts having all selected tags
  - Action: Filter by custom tag "Technology" together with intelligent tag "Python" and apply.
  - Expected: Only posts having both "Technology" as a custom tag and "Python" as an extracted intelligent tag are listed; a post missing either one is excluded.
  - Note: With both chips active the UI states "(showing posts matching all selected tags)" and exactly one post was listed — "Python Frontend Notes Updated" (custom tag Technology + auto tag Python). "Weekend Garden Journal" (Technology, no Python), seeded post-3 (Technology, no Python) and post-1/post-2 (no Technology) were all excluded.

- [ ] CS-07: Only the signed-in user can access and modify their own backend analytics and saved lists
  - Action: Sign in as user A and try to open user B's backend/analytics view or saved-list URL directly; also try to reach the backend while signed out.
  - Expected: Access is denied or redirected to sign-in; no other user's analytics or saved items are revealed.
  - Bug Report:
    - Issue: Cross-user data leak — the saved-post list is global instead of per-user.
    - Actual: Signed in as QA Tester (user-1794059178561) and saved "The Art of Writing Clean Code"; after signing in as Marcus Webb (user-2), /saved showed "Saved Posts — 1 post saved for later" containing QA Tester's saved post, and the remove control deleted QA Tester's saved item (list went to "0 posts saved for later"). Root cause: the list is stored in one shared key (`blog_saved_posts` in localStorage). Secondary observations: another user's profile correctly hides the Drafts/Analytics tabs (only "Posts by …" is rendered) and /write while signed out renders no editor — but both render a blank main area instead of redirecting to sign-in, and a hard reload of /saved as a signed-in user also produced a blank page instead of the saved list.

## Interaction

- [X] IX-01: Post list filter controls reflect the selected tags and can be cleared
  - Action: Apply a custom tag filter on the article list, then switch the filter dimension to intelligent tag.
  - Expected: The active filter is visibly indicated, the result list updates immediately, and a clear/reset control removes the filter and restores the full list.
  - Note: Selecting Technology showed an "Active: Technology" chip, a "Filter by Tags 1" counter badge and immediately re-rendered the list to 3 posts; adding the intelligent tag Python produced a second chip + "2" badge and updated the result; selected tag buttons inside the dialog carry the selected style (`bg-primary/20 text-primary` vs `bg-primary/5`); the "Clear" control removed all chips/badges and restored the full "Latest Stories" list.

- [X] IX-02: Saved tag groups can be created, applied, and removed
  - Action: On the article list, select tags "Technology" + "Python", click "Save tag group", name it, save; later apply the saved group from the tag-group list, then delete that group.
  - Expected: The group appears in the saved groups list, applying it sets the same filters and results, and deleting it removes it from the list.
  - Note: "Save Filter" → dialog "Save Tag Filter" showing "Selected tags: Technology / Python" → named "Tech + Python" → the group appears under "Saved Filters" as "Tech + Python (2 tags)"; after clearing the filters, clicking the group restored both chips, the "2" badge, "(showing posts matching all selected tags)" and the identical single-post result; the delete control removed it and the list then read "No saved filters yet".

- [X] IX-03: Like and Save buttons show immediate state feedback on the post page
  - Action: Click "Like" and "Save" on a post and observe the buttons and counters.
  - Expected: The buttons switch to an active/liked/saved visual state and the like counter updates without a page error or reload.
  - Note: Like: counter 0 → 1 instantly and the button style changed to the active `bg-primary/10 text-primary`. Save: label changed "Save" → "Unsave" with the active style. No navigation, reload or console error occurred.

- [X] IX-04: Comment submission gives feedback and the comment box clears
  - Action: Post a comment under a post and observe the comment area.
  - Expected: The new comment is appended to the list, the comment count increments, and the comment input is cleared for the next comment.
  - Note: The comment was appended to the list with author/timestamp, heading changed "Comments (0)" → "Comments (1)", and the input value was cleared (button returned to disabled).

- [ ] IX-05: Author dashboard provides navigation to posts, tags, and analytics sections
  - Action: Sign in as an author and open the backend/dashboard.
  - Expected: Separate links or tabs exist for managing posts, managing/viewing tags, and viewing tag analytics, and each opens the expected content.
  - Bug Report:
    - Issue: Missing tags section in the author dashboard.
    - Actual: The dashboard (own profile page) exposes exactly three tabs — "Published (n)", "Drafts (n)" and "Analytics" (Published lists the posts, Drafts lists drafts / "No drafts", Analytics shows the tag report). There is no separate link or tab for managing or viewing tags: tags can only be edited inside the post editor, and the dedicated URL /tags returns the 404 page ("Oops! Page not found").

## Content

- [X] CT-01: Post detail page shows correct metadata for the post
  - Action: Open a post and inspect the header area.
  - Expected: The displayed title, author name, publication date, and tag labels all match the post's actual data.
  - Note: Header showed title "Python Frontend Notes Updated", author "QA Tester" (linked to /profile/user-1794059178561), date 2026-11-07 with "1 min read", and tag chip "Technology" — all matching the stored record (tags: ["Technology"]). (Only custom tags are displayed; see CS-05.)

- [ ] CT-02: Extracted intelligent tags are meaningful keywords found in the post body
  - Action: Publish a post about Python and frontend development, then list its intelligent tags.
  - Expected: The intelligent tags are real terms from the article content (e.g. "Python", "Frontend Development") and are not empty, duplicated, or unrelated placeholder words.
  - Bug Report:
    - Issue: Intelligent tags are drawn from a fixed vocabulary rather than extracted from the article body.
    - Actual: The Python/Frontend article received the intelligent tags "Python, Testing, Best Practices, Productivity, Reading Notes". Only "Python" and "Testing" occur in the body; "Frontend Development" (twice in the body) was never detected, while "Best Practices", "Productivity" and "Reading Notes" appear nowhere in the content. A second article (a garden journal about tomatoes and herbs) was auto-tagged "Design" — a term absent from its content.

- [ ] CT-03: Analytics tag list and report contain only the author's own tags and accurate counts
  - Action: Open the backend tag statistics and the popularity report, and compare with the author's posts.
  - Expected: Every listed tag belongs to that author, no other author's tags appear, and the view/like/comment numbers match the actual posts.
  - Bug Report:
    - Issue: Inaccurate view counts and double-counted report totals.
    - Actual: Tag ownership is correct (only the author's own tags are listed) and per-tag like/comment counts are correct (Technology 2 posts/1 like/1 comment; Design 1 post/1 like/1 comment; Python/Testing/Best Practices/Productivity/Reading Notes 1 post/0/0), but (a) every view value is 0 although both posts were opened many times — the view counter is never incremented (the seeded post-1 also stayed at 142 after being opened), and (b) the report's "Total Likes 2" and "Total Comments 2" count the single like and the single comment twice because the same post carries two tags, so the totals do not match the author's actual 1 like / 1 comment.

- [ ] CT-04: All displayed labels and empty states are relevant to blogging
  - Action: Review navigation labels, buttons, filter labels, and empty states (e.g. no posts, no saved items, no comments).
  - Expected: Labels use blogging-related wording (Posts, Comments, Tags, Saved, Likes) and empty states give a meaningful message; no placeholder, lorem-ipsum, or unrelated sample text is shown.
  - Bug Report:
    - Issue: Contradictory empty state shown when a filtered result does exist.
    - Actual: All labels are blogging-related and free of placeholder/lorem-ipsum text ("Posts", "Comments", "Custom Tags", "Intelligent Tags", "Saved Posts", "Save Filter", "Post Comment", "No published posts yet", "No drafts", "No saved posts yet", "No comments yet. Be the first to share your thoughts!"). However, when a tag filter yields exactly one matching post, the page renders that post and the heading "Filtered Stories (1)" while immediately below it shows the empty state "No posts match the selected tags." — a message that is not meaningful in that situation and contradicts the content displayed above it.