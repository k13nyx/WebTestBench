# Test Result

## Functionality

- [ ] FT-01: Visitor can register a new resident account
  - Action: Click "Sign Up", fill name, email, and password (with confirmation), submit the form.
  - Expected: Account is created, a success confirmation is shown, and the user is signed in (header shows their name / a "Log Out" or "My Profile" option).
  - Bug Report:
    - Issue: Missing Feature (No Sign Up / Registration UI)
    - Actual: No "Sign Up" control exists anywhere in the application. The full DOM contains no "Sign Up", "password", or "email" text/inputs, and the router (`/src/App.tsx`) defines only two routes — `/` and a `*` 404 catch-all. Navigating to `/signup` renders the "404 — Oops! Page not found" page. The app ships with a hard-coded `currentUser` (Sarah Mitchell) and no registration flow.

- [ ] FT-02: Registered user can log in and log out
  - Action: Log out via the header, then use "Log In" with the registered email and password, then log out again.
  - Expected: Each step succeeds with no error, and the session state (signed-in vs. signed-out UI) matches the action performed.
  - Bug Report:
    - Issue: Missing Feature (No Log In / Log Out UI)
    - Actual: The header contains only "New Post", a notifications bell, and a static avatar + "Sarah" label. The avatar is not clickable (clicking it produced no menu) and there is no "Log Out", "Log In", "My Profile", or "Account" element in the DOM. The session is hard-coded, so signed-out state is unreachable.

- [X] FT-03: Resident can create a post with a title, body, and category
  - Action: Open the post creation form (e.g. "Create Post" / "New Post"), enter a title and short body, select category "Safety Alert", submit.
  - Expected: The post is created and appears in the feed with its title, body text, category label, author name, and a timestamp.

- [X] FT-04: All three categories are selectable and applied to created posts
  - Action: Create one post each with "Safety Alert", "Lost and Found", and "Community Event" categories.
  - Expected: Each post is created and displays the exact category label it was assigned.

- [X] FT-05: Feed displays existing default posts on initial page load
  - Action: Open the homepage/feed without logging in.
  - Expected: The feed renders the application's pre-existing default posts, each showing title, body excerpt, category, author, and timestamp.

- [X] FT-06: Resident can filter the feed by category
  - Action: Select the "Lost and Found" category filter (tab, dropdown, or filter control).
  - Expected: The feed shows only posts categorized as "Lost and Found"; no other category's posts remain visible.

- [X] FT-07: Resident can search the feed by keyword
  - Action: Type a keyword matching text in one default post's title/body into the search field and submit or wait for results.
  - Expected: Only posts matching that keyword are shown, and non-matching posts are excluded.

- [X] FT-08: Search can be combined with a category filter
  - Action: Select a category filter and enter a keyword, then view results.
  - Expected: The feed shows only posts that satisfy both conditions (matching category AND matching keyword).

- [X] FT-09: Resident can comment on a post
  - Action: Open the comments area of any post, type a comment, and submit it.
  - Expected: The comment is added and displayed immediately under that post with its text and author name.

- [X] FT-10: Marking an alert as resolved updates its state
  - Action: Click the "Resolve" / "Mark as Resolved" control on an unresolved alert post.
  - Expected: The post is visibly marked as resolved (e.g. "Resolved" badge/status) and the control no longer offers to resolve it again.

- [ ] FT-11: Resident can mark a post as no longer relevant
  - Action: Click the "Not Relevant" / "No Longer Relevant" control on a post.
  - Expected: The post is visibly marked as not relevant, distinct from the resolved state.
  - Bug Report:
    - Issue: Missing Feature (No "Not Relevant" Control / State)
    - Actual: There is no "Not Relevant" / "No Longer Relevant" control on any post card. A full button inventory of the rendered page yields only: "New Post", "3", "All", "Safety Alert", "Lost & Found", "Community Event", "Showing resolved", "<N> comments", "Mark Resolved", and "Reopen". The `Post` type in `/src/types/index.ts` has no relevance flag (`isRelevant`/`isNotRelevant` do not exist), and the app's only post state toggles are `isResolved`.

