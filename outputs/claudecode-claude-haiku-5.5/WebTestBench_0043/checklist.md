# Test Checklist

## Functionality
- [ ] FT-01: New visitor can sign up for an account.
  - Action: Click "Sign Up", enter a new unused email and a password, then click "Create Account".
  - Expected: The account is created, the user is logged in, and "My Profile" appears in the navigation.
- [ ] FT-02: Author can write a Markdown post and publish it to their profile.
  - Action: Click "New Post", enter title "QA Markdown Test", enter body "# Heading" on line 1 and "**bold text**" on line 2, then click "Publish".
  - Expected: The post appears on the author's profile page, "Heading" renders as a large heading, and "bold text" renders in bold.
- [ ] FT-03: Author can edit their own post.
  - Action: Open a post authored by the logged-in user, click "Edit", change the body text, then click "Save".
  - Expected: The updated text appears on the post page and on the author's profile.
- [ ] FT-04: Visitor can open and read any post.
  - Action: Logged out, open the author profile, then click the title of an existing post.
  - Expected: The full title, body, author name, and publish date are displayed.
- [ ] FT-05: Logged-in user can comment on a post.
  - Action: Log in as a different user, open a post, type "Great read" in the comment box, then click "Post Comment".
  - Expected: The comment appears under the post with the commenter's name and a timestamp.
- [ ] FT-06: Logged-in user can like a post.
  - Action: Open a post with a visible like count, note the count, click "Like", then reload the page.
  - Expected: The like count increases by 1 and remains increased after reload.
- [ ] FT-07: Logged-in user can save a post to a personal list.
  - Action: Click "Save" on a post, then open the "Saved" list from the user menu.
  - Expected: The post appears in the Saved list.
- [ ] FT-08: System generates intelligent tags automatically when a post is published.
  - Action: Publish a post with the body "Building a Python API with a React frontend" and no custom tags.
  - Expected: The post shows intelligent tags labeled separately from custom tags, including "Python" and "Frontend Development", without the author entering them.
- [ ] FT-09: Visitor can filter posts by a custom tag and by an intelligent tag.
  - Action: On the Browse page, click the custom tag "Technology", then clear it and click the intelligent tag "Python".
  - Expected: Each filter shows only posts carrying that tag, and every result displays the selected tag.
- [ ] FT-10: Visitor can combine a custom tag and an intelligent tag in one search.
  - Action: Select custom tag "Technology" and intelligent tag "Python" together, then apply the filter.
  - Expected: Only posts with both tags are listed, and each result displays both tags.
- [ ] FT-11: Visitor can save a tag group and reuse it.
  - Action: With "Technology + Python" selected, click "Save Tag Group", name it "Tech Python", then clear the filter and select the saved group "Tech Python".
  - Expected: The group is listed under saved groups, and selecting it re-applies the same filter and returns the same results.
- [ ] FT-12: Author backend shows views, likes, and comments per tag.
  - Action: Log in as an author with published posts, open the backend "Dashboard", and open the "Tag Statistics" tab.
  - Expected: Each tag row shows total views, likes, and comments that equal the sum of those values across that author's posts with the tag.
- [ ] FT-13: Author can generate a tag popularity report.
  - Action: In the backend Dashboard, click "Generate Tag Report".
  - Expected: A report opens listing tags ranked by popularity, with views, likes, and comments per tag matching the Tag Statistics values.

## Constraint
- [ ] CS-01: Sign-up is blocked for an email that is already registered.
  - Action: On the Sign Up page, enter an email already in use and submit.
  - Expected: The error "Email already registered" appears, and no new account is created.
- [ ] CS-02: Post cannot be published without a title.
  - Action: Click "New Post", leave the title empty, enter body text, then click "Publish".
  - Expected: The error "Title is required" appears, and the post is not published.
- [ ] CS-03: Users cannot edit posts authored by others.
  - Action: Log in as a user who did not write a post, open that post, and look for an "Edit" button. Then enter the post's edit URL directly.
  - Expected: No "Edit" button is shown, and the direct edit URL displays "Not authorized" without loading the editor.
- [ ] CS-04: Empty comments cannot be posted.
  - Action: Log in, open a post, leave the comment box empty, and click "Post Comment".
  - Expected: The button is disabled or the error "Comment cannot be empty" appears, and no comment is added.
- [ ] CS-05: Logged-out visitors cannot like, save, or comment.
  - Action: Logged out, click "Like", click "Save", and submit a comment on any post.
  - Expected: Each action prompts the login page or a "Please log in" message, and no like count or comment changes.
- [ ] CS-06: Combined tag search with no matching posts shows an empty state.
  - Action: Select two tags that no single post shares, such as "Life" and "Python" if no post has both, then apply the filter.
  - Expected: The message "No posts match these tags" appears, and no posts are listed.

## Interaction
- [ ] IX-01: Publishing shows a success notification and opens the new post.
  - Action: Create a valid post with a title and body, then click "Publish".
  - Expected: A success toast reading "Post published" appears, and the browser navigates to the new post's page.

## Content
- [ ] CT-01: Intelligent tags on default posts are relevant to their content.
  - Action: Open three default posts with different topics, and compare each post's intelligent tags with its title and body.
  - Expected: Every intelligent tag is supported by words in that post's content, and no tag belongs to an unrelated topic.