# Test Result

## Functionality
- [ ] FT-01: New visitor can sign up for an account.
  - Action: Click "Sign Up", enter a new unused email and a password, then click "Create Account".
  - Expected: The account is created, the user is logged in, and "My Profile" appears in the navigation.
  - Bug Report:
    - Issue: Incorrect Navigation Label (Missing Element)
    - Actual: Account was created and the user was logged in (welcome toast shown). The navigation shows only "Home", "Saved", "Write" and an avatar button "QA Author". No "My Profile" link is in the navigation. The avatar menu contains "Profile", "Saved Posts" and "Sign Out".

- [X] FT-02: Author can write a Markdown post and publish it to their profile.
  - Action: Click "New Post", enter title "QA Markdown Test", enter body "# Heading" on line 1 and "**bold text**" on line 2, then click "Publish".
  - Expected: The post appears on the author's profile page, "Heading" renders as a large heading, and "bold text" renders in bold.

- [ ] FT-03: Author can edit their own post.
  - Action: Open a post authored by the logged-in user, click "Edit", change the body text, then click "Save".
  - Expected: The updated text appears on the post page and on the author's profile.
  - Bug Report:
    - Issue: Stale Content on Author Profile
    - Actual: The post page shows the updated text ("edited text" in bold). The author's profile card still shows the old excerpt "# Heading **bold text**...", so the updated text does not appear on the profile. The "Saved Posts" list also shows the old excerpt.

- [X] FT-04: Visitor can open and read any post.
  - Action: Logged out, open the author profile, then click the title of an existing post.
  - Expected: The full title, body, author name, and publish date are displayed.

- [X] FT-05: Logged-in user can comment on a post.
  - Action: Log in as a different user, open a post, type "Great read" in the comment box, then click "Post Comment".
  - Expected: The comment appears under the post with the commenter's name and a timestamp.

- [X] FT-06: Logged-in user can like a post.
  - Action: Open a post with a visible like count, note the count, click "Like", then reload the page.
  - Expected: The like count increases by 1 and remains increased after reload.

- [X] FT-07: Logged-in user can save a post to a personal list.
  - Action: Click "Save" on a post, then open the "Saved" list from the user menu.
  - Expected: The post appears in the Saved list.

- [ ] FT-08: System generates intelligent tags automatically when a post is published.
  - Action: Publish a post with the body "Building a Python API with a React frontend" and no custom tags.
  - Expected: The post shows intelligent tags labeled separately from custom tags, including "Python" and "Frontend Development", without the author entering them.
  - Bug Report:
    - Issue: Missing Element (Intelligent Tags Not Displayed on Post)
    - Actual: The published post page ("Python API Post") shows no tags at all, neither custom nor intelligent. Intelligent tags are only visible in the Browse filter dialog, where this post is listed under "Python", "React", "Backend Development" and "Design". "Frontend Development" is not generated, and "Design" is unrelated to the content.

- [ ] FT-09: Visitor can filter posts by a custom tag and by an intelligent tag.
  - Action: On the Browse page, click the custom tag "Technology", then clear it and click the intelligent tag "Python".
  - Expected: Each filter shows only posts carrying that tag, and every result displays the selected tag.
  - Bug Report:
    - Issue: Result Cards Do Not Display Selected Tag
    - Actual: Filtering works. "Technology" returned 1 post ("The Future of Human-AI Collaboration"), and "Python" returned 1 post ("Python API Post"). The result cards do not display the selected tag. The Technology result shows only "AI" and "Future", and the Python result shows no tag chip. The filtered view also shows "No posts match the selected tags." beside "Filtered Stories (1)".

- [ ] FT-10: Visitor can combine a custom tag and an intelligent tag in one search.
  - Action: Select custom tag "Technology" and intelligent tag "Python" together, then apply the filter.
  - Expected: Only posts with both tags are listed, and each result displays both tags.
  - Bug Report:
    - Issue: Result Cards Do Not Display Both Tags
    - Actual: Only "Python Tips" (which has both tags) is listed, and the filter bar shows "Active: Technology, Python". The result card shows the "Technology" chip but not the "Python" tag. The stray text "No posts match the selected tags." is also shown beside "Filtered Stories (1)". (Before "Python Tips" was published, the same pair correctly returned 0 posts.)

- [X] FT-11: Visitor can save a tag group and reuse it.
  - Action: With "Technology + Python" selected, click "Save Tag Group", name it "Tech Python", then clear the filter and select the saved group "Tech Python".
  - Expected: The group is listed under saved groups, and selecting it re-applies the same filter and returns the same results.

