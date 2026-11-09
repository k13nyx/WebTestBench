I have completed all checks. Here is the full updated checklist.

# Test Result

## Functionality
- [ ] FT-01: New resident can sign up for the neighborhood watch site
  - Action: Enter a valid name, email, and password, then click "Sign Up".
  - Expected: Account is created and user is signed in / redirected to the feed.
  - Bug Report:
    - Issue: Missing Feature (no sign-up/sign-in UI or route)
    - Actual: No sign-up form or control exists. The app loads already authenticated as "Sarah" with no account/avatar menu, and navigating to `/signup` and `/login` both return a "404 – Oops! Page not found" page. It is impossible to register.
- [X] FT-02: Signed-in user can create a short post
  - Action: Enter a title and body, select a category, click "Post".
  - Expected: The post is submitted and saved successfully.
- [X] FT-03: Newly created post appears in the feed
  - Action: Create a post, then view the feed.
  - Expected: The new post is displayed in the feed (at/near the top as the most recent alert).
- [X] FT-04: User can browse the feed of recent alerts
  - Action: Load the feed with default data present.
  - Expected: A list of existing posts is displayed in reverse-chronological order.
- [X] FT-05: User can categorize a post
  - Action: When creating a post, choose one of the categories (e.g. "Safety Alert", "Lost and Found", "Community Event").
  - Expected: The selected category is saved and shown on the post.
- [X] FT-06: User can filter the feed by category
  - Action: Select a single category in the filter (e.g. "Lost and Found").
  - Expected: Only posts belonging to that category are shown in the feed.
- [X] FT-07: User can search the feed by keyword
  - Action: Type a keyword that exists in a default post (e.g. a word from its title) into the search box.
  - Expected: Only posts containing the keyword are shown.
- [X] FT-08: User can comment on a post
  - Action: Open a post, enter comment text, click "Comment" / "Post Comment".
  - Expected: The comment is submitted and attached to that post.
- [X] FT-09: User can mark an alert as resolved
  - Action: On a default "Safety Alert" post, click "Mark as Resolved".
  - Expected: The post is updated to a resolved state.

## Constraint
- [ ] CS-01: Sign up cannot be submitted with empty required fields
  - Action: Leave email and/or password blank and click "Sign Up".
  - Expected: Submission is blocked and a validation message indicates the required field(s).
  - Bug Report:
    - Issue: Missing Feature (no sign-up form exists)
    - Actual: No email/password sign-up fields render anywhere in the app (app is pre-authenticated as "Sarah"), so this validation cannot be observed; no required-field message exists.
- [ ] CS-02: Post cannot be submitted with empty content
  - Action: Leave the post title and/or body blank and click "Post".
  - Expected: Submission is blocked with a message that content is required.
  - Bug Report:
    - Issue: Missing validation message (no feedback on attempted submit)
    - Actual: With Title and/or Details blank, "Post to Neighborhood" stays `disabled` and clicking it produces no response; no message stating that content is required is displayed anywhere (no error element / `role="alert"` / `required` attribute present in the dialog).
- [ ] CS-03: Post cannot be submitted without a category
  - Action: Enter valid post content but leave the category unselected, click "Post".
  - Expected: Submission is blocked with a message that a category must be selected.
  - Bug Report:
    - Issue: No category-required validation message; category cannot be left unselected
    - Actual: "Safety Alert" is selected by default and cannot be deselected (clicking the active category has no effect), so the "no category selected" state is unreachable and no "category must be selected" message is ever shown.
- [X] CS-04: Empty comment cannot be submitted
  - Action: With the comment field empty, click "Comment".
  - Expected: No comment is added; submission is blocked or disabled.
- [X] CS-05: Search/filter with no matches shows an empty state
  - Action: Enter a keyword or category that no default post matches.
  - Expected: An empty-state message (e.g. "No posts found") is shown instead of stale/incorrect posts.
- [ ] CS-06: Resolved alerts remain in a consistent resolved state
  - Action: Mark an alert as resolved, refresh the feed.
  - Expected: The post is still shown as resolved (state persists) and is not reverted to active.
  - Bug Report:
    - Issue: State not persisted on reload
    - Actual: After marking "Suspicious vehicle spotted on Oak Street" as resolved (badge "Resolved", button changed to "Reopen", stats Active 0 / Resolved 3), refreshing the page reverts it to "Mark Resolved" and the stats return to Active 1 / Resolved 2; the resolution is not persisted.

## Interaction
- [X] IX-01: User receives confirmation after creating a post
  - Action: Successfully create a post.
  - Expected: A visible success confirmation (toast/message) is shown.
- [X] IX-02: Resolved alerts are visually distinguished in the feed
  - Action: View the feed after marking a post resolved.
  - Expected: That post displays a clear "Resolved" indicator (label, badge, or dimmed style).
- [X] IX-03: Feed updates to reflect the active filter/search selection
  - Action: Apply a category filter, then clear it or switch categories.
  - Expected: The feed and the highlighted filter selection update accordingly without a full reload.

## Content
- [X] CT-01: Category labels match the specified set
  - Action: Inspect the category selector/options.
  - Expected: The categories "Safety Alert", "Lost and Found", and "Community Event" are available.
- [X] CT-02: Feed content is relevant to the neighborhood watch purpose
  - Action: Review the default posts and any images/icons shown.
  - Expected: All displayed content relates to local safety concerns and community events (no unrelated/placeholder imagery or text).

---

### Summary of findings
- **Passed (14):** FT-02, FT-03, FT-04, FT-05, FT-06, FT-07, FT-08, FT-09, CS-04, CS-05, IX-01, IX-02, IX-03, CT-01, CT-02.
- **Failed (5):**
  1. **FT-01 / CS-01** – No sign-up/sign-in capability at all (no UI, `/signup` and `/login` = 404). The app is hard-wired to a single pre-authenticated user.
  2. **CS-02 / CS-03** – Post validation relies solely on a `disabled` submit button; no "content required" or "category required" message is ever shown, and the category cannot be left unselected (defaults to Safety Alert).
  3. **CS-06** – Resolution state is not persisted; refreshing the feed reverts the post to active (post creation and comments also reset on reload).

Note: FT-09/IX-02 pass on immediate behavior, but the same underlying non-persistence surfaced by CS-06 also causes newly created posts and comments to disappear after a refresh.