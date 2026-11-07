# Test Result

## Functionality

- [ ] FT-01: New resident can sign up and access the site as a registered user
  - Action: Click the "Sign Up" / "Register" control, fill in display name, email, and password with valid values, and submit the form.
  - Expected: Registration succeeds, the user is signed in, their display name appears in the header/account area, and the post-creation control is available.
  - Bug Report:
    - Issue: Missing Feature — No registration/sign-up flow exists
    - Actual: There is no "Sign Up" / "Register" control anywhere in the UI. The header contains only "New Post", a notification button ("3"), and a static "Sarah Mitchell" account chip that opens no menu when clicked (no sign-out, no account options). Navigating to /register, /signup, /login, /auth, /sign-in and /join all render the app's 404 page ("Oops! Page not found / Return to Home"). /src/App.tsx defines only two routes (Index and NotFound), and /src/data/mockData.ts hard-codes `export const currentUser = users[0];`, so the session is permanently fixed to the seed user "Sarah Mitchell" with no way to create an account.

- [X] FT-02: Signed-in user can create a short post and it appears in the feed
  - Action: Click "New Post" (or equivalent), enter a short title/body about a safety concern, select a category, and submit.
  - Expected: The post is saved and appears in the feed of recent alerts with its title, body, category label, author name, and timestamp.

- [X] FT-03: Feed displays existing recent alerts by default
  - Action: Load the home/feed page without applying any filter or search.
  - Expected: A feed of pre-existing posts is visible, each showing title, body text, category label, author, and timestamp, ordered with the most recent post first.

- [X] FT-04: User can comment on an existing post
  - Action: Open a post from the default feed, type an update into the comment field, and submit it.
  - Expected: The comment is saved and appears in that post's comment list with the commenter's name and the comment text.

- [ ] FT-05: User can mark an alert as resolved / no longer relevant
  - Action: On a post in the default feed, click the "Mark as Resolved" (or "Resolved / No Longer Relevant") control and confirm if prompted.
  - Expected: The post's status becomes Resolved, and the resolved status is still present after reloading the page.
  - Bug Report:
    - Issue: State Not Persisted — resolved status is lost on page reload
    - Actual: Clicking "Mark Resolved" on the default post "Missing orange tabby cat - answers to \"Mango\"" immediately worked in-session: the card showed the "Resolved" badge, its button changed to "Reopen", and the stats updated. However, after reloading the page the post reverted to an active alert ("Mark Resolved" button, no "Resolved" badge) and the stats reverted to the seed values (Active Alerts "1", Resolved "2"). The two posts created during this session also disappeared after reload, confirming post state is held only in in-memory React state with no persistence.

- [X] FT-06: Feed can be filtered by category
  - Action: Use the category filter and select "Safety Alert".
  - Expected: The feed shows only posts labeled "Safety Alert"; posts of other categories (e.g., "Lost and Found", "Community Event") are not displayed.

- [X] FT-07: Feed can be searched by keyword
  - Action: Type a word that appears in the body/title of a default post into the search field and submit.
  - Expected: The feed shows only posts containing that keyword (title or body); posts without the keyword are not displayed.

## Constraint

- [ ] CS-01: A post cannot be submitted with an empty body
  - Action: Open the new-post form, leave the body/description field empty (title may be filled), and submit.
  - Expected: Submission is blocked, a validation message about the required description is shown, and no new post is added to the feed.
  - Bug Report:
    - Issue: Missing Validation Message — submission is silently blocked with no user-facing error
    - Actual: With the Title filled ("Only title no body provided") and Details empty — or containing only whitespace ("   ") — submission was blocked and no post was added, but no validation message was shown. The Details textarea carried no error styling (its class remained the plain `border border-input … min-h-[120px] bg-card`), had no `aria-invalid` attribute, and the dialog contained no `role="alert"` element or any text mentioning a required description. The only feedback was that the "Post to Neighborhood" button was greyed out (`disabled`), so a user gets no explanation of why the form cannot be submitted.

- [ ] CS-02: A post cannot be submitted without choosing a category
  - Action: Open the new-post form, fill title and body, leave the category unselected/default-empty, and submit.
  - Expected: Submission is blocked with a category-required message, and no new post is added to the feed.
  - Bug Report:
    - Issue: Validation Not Enforced — post is created with no category selected and no error shown
    - Actual: With the Title and Details filled and no category selected (all three category buttons rendered unselected, the "Safety Alert" button showing red error styling `border-2 border-destructive bg-destructive/5`), the "Post to Neighborhood" button stayed enabled. Clicking it closed the dialog, showed the success toast "Post created / Your post has been shared with the neighborhood", and added a new post to the feed (feed went from 6 to 7 posts) silently labeled "Safety Alert" — "Sarah Mitchell | 1 minute ago | Safety Alert | Test post for category validation". No category-required message was displayed at any point.

