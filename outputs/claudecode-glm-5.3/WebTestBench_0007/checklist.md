# Test Checklist

## Functionality
- [ ] FT-01: New resident can sign up for an account
  - Action: On the signup page, fill in a valid name, email, and password and click the "Sign Up" button.
  - Expected: The account is created and the user is signed in (or redirected to sign in), with no error shown.

- [ ] FT-02: Registered user can sign in
  - Action: Sign in with the credentials created during signup.
  - Expected: The user is signed in and identified by their name/username in the page header or navigation.

- [ ] FT-03: Signed-in user can create a post with a category
  - Action: Use the post creation form to enter a short title and body (e.g., "Suspicious van on Elm Street"), select the category "safety alert", and submit.
  - Expected: The post is created and appears in the feed with the entered title, body, and selected category.

- [ ] FT-04: Feed displays recent posts from default data
  - Action: Open the feed page without applying any filters or searches.
  - Expected: Multiple pre-existing posts are listed, most recent first, each showing at least a title, category, and timestamp.

- [ ] FT-05: User can filter the feed by category
  - Action: Apply the category filter "community event" on the feed.
  - Expected: Only posts categorized as "community event" are displayed; posts of other categories are hidden.

- [ ] FT-06: User can search the feed by keyword
  - Action: Type a keyword that exists in a default post's title or body (e.g., "lost") into the search box and submit.
  - Expected: Only posts containing that keyword are displayed.

- [ ] FT-07: User can comment on a post to share an update
  - Action: Open any post, type a comment (e.g., "The van was gone this morning") into the comment box, and submit it.
  - Expected: The comment appears attached to that post.

- [ ] FT-08: User can mark an important alert as resolved
  - Action: On an unresolved post (e.g., a safety alert), click the "Mark as Resolved" control.
  - Expected: The post's status changes to resolved/no longer relevant and remains that way after reloading the page.

## Constraint
- [ ] CS-01: Signup cannot be completed with empty required fields
  - Action: On the signup page, leave required fields (e.g., email or password) empty and click "Sign Up".
  - Expected: The form is not submitted, an inline validation message indicates the missing field(s), and no account is created.

- [ ] CS-02: Signup cannot reuse an already-registered email
  - Action: Attempt to sign up with an email address that already has an account.
  - Expected: The signup is rejected with a message indicating the email is already in use.

- [ ] CS-03: Post creation cannot be completed with empty content or no category
  - Action: In the post creation form, submit with an empty title/body, or without selecting a category.
  - Expected: The post is not created and a message indicates which required input is missing.

- [ ] CS-04: Comment cannot be submitted when empty
  - Action: Click the comment submit button without typing anything.
  - Expected: No comment is added to the post; a validation message or blocked submission occurs.

- [ ] CS-05: Filter and search cannot return irrelevant posts
  - Action: Apply the "lost and found" category filter and note the results; then clear it and search a keyword found only in a "safety alert" post.
  - Expected: Each result set contains only posts matching the applied filter/search criterion, with no posts from unrelated categories or without the keyword.

## Interaction
- [ ] IX-01: Signup success is confirmed to the user
  - Action: Complete a valid signup.
  - Expected: A success message or welcome indication is shown (e.g., "Account created" toast) before navigating away from the form.

- [ ] IX-02: Feed updates immediately after a new post is created
  - Action: Create a new post, then return to the feed without reloading the page.
  - Expected: The new post appears at the top of the feed immediately, without a manual page refresh.

- [ ] IX-03: Marking a post as resolved visibly changes its appearance
  - Action: Click "Mark as Resolved" on an active safety alert post.
  - Expected: The post immediately displays a resolved indicator (e.g., a "Resolved" badge or dimmed styling) without a page reload.

- [ ] IX-04: Applying or clearing a filter updates the feed instantly
  - Action: Select a category filter, then clear it (e.g., choose "All").
  - Expected: The feed updates to show the filtered subset, then restores the full list, without errors.

## Content
- [ ] CT-01: Each post displays its correct category label
  - Action: Inspect several default posts in the feed and compare each post's category label against its content.
  - Expected: Every post shows exactly one of the defined categories ("safety alert", "lost and found", or "community event") that matches what the post is about.

- [ ] CT-02: Feed content is relevant to the neighborhood watch theme
  - Action: Read the titles and bodies of all default posts in the feed.
  - Expected: All posts concern safety concerns, lost and found items, or community events — no unrelated or placeholder content.

- [ ] CT-03: Comments and posts display author information and timestamps
  - Action: Inspect posts and their comments on the feed.
  - Expected: Posts and comments show the author's name (or username) and a readable date/time; comment text is relevant to the post it belongs to.