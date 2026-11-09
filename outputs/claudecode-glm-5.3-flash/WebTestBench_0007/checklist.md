# Test Checklist

## Functionality
- [ ] FT-01: New resident can sign up for an account
  - Action: Open the sign-up form, enter a name, email, and password, and submit the registration.
  - Expected: Account is created successfully and the user is signed in (or redirected to the feed) with their identity visible.
- [ ] FT-02: Signed-in resident can create a post about a safety concern or community event
  - Action: Sign in, click the "Create Post" (or similarly named) button, enter a title and short body text, and submit.
  - Expected: The new post appears in the feed with the entered title, body, author name, and timestamp.
- [ ] FT-03: User can assign a category when creating a post
  - Action: Create a post and select a category (e.g., "Safety Alert", "Lost and Found", or "Community Event") from the category selector before submitting.
  - Expected: The published post displays the selected category label/badge on its card in the feed.
- [ ] FT-04: User can comment on an existing post
  - Action: Open a post in the feed, type a comment (e.g., "Update: the streetlight is fixed.") in the comment field, and submit it.
  - Expected: The comment appears under the post, associated with the commenter's name, without a page error.
- [ ] FT-05: User can filter the feed by category
  - Action: Click or select a single category filter (e.g., "Safety Alert") on the feed.
  - Expected: The feed shows only posts labeled with that category; posts of other categories are hidden.
- [ ] FT-06: User can search the feed by keyword
  - Action: Enter a keyword that matches the text of a known pre-existing post (e.g., a distinctive word from a default post's title) into the search box and submit.
  - Expected: Only posts containing that keyword (in title or body) are displayed.
- [ ] FT-07: User can mark an alert post as resolved or no longer relevant
  - Action: On a pre-existing alert post, click the "Mark as Resolved" (or "No Longer Relevant") action.
  - Expected: The post's status updates to show a visible "Resolved"/"No Longer Relevant" indicator in the feed.
- [ ] FT-08: Feed displays a list of recent posts by default
  - Action: Load the homepage/feed without applying any filter or search.
  - Expected: A list of pre-existing posts is displayed, ordered with the most recent posts first.

## Constraint
- [ ] CS-01: Post cannot be submitted with empty required fields
  - Action: Open the "Create Post" form, leave the title and/or body empty, and click submit.
  - Expected: Submission is blocked and a validation message (e.g., "Title is required") is shown; no empty post is added to the feed.
- [ ] CS-02: Post must have a category selected
  - Action: Fill in the title and body but leave the category unselected (if not pre-selected), then submit.
  - Expected: Submission is blocked with a validation message, or a valid default category is explicitly applied — the post never appears with a missing/undefined category.
- [ ] CS-03: Guest (non-signed-in) users cannot create posts or comments
  - Action: Sign out (or load the site in a fresh session without signing in) and attempt to create a post or submit a comment.
  - Expected: The create/comment actions are unavailable or prompt the user to sign in; no post/comment is created anonymously.
- [ ] CS-04: Comment cannot be submitted with empty text
  - Action: Open a post's comment area and click the comment submit button with the text field empty.
  - Expected: Submission is blocked (button disabled or validation message shown); no empty comment is added.
- [ ] CS-05: Category filter and keyword search can be combined without breaking the feed
  - Action: Apply a category filter, then enter a search keyword that matches no posts in that category.
  - Expected: The feed shows an empty-state message (e.g., "No posts found") rather than unrelated posts or an error.

## Interaction
- [ ] IX-01: Submitting a post gives immediate visible feedback
  - Action: Successfully submit a new post.
  - Expected: The interface responds immediately (e.g., success toast/message or the feed scrolls to / highlights the new post) without requiring a manual page reload.
- [ ] IX-02: Filters and search update the feed without a full page reload breaking state
  - Action: Click a category filter chip or press Enter in the search box.
  - Expected: The visible feed updates to the filtered result set immediately; an active filter is visually indicated (e.g., highlighted chip).
- [ ] IX-03: Clearing the filter/search restores the full feed
  - Action: After filtering or searching, click "Clear"/"All" (or empty the search box).
  - Expected: The feed returns to showing all posts, including those hidden by the filter.
- [ ] IX-04: Resolved status change is reflected immediately on the post card
  - Action: Click "Mark as Resolved" on a post and observe the card without reloading.
  - Expected: The card's status badge/indicator changes to resolved state instantly (e.g., styled as resolved/greyed out).

## Content
- [ ] CT-01: Default feed content is relevant to neighborhood watch themes
  - Action: Review all pre-existing posts on the loaded feed.
  - Expected: Every post relates to neighborhood safety concerns or community events (e.g., suspicious activity, lost pet, block party) — no irrelevant/off-topic content.
- [ ] CT-02: Category labels on posts are accurate and limited to the defined set
  - Action: Inspect the category badge on each post in the feed.
  - Expected: Each badge shows one of the supported categories ("Safety Alert", "Lost and Found", "Community Event", or equivalent defined set) and matches the post's topic.
- [ ] CT-03: Posts display complete metadata
  - Action: Inspect individual post cards in the feed.
  - Expected: Each post shows author name, a readable timestamp/date, title, and body text — no placeholder text (e.g., "Lorem ipsum") or missing fields.