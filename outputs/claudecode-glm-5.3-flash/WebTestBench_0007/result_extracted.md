# Test Result

## Functionality

- [X] FT-02: Signed-in resident can create a post about a safety concern or community event
  - Action: Sign in, click the "Create Post" (or similarly named) button, enter a title and short body text, and submit.
  - Expected: The new post appears in the feed with the entered title, body, author name, and timestamp.
  - Observed: Via "New Post" dialog, submitted "Summer Movie Night in the Park - June 14th"; it appeared at the top of the feed with full body, author "Sarah Mitchell", and timestamp "less than a minute ago" — no reload needed.

- [X] FT-03: User can assign a category when creating a post
  - Action: Create a post and select a category from the category selector before submitting.
  - Expected: The published post displays the selected category label/badge on its card in the feed.
  - Observed: Selected "Community Event" in the dialog; the published post card displays a "Community Event" badge.

- [X] FT-04: User can comment on an existing post
  - Action: Open a post in the feed, type a comment in the comment field, and submit it.
  - Expected: The comment appears under the post, associated with the commenter's name, without a page error.
  - Observed: Comment "Update: we now have 12 volunteers signed up for the 6 PM setup team!" rendered under the post with author "Sarah Mitchell" and timestamp; comment counter changed 0 → 1 comments; no page error.

- [X] FT-05: User can filter the feed by category
  - Action: Click a single category filter (e.g., "Safety Alert").
  - Expected: The feed shows only posts labeled with that category; posts of other categories are hidden.
  - Observed: Clicking the "Safety Alert" chip left only the 2 Safety Alert posts ("Suspicious vehicle…", "Package thefts…"); Lost & Found and Community Event posts were hidden.

- [X] FT-06: User can search the feed by keyword
  - Action: Enter a keyword matching a known pre-existing post into the search box and submit.
  - Expected: Only posts containing that keyword (in title or body) are displayed.
  - Observed: Searching "Mango" (matches the cat post title) showed exactly one post: "Missing orange tabby cat - answers to 'Mango'". Search updates live as you type.

- [X] FT-07: User can mark an alert post as resolved or no longer relevant
  - Action: On a pre-existing alert post, click the "Mark as Resolved" action.
  - Expected: The post's status updates to show a visible "Resolved" indicator in the feed.
  - Observed: Clicking "Mark Resolved" on "Suspicious vehicle spotted on Oak Street" added a visible "Resolved" badge next to its "Safety Alert" badge, and the action button changed to "Reopen".

- [X] FT-08: Feed displays a list of recent posts by default
  - Action: Load the homepage/feed without applying any filter or search.
  - Expected: A list of pre-existing posts is displayed, ordered with the most recent posts first.
  - Observed: All 6 pre-existing posts load on the homepage; the newly created post (1 minute old) was placed at the very top of the feed, confirming most-recent-first ordering. (All seed posts share the coarse label "almost 2 years ago", so their relative order among themselves is not individually distinguishable, but newest-first behavior is confirmed.)

- [ ] FT-01: New resident can sign up for an account
  - Action: Open the sign-up form, enter a name, email, and password, and submit the registration.
  - Expected: Account is created successfully and the user is signed in with their identity visible.
  - Bug Report:
    - Issue: Missing Feature — no sign-up capability exists
    - Actual: There is no sign-up form anywhere in the app. The header contains only "New Post" and a non-functional "3" (notifications) button plus a static user chip; the full DOM contains zero occurrences of "Sign up", "Sign in", "Register", "Log in", or "Sign out". Direct navigation to `http://localhost:6007/signup` and `/login` both return the app's 404 page ("Oops! Page not found"). The app auto-authenticates a demo user ("Sarah Mitchell") on load with no way to register a new account.

## Constraint

- [X] CS-01: Post cannot be submitted with empty required fields
  - Action: Open the "Create Post" form, leave the title and/or body empty, and click submit.
  - Expected: Submission is blocked and a validation message is shown; no empty post is added to the feed.
  - Observed: Submitting with empty title/body is blocked (validated earlier in this session) — no empty post was added to the feed.

- [X] CS-02: Post must have a category selected
  - Action: Fill in the title and body but leave the category unselected, then submit.
  - Expected: Submission is blocked, or a valid default category is explicitly applied — the post never appears with a missing/undefined category.
  - Observed: The "Create New Post" dialog pre-selects "Safety Alert" as the default (chip in [active] state on open), and every post in the feed (7/7 checked) displays one of the three defined category badges — no post ever appears with a missing/undefined category.

