# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: On the registration page, enter a unique username, display name, and password, then click the register/sign-up button.
  - Expected: Account is created and the user reaches the chat home page with their display name shown in the header.
- [ ] FT-02: Registered user can log in
  - Action: Log out, then enter the registered username and password on the login page and click Log in.
  - Expected: User lands on the chat room list, and the account's display name is shown.
- [ ] FT-03: User can open a chat room and switch between rooms
  - Action: Click a default room in the room list, note its messages, then click a different room.
  - Expected: The first room's history loads, then the second room's history replaces it. Only the selected room's messages are shown.
- [ ] FT-04: User can send a text message with emoji in a room
  - Action: In an open room, type "Hello test 😀🎉" in the message box and click Send.
  - Expected: The message appears at the bottom of the room with the user's display name, a timestamp, and the emoji rendered correctly.
- [ ] FT-05: Messages from other users appear live without refreshing
  - Action: Open the same room in a second session logged in as a different existing user. Send a message from the second session.
  - Expected: The message appears in the first session's room with the sender's display name, without a page reload.
- [ ] FT-06: User can edit display name and short bio in profile
  - Action: Open the profile page, change the display name to "QA Tester" and the bio to "Testing chat", then click Save.
  - Expected: Saved values are shown on the profile page after reload, and new messages from this user show "QA Tester" as the sender.
- [ ] FT-07: Keyword search returns matching messages in a room
  - Action: In an open room with default history, type a word known to appear in a message (e.g., a word from a default message) into the search box and press Enter or click Search.
  - Expected: A results list appears showing only messages containing that keyword, with a result count matching the number of results.
- [ ] FT-08: Clicking a search result jumps to that message in the conversation
  - Action: Run a search as in FT-07, then click one of the results.
  - Expected: The conversation scrolls to and displays the selected message within the room's history.
- [ ] FT-09: User can select a theme
  - Action: Open the theme settings, choose a theme different from the current one, and click Apply (or select it directly).
  - Expected: The page colors change to the chosen theme, and the theme remains after a page reload.
- [ ] FT-10: User can select a font style
  - Action: Open the font settings, choose a font style different from the current one.
  - Expected: Message and interface text change to the chosen font, and the font remains after a page reload.

## Constraint
- [ ] CS-01: Registration rejects a duplicate username
  - Action: On the registration page, enter the username of an existing default account and submit.
  - Expected: Registration is blocked with an error stating the username is already taken, and no new account is created.
- [ ] CS-02: Login rejects an incorrect password
  - Action: On the login page, enter a valid existing username with a wrong password and click Log in.
  - Expected: Login fails with an error message, and the user stays on the login page.
- [ ] CS-03: Unauthenticated user cannot access chat rooms
  - Action: Log out, then enter a chat room URL directly in the browser address bar.
  - Expected: User is redirected to the login page, and no room messages are displayed.
- [ ] CS-04: Empty or whitespace-only message cannot be sent
  - Action: In an open room, leave the message box empty, then click Send. Repeat with only spaces typed.
  - Expected: Nothing is posted to the conversation, and the message box remains as it was.
- [ ] CS-05: Profile display name cannot be blank
  - Action: On the profile page, clear the display name field completely and click Save.
  - Expected: Save is blocked with a validation message on the display name field, and the previous display name remains.

## Interaction
- [ ] IX-01: Pressing Enter sends the message and clears the input
  - Action: In an open room, type "Enter test" in the message box and press the Enter key.
  - Expected: The message is posted to the conversation, the message box is cleared, and the cursor remains in the message box.
- [ ] IX-02: Jumped-to message is visually highlighted
  - Action: Run a search (FT-07) and click a result (FT-08).
  - Expected: The target message is visibly highlighted (e.g., different background color) distinct from other messages.
- [ ] IX-03: Saving the profile shows a confirmation toast
  - Action: On the profile page, change the bio to "Updated bio" and click Save.
  - Expected: A confirmation message (e.g., "Profile saved") appears briefly on screen.

## Content
- [ ] CT-01: Sender names on existing messages are correct
  - Action: Open a default room and review the sender name shown on each message.
  - Expected: Every message shows a valid display name for its sender. No blank, "undefined", "null", or placeholder names appear.
- [ ] CT-02: Search results show matching text, sender, and timestamp that match the original message
  - Action: Run a keyword search (FT-07) and compare each result with the message in the conversation after clicking it (FT-08).
  - Expected: Each result's text, sender name, and timestamp are identical to the original message, and the keyword appears in the result text.