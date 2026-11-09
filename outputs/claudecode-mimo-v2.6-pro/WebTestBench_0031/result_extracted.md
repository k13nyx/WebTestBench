# Test Result

## Functionality
- [X] FT-01: User can register a new account with username, password, display name, and bio.
  - Action: Open the registration page, fill all fields with valid values (e.g., username "testuser1", display name "Test User", bio "Hello, I am a tester"), and click the "Register" (or "Sign up") button.
  - Expected: Registration succeeds and the user is redirected to the login page (or logged in directly), with the new account usable for login.
- [X] FT-02: User can log in with valid credentials.
  - Action: On the login page, enter the credentials registered in FT-01 and click the "Log in" (or "Sign in") button.
  - Expected: Login succeeds and the main chat page (room list / conversation view) is displayed.
- [X] FT-03: User can log out of the application.
  - Action: While logged in, click the "Log out" button/link.
  - Expected: The session ends and the login page is displayed; chat content is no longer accessible.
- [X] FT-04: User can join one or more chat rooms.
  - Action: From the room list, open/join one default chat room, then open/join a second default chat room.
  - Expected: Both rooms are joined and listed for the user, and the user can participate in each.
- [X] FT-05: User can switch between joined chat rooms and see each room's messages.
  - Action: Click on room A in the room list, then click on room B.
  - Expected: The conversation view updates to show the message history of the selected room, matching the correct room each time.
- [X] FT-06: User can send a text message in a chat room.
  - Action: Open a joined room, type "Hello everyone" in the message input, and click "Send" (or press Enter).
  - Expected: The message "Hello everyone" appears in the conversation of that room with the sender's display name and a timestamp.
- [X] FT-07: User can send a message containing emoji.
  - Action: Type a message containing emoji characters (e.g., "Great job! 🎉👍") in the message input and send it.
  - Expected: The message appears in the conversation with the emoji rendered as emoji (not as escaped text such as `:joy:` or `&#x1F;`).
- [ ] FT-08: Messages sent by other users appear in the conversation.
  - Action: With two accounts in the same room (two browser sessions), send a message from user B while user A views the room.
  - Expected: User A sees user B's message appear in the conversation of the shared room.
  - Bug Report:
    - Issue: Missing Live Message Sync (Cross-Session Message Delivery Failure)
    - Actual: User B's message "Hello from user B session" (sent from a second session as Alex Chen) was accepted and stored in the shared room history, but it never appeared in user A's open conversation view — not during 20+ seconds of hands-off observation, not after bringing user A's tab to focus, and not after switching rooms away and back. The message list continued to end at "Great job! 🎉👍"; the new message became visible only after a full page reload.
- [X] FT-09: User can edit profile display name and short bio.
  - Action: Open the profile page/settings, change the display name to "QA Tester" and the bio to "Testing chats", and save.
  - Expected: The profile saves successfully and shows display name "QA Tester" and bio "Testing chats".
- [X] FT-10: User can choose a theme and a font style.
  - Action: Open appearance settings, select a different theme, then select a different font style.
  - Expected: At least two themes and at least two font styles are offered, and the selected options are saved as the user's choices (persist after page reload).
- [ ] FT-11: User can search chat history by keyword.
  - Action: Enter a keyword that exists in a default message of the current room's history (e.g., a word from an existing message) in the search field and submit.
  - Expected: A list of matching messages from the chat history is displayed, each showing the matched message content.
  - Bug Report:
    - Issue: Missing Search Results List
    - Actual: Submitting keywords such as "standups" or "design" only displays a static "N of M results" counter (e.g., "1 of 2 results") next to the search input and highlights the first matching message inside the full conversation. No list of matching messages is rendered anywhere in the DOM (no results panel, dropdown, or result items showing matched message content).
