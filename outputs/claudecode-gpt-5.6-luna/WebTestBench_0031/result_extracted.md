# Test Result

## Functionality

- [X] FT-01: User can register a new account with valid details.
  - Action: Open **Register/Sign Up**, enter valid required details, and submit the form.
  - Expected: The account is created successfully and the user receives access to the chat experience or a confirmation that the account is ready for login.

- [X] FT-02: User can log in with valid account credentials.
  - Action: Open **Login**, enter valid credentials for an available account, and submit.
  - Expected: The user is authenticated and the chat room interface is displayed.

- [X] FT-03: User can access more than one available chat room.
  - Action: Open one default chat room, then select a different available room from the room list or selector.
  - Expected: Both rooms open successfully and each displays its corresponding conversation.

- [X] FT-04: User can send a text message in the active chat room.
  - Action: Enter text in the message composer and select **Send**.
  - Expected: The message appears in the active conversation with the sender’s display name.

- [X] FT-05: User can send a message containing an emoji.
  - Action: Open the emoji picker, select an emoji, add it to a message, and select **Send**.
  - Expected: The sent message displays the selected emoji correctly in the conversation.

- [X] FT-06: User can save a profile display name and short bio.
  - Action: Open **Profile**, enter a display name and short bio, and select **Save**.
  - Expected: The profile is saved and the updated display name and bio are shown when the profile is reopened.

- [X] FT-07: User can apply each available visual theme.
  - Action: Open the appearance or settings controls and select each listed theme one at a time.
  - Expected: The webpage visibly applies the selected theme after each selection.

- [X] FT-08: User can apply each available font style.
  - Action: Open the appearance or settings controls and select each listed font style one at a time.
  - Expected: Chat text visibly uses the selected font style after each selection.

- [ ] FT-09: User can search chat history by keyword.
  - Action: Enter a keyword known to exist in the default chat history into the chat-history search field and submit the search.
  - Expected: Search results identify messages in the history that contain the entered keyword.
  - Bug Report:
    - Issue: Incomplete Search Results Presentation
    - Actual: Searching for “React” displayed “1 of 1 results,” but no result list or result text containing the searched keyword was displayed for inspection.

## Constraint

- [ ] CS-01: Registration prevents submission when required fields are empty or invalid.
  - Action: Leave one or more required registration fields empty or enter invalid values, then submit.
  - Expected: Registration is not completed and a validation message identifies the invalid or missing field.
  - Bug Report:
    - Issue: Missing Registration Validation Message
    - Actual: Submitting the empty registration form kept the user on the registration form and focused the Username field, but no validation message identifying the missing field was displayed.

- [X] CS-02: Login rejects invalid credentials.
  - Action: Submit the login form with an incorrect password or an unrecognized account.
  - Expected: The user remains unauthenticated and an invalid-credentials error is displayed.

- [ ] CS-03: User cannot send an empty chat message.
  - Action: Leave the message composer empty or enter only whitespace, then select **Send**.
  - Expected: No message is added to the conversation and the composer indicates that message content is required.
  - Bug Report:
    - Issue: Missing Empty-Message Validation Feedback
    - Actual: No message was added and the Send button remained disabled, but the composer did not display a validation message indicating that message content is required.

- [ ] CS-04: Search handles a keyword with no matches.
  - Action: Search chat history for a keyword that does not occur in the available messages.
  - Expected: No messages are returned and a clear no-results state is displayed.
  - Bug Report:
    - Issue: Missing No-Results State
    - Actual: Searching for “zzzz_no_match” left the existing conversation visible and did not display a clear no-results message.

## Interaction

- [ ] IX-01: Messages from another participant appear while the conversation continues.
  - Action: Open the same room in two authenticated sessions and send a message from the other session.
  - Expected: The new message appears in the first session’s conversation without requiring a manual page reload.
  - Bug Report:
    - Issue: Missing Real-Time Message Synchronization
    - Actual: A message sent from one authenticated session was not observed in the other session without additional interaction; the receiving session continued to show the previous conversation state.

- [X] IX-02: Switching rooms updates the active-room state and conversation.
  - Action: Select different available rooms from the room list.
  - Expected: The selected room is visibly marked active and its message history replaces the previously active room’s history.

- [X] IX-03: Selecting an emoji inserts it into the message composer.
  - Action: Open the emoji picker and select an emoji without sending the message.
  - Expected: The selected emoji appears in the composer at the insertion point and remains available for sending.

- [ ] IX-04: User can jump to a matching message from search results.
  - Action: Run a keyword search and select a returned matching result.
  - Expected: The conversation moves to the corresponding message and the matching message is visibly identified or highlighted.
  - Bug Report:
    - Issue: Search Result Navigation Unavailable
    - Actual: The search interface displayed a result count but did not expose a returned matching message result that could be selected to jump to or highlight the corresponding conversation entry.

## Content

- [X] CT-01: Messages identify the correct sender and preserve message content.
  - Action: Review messages in an active room, including messages containing emoji.
  - Expected: Each message shows the correct display name and readable original text; emoji are rendered as intended rather than as broken characters.

- [X] CT-02: Profile content is displayed accurately.
  - Action: Open a user profile after saving a display name and short bio.
  - Expected: The displayed name and bio exactly match the saved profile values.

- [ ] CT-03: Search results contain the searched keyword and original message context.
  - Action: Search for a keyword present in the default chat history and inspect every returned result.
  - Expected: Each result contains the searched keyword and shows enough original message content to identify the matching conversation entry.
  - Bug Report:
    - Issue: Search Results Do Not Expose Message Context
    - Actual: The search reported “1 of 1 results,” but no returned result content containing “React” or enough original message context was displayed.
