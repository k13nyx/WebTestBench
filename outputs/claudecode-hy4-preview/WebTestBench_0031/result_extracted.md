# Test Result

## Functionality

- [X] FT-01: New user can register an account
  - Action: Open the registration page, enter a new username, email, and password, then click "Register" / "Sign Up".
  - Expected: Account is created; user is taken to the logged-in chat area (rooms list or a room) without an error message.

- [X] FT-02: Registered user can log in
  - Action: Log out (if logged in), then on the login page enter the registered username and correct password and click "Log In".
  - Expected: User is authenticated and lands on the chat area; the login form is no longer shown.

- [X] FT-03: User can open a default chat room and see its existing message history
  - Action: From the chat area, click a default chat room in the room list.
  - Expected: The room opens and displays its existing messages (at least one pre-existing message), each with sender name, time, and text.

- [X] FT-04: User can send a text message in a chat room
  - Action: Type "Hello everyone" into the message input and click "Send" (or press Enter).
  - Expected: The message appears at the bottom of the open conversation attributed to the current user, and the input is cleared.

- [X] FT-05: User can send a message containing emoji
  - Action: Type "Good morning 😀🎉" into the message input and send it.
  - Expected: The posted message appears in the conversation with the emoji visible as part of the message text.

- [X] FT-06: User can participate in more than one chat room
  - Action: Join/open a second default room, post "Message in room two", then switch back to the first room.
  - Expected: Both rooms are available to the user; the second room shows the posted message, and the first room's history does not contain it.

- [X] FT-07: User can set a profile display name and short bio
  - Action: Open Profile/Settings, enter a display name and a short bio, and save.
  - Expected: Saved successfully; the new display name appears on the user's own messages and in the profile view, and the bio is displayed on the profile view.

- [X] FT-08: User can choose from several themes
  - Action: Open theme settings, select a theme different from the default, and reload the page.
  - Expected: At least 3 theme options are offered; the selected theme is applied to the chat UI immediately and still applied after reload.

- [ ] FT-09: User can choose from several font styles
  - Action: Open font settings, select a font style different from the default, and reload the page.
  - Expected: At least 3 font options are offered; message text renders in the chosen font immediately and still uses it after reload.
  - Bug Report:
    - Issue: Font style selection has no visible effect on message text (CSS not applied to content)
    - Actual: 4 font options are offered (Clean, Modern, Friendly, Monospace) and clicking them updates the root element class (e.g. `html class="theme-emerald font-style-mono"`, `font-style-modern`, `font-style-rounded`), and the class persists after reload — but the computed `font-family` of the message paragraphs (`.text-foreground/90`) stays `Inter, system-ui, sans-serif` in every font mode. The rule `.font-style-mono { font-family: var(--font-mono); }` is applied only to `<html>`, while `<body>` carries its own explicit `Inter` font-family that overrides inheritance, so message text never renders in the selected font.

- [X] FT-10: Chat history is searchable by keyword
  - Action: In the search field, type a keyword that exists in the room's history (e.g., a word from a default message) and submit the search.
  - Expected: A result list of matching messages from the chat history is shown, and each result shows the matching message text.

## Constraint

- [X] CS-01: Registration rejects invalid or duplicate credentials
  - Action: Attempt to register with an empty username, then attempt again using a username that already exists.
  - Expected: Both attempts are rejected with a visible validation message; no account is created and the user is not logged in.

- [X] CS-02: Login rejects incorrect credentials
  - Action: On the login page, enter an existing username with a wrong password and click "Log In".
  - Expected: Login fails with an error message; the chat area and messages are not accessible.

- [X] CS-03: Empty or whitespace-only message cannot be sent
  - Action: With the message input empty, click "Send"; then enter only spaces and send again.
  - Expected: No empty message is added to the conversation in either attempt (send is blocked or ignored).

- [ ] CS-04: Bio is limited to a short length
  - Action: In the profile form, enter a bio longer than the allowed short limit (e.g., 300+ characters) and save.
  - Expected: The over-long bio is rejected or truncated to the allowed limit; no error-free save of an unlimited bio occurs.
  - Bug Report:
    - Issue: Missing bio length validation — over-long bio is saved in full
    - Actual: Entering a 350-character bio ("AAA…") into the profile Bio textarea and clicking "Save" succeeded with no error, no warning and no truncation: the Settings/profile view then displayed the full 350-character string. The textarea has no `maxlength` attribute (`maxLength = -1`) and no JS-side check/truncation, so an unlimited bio can be saved error-free.

- [ ] CS-05: Search with no matches shows a no-results state
  - Action: Search for a nonsense keyword (e.g., "zzzqqq123") that appears nowhere in the history.
  - Expected: A clear "no results" / "no matching messages" state is shown; the app does not crash or display unrelated messages.
  - Bug Report:
    - Issue: Missing "no results" state for empty search results
    - Actual: After submitting "zzzqqq123" in the "Search messages..." field, the results bar (which normally shows "1 of 2 results" with prev/next navigation) disappeared entirely. No "No results", "No matching messages" or equivalent message is rendered anywhere in the DOM — the page just returns to the plain conversation view, leaving the user with no feedback that the search returned nothing.

## Interaction

- [ ] IX-01: Another user's message appears in the open conversation without a manual refresh
  - Action: With a room open, have a second user (or a second logged-in browser session) post a message to that same room; do not reload the page.
  - Expected: The new message from the other user appears in the conversation automatically, showing their display name.
  - Bug Report:
    - Issue: No real-time/cross-session message propagation
    - Actual: With General open as `qa_tester_jordan`, a second logged-in session (`sarah_designs`, verified logged in) posted "Sarah second-session live check ✅" to General. After 3.5 seconds the message was present in the second session's DOM but was absent from the first session's conversation; it only appeared after a manual reload. No `storage` events fired and no backend sync exists (e.g. `GET /api/rooms` returns the Vite index.html), so incoming messages are never pushed to an open conversation.

- [X] IX-02: Emoji picker inserts the selected emoji into the message input
  - Action: Click the emoji button/icon next to the message input, then click an emoji in the picker.
  - Expected: The picker opens with a set of emoji, and the chosen emoji is inserted into the message input at the cursor (picker closes or stays usable).

- [X] IX-03: Clicking a search result jumps to that message in the conversation
  - Action: Search for a keyword that occurs in an older message, then click that result.
  - Expected: The conversation scrolls to that message, the message is visible in context with surrounding messages, and it is visually highlighted / marked as the match.

## Content

- [X] CT-01: Chat content is complete, relevant, and free of placeholder text
  - Action: Inspect the room list, the open conversation, and the profile view.
  - Expected: Room names and default messages are meaningful and relevant to a chat application; no "lorem ipsum", "TODO", or generic placeholder text is displayed anywhere in the UI.

- [X] CT-02: Emoji render correctly and the picker is populated with recognizable emoji
  - Action: Open the emoji picker and send several different emoji (e.g., 😀 ❤️ 👍).
  - Expected: The picker shows multiple recognizable emoji (not blank or empty entries), and the sent emoji display as emoji characters in the conversation — not as empty boxes, raw text codes, or missing images.
