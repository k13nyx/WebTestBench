# Test Checklist

## Functionality
- [ ] FT-01: Company can create a new booth with name and description
  - Action: Open the booth setup/create page, enter company name "Acme Robotics" and a short description, click Save/Create.
  - Expected: Booth is created and its booth page displays the entered company name and description.

- [ ] FT-02: Company can add a logo to its booth
  - Action: On the booth setup page, upload an image file in the Logo field and save.
  - Expected: The uploaded image is displayed as the booth logo on the booth page.

- [ ] FT-03: Company can add an item to the products/services list
  - Action: On a default booth's setup page, add a product/service entry "Industrial Arm X1" and save.
  - Expected: "Industrial Arm X1" appears as a list item in the booth's Products/Services section.

- [ ] FT-04: Company can add an image to the booth media section
  - Action: In the booth's media/images section, upload or add an image and save.
  - Expected: The image appears in the booth's media gallery and renders visibly on the booth page.

- [ ] FT-05: Company can add a video to the booth media section
  - Action: In the booth's media section, add a video (file upload or video link) and save.
  - Expected: The video appears in the booth's media gallery with a visible player; pressing play starts playback.

- [ ] FT-06: Booth edits persist after reloading the page
  - Action: Edit the short description of a default booth, save, then reload the booth page.
  - Expected: The updated description is shown and the previous text is no longer displayed.

- [ ] FT-07: Attendee can browse all booths
  - Action: Open the booth directory / browse page as an attendee.
  - Expected: All existing booths are listed (grid or list), each showing at least a company name and logo, and the count matches the number of booths in the app.

- [ ] FT-08: Attendee can click into a booth to read more
  - Action: From the browse page, click any booth card/name.
  - Expected: The page navigates to that booth's detail page showing its logo, description, products/services list, and media section.

- [ ] FT-09: Attendee can send a text message to a booth
  - Action: On a booth detail page, type "Do you ship to Europe?" in the message box and click Send.
  - Expected: The message is accepted and a success confirmation is shown.

- [ ] FT-10: Sent message is delivered to the booth's messages
  - Action: Open the booth owner's messages/inbox view for the booth used in FT-09.
  - Expected: The message "Do you ship to Europe?" is listed as received for that booth.

## Constraint
- [ ] CS-01: Booth cannot be created without a company name
  - Action: On the booth setup page, leave the company name field empty and submit.
  - Expected: Submission is blocked, a validation message about the missing company name is shown, and no new booth appears in the browse list.

- [ ] CS-02: Empty or whitespace-only message cannot be sent
  - Action: On a booth detail page, leave the message box empty (or enter only spaces) and click Send.
  - Expected: The message is not sent — either Send is disabled or an error message is shown; no new entry appears in the booth's messages.

- [ ] CS-03: Duplicate booth name is prevented
  - Action: Create a new booth using the exact company name of an existing default booth and submit.
  - Expected: Creation is rejected with a message stating the booth/company name already exists, and no duplicate booth is added to the browse list.

- [ ] CS-04: Unsupported file types are rejected for logo/media
  - Action: On the booth setup page, attempt to upload a non-image file (e.g., a .pdf or .txt file) as the logo or media image.
  - Expected: The upload is rejected with an error message and the invalid file is not added to the booth.

## Interaction
- [ ] IX-01: Confirmation feedback appears after saving booth changes
  - Action: Change any booth field and click Save.
  - Expected: A success message/toast confirming the booth was saved is displayed.

- [ ] IX-02: Message box clears and confirmation appears after sending
  - Action: Type a valid message and click Send.
  - Expected: A success confirmation is shown and the message input field is cleared.

- [ ] IX-03: Newly created booth appears in the browse list
  - Action: Create a new booth, then open the browse page without manually re-entering data.
  - Expected: The newly created booth is visible in the booth list among the existing booths.

## Content
- [ ] CT-01: Browse page shows complete, relevant booth information
  - Action: Open the browse page and inspect each booth card.
  - Expected: Every booth card shows its real company name, a rendered logo image (no broken-image icon), and its short description — with no unrelated or placeholder text.

- [ ] CT-02: Booth detail page content matches the selected booth
  - Action: Open a specific default booth from the browse page and compare its content to the booth card clicked.
  - Expected: The detail page shows the same company name and logo as the card, plus that booth's own description, products/services list, and media — not another booth's data.

- [ ] CT-03: All booth media renders correctly
  - Action: Open several default booths and view their logos and media galleries.
  - Expected: Every image loads and displays (no broken-image icons), every video shows a working player, and all media is relevant to that company/booth.