- [ ] FT-12: Author backend shows views, likes, and comments per tag.
  - Action: Log in as an author with published posts, open the backend "Dashboard", and open the "Tag Statistics" tab.
  - Expected: Each tag row shows total views, likes, and comments that equal the sum of those values across that author's posts with the tag.
  - Bug Report:
    - Issue: Missing Element (Dashboard / Tag Statistics Not Found)
    - Actual: /dashboard returns "404 Page not found". There is no "Dashboard" or "Tag Statistics" tab. The author's profile has an "Analytics" tab with a "Tag Popularity Report" listing tag "Testing": 0 views, 1 like, 1 comment. These values match the author's only post, but the view is not the one the test expects.

- [ ] FT-13: Author can generate a tag popularity report.
  - Action: In the backend Dashboard, click "Generate Tag Report".
  - Expected: A report opens listing tags ranked by popularity, with views, likes, and comments per tag matching the Tag Statistics values.
  - Bug Report:
    - Issue: Missing Element (Generate Tag Report Button)
    - Actual: There is no "Generate Tag Report" button in the backend or on the profile Analytics tab, and no Dashboard exists (/dashboard is 404). The Analytics tab shows the report contents directly, with no generate action.

## Constraint
- [ ] CS-01: Sign-up is blocked for an email that is already registered.
  - Action: On the Sign Up page, enter an email already in use and submit.
  - Expected: The error "Email already registered" appears, and no new account is created.
  - Bug Report:
    - Issue: Incorrect Error Message
    - Actual: Sign-up was blocked and the user stayed on /signup, but the message shown is "Sign up failed / An account with this email already exists." The expected text "Email already registered" did not appear.

- [ ] CS-02: Post cannot be published without a title.
  - Action: Click "New Post", leave the title empty, enter body text, then click "Publish".
  - Expected: The error "Title is required" appears, and the post is not published.
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: The post was not published (URL stayed at /write). The toast shows "Title required / Please add a title for your post.", not "Title is required".

- [ ] CS-03: Users cannot edit posts authored by others.
  - Action: Log in as a user who did not write a post, open that post, and look for an "Edit" button. Then enter the post's edit URL directly.
  - Expected: No "Edit" button is shown, and the direct edit URL displays "Not authorized" without loading the editor.
  - Bug Report:
    - Issue: Improper Authorization Feedback
    - Actual: No "Edit" button is shown to the non-author. Entering /edit/post-1794232265600 directly redirected to /post/post-1794232265600. No "Not authorized" message appeared, and the editor did not load.

- [X] CS-04: Empty comments cannot be posted.
  - Action: Log in, open a post, leave the comment box empty, and click "Post Comment".
  - Expected: The button is disabled or the error "Comment cannot be empty" appears, and no comment is added.

- [ ] CS-05: Logged-out visitors cannot like, save, or comment.
  - Action: Logged out, click "Like", click "Save", and submit a comment on any post.
  - Expected: Each action prompts the login page or a "Please log in" message, and no like count or comment changes.
  - Bug Report:
    - Issue: Missing Element (Like and Save Controls for Logged-out Visitors)
    - Actual: On the logged-out post page, no "Like" or "Save" control is rendered; only "Share" appears. The comment area shows "Join the conversation" with "Sign In" and "Sign Up" links, which is a login prompt. Like and Save could not be clicked, so those two actions could not be verified.

- [ ] CS-06: Combined tag search with no matching posts shows an empty state.
  - Action: Select two tags that no single post shares, such as "Life" and "Python" if no post has both, then apply the filter.
  - Expected: The message "No posts match these tags" appears, and no posts are listed.
  - Bug Report:
    - Issue: Incorrect Empty-State Message
    - Actual: With "AI" + "Python" selected (no post has both), the result is "Filtered Stories (0)" with no posts listed, but the message reads "No posts match the selected tags.", not "No posts match these tags".

## Interaction
- [X] IX-01: Publishing shows a success notification and opens the new post.
  - Action: Create a valid post with a title and body, then click "Publish".
  - Expected: A success toast reading "Post published" appears, and the browser navigates to the new post's page.

## Content
- [ ] CT-01: Intelligent tags on default posts are relevant to their content.
  - Action: Open three default posts with different topics, and compare each post's intelligent tags with its title and body.
  - Expected: Every intelligent tag is supported by words in that post's content, and no tag belongs to an unrelated topic.
  - Bug Report:
    - Issue: Unsupported Intelligent Tags
    - Actual: Intelligent tags are not shown on post pages and were read from the filter dialog. "The Art of Writing Clean Code" (Code Examples, JavaScript, Best Practices) is supported by its code samples. "Finding Creativity in Constraints" (Design, Opinion) is supported. "The Future of Human-AI Collaboration" has tags "Machine Learning" and "Productivity", but neither word or phrase appears in its body (1,512 characters checked), so those two tags are not supported by the content.