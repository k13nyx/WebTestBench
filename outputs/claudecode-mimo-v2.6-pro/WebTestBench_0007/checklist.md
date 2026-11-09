# Test Checklist

## Functionality
- [ ] FT-01: Resident can sign up for an account with valid details.
  - Action: Open the Sign Up form, enter a name, a valid email, and a password, click "Sign Up".
  - Expected: Account is created and the user is signed in and taken to the alerts feed.
- [ ] FT-02: Signed-in user can create a short post.
  - Action: Click "Create Post", enter a title and body text, select a category, click "Post".
  - Expected: The new post appears at the top of the alerts feed with its title and body.
- [ ] FT-03: User can categorize a post as "Safety Alert".
  - Action: Create a post with category "Safety Alert" selected.
  - Expected: The saved post displays the label "Safety Alert".
- [ ] FT-04: User can categorize a post as "Lost and Found".
  - Action: Create a post with category "Lost and Found" selected.
  - Expected: The saved post displays the label "Lost and Found".
- [ ] FT-05: User can categorize a post as "Community Event".
  - Action: Create a post with category "Community Event" selected.
  - Expected: The saved post displays the label "Community Event".
- [ ] FT-06: Feed shows recent alerts in reverse-chronological order.
  - Action: Open the main feed page and observe the order of the default posts.
  - Expected: All default posts are listed, newest first, with visible timestamps.
- [ ] FT-07: User can filter the feed by category.
  - Action: Select "Safety Alert" in the category filter control.
  - Expected: The feed shows only posts labeled "Safety Alert"; posts of other categories are hidden.
- [ ] FT-08: User can search the feed by keyword.
  - Action: Type a word present in one default post's title or body into the search field and submit.
  - Expected: The feed shows only posts containing that keyword.
- [ ] FT-09: User can comment on a post.
  - Action: Open a default post, type text into its comment field, click "Comment".
  - Expected: The comment appears under that post with its text and author.
- [ ] FT-10: User can mark an alert as resolved.
  - Action: Click "Mark as Resolved" on a post.
  - Expected: The post is updated to show a "Resolved" status.
- [ ] FT-11: User can mark an alert as no longer relevant.
  - Action: Click "Mark as No Longer Relevant" on a post.
  - Expected: The post is updated to show a "No Longer Relevant" status.

## Constraint
- [ ] CS-01: Sign up form cannot be submitted with empty required fields.
  - Action: Leave name, email, or password empty and click "Sign Up".
  - Expected: Submission is blocked and a message indicates the missing field(s); no account is created.
- [ ] CS-02: Sign up is rejected for an already-registered email.
  - Action: Sign up using the email of an existing user.
  - Expected: Submission is rejected with a message that the email is already registered; no duplicate account is created.
- [ ] CS-03: A post cannot be created with an empty title or body.
  - Action: Click "Create Post", leave the title or body empty, click "Post".
  - Expected: Submission is blocked with a validation message; no post is added to the feed.
- [ ] CS-04: A post cannot be created without a category.
  - Action: Click "Create Post", enter title and body, leave the category unselected, click "Post".
  - Expected: Submission is blocked with a message that a category is required.
- [ ] CS-05: A comment cannot be submitted empty.
  - Action: Click "Comment" on a post without typing any comment text.
  - Expected: Submission is blocked and no empty comment is added.
- [ ] CS-06: Resolved and "No Longer Relevant" states are mutually exclusive and cannot be re-applied.
  - Action: Click "Mark as Resolved" on a post, then click "Mark as Resolved" again and try "Mark as No Longer Relevant" on the same post.
  - Expected: The post stays "Resolved"; the second resolve action is disabled or ignored, and it cannot simultaneously hold "No Longer Relevant" status.

## Interaction
- [ ] IX-01: Creating a post shows a success confirmation.
  - Action: Submit a valid new post and observe the page.
  - Expected: A success message (e.g., toast "Post created") is shown and the feed refreshes to include the post.
- [ ] IX-02: Status changes give immediate visual feedback.
  - Action: Mark a post as resolved and observe the post card.
  - Expected: The post card visibly updates to show the "Resolved" status without requiring a manual page reload.
- [ ] IX-03: A search with no matches shows an empty-result message.
  - Action: Search for a keyword that appears in no post (e.g., "zzzzqqq").
  - Expected: The feed area shows a "No results found" style message instead of an error or an unchanged feed.

## Content
- [ ] CT-04: Each feed post displays complete, relevant content.
  - Action: Inspect any default post in the feed.
  - Expected: The post card shows its title, body text, category label, author name, and timestamp — all matching the post's actual data.
- [ ] CT-05: Category labels always match the three defined themes.
  - Action: Review the category labels shown on default posts and the options in the category filter.
  - Expected: Only "Safety Alert", "Lost and Found", and "Community Event" appear, spelled consistently in both the post labels and the filter options.
- [ ] CT-06: Comments display correct content under the correct post.
  - Action: Comment on one specific default post, then review the feed.
  - Expected: The comment text and author appear only under that post, with no comment shown on unrelated posts.