- [ ] CS-03: A comment cannot be submitted when empty
  - Action: Open a post's comment area and submit with an empty or whitespace-only comment field.
  - Expected: The empty comment is rejected, an inline message is shown, and no blank entry is added to the comment list.
  - Bug Report:
    - Issue: Missing Validation Message — empty comment silently rejected
    - Actual: With the comment field holding only whitespace ("    "), the send button was `disabled` and pressing Enter left the field unchanged ("    \n") with no blank entry added to the comment list. However, no inline message was displayed — the page contained no `role="alert"` or error text associated with the comment field. As with CS-01, rejection is enforced only by disabling the control, with no explanatory message to the user.

- [ ] CS-04: Sign-up rejects invalid or duplicate registration data
  - Action: Submit the sign-up form using an email that already exists in the default user data (then repeat with an empty email).
  - Expected: Registration fails with a clear error (e.g., "email already in use" / "email is required"), no account is created, and the user is not signed in.
  - Bug Report:
    - Issue: Missing Feature — no sign-up form to validate (depends on FT-01)
    - Actual: There is no sign-up form and no email field anywhere in the application, so neither a duplicate-email nor an empty-email submission can be performed. All auth routes (/register, /signup, /login, /auth, /sign-in, /join) return the 404 page, and the signed-in user is hard-coded to the seed user (Sarah Mitchell) in /src/data/mockData.ts. Consequently no duplicate-email or required-email error can ever be produced, and no account-creation path exists to be blocked.

- [X] CS-05: A post's status is mutually exclusive — resolved posts are not shown as active alerts
  - Action: Mark a default post as Resolved, then filter the feed by "Active" status (or check the active alerts view) if available; otherwise check the post's status area.
  - Expected: The post displays exactly one status — "Resolved" — and never simultaneously appears as an active/open alert.

- [X] CS-06: A search that matches nothing shows an empty state, not the unfiltered feed
  - Action: Enter a nonsense keyword (e.g., "zzzzqqq") into the search field and submit.
  - Expected: The feed shows no posts and displays a "No posts found" / "No results" message; no unrelated posts are listed and no error appears.

## Interaction

- [X] IX-01: Applying a category filter updates the feed in place
  - Action: With the full feed displayed, select a different category from the category filter.
  - Expected: The feed updates immediately without a full page reload or navigation, showing only the selected category's posts, and the selected filter remains visibly active.

- [X] IX-02: Clearing the filter/search restores the full feed
  - Action: Apply a category filter, then clear it (select "All" / click the clear control), and clear any search text.
  - Expected: The full default feed is shown again with all categories represented, and no filter remains active.

- [X] IX-03: Marking a post resolved updates that post immediately in the feed
  - Action: Click "Mark as Resolved" on a post while viewing the feed.
  - Expected: The post updates in place (no page reload, user stays on the feed) and shows a visible "Resolved" badge/indicator right away.

- [X] IX-04: Creating a post shows a confirmation and adds it to the top of the feed
  - Action: Submit a valid new post.
  - Expected: A success toast/notification confirms the post was created, the creation form closes, and the new post appears at the top of the feed.

- [X] IX-05: A post's comments can be opened and viewed from the feed
  - Action: Click a post's comment control/comment count in the feed.
  - Expected: The post's comment section expands in place revealing the existing comments and a comment input; clicking again collapses it.

## Content

- [X] CT-01: Feed posts show complete, relevant metadata
  - Action: Inspect three different default posts in the feed.
  - Expected: Each post displays a non-empty title, body text, category label, author name, and timestamp/relative date — with no missing or "undefined"/"null" placeholders.

- [X] CT-02: Category options exactly match the required neighborhood-watch categories
  - Action: Open the new-post category selector and compare with the filter's category options.
  - Expected: The available categories are "Safety Alert", "Lost and Found", and "Community Event" (wording may vary in case), with no extra unrelated categories and no placeholder options like "Category 1".

- [X] CT-03: Page content is on-theme for a neighborhood watch community
  - Action: Read the site title/heading, navigation labels, and the default feed content.
  - Expected: All headings, labels, and default posts relate to neighborhood safety, lost and found, or community events; no lorem ipsum, no off-topic or unrelated sample content, and no broken images/icons.
