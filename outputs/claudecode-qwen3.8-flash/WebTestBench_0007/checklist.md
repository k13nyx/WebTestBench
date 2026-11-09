# Test Checklist

## Functionality
- [ ] FT-01: Visitor can sign up as a local resident and gain access as a logged-in user
  - Action: Click "Sign Up", enter name, email, and password, submit the form
  - Expected: Account is created and user is logged in (feed and "Create Post" are accessible, user identity is shown)

- [ ] FT-02: Logged-in user can create a post with a selected category
  - Action: Click "Create Post" / "New Post", enter a title and body (e.g., "Suspicious activity on Maple St"), select category "Safety Alert", submit
  - Expected: Post is created and appears in the feed with the correct category label

- [ ] FT-03: Recent alerts feed displays posts newest-first with key details
  - Action: Open the home/feed page without interacting
  - Expected: Feed lists posts in reverse chronological order; each card shows title, category, author, and timestamp

- [ ] FT-04: User can open a post to view full details
  - Action: Click a default post in the feed
  - Expected: Post detail view (or expanded card) shows the full body and its comments section

- [ ] FT-05: User can add a comment to an existing post
  - Action: Open a default post, type a comment (e.g., "Saw the same car twice last night"), submit
  - Expected: Comment appears under the post with the commenter's name and timestamp

- [ ] FT-06: User can mark a safety alert as resolved / no longer relevant
  - Action: Open a default "Safety Alert" post, click "Mark Resolved" (or "No Longer Relevant")
  - Expected: Post visibly displays a "Resolved" state/badge distinguishing it from active alerts

- [ ] FT-07: User can search the feed by keyword
  - Action: Type a keyword present in a default post (e.g., "bicycle") into the search field and submit
  - Expected: Feed shows only posts whose title or body contains the keyword

- [ ] FT-08: User can filter the feed by category
  - Action: Select the "Lost and Found" category filter
  - Expected: Feed shows only posts categorized as "Lost and Found"; other categories are hidden

## Constraint
- [ ] CS-01: Posting and commenting require a signed-up, logged-in user
  - Action: While signed out, attempt to reach "Create Post" and a comment form
  - Expected: Actions are hidden or disabled, with a prompt to sign in/log in; no post or comment is created

- [ ] CS-02: Empty required fields are rejected on post and comment forms
  - Action: Submit the post form with empty title/body or no category selected; submit an empty comment
  - Expected: Validation error message is shown for each missing field; nothing is added to the feed or post

- [ ] CS-03: Duplicate sign-up with an existing email is rejected
  - Action: Sign up again using an email that already belongs to a resident account
  - Expected: Error message (e.g., "Email already registered"); no duplicate account is created

- [ ] CS-04: Search with a non-matching keyword produces an explicit empty state
  - Action: Enter a keyword that appears in no default post (e.g., "zzzqqq") and search
  - Expected: A "no results" / "no matching posts" message is shown; the feed does not error or silently show all posts

- [ ] CS-05: Resolved state persists across navigation/reload
  - Action: Mark a default alert as resolved, then reload the page (still logged in)
  - Expected: The post still displays as resolved; the state was not lost

## Interaction
- [ ] IX-01: New post appears in the feed immediately with confirmation
  - Action: Create a post as a logged-in user and observe the feed
  - Expected: Success message/toast is shown and the new post appears at the top of the feed without manual data entry elsewhere

- [ ] IX-02: Active category filter is visually indicated and can be cleared
  - Action: Select "Community Event" filter, observe its state, then select "All" / clear the filter
  - Expected: The chosen filter shows an active/selected style; clearing restores the full feed

- [ ] IX-03: Comment count on the feed card updates after commenting
  - Action: Add a comment to a post showing "N comments", return to the feed
  - Expected: The post's comment count displays N+1

- [ ] IX-04: Marking resolved updates the post in place
  - Action: From the feed or post view, click "Mark Resolved" on an alert
  - Expected: The post immediately shows the resolved badge (button hidden or changed to "Reopen") without a full page reload

## Content
- [ ] CT-01: Default feed data covers all three categories with on-theme content
  - Action: Browse the default posts and category filter options
  - Expected: Pre-existing posts exist under "Safety Alert", "Lost and Found", and "Community Event"; titles/bodies relate to neighborhood safety or community life

- [ ] CT-02: Category labels are consistent everywhere
  - Action: Compare category names shown on post cards, in the create-post selector, and in the filter controls
  - Expected: The same exact labels are used in all three places (no typos or mismatched names)

- [ ] CT-03: No placeholder or broken content on the site
  - Action: Inspect the home page, a post detail, and the sign-up form
  - Expected: Site title/branding reflects a neighborhood watch purpose; no "lorem ipsum", empty broken links, missing images, or placeholder text remains