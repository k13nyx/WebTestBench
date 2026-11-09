# Test Checklist

## Functionality
- [ ] FT-01: Booth listing page shows all available booths
  - Action: Navigate to the main booth browse/listing page.
  - Expected: A list/grid of booths is displayed, each showing at least the company name and logo.
- [ ] FT-02: Attendee can open a booth's detail page
  - Action: Click on a booth from the listing page.
  - Expected: The booth's dedicated page opens showing its logo, company description, product/service list, and images/videos.
- [ ] FT-03: Booth detail page displays all content sections
  - Action: Open any booth page and inspect its content.
  - Expected: The page contains a visible logo, a short company description, a list of products or services, and at least one image or video.
- [ ] FT-04: Company can create a new booth
  - Action: As a company user, use the booth setup/creation form and fill in company name, description, and other required fields, then submit.
  - Expected: A new booth is created and appears in the booth listing.
- [ ] FT-05: Company can edit booth content (logo, description, products, media)
  - Action: As a company user, open the booth editor, upload/change the logo, edit the description, add or remove a product/service, add or remove an image/video, then save.
  - Expected: The booth page reflects all updated content after saving.
- [ ] FT-06: Attendee can send a text message to a booth
  - Action: On a booth page, type a question in the message input and click the send button.
  - Expected: The message is submitted and appears in the conversation/message view for that booth.
- [ ] FT-07: Booth messaging preserves per-booth conversations
  - Action: Send a message to Booth A, then open Booth B and return to Booth A.
  - Expected: Booth A shows only messages sent to Booth A; Booth B does not display Booth A's messages.

## Constraint
- [ ] CS-01: Booth cannot be saved with empty required fields
  - Action: Attempt to create or save a booth with the company name (or other required fields) left empty.
  - Expected: Submission is blocked and an error message identifies the required field; no empty booth is created.
- [ ] CS-02: Empty message cannot be sent
  - Action: With the message input empty (or whitespace only), click the send button.
  - Expected: The message is not sent, no empty message appears in the conversation, and an error/validation hint is shown.
- [ ] CS-03: Only the owning company can edit its booth
  - Action: As a company user, attempt to access the edit page/form for a booth belonging to another company.
  - Expected: Editing is prevented (access denied or edit controls not available), and the other booth's content is unchanged.

## Interaction
- [ ] IX-01: Send action provides immediate feedback
  - Action: Send a valid message to a booth.
  - Expected: The sent message appears in the conversation immediately, and the message input is cleared after sending.
- [ ] IX-02: Booth cards are clickable and give visual hover feedback
  - Action: Hover over a booth card in the listing, then click it.
  - Expected: The card shows a visible hover state (e.g., highlight or pointer cursor), and clicking navigates to that booth's detail page.
- [ ] IX-03: Saving booth edits shows a success confirmation
  - Action: Edit a booth's description and save.
  - Expected: A visible success indication (e.g., toast/confirmation message) appears confirming the booth was saved.

## Content
- [ ] CT-01: Booth listing content matches the trade show theme
  - Action: Review the booth listing page.
  - Expected: All displayed names, logos, and descriptions are company/booth-related; no irrelevant or placeholder (e.g., "Lorem ipsum") content is shown.
- [ ] CT-02: Booth logo and media render correctly
  - Action: Open a booth page and view its logo and images/videos.
  - Expected: The logo displays clearly (not broken), and all images/videos load and correspond to the company's products or services.
- [ ] CT-03: Product/service list content is accurate and readable
  - Action: Read the product/service list on a booth page.
  - Expected: Each entry has a name and description relevant to the exhibiting company, with no empty or truncated items.