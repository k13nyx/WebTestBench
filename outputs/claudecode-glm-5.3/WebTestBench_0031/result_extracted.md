# Test Result

## Functionality
- [X] FT-01: New user can register an account
  - Action: Open the registration page, fill in all required fields (e.g., username/email, password) with valid values, click "Register" / "Sign Up".
  - Expected: Registration succeeds; the app confirms account creation or redirects to the login/chat page.

- [X] FT-02: Registered user can log in
  - Action: On the login page, enter the credentials created in FT-01 and click "Login".
  - Expected: User enters the chat interface showing the chat room list.

- [X] FT-03: User can open a chat room and view its history
  - Action: After login, click one of the default chat rooms in the room list.
  - Expected: The room opens and its existing message history is displayed in the conversation pane.

- [X] FT-04: User can send a text message
  - Action: In an open room, type "Hello everyone" into the message input and press Enter / click "Send".
  - Expected: The message appears in the conversation pane.

- [X] FT-05: User can send a message containing an emoji
  - Action: In an open room, type text, insert an emoji (e.g., 😀) via the emoji picker or keyboard, and send the message.
  - Expected: The sent message includes both the typed text and the inserted emoji.

- [ ] FT-06: Two users in the same room see each other's messages
  - Action: Log in as a second registered user in another browser window/incognito session, open the same room, and send a message.
  - Expected: The first user's conversation pane shows the second user's message.
  - Bug Report:
    - Issue: Missing real-time/cross-session message delivery (no sync between sessions)
    - Actual: Second user "Second Tester" (registered in a second browser tab) sent "Hi from the second user!" in #General; the first user's (QA Engineer) conversation pane in the same room never showed the message — the first tab stayed idle without reload for 13+ seconds and still displayed only the 4 default messages. A manual `storage` event listener confirmed the `chat_app_messages` change event fired in the first tab, but the app has no listener/polling to react; the second user's message only appeared in the first pane after a manual page reload.

- [X] FT-07: Chat history is searchable by keyword
  - Action: With a room open, pick a word visible in its history (from default data), enter it into the search box, and run the search.
  - Expected: Search results list the messages containing that keyword, and messages without the keyword are excluded.

- [X] FT-08: User can jump to a matching message
  - Action: From the FT-07 search results, click/select one matching message.
  - Expected: The conversation view navigates to that message (e.g., scrolls to it and/or highlights it) in context.

- [X] FT-09: User can edit profile display name and bio
  - Action: Open the profile page, change the display name and short bio, and save.
  - Expected: The profile shows the updated name and bio; changes persist after a page reload.

- [X] FT-10: User can switch between chat rooms
  - Action: From an open room, click a different default room in the room list.
  - Expected: The conversation pane loads the newly selected room's own message history.

## Constraint
- [X] CS-01: Registration with empty required fields is rejected
  - Action: On the registration page, leave required fields (e.g., username, password) empty and submit.
  - Expected: Registration is blocked with a validation error; no account is created.

- [X] CS-02: Login with wrong credentials is rejected
  - Action: On the login page, enter a valid username with an incorrect password and click "Login".
  - Expected: Login fails with an error message; user remains on the login page.

- [X] CS-03: Empty message cannot be sent
  - Action: In an open room, click "Send" with an empty (or whitespace-only) message input.
  - Expected: No empty message is added to the conversation.

## Interaction
- [ ] IX-01: Incoming messages appear without a page refresh
  - Action: With two users in the same room (per FT-06), have the second user send a message while the first user's window stays idle.
  - Expected: The message appears in the first user's conversation pane automatically, without reloading the page.
  - Bug Report:
    - Issue: No automatic update of conversation pane (no WebSocket/polling/storage-event sync)
    - Actual: While the first user's window stayed idle in #General, the second user sent "Hi from the second user!" from another tab; after 13+ seconds the message had not appeared in the first user's pane. Verified the browser `storage` event for `chat_app_messages` fired in the first tab, but the app UI never re-rendered — the message only became visible after a manual page reload (navigation to the same URL).

- [X] IX-02: Theme switch applies immediately
  - Action: Open theme settings and select a different theme (e.g., dark theme).
  - Expected: The chat interface colors update immediately to the selected theme.

- [ ] IX-03: Font style switch applies immediately
  - Action: Open font/style settings and choose a different font style option.
  - Expected: Message and interface text render in the newly selected font immediately.
  - Bug Report:
    - Issue: Font style setting has no visible effect (CSS override prevents new font from rendering)
    - Actual: Selecting "Monospace" and "Modern" in Settings toggles the html class (`font-style-mono` → `font-family: var(--font-mono)` = "JetBrains Mono, monospace"; `font-style-modern` → Poppins), but all visible text — messages, sender names, headings, inputs — still computes `font-family: "Inter", system-ui, sans-serif`, because the stylesheet rule `body { font-family: var(--font-sans) }` overrides the html-level font for the entire app. Only the html element itself (not visible text) and the ChatFlow logo (explicit `font-display` class) change font; message and interface text never render in the newly selected font.

## Content
- [X] CT-01: Emoji render as proper emoji characters
  - Action: Send a message containing emoji (e.g., 😀, 🎉) and view it in the conversation pane.
  - Expected: Emoji display as correct graphical emoji glyphs — no garbled text, escape sequences, or broken characters.

- [X] CT-02: Messages are labeled with the sender's display name
  - Action: View messages in a room, including your own and others' from the default data.
  - Expected: Each message shows the sender's display name, matching what is set/displayed on that user's profile.

- [X] CT-03: Chat UI media and icons load correctly
  - Action: Browse the room list, an open conversation, the emoji picker, profile page, and theme settings.
  - Expected: All icons, avatars, and emoji-picker graphics render as intended with no broken image placeholders.
