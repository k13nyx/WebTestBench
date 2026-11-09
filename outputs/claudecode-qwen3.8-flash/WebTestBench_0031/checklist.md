# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: From the landing/login page, open the registration form, enter a unique username, password, display name, and submit.
  - Expected: Registration succeeds and the user is granted access to the chat rooms as the new account.

- [ ] FT-02: Existing user can log in
  - Action: Log out (or open a fresh session), enter the credentials of a default/pre-existing account, and submit the login form.
  - Expected: Login succeeds and the chat room list is displayed.

- [ ] FT-03: User can enter and switch between chat rooms
  - Action: From the room list, open the first default room, then select a second default room.
  - Expected: Each selected room opens and shows that room's own message history; multiple rooms exist and are individually accessible.

- [ ] FT-04: User can send a text message
  - Action: In an open room, type "hello world" into the message input and send it.
  - Expected: The message appears in the room's conversation with the sender's display name and a timestamp.

- [ ] FT-05: User can send a message containing emoji
  - Action: Open the emoji picker, insert at least two emoji (e.g., 😀 and 🎉) into the message input, and send.
  - Expected: The sent message renders the emoji as graphical characters, not as raw codes like `:smile:`.

- [ ] FT-06: User can view and edit their profile
  - Action: Open the profile page/settings for the logged-in user, change the display name and the short bio, and save.
  - Expected: The profile shows both a display name and a bio field; after saving, the new values are persisted and the new display name is shown on subsequently sent messages.

- [ ] FT-07: Chat history is searchable by keyword
  - Action: Use the search field and type a keyword known to exist in the default room history.
  - Expected: A result list is returned showing the matching message text, its sender, and its room/timestamp; a keyword with no matches returns an explicit "no results" state.

- [ ] FT-08: User can jump to a matching message
  - Action: From the search results, activate a match that is not currently visible in the conversation (e.g., an older message).
  - Expected: The conversation scrolls to that exact message and marks it as the located result (highlighted or selected).

## Constraint
- [ ] CS-01: Duplicate account identifiers are rejected
  - Action: Attempt to register using the username or email of an existing default account.
  - Expected: Registration is refused with a visible error naming the conflicting field; no second account is created.

- [ ] CS-02: Empty messages cannot be sent
  - Action: With the message input empty (or containing only spaces), press Enter / click the send button.
  - Expected: No message is added to the conversation and the input is not cleared.

- [ ] CS-03: Unauthenticated visitors cannot participate
  - Action: In a logged-out session, attempt to open a chat room and to submit the message input.
  - Expected: The app blocks access and directs the visitor to register/log in instead of showing or accepting messages.

- [ ] CS-04: Profile required fields are enforced
  - Action: In the profile editor, clear the display name and attempt to save.
  - Expected: The save is rejected with a validation message; the previously saved profile values remain unchanged.

## Interaction
- [ ] IX-01: Others' messages appear without a page reload
  - Action: Keep a room open in this browser while a second logged-in user sends a message in the same room.
  - Expected: The new message is appended to the open conversation automatically within a few seconds, with no manual refresh.

- [ ] IX-02: Theme selection applies to the interface
  - Action: Open the theme selector, choose a different available theme, then revisit the chat and profile views.
  - Expected: The chosen theme is applied immediately (background, text, and accent colors change) and remains applied after navigating or relogging.

- [ ] IX-03: Font style selection changes message typography
  - Action: Open the font/style selector and choose a different font option.
  - Expected: The rendered chat text visibly changes to the selected style (size/typeface differs from before) and persists for new messages.

- [ ] IX-04: Sending a message updates the input and view state
  - Action: Scroll up in a long conversation, type a message at the bottom input, and send it.
  - Expected: The input clears and the view returns to the newest message so the just-sent message is visible.

## Content
- [ ] CT-01: Default rooms and history are present and coherent
  - Action: Log in as a default user and inspect the room list and each room's history.
  - Expected: At least one (ideally multiple) named chat rooms exist, each pre-populated with messages from named users relevant to a chat application.

- [ ] CT-02: Theme and font options are offered as a set
  - Action: Open the theme selector and the font style selector.
  - Expected: Each selector lists several (at least three) clearly labeled options that can be chosen; no option is blank or duplicated.

- [ ] CT-03: Emoji picker content is usable
  - Action: Open the emoji picker in a room.
  - Expected: A grid/list of multiple distinct emoji is shown, each clickable to insert into the message input.