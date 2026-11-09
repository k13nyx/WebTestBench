# Test Result

## Functionality
- [X] FT-01: Booth listing page shows all available booths
  - Action: Navigate to the main booth browse/listing page.
  - Expected: A list/grid of booths is displayed, each showing at least the company name and logo.
- [X] FT-02: Attendee can open a booth's detail page
  - Action: Click on a booth from the listing page.
  - Expected: The booth's dedicated page opens showing its logo, company description, product/service list, and images/videos.
- [X] FT-03: Booth detail page displays all content sections
  - Action: Open any booth page and inspect its content.
  - Expected: The page contains a visible logo, a short company description, a list of products or services, and at least one image or video.
- [ ] FT-04: Company can create a new booth
  - Action: As a company user, use the booth setup/creation form and fill in company name, description, and other required fields, then submit.
  - Expected: A new booth is created and appears in the booth listing.
  - Bug Report:
    - Issue: Missing Feature (No Booth Creation Form)
    - Actual: The application contains no booth setup/creation form anywhere. The router defines only three routes ("/", "/booth/:id", "*"), there is no company/login concept, no creation link in the nav or footer, and navigating to /create-booth renders the "404 - Oops! Page not found" page. No new booth could be created.
- [ ] FT-05: Company can edit booth content (logo, description, products, media)
  - Action: As a company user, open the booth editor, upload/change the logo, edit the description, add or remove a product/service, add or remove an image/video, then save.
  - Expected: The booth page reflects all updated content after saving.
  - Bug Report:
    - Issue: Missing Feature (No Booth Editor)
    - Actual: No booth editor exists. The booth detail page exposes only read-only content plus a visitor message form (no edit controls), and navigating to /booth/techvision/edit renders the "404 - Oops! Page not found" page. Source inspection of Index.tsx and BoothDetail.tsx shows no create/edit/save logic, so no editing or saving could be performed.
- [ ] FT-06: Attendee can send a text message to a booth
  - Action: On a booth page, type a question in the message input and click the send button.
  - Expected: The message is submitted and appears in the conversation/message view for that booth.
  - Bug Report:
    - Issue: Missing Element (No Conversation/Message View)
    - Actual: Submitting shows a "Message sent! Your message has been sent to TechVision AI." toast and replaces the form with a "Message Sent!" panel, but the typed message never appears in any conversation/message view — the sent text is absent from the DOM (body text does not contain it), and no message list/history component exists on the page.
- [ ] FT-07: Booth messaging preserves per-booth conversations
  - Action: Send a message to Booth A, then open Booth B and return to Booth A.
  - Expected: Booth A shows only messages sent to Booth A; Booth B does not display Booth A's messages.
  - Bug Report:
    - Issue: Missing Feature (No Persisted Per-Booth Conversations)
    - Actual: After sending messages to both TechVision AI (Booth A) and GreenLeaf Sustainability (Booth B), neither booth displays any conversation. Returning to Booth A shows an empty message form with none of its previously sent messages, and localStorage contains no stored messages. Booth B shows nothing (isolation passes only because no messages are ever displayed anywhere).

## Constraint
- [ ] CS-01: Booth cannot be saved with empty required fields
  - Action: Attempt to create or save a booth with the company name (or other required fields) left empty.
  - Expected: Submission is blocked and an error message identifies the required field; no empty booth is created.
  - Bug Report:
    - Issue: Missing Feature (No Booth Form to Validate)
    - Actual: There is no booth creation or save form in the application (only routes "/", "/booth/:id", and "*" exist; /create-booth returns the 404 page), so an empty-field submission cannot even be attempted and no required-field validation exists to observe. No booth form submission of any kind is possible.
- [X] CS-02: Empty message cannot be sent
  - Action: With the message input empty (or whitespace only), click the send button.
  - Expected: The message is not sent, no empty message appears in the conversation, and an error/validation hint is shown.
- [ ] CS-03: Only the owning company can edit its booth
  - Action: As a company user, attempt to access the edit page/form for a booth belonging to another company.
  - Expected: Editing is prevented (access denied or edit controls not available), and the other booth's content is unchanged.
  - Bug Report:
    - Issue: Missing Feature (No Edit Page or Company Ownership Concept)
    - Actual: The requested ownership-based access control cannot be exercised: there is no edit route (/booth/techvision/edit renders the 404 page), no edit controls on the booth detail page, and no company user/authentication concept exists in the app (empty localStorage, no login routes). Editing cannot be attempted at all, so no access-denied behavior can be verified (booth content is unchanged only because nothing can modify it).

## Interaction
- [ ] IX-01: Send action provides immediate feedback
  - Action: Send a valid message to a booth.
  - Expected: The sent message appears in the conversation immediately, and the message input is cleared after sending.
  - Bug Report:
    - Issue: Missing Element (Sent Message Not Shown in Conversation)
    - Actual: Feedback is partial: a success toast appears and the form resets (input cleared after clicking "Send another message"), but the sent message itself never appears anywhere on the page — the conversation view where it should be rendered does not exist, so the message text is not visible immediately after sending.
- [X] IX-02: Booth cards are clickable and give visual hover feedback
  - Action: Hover over a booth card in the listing, then click it.
  - Expected: The card shows a visible hover state (e.g., highlight or pointer cursor), and clicking navigates to that booth's detail page.
- [ ] IX-03: Saving booth edits shows a success confirmation
  - Action: Edit a booth's description and save.
  - Expected: A visible success indication (e.g., toast/confirmation message) appears confirming the booth was saved.
  - Bug Report:
    - Issue: Missing Feature (No Save/Edit Operation)
    - Actual: No booth editing or saving functionality exists (no edit route — /booth/techvision/edit returns 404; no edit controls on the booth page), so there is no save action that could produce a success confirmation.

## Content
- [X] CT-01: Booth listing content matches the trade show theme
  - Action: Review the booth listing page.
  - Expected: All displayed names, logos, and descriptions are company/booth-related; no irrelevant or placeholder (e.g., "Lorem ipsum") content is shown.
- [X] CT-02: Booth logo and media render correctly
  - Action: Open a booth page and view its logo and images/videos.
  - Expected: The logo displays clearly (not broken), and all images/videos load and correspond to the company's products or services.
- [X] CT-03: Product/service list content is accurate and readable
  - Action: Read the product/service list on a booth page.
  - Expected: Each entry has a name and description relevant to the exhibiting company, with no empty or truncated items.
