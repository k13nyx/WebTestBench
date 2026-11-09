# Test Result

## Functionality
- [X] FT-01: Registered user can create a poll with all fields
  - Action: Logged in as demo user (created account for QA Tester first; used demo since sign-up accounts don't persist across reloads), opened /create, entered question "Best QA Tool for 2026?", description, two choices (Playwright, Selenium), deadline 2026-12-31T23:59, selected Anonymous mode, submitted.
  - Expected: Poll created and viewable; all fields displayed correctly. → Confirmed on `/manage/` and `/poll/` views: question, description, choices, "Ends Dec 31, 11:59 PM", "Anonymous" all displayed; toast "Poll created successfully!".

- [ ] FT-02: Poll creator can obtain a shareable link
  - Action: Opened created poll's manage page, clicked "Copy" in the Share Your Poll panel, then opened the shared link.
  - Expected: A unique poll link is displayed/copyable, and opening that link leads directly to the voting page for that poll.
  - Bug Report:
    - Issue: Broken shared-link access / non-persistent data store
    - Actual: The unique link `http://localhost:6015/poll/poll-1794109493583` is displayed and "Copy" works (toast "Link copied to clipboard!", button becomes "Copied!"). But opening that link in a fresh page load or a second tab — the only way a real recipient can open a shared link — renders "Poll Not Found" ("This poll may have been deleted or the link is incorrect."). The app's poll/user state lives only in tab memory (localStorage/sessionStorage are empty; a same-tab reload also wipes the poll and logs the user out). Full page reloads of /create even kick a logged-in user to /login.

- [X] FT-03: Voter can cast a vote via the shared link
  - Action: As a logged-out voter, opened the poll page for the shared URL (`/poll/poll-1794109493583`), selected "Playwright", clicked "Submit Vote".
  - Expected: Vote recorded and confirmation shown. → Vote count went 0 → 1 ("1 votes" header, "Total votes: 1"), page confirmed with toast "Your vote has been recorded!" and "✓ Thank you for voting!" results view. (Link target reached via in-session routing; fresh-session reachability defect is logged under FT-02.)

- [X] FT-04: Live results are visible after voting
  - Action: Remained on the results view after voting.
  - Expected: Bar-style breakdown shown immediately with per-choice counts/percentages. → Immediately after the vote the results view rendered: Playwright "1 vote 100%", Selenium "0 votes 0%", "Total votes: 1", with proportional animated bars.

- [X] FT-05: Results update as new votes are cast
  - Action: Cast an additional vote (Selenium) from a different voter session (logged-in demo identity, distinct from the earlier logged-out anonymous vote), then re-checked the results view.
  - Expected: Bar breakdown reflects new totals. → Totals updated 1 → 2 ("2 votes" header, "Total votes: 2"), bars re-split to Playwright 50% / Selenium 50%. Note: a fully separate browser session could not be used because the poll does not exist outside the creator's tab session (FT-02 defect); within the app's reachable scope, results updated correctly.

- [X] FT-06: Creator can manage poll status (close, reopen, read-only)
  - Action: On `/manage/poll-1794109493583`, clicked Close, then Open, then Read-only, verifying the vote page after each change.
  - Expected: Close → voting disabled; reopen → voting enabled; read-only → results shown, no new votes. → After Close: badge "closed", toast "Poll has been closed", vote page showed "This poll is closed and no longer accepting votes." with no voting controls. After Open: badge "active", "Poll is accepting votes", choice buttons re-enabled (Submit enabled after selection). After Read-only: badge "readonly", "Poll is now in read-only mode", vote page showed results (Total votes: 2) with zero voting controls present.

- [ ] FT-07: Dashboard lists polls and supports search and sort
  - Action: Opened dashboard, searched "QA", and sorted by title (Title A-Z), creation date (Newest/Oldest first), and attempted to sort by status.
  - Expected: Search filters by title keyword; sorting reorders by title, creation date, and status respectively.
  - Bug Report:
    - Issue: Missing sort option (status)
    - Actual: Search "QA" correctly filtered to "Best QA Tool for 2026?" (note: it also matches description text, not only title — e.g., query "Q" showed the Coffee polls whose titles lack "Q" due to "required" in the description). Title A-Z ordering correct (Best Programming… < Best QA… < Coffee… < Office… < Team…). Oldest/Newest ordering correct by date. However the sort dropdown offers only "Newest first, Oldest first, Title A-Z, Most votes" — there is no sort-by-status control; status is only available as filter tabs (all/active/closed/readonly), so "sort by status" is not supported.

## Constraint
- [ ] CS-01: Poll requires a question and at least two choices
  - Action: Submitted the creation form with fewer than two choices filled, and separately with the question empty.
  - Expected: Creation blocked and a validation error shown; poll not created.
  - Bug Report:
    - Issue: Missing validation message for empty question
    - Actual: Fewer-than-two-choices case is correct: submit is accepted but blocked with error toast "Please add at least 2 options" and no poll created. Empty-question case: creation is blocked, but only because the "Create Poll" button silently becomes `disabled` — no validation error message is displayed at all (form text contains no "required"/"Please…" hint). The expected "validation error is shown" is not met for the question field.

- [X] CS-02: Anonymous polls allow voting without sign-in; sign-in-required polls reject anonymous voters
  - Action: While logged out, opened the anonymous poll (`/poll/poll-1794109493583`) and voted; while logged out, opened the sign-in-required poll (`/poll/poll-1794109578662`).
  - Expected: Anonymous poll accepts vote with no login prompt; sign-in-required poll shows sign-in prompt and blocks voting. → Anonymous poll: active choice buttons + Submit, vote recorded, no login prompt anywhere. Sign-in-required poll: "Sign in to vote / This poll requires authentication to prevent duplicate votes." panel with Log in / Sign up buttons, and Coffee/Tea/Submit Vote controls all `disabled`.

- [X] CS-03: Expired polls do not accept votes
  - Action: Opened default poll `/poll/poll-1` (deadline Nov 1, 2024 — passed) and attempted to vote.
  - Expected: Voting controls disabled/hidden, results still viewable, no vote recorded. → No choice buttons or Submit Vote rendered; message "This poll has expired and is no longer accepting votes."; full results shown (Python 45, JavaScript 32, Scratch 18, Java 12; Total votes: 107).

- [X] CS-04: A voter cannot vote twice on the same poll
  - Action: After successfully voting on a poll, immediately attempted to vote again in the same session/account.
  - Expected: Second vote rejected and total does not increase. → After each vote, the voting controls are replaced by the "✓ Thank you for voting!" results view — no option or Submit Vote control remains, and the total stayed at 1 (later at 2 after a distinct voter-session vote); no re-vote path exists.

## Interaction
- [X] IX-01: Confirmation feedback on vote submission
  - Action: Submitted votes and observed the interface.
  - Expected: Clear confirmation appears. → Toast "Your vote has been recorded!" plus immediate switch to the results view headed "✓ Thank you for voting!" on both votes.

- [X] IX-02: Status change is reflected in the UI immediately
  - Action: Closed, reopened, and set the poll to read-only as creator, observing the poll/manage pages and dashboard.
  - Expected: Status label updates immediately on poll page and dashboard without stale state. → Status chip flipped "active → closed → active → readonly" instantly on both manage and vote pages with matching toasts ("Poll has been closed", etc.) and helper text ("Poll is closed, no new votes allowed" → "Poll is accepting votes" → "Poll is now in read-only mode"). Dashboard reflected the newest state without reload: entry badge "readonly" and counts recalculated (active (4), readonly (2)).

- [X] IX-03: Search filters the dashboard list in real time
  - Action: Typed into the search field one character/segment at a time ("Q" → "QA " → "zzz").
  - Expected: List updates as query is entered; only matches shown; non-matching query shows explicit empty state. → After "Q": 3 polls; after "QA ": 1 poll ("Best QA Tool for 2026?"); after "zzz": list emptied with explicit "No polls found — Try adjusting your filters or search terms" state; clearing restored the full list. All without submit/reload.

## Content
- [ ] CT-01: Poll details display completely and consistently everywhere
  - Action: Compared question, description, choices, deadline, and mode on the voting page, the shared-link page, and the dashboard entry.
  - Expected: All fields display identically and legibly in each view; description and deadline not truncated or missing.
  - Bug Report:
    - Issue: Missing content on shared-link page (fresh session) / inconsistent field rendering
    - Actual: The shared-link page opened in a new tab or after any reload shows "Poll Not Found" — no question, description, choices, deadline, or mode displayed at all for created polls (state is per-tab in memory). Additionally, the deadline is rendered inconsistently across views ("Ends Dec 31, 11:59 PM" on the vote page vs "Due Dec 31" on dashboard vs "Expired Dec 31" on the seeded expired poll's vote page, whose dashboard entry shows only "Expired" with no deadline date), choices are truncated on dashboard entries ("+1 more options"), and expired polls still show an "active" status chip on the vote page.

- [X] CT-02: Bar breakdown content is accurate and relevant
  - Action: Inspected the results chart of default poll `/poll/poll-1` (107 recorded votes).
  - Expected: Each choice has a bar labeled with text, count, and percentage; bars proportional to counts; matches total. → All four choices (Python, JavaScript, Scratch, Java) have labeled bars: 45/32/18/12 votes = 107 total, displayed as 42%/30%/17%/11%; measured bar widths were exactly proportional (42.056%, 29.907%, 16.822%, 11.215% — matching count/total).