- [X] FT-12: Clear filters/search restores the full feed
  - Action: Apply a category filter and a search keyword, then use the "Clear" / "Reset" / "All" control.
  - Expected: The feed returns to showing all default posts again.

## Constraint

- [ ] CS-01: Post cannot be submitted with empty required fields
  - Action: Open the create-post form, leave the title and/or body blank, and submit.
  - Expected: Submission is blocked and a visible validation message indicates the missing required field(s); no empty post is added to the feed.
  - Bug Report:
    - Issue: Missing Validation Feedback (No Visible Error Message)
    - Actual: Submission is blocked and no empty post is added (the "Post to Neighborhood" button has `disabled: !title.trim() || !content.trim()`), but **no visible validation message is ever shown**. Clicking the disabled button left the dialog with only the static text "Create New Post / Share something with your neighbors / Category / Title / Details" and no error text, and no required-field indicator appears on the Title or Details inputs.

- [ ] CS-02: Post cannot be submitted without selecting a category
  - Action: Open the create-post form, enter a valid title and body, and attempt to submit without choosing a category.
  - Expected: Submission is blocked with a visible prompt to select a category, and no uncategorized post is created.
  - Bug Report:
    - Issue: Incorrect Form Validation (Silent Default Instead of Prompt)
    - Actual: Submission is **not** blocked and no prompt to select a category is shown. The form initializes `category` to `'community-event'` (`useState('community-event')`), so with only a title and body entered, "Post to Neighborhood" is enabled and the post is created silently as "Community Event". The expected behavior (block + visible prompt) never occurs; only the "no uncategorized post" half of the requirement holds.

- [ ] CS-03: Comment cannot be submitted with empty text
  - Action: Open a post's comment area, leave the comment field empty, and submit.
  - Expected: Submission is blocked with a validation message and no blank comment is added.
  - Bug Report:
    - Issue: Missing Validation Feedback (No Visible Error Message)
    - Actual: The submit button is disabled when the comment is empty (`disabled: !newComment.trim()`) and no blank comment is added, but **no validation message is displayed**. The comment form area contained no error text after attempting submission, and the "Add a comment..." field showed no invalid/required state.

- [ ] CS-04: Sign-up rejects an email that is already registered
  - Action: Attempt to sign up again using the email of an existing account.
  - Expected: The form shows an error stating the email is already in use, and no duplicate account is created.
  - Bug Report:
    - Issue: Missing Feature (No Sign Up Form / No Account Store)
    - Actual: No sign-up form or account-registration mechanism exists, so this scenario cannot be exercised. There is no email input, no account list, and no `/signup` route (it resolves to the 404 page). Accounts are hard-coded static objects in `/src/data/mockData.ts`.

- [ ] CS-05: Sign-up validates email format and password confirmation
  - Action: Submit a sign-up form with a malformed email, then with mismatched password and confirmation.
  - Expected: Each invalid submission is rejected with a specific validation message, and no account is created.
  - Bug Report:
    - Issue: Missing Feature (No Sign Up Form / No Password Fields)
    - Actual: No sign-up form exists; the words "password", "email", and "confirmation" appear nowhere in the rendered DOM, and the application has no registration code path. Both invalid-submission scenarios are untestable.

- [ ] CS-06: Login rejects invalid credentials
  - Action: Log in with a registered email and an incorrect password.
  - Expected: An error message is shown and the user is not signed in.
  - Bug Report:
    - Issue: Missing Feature (No Login Form)
    - Actual: No login form or credential check exists. The DOM contains no "Log In" / "Sign In" control and no email/password inputs; the session identity is a hard-coded `currentUser` constant, so there is no credential form to submit.

- [ ] CS-07: A resolved or not-relevant post cannot be resolved/marked again
  - Action: On a post already marked "Resolved", look for and attempt to use the resolve control; repeat for a "Not Relevant" post.
  - Expected: The state-changing control is disabled, hidden, or the action is rejected without changing the post's existing state.
  - Bug Report:
    - Issue: Partially Untestable (No "Not Relevant" Post State Exists)
    - Actual: The resolved-post half passes — a resolved post shows a "Resolved" badge with a line-through title and the "Mark Resolved" button is replaced by "Reopen" (`variant: post.isResolved ? 'ghost' : 'success'`), so it cannot be resolved again. However, the second half of the action is impossible: the application has no "Not Relevant" state or control (see FT-11), so no such post can be created or tested for re-marking.

