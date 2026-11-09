# Test Result

## Functionality
- [ ] FT-01: Company can set the booth logo
  - Action: As a company user, open the booth setup page for a default booth, upload an image file as the logo, and save.
  - Expected: The logo is saved and displayed on the booth page.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page)
    - Actual: The booth setup page does not exist. The app's route table only defines `/`, `/booth/:id`, and a 404 catch-all; navigating to `/setup` and `/admin` both return the 404 page ("404 — Oops! Page not found"), and no setup/edit/login entry point exists anywhere in the navigation or on booth pages, so a company user cannot upload a logo at all.

- [ ] FT-02: Company can add a short company description
  - Action: On the booth setup page, enter text into the company description field and save.
  - Expected: The entered description is saved and displayed on the booth page.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page / no editable description field)
    - Actual: No booth setup page or description editing UI exists anywhere in the app (only booth listing and read-only booth detail pages are routed); the description cannot be entered or saved by a company user.

- [ ] FT-03: Company can add products or services
  - Action: On the booth setup page, add a product/service entry to the booth's list and save.
  - Expected: The new entry appears in the products/services list on the booth page.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page / no product management)
    - Actual: There is no setup page and no UI to add product/service entries; the products/services lists on booth pages are static, read-only content that a company user cannot modify.

- [ ] FT-04: Company can add images or videos
  - Action: On the booth setup page, upload an image or video file into the booth's media section and save.
  - Expected: The uploaded media is saved and displayed on the booth page.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page / no media upload)
    - Actual: No booth setup page or media upload control exists anywhere in the application; the Gallery sections on booth pages are static and cannot be modified by a company user.

- [X] FT-05: Attendee can browse all booths
  - Action: Open the booths listing page as an attendee.
  - Expected: All default booths are listed, each identifiable by its company name (and logo where set).

- [X] FT-06: Attendee can open a booth detail page
  - Action: Click a default booth entry in the listing.
  - Expected: That booth's detail page opens showing its logo, description, products/services, and media.

- [X] FT-07: Attendee can send a text message to a booth
  - Action: On a booth page, type a question into the message field and click the send button.
  - Expected: The message is sent successfully to that booth.

- [ ] FT-08: Booth receives the attendee's message
  - Action: After an attendee sends a message, open the booth's messages view as the company user.
  - Expected: The sent message and its exact text are visible in the booth's received messages.
  - Bug Report:
    - Issue: Missing Feature (no company-side messages view)
    - Actual: After sending "Hello, I would like to know more about VisionML Platform pricing and deployment options. - QA Test 9876" to TechVision AI, there is no messages view/inbox anywhere in the app — no company login, no messages route, and no received-messages UI on booth pages — so the sent message cannot be viewed by the booth.

## Constraint
- [ ] CS-01: Booth cannot be saved with empty required fields
  - Action: On the booth setup page, clear a required field (e.g., company/booth name) and attempt to save.
  - Expected: Save is blocked with a validation message; the booth keeps its previous valid content.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page / no save operation)
    - Actual: The booth setup page does not exist (routes are only `/`, `/booth/:id`, and 404), so there is no save action and no required-field validation to test; booth content is entirely static.

- [X] CS-02: Empty message cannot be sent
  - Action: On a booth page, leave the message field empty and click the send button.
  - Expected: No message is sent; the app prompts the attendee to enter message text.

- [ ] CS-03: Invalid media file is rejected
  - Action: On the booth setup page, attempt to upload a non-image/non-video file (e.g., a `.txt` file) as logo or media.
  - Expected: The upload is rejected with an error message and the file is not added to the booth.
  - Bug Report:
    - Issue: Missing Feature (no upload capability)
    - Actual: The booth setup page and all upload controls are absent from the application, so there is no upload flow in which an invalid file could be submitted or rejected.

## Interaction
- [ ] IX-01: Saving booth changes shows confirmation
  - Action: Make a valid edit on the booth setup page and save.
  - Expected: A success confirmation (toast/banner) appears with no error state.
  - Bug Report:
    - Issue: Missing Feature (no booth setup page / no save)
    - Actual: There is no booth setup page and no save operation in the application, so no edit-save confirmation flow exists to test.

- [X] IX-02: Sending a message shows confirmation and clears the input
  - Action: Send a valid message from a booth page.
  - Expected: A success confirmation is shown and the message input is cleared.

## Content
- [X] CT-01: Booth list entries identify their companies
  - Action: Review each default booth entry on the booths listing page.
  - Expected: Every entry shows a company name (and logo where set) that matches the same booth's detail page.

- [X] CT-02: Booth detail content is relevant and intact
  - Action: Read the logo, description, and products/services list on a default booth page.
  - Expected: All text is complete (no placeholder text) and relevant to that booth's company.

- [X] CT-03: Booth images and videos display correctly
  - Action: View all images and play all videos on a default booth page.
  - Expected: Every image renders and every video plays; media is relevant to the company with no broken items.
