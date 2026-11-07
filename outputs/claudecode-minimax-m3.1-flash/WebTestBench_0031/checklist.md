# Test Checklist

## Functionality
- [ ] FT-01: New visitor can register an account
  - Action: Open the app home page, click the "Register" / "Sign up" link, fill in the registration form with a new username, a password, and confirm the password, then click "Register".
  - Expected: Registration succeeds, the app switches to the authenticated chat view (rooms sidebar + message area), and the new account's display name appears in the header/profile area.

- [ ] FT-02: Registered user can log in
  - Action: Log out if signed in, go to the login form, enter the username and password of the account created in FT-01, click "Log in".
  - Expected: Login succeeds, the user lands in the chat page, and the chat page shows the account's display name (not the raw username).

- [ ] FT-03: User can open a default chat room and see its existing history
  - Action: On the chat page, in the room list/sidebar, click any of the pre-existing (default) chat rooms.
  - Expected: The room opens, its name is shown as the active room, and existing messages for that room are displayed in the message list.

- [ ] FT-04: User can participate in more than one chat room
  - Action: Open a first room from the room list, then open a second, different room; then switch back to the first room.
  - Expected: Both rooms remain listed/joined; switching changes the active room, and each room shows only its own messages with no messages leaking between rooms.

- [ ] FT-05: User can send a message that appears in the conversation
  - Action: With a room open, type "Hello testing 1" in the message input box and press "Send" (or Enter).
  - Expected: The message immediately appears in the message list of the current room, attributed to the sender, and the input box is ready for the next message.

- [ ] FT-06: Messages support emoji
  - Action: Send a message containing emoji characters, e.g. "Hi 😀🎉" (via the emoji picker or typed directly).
  - Expected: The message is posted with its full text, and the emoji appear as rendered graphics/characters, not as broken images, empty boxes, or raw escape codes such as `:smile:`.

- [ ] FT-07: Messages from another user appear in the current user's conversation
  - Action: Open a second browser (or incognito) window, log in as a different registered user, join the same room, and send a message such as "Hello from user two".
  - Expected: The message appears in the first user's room view automatically, without manually refreshing the page, showing the second user's display name.

- [ ] FT-08: User profile holds a display name and a short bio
  - Action: Open the profile/settings page, set a display name (e.g. "Alex Tester") and a short bio (e.g. "QA bot for the chat app"), save, then reopen the profile page.
  - Expected: The saved display name and bio are shown exactly as entered, and the display name is used on subsequently sent messages.

- [ ] FT-09: Chat history is searchable by keyword
  - Action: In a room containing several messages, type an existing word from one message into the chat search box and trigger the search.
  - Expected: A result list is shown containing only the message(s) whose text contains the keyword, with the matching message identifiable (sender/context visible).

- [ ] FT-10: Search with no matching keyword is reported clearly
  - Action: Search the chat history for a keyword that does not exist in any message, e.g. "zzzqqq999".
  - Expected: The app shows an explicit "no results"/"no messages found" indication instead of an empty area with no explanation or an error.

- [ ] FT-11: User can change the visual theme
  - Action: Open the theme/appearance selector and choose a theme different from the current one (e.g. Dark when Light is active).
  - Expected: The visible color scheme of the chat page (background, panels, text) changes to match the selected theme immediately, without a page error.

- [ ] FT-12: User can change the font style
  - Action: Open the font/style selector and choose a font style different from the current one (e.g. a serif or monospace option).
  - Expected: The typeface of the chat interface (message text, headings, UI labels) changes to the selected font, visibly different from the previous style.

## Constraint
- [ ] CS-01: Invalid registration input is rejected
  - Action: Submit the registration form with a blank required field; then, separately, try to register with a username that already exists.
  - Expected: Each attempt is refused with a visible validation error (e.g. "Username required", "Username already taken"), and no account is created or overwritten.

- [ ] CS-02: Login with invalid credentials is rejected
  - Action: Enter an existing username with an incorrect password, then an unknown username, and click "Log in".
  - Expected: An error message is shown and the user remains on the login page without access to any chat room.

- [ ] CS-03: Empty messages cannot be sent
  - Action: With a room open, clear the message input box (and separately enter only spaces), then press "Send"/Enter.
  - Expected: No message is added to the conversation and no empty bubble is created; an error or disabled send state may be shown.

- [ ] CS-04: Theme and font choices persist after reload
  - Action: Select a non-default theme and a non-default font style, then reload the page (or log out and log back in).
  - Expected: The selected theme and font style are still applied after the reload/login, without reverting to defaults.

## Interaction
- [ ] IX-01: Emoji picker opens and inserts an emoji into the message input
  - Action: Click the emoji button/control next to the message input, then click an emoji in the opened picker.
  - Expected: The picker opens as a visible overlay/list of emoji; clicking an emoji inserts it into the message input box at the cursor, ready to send.

- [ ] IX-02: Clicking a search result jumps to that message in the conversation
  - Action: Perform a keyword search, then click one of the returned matches in the search results.
  - Expected: The main conversation view scrolls to that exact message and the message is visually indicated (e.g. highlighted), so the user can see it in context.

- [ ] IX-03: Incoming message updates the view without user action
  - Action: Keep a room open in one window while a second logged-in user posts a new message in that room.
  - Expected: The new message is appended to the message list in the first window without a manual refresh, and the view shows the new message's sender name and text.

## Content
- [ ] CT-01: Default chat room list is populated with meaningful rooms
  - Action: Open the room list/sidebar on the chat page.
  - Expected: The list is non-empty and shows chat-related room names (no blank entries, no "undefined", no lorem-ipsum/error text).

- [ ] CT-02: Every message is attributed and timestamped
  - Action: Inspect several messages in a room's history (including messages sent by another user).
  - Expected: Each message shows the sender's display name and a time/date indication, and the displayed text matches exactly what was sent (no truncation, encoding errors, or leftover markup).