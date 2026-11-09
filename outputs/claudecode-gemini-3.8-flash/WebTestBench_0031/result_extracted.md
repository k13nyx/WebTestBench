# Test Result

## Functionality
- [X] FT-01: User registration with valid details
  - Action: Fill in valid registration details (username, email, password) and click the "Register" button.
  - Expected: Account is created successfully and user is navigated to the chat dashboard or login page.
- [X] FT-02: User login with valid credentials
  - Action: Enter valid registered credentials in the login form and click "Log In".
  - Expected: User is authenticated and redirected to the chat room interface.
- [X] FT-03: Switch between chat rooms
  - Action: Click on a different chat room from the rooms sidebar/list.
  - Expected: Active chat room switches and loads the message history specific to the selected room.
- [X] FT-04: Send a message containing emojis
  - Action: Type a text message, select an emoji from the emoji picker, and click "Send".
  - Expected: Message containing both text and the selected emoji renders in the active chat feed.
- [ ] FT-05: Real-time incoming message display
  - Action: Receive a message sent by another user in the current chat room.
  - Expected: The new message appears at the bottom of the conversation without requiring a page refresh.
  - Bug Report:
    - Issue: Missing Real-Time Cross-Client Message Synchronization
    - Actual: New messages sent in the active chat room from another browser session or tab do not appear in the conversation feed without a manual page refresh, as `ChatProvider` only loads messages on mount and lacks a storage or real-time event listener.
- [X] FT-06: Update profile display name and bio
  - Action: Edit the display name and short bio fields in profile settings and click "Save".
  - Expected: Updated display name and bio are saved and reflected in the profile view.
- [X] FT-07: Switch application theme
  - Action: Select an alternative theme (e.g., Dark Theme) from the theme selection settings.
  - Expected: The application interface immediately updates its color scheme to match the chosen theme.
- [ ] FT-08: Change typography font style
  - Action: Select a different font style from the font settings dropdown.
  - Expected: The chat message text updates to render in the selected font family/style.
  - Bug Report:
    - Issue: Body Font Override Blocks Typography Style Changes
    - Actual: Selecting "Modern", "Friendly", or "Monospace" applies the corresponding class (e.g. `.font-style-mono`) to `<html>`, but `body` has a hardcoded CSS rule `body { font-family: var(--font-sans); }` which overrides the root font family; consequently, chat message text remains rendered in "Inter, system-ui, sans-serif".
- [X] FT-09: Search chat history by keyword
  - Action: Enter an existing keyword into the chat search bar and press Enter.
  - Expected: A list of search results matching the keyword within the chat history is displayed.
- [X] FT-10: Jump to matching message from search
  - Action: Click on a specific search result item from the search results list.
  - Expected: The chat viewport scrolls directly to the position of that message within the conversation timeline.

## Constraint
- [X] CS-01: Prevent sending empty messages
  - Action: Clear the message input field and click the "Send" button or press Enter.
  - Expected: The message is not sent and no empty message bubble appears in the chat.
- [X] CS-02: Prevent registration with existing username
  - Action: Attempt to register with a username that is already taken.
  - Expected: Registration is rejected and an error message indicates the username is unavailable.
- [X] CS-03: Enforce required fields on login
  - Action: Leave the username/email and password fields blank and click "Log In".
  - Expected: Form submission is blocked with inline validation error indicators on the required fields.
- [ ] CS-04: Non-matching search query state
  - Action: Enter a non-existent keyword into the chat search bar and execute search.
  - Expected: Search view displays a "No messages found" state without breaking chat history display.
  - Bug Report:
    - Issue: Missing "No messages found" Search Empty State
    - Actual: Executing a search for a non-existent keyword (e.g. "nonexistentxyz12345") displays no empty state or "No messages found" notification; the search results bar simply does not render when no matches exist.

## Interaction
- [X] IX-01: Toggle emoji picker popover
  - Action: Click the emoji icon button beside the message input field.
  - Expected: Emoji picker popover opens; clicking outside or clicking the icon again closes it.
- [X] IX-02: Visual highlight on jumped message
  - Action: Click a search result to jump to a message in the conversation.
  - Expected: The target message briefly flashes or shows a distinct highlight color to draw attention.
- [X] IX-03: Active room selection indicator
  - Action: Click on an unselected chat room in the sidebar.
  - Expected: The selected room item displays an active visual state (e.g., highlighted background or border).

## Content
- [X] CT-01: Profile details display completeness
  - Action: Open user profile card/modal.
  - Expected: Displays the user's avatar, display name, and short bio text accurately.
- [X] CT-02: Customization options listing
  - Action: Navigate to the appearance/settings section.
  - Expected: Displays multiple distinct theme choices and several selectable font style options with descriptive labels.