- [ ] CS-08: Creating a post requires being signed in
  - Action: While signed out, open the create-post form and attempt to submit a post.
  - Expected: The user is prompted to log in or sign up, and no post is created.
  - Bug Report:
    - Issue: Missing Authentication Guard
    - Actual: There is no signed-out state and no auth guard. The app always renders the hard-coded `currentUser` (Sarah Mitchell) in the header, "New Post" is always enabled, and the "Create New Post" dialog opens and submits successfully for any visitor — no "log in or sign up" prompt is ever shown. Because no logout control exists (FT-02), the signed-out precondition of this test is also unreachable.

- [X] CS-09: Search with a keyword that matches no post shows an empty-result state
  - Action: Enter a nonsense keyword (e.g. "zzqx99") in the search field.
  - Expected: The feed shows a clear "no posts found" message with no post cards shown, rather than a blank or broken page.

## Interaction

- [X] IX-01: Successful post creation confirms with a visible success message
  - Action: Submit a valid new post and observe the page immediately after submission.
  - Expected: A success toast/notification (or equivalent confirmation) is displayed and the new post is visible in the feed.

- [X] IX-02: Category filter controls show the active selection
  - Action: Click a category filter, then click a different category filter.
  - Expected: The active filter is visually highlighted/selected, and the feed updates to the newly selected category.

- [X] IX-03: Post detail/comments expand on demand
  - Action: Click a post's title or a "View details" / comment-count control.
  - Expected: The post's full content and comment section are shown, and the "Comment" input becomes usable.

- [X] IX-04: Feed updates after commenting without a full page error
  - Action: Submit a comment and observe the post card.
  - Expected: The comment list and comment count update in place, the input clears, and the page remains fully functional.

- [X] IX-05: Post status change gives immediate visual feedback
  - Action: Click "Mark as Resolved" on an alert and observe the card immediately.
  - Expected: The card immediately shows the resolved state (badge/color/label change) without requiring a manual page reload.

- [X] IX-06: Search input reflects the typed keyword and responds on submit
  - Action: Type "street" into the search field and press Enter (or click the search button).
  - Expected: The typed keyword remains visible in the search field and the results update to matching posts.

## Content

- [X] CT-01: Page content is relevant to a neighborhood watch community site
  - Action: Review the homepage heading, navigation labels, section titles, and button labels.
  - Expected: All visible labels concern neighborhood watch activity (alerts, posts, categories, comments, sign up/log in) with no unrelated or placeholder text.

- [X] CT-02: Every feed post displays all required information
  - Action: Inspect each default post card in the feed.
  - Expected: Each shows a title, post body text, a category label, an author name, and a posted date/time.

- [ ] CT-03: Category labels use the specified wording
  - Action: Read the category labels used in the create-post form and on feed cards.
  - Expected: The three categories appear as "Safety Alert", "Lost and Found", and "Community Event".
  - Bug Report:
    - Issue: Incorrect Label Wording
    - Actual: The lost-and-found category is labeled **"Lost & Found"** (with an ampersand), not "Lost and Found". The wording comes from the shared `CATEGORY_CONFIG` in `/src/types/index.ts` (`'lost-and-found': { label: 'Lost & Found', ... }`) and is rendered identically in the feed filter bar, on every post card badge, and in the create-post dialog. Only "Safety Alert" and "Community Event" match the specified wording.

- [X] CT-04: Comments display their author and text correctly
  - Action: Read the comment entries under any post that has comments.
  - Expected: Each comment shows the comment text exactly as entered, the commenter's name, and a timestamp, with no truncation of the entered text.

- [X] CT-05: Default post content is meaningful neighborhood watch content
  - Action: Read the body text of the default posts in the feed.
  - Expected: Each post describes a plausible safety concern, lost-and-found item, or community event rather than lorem ipsum, empty, or test placeholder text.
