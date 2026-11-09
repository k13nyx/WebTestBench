# Test Checklist

## Functionality
- [ ] FT-01: New user registration
  - Action: Open the page, go to the register/sign-up form, enter a unique username, password, display name, and short bio, then submit.
  - Expected: Registration succeeds and the user is either logged in immediately or shown a login form; no error is displayed.
- [ ] FT-02: Login with registered credentials
  - Action: On the login form, enter the credentials of a registered user and submit.
  - Expected: The user is logged in and sees the chat interface (e.g., room list or chat view) with their display name visible.
- [ ] FT-03: Send a message in a chat room
  - Action: Log in, open any chat room, type "Hello world" in the message input, and send it.
  - Expected: The message "Hello world" appears in the room's message list attributed to the current user's display name.
- [ ] FT-04: Send a message containing emoji
  - Action: In a chat room, type a message containing an emoji (e.g., "Great job 🎉") and send it.
  - Expected: The message appears in the chat with the emoji rendered correctly (as an emoji character or image, not broken text).
- [ ] FT-05: Messages from other users appear as the conversation continues
  - Action: Log in as User A in one browser, open the same room as User B in a second browser/session, and have User B send "Hi from B".
  - Expected: User A's view shows "Hi from B" from User B without requiring a manual page reload.
- [ ] FT-06: Participate in multiple chat rooms
  - Action: While logged in, join/enter a second chat room and send a message in it.
  - Expected: The message appears in the second room, and switching back to the first room shows the first room's separate history intact.
- [ ] FT-07: Search chat history by keyword
  - Action: In a room with existing messages, enter a keyword that exists in some messages (e.g., "deploy") into the search field and run the search.
  - Expected: Matching messages are listed/shown, and only messages containing the keyword are returned.
- [ ] FT-08: Jump to a matching message from search results
  - Action: Click on a search result for a keyword.
  - Expected: The conversation view scrolls to (or clearly navigates to/highlights) the matching message within the chat history.
- [ ] FT-09: Edit profile with display name and bio
  - Action: Open the profile page, change the display name and the short bio, and save.
  - Expected: The new display name and bio are saved and reflected in the profile view (and the new display name appears on messages the user sends afterwards).
- [ ] FT-10: Log out
  - Action: Click the logout button.
  - Expected: The user is logged out and returns to the login/landing screen; accessing chat content now requires logging in again.

## Constraint
- [ ] CS-01: Duplicate registration rejected
  - Action: Attempt to register with a username that already exists (e.g., one used in FT-01).
  - Expected: Registration is rejected with a clear error message (e.g., "username already taken") and the account is not created.
- [ ] CS-02: Login with wrong password rejected
  - Action: Enter a registered username with an incorrect password and submit.
  - Expected: Login fails with an error message; the user is not taken into the chat interface.
- [ ] CS-03: Cannot send an empty message
  - Action: In a chat room, click send with the message input empty (or containing only spaces).
  - Expected: No empty message is added to the chat; the input remains for typing (send is blocked or an error/validation is shown).
- [ ] CS-04: Search with no matches handled gracefully
  - Action: Search a room's history for a keyword that does not appear in any message (e.g., "zzzqqq").
  - Expected: A "no results" indication is shown; no error, no unrelated messages returned.

## Interaction
- [ ] IX-01: Theme selection changes the interface appearance
  - Action: Open the theme chooser (which offers several themes), select a different theme, and apply it.
  - Expected: The page's colors/visual appearance visibly change to the selected theme, and the choice persists after a page reload.
- [ ] IX-02: Font style selection changes text rendering
  - Action: Open the font style chooser, select a different font style, and apply it.
  - Expected: Chat text and UI text visibly render in the selected font style, and the choice persists after a page reload.
- [ ] IX-03: Enter key sends message
  - Action: Type a message in the chat input and press Enter.
  - Expected: The message is sent and appears in the chat, and the input field is cleared.
- [ ] IX-04: New message from another user draws attention / view follows conversation
  - Action: With User B sending a new message while User A is scrolled up in the room (or at the bottom), observe User A's view.
  - Expected: The new message becomes visible to User A (chat auto-scrolls to it or a "new message" indicator appears) without User A refreshing.

## Content
- [ ] CT-01: Default rooms and messages are present on first load
  - Action: Log in with a fresh/default account and view the room list and at least one room's history.
  - Expected: At least one chat room exists and contains pre-existing messages showing sender display names, message text, and timestamps.
- [ ] CT-02: Messages display sender and timestamp correctly
  - Action: Open a chat room and inspect several messages.
  - Expected: Each message shows the sender's display name and a readable timestamp, and content matches the chat-room context (no placeholder or irrelevant filler text).