- [X] CS-04: Comment cannot be submitted with empty text
  - Action: Open a post's comment area and click the comment submit button with the text field empty.
  - Expected: Submission is blocked (button disabled or validation message shown); no empty comment is added.
  - Observed: With the comment field empty, the submit button is `disabled`; programmatically clicking it added nothing (comment counts unchanged before/after).

- [X] CS-05: Category filter and keyword search can be combined without breaking the feed
  - Action: Apply a category filter, then enter a search keyword that matches no posts in that category.
  - Expected: The feed shows an empty-state message rather than unrelated posts or an error.
  - Observed: With the "Safety Alert" filter active, searching "Mango" (a Lost & Found keyword) produced the empty state "No posts found" — no unrelated posts, no error.

- [ ] CS-03: Guest (non-signed-in) users cannot create posts or comments
  - Action: Sign out (or load the site in a fresh session without signing in) and attempt to create a post or submit a comment.
  - Expected: The create/comment actions are unavailable or prompt the user to sign in; no post/comment is created anonymously.
  - Bug Report:
    - Issue: Missing Feature — no sign-out / guest state is unreachable
    - Actual: A fresh session (first page load) automatically presents an authenticated demo user ("Sarah Mitchell") without any sign-in step, and the "New Post" button and comment forms are immediately available. There is no sign-out control anywhere (user chip has no click handler; no menu; no "Sign out"/"Log out" text in the DOM), so a guest state can never be reached and the constraint's precondition ("sign out, or load a fresh session without signing in") cannot produce an unauthenticated session. The restriction is therefore unverifiable as specified.

## Interaction

- [X] IX-01: Submitting a post gives immediate visible feedback
  - Action: Successfully submit a new post.
  - Expected: The interface responds immediately (success toast/message or the feed scrolls to / highlights the new post) without requiring a manual page reload.
  - Observed: Immediately after clicking "Post to Neighborhood", a toast appeared: "Post created — Your post has been shared with the neighborhood.", the dialog closed, and the new post was visible at the top of the feed — all without a reload.

- [X] IX-02: Filters and search update the feed without a full page reload breaking state
  - Action: Click a category filter chip or press Enter in the search box.
  - Expected: The visible feed updates to the filtered result set immediately; an active filter is visually indicated.
  - Observed: Clicking "Safety Alert" updated the feed instantly (element refs persisted → client-side update, no reload); the active chip received highlighted `[active]` styling and an "Active filters: Safety Alert" indicator with a remove (×) button appeared. Search filtering also applied live while typing.

- [X] IX-03: Clearing the filter/search restores the full feed
  - Action: After filtering or searching, click "Clear"/"All" (or empty the search box).
  - Expected: The feed returns to showing all posts, including those hidden by the filter.
  - Observed: Emptying the search box and clicking "All" restored the complete feed (all 7 posts at the time, including the previously hidden categories).

- [X] IX-04: Resolved status change is reflected immediately on the post card
  - Action: Click "Mark as Resolved" on a post and observe the card without reloading.
  - Expected: The card's status badge/indicator changes to resolved state instantly.
  - Observed: Within the same interaction (checked <500 ms after click, no reload), the card gained the "Resolved" badge and the button switched from "Mark Resolved" to "Reopen" — instant client-side update.

## Content

- [X] CT-01: Default feed content is relevant to neighborhood watch themes
  - Action: Review all pre-existing posts on the loaded feed.
  - Expected: Every post relates to neighborhood safety concerns or community events — no irrelevant/off-topic content.
  - Observed: All 6 seed posts are on-topic: suspicious vehicle report, missing cat, holiday block party, package thefts, found car keys, neighborhood cleanup day. No off-topic content.

- [X] CT-02: Category labels on posts are accurate and limited to the defined set
  - Action: Inspect the category badge on each post in the feed.
  - Expected: Each badge shows one of the supported categories and matches the post's topic.
  - Observed: Badges are limited to exactly "Safety Alert", "Lost & Found", "Community Event", and each matches its post's topic (e.g., "Mango" cat → Lost & Found; block party → Community Event; suspicious vehicle → Safety Alert).

- [X] CT-03: Posts display complete metadata
  - Action: Inspect individual post cards in the feed.
  - Expected: Each post shows author name, a readable timestamp/date, title, and body text — no placeholder text or missing fields.
  - Observed: Automated check of all 6 cards: each has an author name (Marcus Johnson, Elena Rodriguez, Sarah Mitchell, David Chen), a readable relative timestamp ("almost 2 years ago"), a title, full body text, and a category badge; zero lorem-ipsum/placeholder text detected.
