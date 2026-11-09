# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Open the registration page, enter a unique username, email, and password, then click "Register".
  - Expected: Account is created and the user is logged in (or redirected to log in), with no error message.

- [ ] FT-02: Registered user can log in
  - Action: Enter valid credentials on the login page and click "Log in".
  - Expected: User is authenticated and taken to the chat interface showing their display name.

- [ ] FT-03: User can join and switch between multiple chat rooms
  - Action: Select room A from the room list, then select room B.
  - Expected: The conversation area switches to the selected room's messages each time, and both rooms remain accessible.

- [ ] FT-04: User can send a message to a room
  - Action: Type "hello world" in the message input and press Enter / click "Send".
  - Expected: The message appears in the conversation attributed to the current user, and the input field clears.

- [ ] FT-05: User can send a message containing an emoji
  - Action: Open the emoji picker, select an emoji (e.g., 😀), and send the message.
  - Expected: The message is posted and the emoji renders correctly in the conversation.

- [ ] FT-06: User sees other users' messages as the conversation continues
  - Action: With two accounts in the same room, send a message from account B.
  - Expected: The message appears in account A's conversation thread under account B's name.

- [ ] FT-07: User can edit profile display name and short bio
  - Action: Open profile settings, change display name and bio, and save.
  - Expected: Saved values are shown on the profile and used for the user's messages.

- [ ] FT-08: User can choose from several themes
  - Action: Open appearance settings and select a different theme from the available options.
  - Expected: The interface updates to the selected theme immediately.

- [ ] FT-09: User can choose from several font styles
  - Action: Open appearance settings and select a different font style.
  - Expected: Displayed text updates to the selected font style immediately.

- [ ] FT-10: User can search chat history by keyword
  - Action: Enter a keyword known to exist in the history into the search field and submit.
  - Expected: The list of matching messages is returned with sender and message context.

- [ ] FT-11: User can jump to a matching message in the conversation
  - Action: From the search results, click/select a matching message.
  - Expected: The conversation scrolls to and highlights that exact message in its original position.

## Constraint
- [ ] CS-01: Registration is blocked for invalid input
  - Action: Attempt to register with an already-used username / email, and separately with required fields left empty.
  - Expected: Submission is rejected with a clear validation error and no account is created.

- [ ] CS-02: Login is blocked with invalid credentials
  - Action: Enter a wrong password (or unknown username) and click "Log in".
  - Expected: Access is denied with an "invalid credentials" style message; user is not logged in.

- [ ] CS-03: Empty or whitespace-only messages cannot be sent
  - Action: Leave the message input empty (or type only spaces) and press Enter / "Send".
  - Expected: No message is posted and the input remains ready for valid input.

- [ ] CS-04: Theme and font selections persist
  - Action: Select a non-default theme and font, then reload the page.
  - Expected: The chat interface reloads with the previously selected theme and font still applied.

## Interaction
- [ ] IX-01: New messages appear live without page reload
  - Action: Keep a room open while a message is sent to it.
  - Expected: The message is appended to the thread automatically and the view scrolls to show it.

- [ ] IX-02: Emoji picker opens and inserts on selection
  - Action: Click the emoji button in the message input.
  - Expected: An emoji picker panel opens; clicking an emoji inserts it into the input field.

- [ ] IX-03: Search navigates between matches with visual feedback
  - Action: Search a keyword with multiple matches and use next/previous controls.
  - Expected: Each navigation highlights the current match and moves the conversation view to it.

## Content
- [ ] CT-01: User profiles display display name and short bio
  - Action: Open a user's profile (own and another user's).
  - Expected: The profile shows the display name and the short bio as entered, with no missing or placeholder content.

- [ ] CT-02: Search highlights the matched keyword in conversation
  - Action: Jump to a search result.
  - Expected: The matched keyword is visually highlighted within the message text in the conversation.