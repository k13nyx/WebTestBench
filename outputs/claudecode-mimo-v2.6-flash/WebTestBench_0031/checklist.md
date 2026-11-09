# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration form, fill in a unique username/email, password, display name, and submit.
  - Expected: Account is created and the user is signed in (or redirected to the login page) without errors.
- [ ] FT-02: User can log in with valid credentials
  - Action: On the login page, enter a registered username/email and correct password, then click "Log In".
  - Expected: User is authenticated and lands on the chat room list or default room.
- [ ] FT-03: User can participate in more than one chat room
  - Action: Join/select a first room, send a message, then switch to a second room and send a message there.
  - Expected: Both rooms exist, each accepts messages, and messages stay in the room where they were sent.
- [ ] FT-04: User can send a message to a chat room
  - Action: Type a text message in the message input of an open room and click "Send" (or press Enter).
  - Expected: The message appears in that room's conversation attributed to the current user.
- [ ] FT-05: Other users' messages appear as the conversation continues
  - Action: With a second logged-in user, send a message from that user while the first user's room is open.
  - Expected: The first user's conversation updates and displays the incoming message without reloading the page.
- [ ] FT-06: User can edit their profile display name and bio
  - Action: Open the profile page, change the display name and enter a short bio, then save.
  - Expected: Profile saves and the new display name and bio are shown on the profile page.
- [ ] FT-07: User can search chat history by keyword
  - Action: Enter a keyword that exists in earlier messages into the chat history search field and submit.
  - Expected: A list of messages containing the keyword is returned with their text shown.
- [ ] FT-08: User can jump from a search result to the matching message
  - Action: Click one of the keyword search results.
  - Expected: The conversation view navigates to that message within the conversation and the target message is visible/indicated.
- [ ] FT-09: User can choose a theme and a font style
  - Action: Open the appearance settings, select a different theme, then select a different font style.
  - Expected: Both options are selectable, the chosen option is marked as selected, and the choice persists after closing the settings.

## Constraint
- [ ] CS-01: Registration cannot be completed with empty required fields
  - Action: Leave the required registration fields (e.g., username/email and password) blank and submit the form.
  - Expected: Submission is blocked and a validation error identifies the missing field(s); no account is created.
- [ ] CS-02: Duplicate accounts cannot be registered
  - Action: Attempt to register using a username/email that already exists.
  - Expected: Registration is rejected with a "username/email already taken" style error message.
- [ ] CS-03: Login with incorrect credentials is rejected
  - Action: Enter a valid username with a wrong password and click "Log In".
  - Expected: Login fails with an invalid-credentials error and access to chat rooms is denied.
- [ ] CS-04: Empty or whitespace-only messages cannot be sent
  - Action: Leave the message input empty (or spaces only) and attempt to send.
  - Expected: No message is posted to the conversation; sending is blocked or an error is shown.

## Interaction
- [ ] IX-01: Emoji can be inserted into a message
  - Action: Open the emoji picker, click an emoji (e.g., 😊) while composing a message.
  - Expected: The selected emoji is inserted at the cursor position in the message input and is sent/rendered correctly if submitted.
- [ ] IX-02: Sending a message gives immediate feedback without a page reload
  - Action: Send a valid message in a room.
  - Expected: The message appears in the conversation immediately, the input clears, and the page does not reload.
- [ ] IX-03: Switching rooms updates the visible conversation
  - Action: Click on a different room in the room list while a conversation is open.
  - Expected: The conversation area is replaced with the selected room's messages, and that room is visually indicated as active.
- [ ] IX-04: Jumping to a search match gives clear visual orientation
  - Action: Click a chat history search result to jump to its message.
  - Expected: The view scrolls to the matching message and the message is highlighted or otherwise clearly indicated.

## Content
- [ ] CT-01: Messages are attributed with the sender's display name
  - Action: Observe the conversation containing messages from multiple users.
  - Expected: Every message shows the sender's profile display name (not a raw username/id).
- [ ] CT-02: The selected theme and font style are actually reflected in the interface
  - Action: Choose a non-default theme and a non-default font style, then view the chat page.
  - Expected: Page colors/styling match the chosen theme and message/text content renders in the chosen font style.
- [ ] CT-03: The profile displays the correct name and bio content
  - Action: Open the profile of a user whose display name and bio were set.
  - Expected: The profile shows exactly the saved display name and bio text, with no placeholder or stale content.