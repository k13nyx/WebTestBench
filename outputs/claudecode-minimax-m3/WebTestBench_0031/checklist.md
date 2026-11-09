# Test Checklist

> **Setup note:** Use the application's default chat rooms and default (pre-existing) messages for all items. A single test account must be registered for the registration/login items (FT-01, FT-02); all other items reuse it plus a second user where a live conversation (FT-06, CS-06) is required.

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the app, click the "Sign up" / "Register" control, enter a new username (e.g. `qa_user_01`), a password, and a password confirmation, then submit.
  - Expected: Registration succeeds with a success message; the app moves to the signed-in chat view and the new account appears as logged in.
- [ ] FT-02: Registered user can log in with valid credentials
  - Action: Sign out (or open the app in a fresh session), enter `qa_user_01` and its password on the login form, and submit.
  - Expected: Login succeeds with a success message and the user lands in the chat interface with their session active.
- [ ] FT-03: User can log out
  - Action: While signed in as `qa_user_01`, click the "Log out" / profile menu exit option.
  - Expected: A logout confirmation message appears, the session ends, and the login/register screen is shown; the chat rooms and messages are no longer accessible.
- [ ] FT-04: User can join one or more chat rooms
  - Action: On the signed-in chat view, open the room list/sidebar and select two different default rooms (e.g. "General" and one other), clicking "Join" on each.
  - Expected: Both rooms show as joined/active in the room list, and the user can switch between them in the conversation area.
- [ ] FT-05: User can send a message to a joined chat room
  - Action: In a joined room, type `Hello QA test message 1` in the message composer and click Send (or press Enter).
  - Expected: The message is submitted and appears in the conversation immediately with no error, and the composer is cleared.
- [ ] FT-06: Other users' messages appear live as the conversation continues
  - Action: With `qa_user_01` signed in on the chat page, have the second test user post a new message (e.g. `Hi from user 2`) in the same joined room.
  - Expected: `qa_user_01` sees the new message appear in the conversation without refreshing the page or re-navigating to the room.
- [ ] FT-07: User can set a display name and a short bio on their profile
  - Action: Open the profile/settings view, change the display name to `QA Tester` and the bio to `QA bot for chat testing`, save, then reopen the profile view.
  - Expected: The saved display name and bio are shown after reopening, confirming the values persisted.
- [ ] FT-08: User can search chat history by keyword
  - Action: In a joined room that contains default messages, open the search/history field, enter a keyword that appears in an existing message (e.g. a word visible in the default history), and submit or wait for results.
  - Expected: A results list appears showing only messages containing that keyword, and each result shows the matching text and its sender.

## Constraint
- [ ] CS-01: Registration is blocked when required fields are empty
  - Action: On the registration form, leave the username blank (or clear the password) and submit; repeat with a blank password confirmation.
  - Expected: Submission is rejected with a visible field-level validation message and no account is created; the form stays on the registration screen.
- [ ] CS-02: Duplicate usernames are rejected
  - Action: Attempt to register with the username `qa_user_01` (already registered) and a different password, then submit.
  - Expected: Registration is rejected with a message stating the username is already taken/in use, and no second account is created.
- [ ] CS-03: Password confirmation mismatch is rejected
  - Action: On the registration form, enter a new username, a password, and a different password in the confirmation field, then submit.
  - Expected: Submission is rejected with a password-mismatch validation message and no account is created.
- [ ] CS-04: Login with invalid credentials is rejected
  - Action: On the login form, enter the existing username `qa_user_01` with an incorrect password, then submit; repeat with a non-existent username.
  - Expected: Login is rejected with an error message (e.g. invalid username/password), no session is created, and the chat interface is not accessible.
- [ ] CS-05: Empty messages cannot be sent
  - Action: In a joined room, leave the composer empty (or enter only spaces) and click Send / press Enter.
  - Expected: No message is added to the conversation and no blank bubble appears; a validation hint or the Send control stays disabled.
- [ ] CS-06: Messages are isolated per room
  - Action: Send distinct messages from the same user in two different joined rooms, then view each room's conversation.
  - Expected: Each room shows only its own sent messages and the other room's messages do not appear.

## Interaction
- [ ] IX-01: Emoji picker opens on click and inserts an emoji into the composer
  - Action: Click the emoji button/icon in the message composer; a picker appears — select an emoji (e.g. a smiley) and observe the composer.
  - Expected: The picker opens on click, the selected emoji character is inserted into the composer text at the cursor, and the Send control becomes usable.
- [ ] IX-02: Selecting a theme applies immediately to the whole interface
  - Action: Open the theme selector, note the current theme, and choose a different theme from the list (the list must offer more than one option); observe the chat screen.
  - Expected: The entire chat interface (background, panels, message bubbles) visibly changes to the selected theme immediately without a page reload, and the newly selected theme is marked as active.
- [ ] IX-03: Selecting a font style applies immediately to message text
  - Action: Open the font-style selector, note the current font, and choose a different font style (the list must offer more than one option); observe the conversation.
  - Expected: The font of the message text visibly changes immediately without a page reload, and the newly selected font is marked as active.
- [ ] IX-04: A search result jumps to the matching message in the conversation
  - Action: Perform a keyword search (see FT-08), then click one of the returned search results.
  - Expected: The conversation view scrolls/jumps to that specific message, and the matched message is highlighted (e.g. highlighted text or focus outline) so it is visually identifiable in the message stream.

## Content
- [ ] CT-01: Each message displays the sender's display name, exact text, and emoji glyphs
  - Action: Send a message containing text and an emoji (e.g. `Hi there 👍`); also observe a message sent by the second test user.
  - Expected: The message bubble shows the sender's display name (not a raw username or blank), the typed text exactly as entered, and the emoji appears as a rendered emoji graphic/character rather than raw text code or a missing-glyph box.
- [ ] CT-02: Profile view displays the user's display name and short bio
  - Action: Open the profile view for `qa_user_01` (updated per FT-07) and inspect the profile fields.
  - Expected: The profile shows the display name `QA Tester` and the bio text `QA bot for chat testing` exactly as saved, with no placeholder, truncation, or empty values.