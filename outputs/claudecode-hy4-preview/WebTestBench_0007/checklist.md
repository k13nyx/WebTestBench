# Test Checklist

## Functionality
- [ ] FT-01: New resident can sign up and access the site as a registered user
  - Action: Click the "Sign Up" / "Register" control, fill in display name, email, and password with valid values, and submit the form.
  - Expected: Registration succeeds, the user is signed in, their display name appears in the header/account area, and the post-creation control is available.

- [ ] FT-02: Signed-in user can create a short post and it appears in the feed
  - Action: Click "New Post" (or equivalent), enter a short title/body about a safety concern, select a category, and submit.
  - Expected: The post is saved and appears in the feed of recent alerts with its title, body, category label, author name, and timestamp.

- [ ] FT-03: Feed displays existing recent alerts by default
  - Action: Load the home/feed page without applying any filter or search.
  - Expected: A feed of pre-existing posts is visible, each showing title, body text, category label, author, and timestamp, ordered with the most recent post first.

- [ ] FT-04: User can comment on an existing post
  - Action: Open a post from the default feed, type an update into the comment field, and submit it.
  - Expected: The comment is saved and appears in that post's comment list with the commenter's name and the comment text.

- [ ] FT-05: User can mark an alert as resolved / no longer relevant
  - Action: On a post in the default feed, click the "Mark as Resolved" (or "Resolved / No Longer Relevant") control and confirm if prompted.
  - Expected: The post's status becomes Resolved, and the resolved status is still present after reloading the page.

- [ ] FT-06: Feed can be filtered by category
  - Action: Use the category filter and select "Safety Alert".
  - Expected: The feed shows only posts labeled "Safety Alert"; posts of other categories (e.g., "Lost and Found", "Community Event") are not displayed.

- [ ] FT-07: Feed can be searched by keyword
  - Action: Type a word that appears in the body/title of a default post into the search field and submit.
  - Expected: The feed shows only posts containing that keyword (title or body); posts without the keyword are not displayed.

## Constraint
- [ ] CS-01: A post cannot be submitted with an empty body
  - Action: Open the new-post form, leave the body/description field empty (title may be filled), and submit.
  - Expected: Submission is blocked, a validation message about the required description is shown, and no new post is added to the feed.

- [ ] CS-02: A post cannot be submitted without choosing a category
  - Action: Open the new-post form, fill title and body, leave the category unselected/default-empty, and submit.
  - Expected: Submission is blocked with a category-required message, and no new post is added to the feed.

- [ ] CS-03: A comment cannot be submitted when empty
  - Action: Open a post's comment area and submit with an empty or whitespace-only comment field.
  - Expected: The empty comment is rejected, an inline message is shown, and no blank entry is added to the comment list.

- [ ] CS-04: Sign-up rejects invalid or duplicate registration data
  - Action: Submit the sign-up form using an email that already exists in the default user data (then repeat with an empty email).
  - Expected: Registration fails with a clear error (e.g., "email already in use" / "email is required"), no account is created, and the user is not signed in.

- [ ] CS-05: A post's status is mutually exclusive — resolved posts are not shown as active alerts
  - Action: Mark a default post as Resolved, then filter the feed by "Active" status (or check the active alerts view) if available; otherwise check the post's status area.
  - Expected: The post displays exactly one status — "Resolved" — and never simultaneously appears as an active/open alert.

- [ ] CS-06: A search that matches nothing shows an empty state, not the unfiltered feed
  - Action: Enter a nonsense keyword (e.g., "zzzzqqq") into the search field and submit.
  - Expected: The feed shows no posts and displays a "No posts found" / "No results" message; no unrelated posts are listed and no error appears.

## Interaction
- [ ] IX-01: Applying a category filter updates the feed in place
  - Action: With the full feed displayed, select a different category from the category filter.
  - Expected: The feed updates immediately without a full page reload or navigation, showing only the selected category's posts, and the selected filter remains visibly active.

- [ ] IX-02: Clearing the filter/search restores the full feed
  - Action: Apply a category filter, then clear it (select "All" / click the clear control), and clear any search text.
  - Expected: The full default feed is shown again with all categories represented, and no filter remains active.

- [ ] IX-03: Marking a post resolved updates that post immediately in the feed
  - Action: Click "Mark as Resolved" on a post while viewing the feed.
  - Expected: The post updates in place (no page reload, user stays on the feed) and shows a visible "Resolved" badge/indicator right away.

- [ ] IX-04: Creating a post shows a confirmation and adds it to the top of the feed
  - Action: Submit a valid new post.
  - Expected: A success toast/notification confirms the post was created, the creation form closes, and the new post appears at the top of the feed.

- [ ] IX-05: A post's comments can be opened and viewed from the feed
  - Action: Click a post's comment control/comment count in the feed.
  - Expected: The post's comment section expands in place revealing the existing comments and a comment input; clicking again collapses it.

## Content
- [ ] CT-01: Feed posts show complete, relevant metadata
  - Action: Inspect three different default posts in the feed.
  - Expected: Each post displays a non-empty title, body text, category label, author name, and timestamp/relative date — with no missing or "undefined"/"null" placeholders.

- [ ] CT-02: Category options exactly match the required neighborhood-watch categories
  - Action: Open the new-post category selector and compare with the filter's category options.
  - Expected: The available categories are "Safety Alert", "Lost and Found", and "Community Event" (wording may vary in case), with no extra unrelated categories and no placeholder options like "Category 1".

- [ ] CT-03: Page content is on-theme for a neighborhood watch community
  - Action: Read the site title/heading, navigation labels, and the default feed content.
  - Expected: All headings, labels, and default posts relate to neighborhood safety, lost and found, or community events; no lorem ipsum, no off-topic or unrelated sample content, and no broken images/icons.