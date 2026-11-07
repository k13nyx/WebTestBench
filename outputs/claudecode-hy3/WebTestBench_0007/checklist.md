# Test Checklist

## Functionality
- [ ] FT-01: User can sign up as a resident
  - Action: Open the sign-up page and register with a valid email and password, then submit.
  - Expected: Account is created and the user is logged in / taken to the home feed.

- [ ] FT-02: User can create a short post
  - Action: Click "Create Post" (or "New Post"), enter post text, and submit.
  - Expected: The new post is saved and appears in the feed.

- [ ] FT-03: User can browse a feed of recent alerts
  - Action: Navigate to the home / feed page.
  - Expected: A list of recent posts is displayed in reverse-chronological order.

- [ ] FT-04: User can assign a category to a post
  - Action: While creating a post, select a category from the category control.
  - Expected: The selected category is recorded and shown on the published post.

- [ ] FT-05: User can filter the feed by category
  - Action: Select a category filter (e.g., "Safety Alert") from the filter control.
  - Expected: Only posts in that category are shown in the feed.

- [ ] FT-06: User can search the feed by keyword
  - Action: Type a keyword into the search box and submit/enter.
  - Expected: Only posts containing the keyword are shown in the feed.

- [ ] FT-07: User can comment on a post
  - Action: Open a post and submit a comment in the comment field.
  - Expected: The comment is added to that post's comment thread.

- [ ] FT-08: User can mark a post as resolved / no longer relevant
  - Action: Open a post and click the "Mark as Resolved" (or equivalent) control.
  - Expected: The post is flagged as resolved / no longer relevant.

## Constraint
- [ ] CS-01: Sign-up cannot be submitted with empty required fields
  - Action: Leave the email or password blank and click "Sign Up".
  - Expected: Submission is blocked with a validation message; no account is created.

- [ ] CS-02: A post cannot be created with empty content or no category
  - Action: Submit a post with empty text or without selecting a category.
  - Expected: Submission is blocked with a validation message; no post is created.

- [ ] CS-03: Post category must be one of the defined options
  - Action: Attempt to assign a category outside the allowed set.
  - Expected: Only the defined categories are selectable; invalid categories are rejected.

- [ ] CS-04: A comment cannot be submitted with empty content
  - Action: Open a post and click "Comment" with an empty comment field.
  - Expected: Submission is blocked; no empty comment is added.

## Interaction
- [ ] IX-01: Success confirmation appears after a post is created
  - Action: Create a valid post and submit.
  - Expected: A success message / toast confirms the post was published.

- [ ] IX-02: The feed updates immediately after a post is created
  - Action: Create a new post from the feed page.
  - Expected: The new post appears at the top of the feed without a manual refresh.

- [ ] IX-03: Resolved posts display a distinct visual state
  - Action: Mark a post as resolved and view it in the feed.
  - Expected: The post shows a clear "Resolved" indicator (badge / styling).

- [ ] IX-04: Success confirmation appears after sign-up
  - Action: Complete a valid sign-up.
  - Expected: A success message confirms the account was created and the user is logged in.

## Content
- [ ] CT-01: Feed shows only neighborhood-watch relevant content
  - Action: Browse the feed and inspect post titles, bodies, and media.
  - Expected: All displayed content is relevant to safety concerns, lost & found, or community events.

- [ ] CT-02: Category labels render exactly as specified
  - Action: Inspect the category control and published posts.
  - Expected: The three categories display as "Safety Alert", "Lost and Found", and "Community Event" (matching the instruction's examples).