- [ ] FT-12: User can jump to a matching message in the conversation.
  - Action: Click one of the search results returned in FT-11.
  - Expected: The conversation view scrolls to and indicates (highlights or centers) the exact matching message in the room.
  - Bug Report:
    - Issue: Missing Element — No Clickable Search Results
    - Actual: The action cannot be performed: there are no clickable search result items. The "N of M results" indicator is a non-interactive `<span>` (cursor: auto; clicking it opens nothing), and pressing Enter again does not advance to the next match ("1 of 2 results" stays on the first match). The app only auto-highlights the first matching message on submit (`message-highlight` class), so the user cannot click/jump to a chosen matching message.

## Constraint
- [X] CS-01: Registration is blocked for an already-used username.
  - Action: On the registration page, submit the form with the username of an existing account and any valid password/other fields.
  - Expected: Registration fails with an error message indicating the username is already taken; no duplicate account is created.
- [X] CS-02: Login is blocked for invalid credentials.
  - Action: On the login page, enter an existing username with an incorrect password and click "Log in".
  - Expected: Login fails with an error message indicating invalid credentials; the chat page is not shown.
- [ ] CS-03: Empty message cannot be sent.
  - Action: Leave the message input empty (or whitespace only) and click "Send".
  - Expected: No message is added to the conversation and an error/notice indicates the message cannot be empty.
  - Bug Report:
    - Issue: Missing Validation Notice (Silent Blocked Send)
    - Actual: With the input empty or whitespace-only ("   "), no message is added (message count unchanged at 18 before/after) and the Send button is disabled with Enter silently ignored — but no error message, toast, or notice of any kind is displayed to indicate the message cannot be empty (notification region stayed empty).
- [X] CS-04: Chat content is not accessible when logged out.
  - Action: Log out (or open a private window without logging in) and navigate directly to a chat room URL.
  - Expected: The user is redirected to the login page or shown a login prompt; no chat messages are displayed.

## Interaction
- [ ] IX-01: Conversation updates automatically when new messages arrive.
  - Action: With user A viewing a room, have user B send a message from another session; do not refresh or scroll on user A's page.
  - Expected: User B's message appears in user A's conversation view automatically, without a manual page refresh.
  - Bug Report:
    - Issue: No Automatic Conversation Update (Missing Live Sync)
    - Actual: User B's message did not appear in user A's view automatically. After 20+ seconds of polling with no refresh or scroll on user A's page, plus tab-focus and in-app room switching, the conversation remained unchanged (still ending at "Great job! 🎉👍"); the message only appeared after a full page reload. The app loads messages from storage once on mount with no storage-event/polling sync between sessions.
- [ ] IX-02: Theme and font changes apply immediately to the interface.
  - Action: In appearance settings, select a different theme and then a different font style, without reloading the page.
  - Expected: The page colors (theme) and text typeface (font) change immediately after each selection, and the visible UI reflects the new choice.
  - Bug Report:
    - Issue: Font Style Change Has No Visible Effect (Ineffective CSS Application)
    - Actual: The theme half works (selecting the emerald swatch immediately changed `--primary` from `238 84% 67%` to `160 84% 39%` and UI accents turned emerald), but selecting "Monospace" produced no typeface change: it only adds `font-style-mono` to `<html>`, and its rule `.font-style-mono { font-family: var(--font-mono) }` is overridden by the body's font-family — a sweep of all 48 visible text elements (body, headings, message text, dialogs) still computed to "Inter, system-ui, sans-serif". The visible UI never reflects the font choice.

## Content
- [X] CT-01: Each message displays its correct sender information and content.
  - Action: View a room containing messages from at least two different users (use default history or the messages sent in FT-06–FT-08).
  - Expected: Every message shows the correct author's display name and the exact message text, with no message attributed to the wrong user.
- [X] CT-02: Profile displays the saved display name and bio accurately.
  - Action: Open the profile page after saving changes in FT-09.
  - Expected: The profile shows exactly the saved display name and bio text, with no truncation or mismatch, and the same display name is shown next to that user's messages in chat.
