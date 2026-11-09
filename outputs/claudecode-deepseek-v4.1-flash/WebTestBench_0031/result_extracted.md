# Test Result

## Functionality

- [X] FT-01: New user can register an account
  - Action: Open the registration page, enter a unique username, email, and password, then click "Register".
  - Expected: Account is created and the user is logged in (or redirected to log in), with no error message.
  - Note: Account was created and the user was logged in directly ("Account created successfully!"). The form has **no email field** (only Username/Display Name/Password/Confirm Password), so the email part of the action was not applicable.

- [X] FT-02: Registered user can log in
  - Action: Enter valid credentials on the login page and click "Log in".
  - Expected: User is authenticated and taken to the chat interface showing their display name.

- [X] FT-03: User can join and switch between multiple chat rooms
  - Action: Select room A from the room list, then select room B.
  - Expected: The conversation area switches to the selected room's messages each time, and both rooms remain accessible.

- [X] FT-04: User can send a message to a room
  - Action: Type "hello world" in the message input and press Enter / click "Send".
  - Expected: The message appears in the conversation attributed to the current user, and the input field clears.

- [X] FT-05: User can send a message containing an emoji
  - Action: Open the emoji picker, select an emoji (e.g., 😀), and send the message.
  - Expected: The message is posted and the emoji renders correctly in the conversation.

- [X] FT-06: User sees other users' messages as the conversation continues
  - Action: With two accounts in the same room, send a message from account B.
  - Expected: The message appears in account A's conversation thread under account B's name.
  - Note: Verified — after account B (Alex Chen) sent a message, account A's General thread contained "Hello from Alex (account B)!" attributed to "Alex Chen". However it only appeared after A's session was refreshed (no live sync — see IX-01).

- [X] FT-07: User can edit profile display name and short bio
  - Action: Open profile settings, change display name and bio, and save.
  - Expected: Saved values are shown on the profile and used for the user's messages.

- [X] FT-08: User can choose from several themes
  - Action: Open appearance settings and select a different theme from the available options.
  - Expected: The interface updates to the selected theme immediately.
  - Note: Selecting a swatch applied `.theme-emerald` on `<html>` and changed `--primary` immediately.

- [ ] FT-09: User can choose from several font styles
  - Action: Open appearance settings and select a different font style.
  - Expected: Displayed text updates to the selected font style immediately.
  - Bug Report:
    - Issue: Font style selection has no visible effect on app content (broken styling / non-functional control).
    - Actual: Selecting "Monospace" applied class `font-style-mono` to `<html>` (`--font-sans` unchanged), but `body { font-family: var(--font-sans) }` overrides inheritance, so all displayed content stays `Inter, system-ui, sans-serif`. Measured: `<h1>` and message `<p>` both remained `"Inter, system-ui, sans-serif"` while only the option button itself rendered its own font. The chat text never changes font.

- [ ] FT-10: User can search chat history by keyword
  - Action: Enter a keyword known to exist in the history into the search field and submit.
  - Expected: The list of matching messages is returned with sender and message context.
  - Bug Report:
    - Issue: Missing results list (feature implemented as in-conversation counter/navigation instead).
    - Actual: Submitting "the" showed only a counter "1 of 2 results" with prev/next arrow buttons. No list of matching messages (no sender/context rows, no `<li>`/results panel) is rendered; clicking the counter does nothing.

- [X] FT-11: User can jump to a matching message in the conversation
  - Action: From the search results, click/select a matching message.
  - Expected: The conversation scrolls to and highlights that exact message in its original position.
  - Note: Achieved via the search next/previous controls (move to each match and highlight it in place by changing `.message-highlight` to that message), rather than by clicking a listed result (no list exists).

## Constraint

- [X] CS-01: Registration is blocked for invalid input
  - Action: Attempt to register with an already-used username / email, and separately with required fields left empty.
  - Expected: Submission is rejected with a clear validation error and no account is created.

- [X] CS-02: Login is blocked with invalid credentials
  - Action: Enter a wrong password (or unknown username) and click "Log in".
  - Expected: Access is denied with an "invalid credentials" style message; user is not logged in.

- [X] CS-03: Empty or whitespace-only messages cannot be sent
  - Action: Leave the message input empty (or type only spaces) and press Enter / "Send".
  - Expected: No message is posted and the input remains ready for valid input.

- [X] CS-04: Theme and font selections persist
  - Action: Select a non-default theme and font, then reload the page.
  - Expected: The chat interface reloads with the previously selected theme and font still applied.

## Interaction

- [ ] IX-01: New messages appear live without page reload
  - Action: Keep a room open while a message is sent to it.
  - Expected: The message is appended to the thread automatically and the view scrolls to show it.
  - Bug Report:
    - Issue: No real-time message delivery (messages from other users do not appear without a reload).
    - Actual: With account A's room open, account B (a separate tab) sent "Hello from Alex (account B)!". The message never appeared in A's open thread (checked immediately and again after 5s — no polling; confirmed absent via DOM). The message was persisted to `localStorage` and only appeared after reloading A's page.

- [X] IX-02: Emoji picker opens and inserts on selection
  - Action: Click the emoji button in the message input.
  - Expected: An emoji picker panel opens; clicking an emoji inserts it into the input field.

- [X] IX-03: Search navigates between matches with visual feedback
  - Action: Search a keyword with multiple matches and use next/previous controls.
  - Expected: Each navigation highlights the current match and moves the conversation view to it.

## Content

- [ ] CT-01: User profiles display display name and short bio
  - Action: Open a user's profile (own and another user's).
  - Expected: The profile shows the display name and the short bio as entered, with no missing or placeholder content.
  - Bug Report:
    - Issue: No way to open another user's profile (own profile only).
    - Actual: The own profile (via Settings) correctly showed display name "QA Tester Pro" and the edited bio. However there is no UI to open another user's profile: clicking member rows, member names, message author names, and avatars (and hovering them) produced no profile; no dialogs/hover cards appeared, no anchors/`profile` elements exist, and other users' bios never render in the DOM.

- [ ] CT-02: Search highlights the matched keyword in conversation
  - Action: Jump to a search result.
  - Expected: The matched keyword is visually highlighted within the message text in the conversation.
  - Bug Report:
    - Issue: The keyword itself is not highlighted (only the whole message is).
    - Actual: The matched message gets a `.message-highlight` background, but the matched text is not wrapped/marked. Inspected the message's `<p>` innerHTML — plain text (e.g., "Hey everyone! 👋 Welcome to the new chat platform!") with no `<mark>`/highlight span around "the". No `<mark>` elements exist anywhere in the DOM.
