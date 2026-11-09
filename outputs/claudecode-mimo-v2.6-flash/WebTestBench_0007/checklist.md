# Test Checklist

## Functionality
- [ ] FT-01: Resident can sign up for an account
  - Action: Open the sign-up form, enter a name, email, and password, then submit.
  - Expected: Account is created and the user is recognized as a signed-in resident (e.g., welcome/greeting or profile shown).

- [ ] FT-02: Signed-in user can create a short post with a category
  - Action: Open the post creation form, enter a title and short message, select the category "safety alert," and submit.
  - Expected: The post is created and appears at the top of the feed with its title, message, and "safety alert" category displayed.

- [ ] FT-03: Feed displays recent posts
  - Action: Navigate to the feed page.
  - Expected: A list of recent posts is shown, each with title, message, category, author, and time posted, ordered newest first.

- [ ] FT-04: User can filter the feed by category
  - Action: Select the category filter "community event."
  - Expected: Only posts categorized as "community event" remain visible in the feed.

- [ ] FT-05: User can search the feed by keyword
  - Action: Type a keyword that appears in an existing post's title or message into the search field.
  - Expected: The feed shows only posts containing that keyword.

- [ ] FT-06: User can comment on a post
  - Action: Open a post, enter a comment in the comment field, and submit.
  - Expected: The comment is saved and displayed under the post along with the commenter's name and time.

- [ ] FT-07: User can mark an important alert as resolved
  - Action: On a "safety alert" post, click the control to mark it resolved.
  - Expected: The post's status changes to resolved and the change persists after reloading the page.

- [ ] FT-08: User can mark an alert as no longer relevant
  - Action: On an alert post, choose the option to mark it as no longer relevant.
  - Expected: The post is marked as no longer relevant (e.g., status label shown) and the state persists after reload.

## Constraint
- [ ] CS-01: Post cannot be submitted with missing required fields
  - Action: Open the post creation form and attempt to submit with an empty title, empty message, or no category selected.
  - Expected: Submission is blocked and a validation message identifies the missing field(s); no post is added to the feed.

- [ ] CS-02: Comment cannot be submitted empty
  - Action: On a post, attempt to submit a comment with an empty comment field.
  - Expected: Submission is blocked with a validation message; no empty comment appears under the post.

- [ ] CS-03: Sign-up cannot proceed with invalid or missing credentials
  - Action: Attempt to sign up with a missing field, an invalid email format, or a password shorter than the stated minimum.
  - Expected: Sign-up is blocked with a message explaining the invalid field; no account is created.

- [ ] CS-04: Posts can only use the allowed categories
  - Action: Inspect the category options in the post creation form and attempt to submit a post without choosing one of the defined categories.
  - Expected: Only the defined categories ("safety alert," "lost and found," "community event") are selectable, and a post with no/unknown category cannot be submitted.

## Interaction
- [ ] IX-01: Creating a post gives immediate visible feedback
  - Action: Submit a valid new post.
  - Expected: A success confirmation (e.g., toast or message) appears, and the new post is visible in the feed without a manual page refresh.

- [ ] IX-02: Feed responds immediately to filter and search changes
  - Action: Change the category filter and type a keyword into search.
  - Expected: The feed updates promptly after each change, and clearing the filter/search restores the full feed.

- [ ] IX-03: Posting a comment gives immediate feedback
  - Action: Submit a valid comment on a post.
  - Expected: A success confirmation appears and the comment is instantly appended to the post's comment list.

- [ ] IX-04: Marking an alert resolved gives immediate visual state change
  - Action: Click the "resolve" control on an alert post.
  - Expected: The post's status indicator updates to "resolved" immediately, with a confirmation message shown.

## Content
- [ ] CT-01: Category labels match the specified set
  - Action: Inspect category options in the post form and category labels shown on feed posts.
  - Expected: The categories displayed are exactly "safety alert," "lost and found," and "community event" (no misspellings or unrelated labels).

- [ ] CT-02: Feed post content is accurate and relevant
  - Action: Compare each feed post's displayed title, message, author, time, and category against the data entered when it was created.
  - Expected: All displayed fields match the original submission exactly, with no truncated or swapped content.

- [ ] CT-03: Post status labels accurately reflect state
  - Action: Inspect the status shown on active, resolved, and no-longer-relevant posts.
  - Expected: Each post displays a label matching its actual state (e.g., active alerts unlabeled or "active," resolved ones marked "resolved"), with no contradictory labels.