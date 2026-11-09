# Test Checklist

## Functionality
- [ ] FT-01: New resident can sign up for the neighborhood watch site
  - Action: Enter a valid name, email, and password, then click "Sign Up".
  - Expected: Account is created and user is signed in / redirected to the feed.
- [ ] FT-02: Signed-in user can create a short post
  - Action: Enter a title and body, select a category, click "Post".
  - Expected: The post is submitted and saved successfully.
- [ ] FT-03: Newly created post appears in the feed
  - Action: Create a post, then view the feed.
  - Expected: The new post is displayed in the feed (at/near the top as the most recent alert).
- [ ] FT-04: User can browse the feed of recent alerts
  - Action: Load the feed with default data present.
  - Expected: A list of existing posts is displayed in reverse-chronological order.
- [ ] FT-05: User can categorize a post
  - Action: When creating a post, choose one of the categories (e.g. "Safety Alert", "Lost and Found", "Community Event").
  - Expected: The selected category is saved and shown on the post.
- [ ] FT-06: User can filter the feed by category
  - Action: Select a single category in the filter (e.g. "Lost and Found").
  - Expected: Only posts belonging to that category are shown in the feed.
- [ ] FT-07: User can search the feed by keyword
  - Action: Type a keyword that exists in a default post (e.g. a word from its title) into the search box.
  - Expected: Only posts containing the keyword are shown.
- [ ] FT-08: User can comment on a post
  - Action: Open a post, enter comment text, click "Comment" / "Post Comment".
  - Expected: The comment is submitted and attached to that post.
- [ ] FT-09: User can mark an alert as resolved
  - Action: On a default "Safety Alert" post, click "Mark as Resolved".
  - Expected: The post is updated to a resolved state.

## Constraint
- [ ] CS-01: Sign up cannot be submitted with empty required fields
  - Action: Leave email and/or password blank and click "Sign Up".
  - Expected: Submission is blocked and a validation message indicates the required field(s).
- [ ] CS-02: Post cannot be submitted with empty content
  - Action: Leave the post title and/or body blank and click "Post".
  - Expected: Submission is blocked with a message that content is required.
- [ ] CS-03: Post cannot be submitted without a category
  - Action: Enter valid post content but leave the category unselected, click "Post".
  - Expected: Submission is blocked with a message that a category must be selected.
- [ ] CS-04: Empty comment cannot be submitted
  - Action: With the comment field empty, click "Comment".
  - Expected: No comment is added; submission is blocked or disabled.
- [ ] CS-05: Search/filter with no matches shows an empty state
  - Action: Enter a keyword or category that no default post matches.
  - Expected: An empty-state message (e.g. "No posts found") is shown instead of stale/incorrect posts.
- [ ] CS-06: Resolved alerts remain in a consistent resolved state
  - Action: Mark an alert as resolved, refresh the feed.
  - Expected: The post is still shown as resolved (state persists) and is not reverted to active.

## Interaction
- [ ] IX-01: User receives confirmation after creating a post
  - Action: Successfully create a post.
  - Expected: A visible success confirmation (toast/message) is shown.
- [ ] IX-02: Resolved alerts are visually distinguished in the feed
  - Action: View the feed after marking a post resolved.
  - Expected: That post displays a clear "Resolved" indicator (label, badge, or dimmed style).
- [ ] IX-03: Feed updates to reflect the active filter/search selection
  - Action: Apply a category filter, then clear it or switch categories.
  - Expected: The feed and the highlighted filter selection update accordingly without a full reload.

## Content
- [ ] CT-01: Category labels match the specified set
  - Action: Inspect the category selector/options.
  - Expected: The categories "Safety Alert", "Lost and Found", and "Community Event" are available.
- [ ] CT-02: Feed content is relevant to the neighborhood watch purpose
  - Action: Review the default posts and any images/icons shown.
  - Expected: All displayed content relates to local safety concerns and community events (no unrelated/placeholder imagery or text).