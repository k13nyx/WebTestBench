# Test Checklist

## Functionality
- [ ] FT-01: Resident can register a new account with valid details.
  - Action: Click "Sign Up", enter a unique name, email, and password, then click "Create Account".
  - Expected: Account is created, and the user can log in with those credentials.
- [ ] FT-02: Resident can log in and log out.
  - Action: Log in with the new account's credentials, then click "Log Out".
  - Expected: Login opens the neighborhood feed. Logout returns the user to the login page.
- [ ] FT-03: Resident can create a categorized post.
  - Action: Click "New Post", select category "Safety Alert", enter a title and description, then click "Publish".
  - Expected: The post appears at the top of the feed with the chosen category, title, description, author name, and timestamp.
- [ ] FT-04: Feed shows recent posts newest first.
  - Action: Open the feed and read the timestamps from top to bottom.
  - Expected: Posts are ordered from most recent to oldest, and each post displays a timestamp.
- [ ] FT-05: Category filter shows only posts in the selected category.
  - Action: Select "Lost and Found" from the category filter, then select "All".
  - Expected: Only "Lost and Found" posts appear. Selecting "All" restores every post.
- [ ] FT-06: Keyword search returns matching posts.
  - Action: Type a word from an existing post's title into the search box and press Enter.
  - Expected: Only posts whose title or description contain that word are shown.
- [ ] FT-07: Resident can add a comment to a post.
  - Action: Open a post, type "Thanks for the update" in the comment box, and click "Post Comment".
  - Expected: The comment appears under the post with the commenter's name and timestamp.
- [ ] FT-08: Post author can mark a post as "Resolved".
  - Action: Open a post created by the logged-in user and click "Mark as Resolved".
  - Expected: The post displays a "Resolved" status.
- [ ] FT-09: Post author can mark a post as "No Longer Relevant".
  - Action: Open a post created by the logged-in user and click "Mark as No Longer Relevant".
  - Expected: The post displays a "No Longer Relevant" status.

## Constraint
- [ ] CS-01: Registration is blocked when required fields are empty.
  - Action: On the sign-up form, leave the email field blank and click "Create Account".
  - Expected: Form is not submitted, the message "Email is required" appears beside the field, and no account is created.
- [ ] CS-02: Registration is blocked for an email already in use.
  - Action: Register with the email of an existing default account.
  - Expected: Error "An account with this email already exists" appears, and no account is created.
- [ ] CS-03: Post cannot be published without a title or category.
  - Action: Open "New Post", leave the title empty, and click "Publish". Repeat with the title filled and no category selected.
  - Expected: Publishing is blocked in both cases, with a validation message on the missing field, and no post is created.
- [ ] CS-04: Login is rejected with an incorrect password.
  - Action: Enter a registered email with a wrong password and click "Log In".
  - Expected: Error "Invalid email or password" appears, and the user stays on the login page.
- [ ] CS-05: Only the post author can change a post's status.
  - Action: Open a post created by another resident.
  - Expected: "Mark as Resolved" and "Mark as No Longer Relevant" are absent or disabled.
- [ ] CS-06: Feed and posting pages are inaccessible when logged out.
  - Action: Log out, then enter the feed page's address directly in the browser.
  - Expected: The user is redirected to the login page, and no feed content is shown.
- [ ] CS-07: Empty comments cannot be submitted.
  - Action: Open a post, leave the comment box empty, and click "Post Comment".
  - Expected: Submission is blocked, and no empty comment is added to the post.

## Interaction
- [ ] IX-01: Success message appears after a post is published.
  - Action: Create and publish a valid post.
  - Expected: A confirmation message "Post published successfully" appears and then disappears automatically.
- [ ] IX-02: Search with no matches shows an empty-state message.
  - Action: Type "zzqx123" into the search box and press Enter.
  - Expected: The message "No posts match your search" is displayed, and no posts are listed.

## Content
- [ ] CT-01: Category labels match the defined category names.
  - Action: Open the category filter and review the options, then review the category label on several posts.
  - Expected: The filter offers "All", "Safety Alert", "Lost and Found", and "Community Event". Each post shows one of these exact labels, with no blank or misspelled labels.
- [ ] CT-02: Default feed content matches the neighborhood watch theme.
  - Action: Scroll through all default posts in the feed.
  - Expected: Every post relates to safety concerns, lost and found items, or community events. No placeholder text (e.g., "lorem ipsum") or unrelated content appears.