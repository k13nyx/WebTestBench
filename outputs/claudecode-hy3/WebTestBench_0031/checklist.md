# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Click "Sign Up", fill the registration form (username, email, password), click "Create Account".
  - Expected: Account is created and the user is logged in / redirected to the chat interface.

- [ ] FT-02: User can log in with valid credentials
  - Action: On the login page, enter a valid username/email and password, click "Log In".
  - Expected: User is authenticated and reaches the chat interface.

- [ ] FT-03: User can participate in one or more chat rooms
  - Action: From the room list, click a chat room (e.g., "General"), then join a second room.
  - Expected: User enters each room and can view/send messages; multiple rooms are accessible.

- [ ] FT-04: User can send a message in a chat room
  - Action: Type text in the message input box, click "Send".
  - Expected: The message appears in the conversation view.

- [ ] FT-05: User can send a message with emoji support
  - Action: Open the emoji picker, select an emoji, then click "Send".
  - Expected: The emoji renders correctly within the sent message.

- [ ] FT-06: User can create/edit a profile with display name and short bio
  - Action: Open profile settings, enter a display name and a short bio, click "Save".
  - Expected: Profile is saved with the provided display name and bio.

- [ ] FT-07: User can choose from several themes
  - Action: Open settings, select a theme (e.g., "Dark") from the list of options.
  - Expected: The selected theme preference is applied/saved.

- [ ] FT-08: User can choose from several font styles
  - Action: Open settings, select a font style from the available options.
  - Expected: The selected font style preference is applied/saved.

- [ ] FT-09: User can search chat history by keyword
  - Action: Enter a keyword in the search box, click "Search".
  - Expected: Chat history returns results matching the keyword.

- [ ] FT-10: User can jump to matching messages within the conversation
  - Action: From the search results, click a matching message.
  - Expected: The view scrolls/jumps to that message in the conversation.

## Constraint
- [ ] CS-01: Login is rejected with invalid credentials
  - Action: Enter a wrong password, click "Log In".
  - Expected: Login is rejected with an error message; no access is granted.

- [ ] CS-02: Empty messages cannot be sent
  - Action: Click "Send" with the message input empty.
  - Expected: Message is not sent; a required-field indicator is shown.

- [ ] CS-03: Profile display name is required
  - Action: Save the profile with an empty display name.
  - Expected: Save is rejected with a "display name required" error.

- [ ] CS-04: Chat rooms require authentication
  - Action: Attempt to open a chat room URL while not logged in.
  - Expected: User is redirected to the login page; rooms are inaccessible.

## Interaction
- [ ] IX-01: Other users' messages appear in real time
  - Action: With another active user in the same room, have them send a message.
  - Expected: The message appears in the conversation without a manual page refresh.

- [ ] IX-02: Selecting a theme updates the UI immediately
  - Action: Select a theme from the list.
  - Expected: The interface appearance changes instantly on selection.

- [ ] IX-03: Selecting a font style updates text immediately
  - Action: Select a font style from the list.
  - Expected: Chat text appearance changes instantly on selection.

- [ ] IX-04: Choosing an emoji inserts it into the input
  - Action: Open the emoji picker and choose an emoji.
  - Expected: The emoji is inserted into the message input field.

## Content
- [ ] CT-01: Profile displays the user's display name and bio
  - Action: Open the user's profile page.
  - Expected: The saved display name and short bio are displayed correctly.

- [ ] CT-02: Search results contain only matching messages
  - Action: Search a keyword and review the returned messages.
  - Expected: Every returned message contains the keyword; no irrelevant messages appear.