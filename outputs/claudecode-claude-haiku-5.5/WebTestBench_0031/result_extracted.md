# Test Result

## Functionality

- [X] FT-01: New user can register an account
  - Action: On the registration page, enter a unique username, display name, and password, then click the register/sign-up button.
  - Expected: Account is created and the user reaches the chat home page with their display name shown in the header.
- [X] FT-02: Registered user can log in
  - Action: Log out, then enter the registered username and password on the login page and click Log in.
  - Expected: User lands on the chat room list, and the account's display name is shown.
- [X] FT-03: User can open a chat room and switch between rooms
  - Action: Click a default room in the room list, note its messages, then click a different room.
  - Expected: The first room's history loads, then the second room's history replaces it. Only the selected room's messages are shown.
- [X] FT-04: User can send a text message with emoji in a room
  - Action: In an open room, type "Hello test 😀🎉" in the message box and click Send.
  - Expected: The message appears at the bottom of the room with the user's display name, a timestamp, and the emoji rendered correctly.
- [ ] FT-05: Messages from other users appear live without refreshing
  - Action: Open the same room in a second session logged in as a different existing user. Send a message from the second session.
  - Expected: The message appears in the first session's room with the sender's display name, without a page reload.
  - Bug Report:
    - Issue: Live Update Missing
    - Actual: Second session (alex_dev, Development room) sent "Live check from Alex" successfully, but it never appeared in the first session's Development message list. It was not seen after 8 seconds of polling and again after 3 more seconds, and no page reload was done.
- [X] FT-06: User can edit display name and short bio in profile
  - Action: Open the profile page, change the display name to "QA Tester" and the bio to "Testing chat", then click Save.
  - Expected: Saved values are shown on the profile page after reload, and new messages from this user show "QA Tester" as the sender.
- [ ] FT-07: Keyword search returns matching messages in a room
  - Action: In an open room with default history, type a word known to appear in a message (e.g., a word from a default message) into the search box and press Enter or click Search.
  - Expected: A results list appears showing only messages containing that keyword, with a result count matching the number of results.
  - Bug Report:
    - Issue: Missing Results List
    - Actual: Searching "React" in Development showed the counter "1 of 1 results" with prev/next arrows. No results list was rendered, and the message list stayed unfiltered, showing all messages in the room.
- [ ] FT-08: Clicking a search result jumps to that message in the conversation
  - Action: Run a search as in FT-07, then click one of the results.
  - Expected: The conversation scrolls to and displays the selected message within the room's history.
  - Bug Report:
    - Issue: Unresponsive Search Navigation
    - Actual: No clickable result items exist after the search. The only navigation controls are the prev/next arrows, which are disabled at "1 of 1 results". There is no result to click, so no jump action occurs.
- [X] FT-09: User can select a theme
  - Action: Open the theme settings, choose a theme different from the current one, and click Apply (or select it directly).
  - Expected: The page colors change to the chosen theme, and the theme remains after a page reload.
- [ ] FT-10: User can select a font style
  - Action: Open the font settings, choose a font style different from the current one.
  - Expected: Message and interface text change to the chosen font, and the font remains after a page reload.
  - Bug Report:
    - Issue: Font Style Not Applied
    - Actual: Selecting "Monospace" set the html class to `font-style-mono` and saved it to preferences. The computed font-family of the html element became JetBrains Mono, but message text ("Hello test") and headings still computed to "Inter, system-ui, sans-serif", the same as before the change.

## Constraint

- [X] CS-01: Registration rejects a duplicate username
  - Action: On the registration page, enter the username of an existing default account and submit.
  - Expected: Registration is blocked with an error stating the username is already taken, and no new account is created.
- [X] CS-02: Login rejects an incorrect password
  - Action: On the login page, enter a valid existing username with a wrong password and click Log in.
  - Expected: Login fails with an error message, and the user stays on the login page.
- [ ] CS-03: Unauthenticated user cannot access chat rooms
  - Action: Log out, then enter a chat room URL directly in the browser address bar.
  - Expected: User is redirected to the login page, and no room messages are displayed.
  - Bug Report:
    - Issue: Missing Auth Redirect
    - Actual: Logged out, `/room/room-general` and `/rooms/room-general` both showed a "404 - Oops! Page not found" page with a "Return to Home" link, not the login page. The app has no addressable room URL, so the real room route could not be tested.
- [X] CS-04: Empty or whitespace-only message cannot be sent
  - Action: In an open room, leave the message box empty, then click Send. Repeat with only spaces typed.
  - Expected: Nothing is posted to the conversation, and the message box remains as it was.
- [ ] CS-05: Profile display name cannot be blank
  - Action: On the profile page, clear the display name field completely and click Save.
  - Expected: Save is blocked with a validation message on the display name field, and the previous display name remains.
  - Bug Report:
    - Issue: Validation Bypass
    - Actual: Clearing the display name and clicking Save persisted an empty name. No validation message appeared (no `:invalid` state, no alert). The sidebar then showed only "@qa_user_0928" with no name. The name was restored to "QA Tester" afterward.

## Interaction

- [X] IX-01: Pressing Enter sends the message and clears the input
  - Action: In an open room, type "Enter test" in the message box and press the Enter key.
  - Expected: The message is posted to the conversation, the message box is cleared, and the cursor remains in the message box.
- [ ] IX-02: Jumped-to message is visually highlighted
  - Action: Run a search (FT-07) and click a result (FT-08).
  - Expected: The target message is visibly highlighted (e.g., different background color) distinct from other messages.
  - Bug Report:
    - Issue: Highlight Not Visible
    - Actual: The matched message row ("Anyone have experience with the new React 19 features?") has class `message-highlight`, but its computed background is `rgba(0, 0, 0, 0)`, the same as other rows. Its computed animation is `fade-in`, which overrides the `highlight-pulse` animation defined for `.message-highlight`, so no highlight appears. No result was clicked (see FT-08).
- [X] IX-03: Saving the profile shows a confirmation toast
  - Action: On the profile page, change the bio to "Updated bio" and click Save.
  - Expected: A confirmation message (e.g., "Profile saved") appears briefly on screen.

## Content

- [X] CT-01: Sender names on existing messages are correct
  - Action: Open a default room and review the sender name shown on each message.
  - Expected: Every message shows a valid display name for its sender. No blank, "undefined", "null", or placeholder names appear.
- [ ] CT-02: Search results show matching text, sender, and timestamp that match the original message
  - Action: Run a keyword search (FT-07) and compare each result with the message in the conversation after clicking it (FT-08).
  - Expected: Each result's text, sender name, and timestamp are identical to the original message, and the keyword appears in the result text.
  - Bug Report:
    - Issue: Missing Results List
    - Actual: No result list is rendered, so there are no result entries to compare. The single match is the original message in Development (Alex Chen, "Dec 13, 10:00 AM"), but no result-level text, sender, or timestamp was shown for comparison.
