# Test Checklist

## Functionality
- [ ] FT-01: Company can set the booth logo
  - Action: As a company user, open the booth setup page for a default booth, upload an image file as the logo, and save.
  - Expected: The logo is saved and displayed on the booth page.
- [ ] FT-02: Company can add a short company description
  - Action: On the booth setup page, enter text into the company description field and save.
  - Expected: The entered description is saved and displayed on the booth page.
- [ ] FT-03: Company can add products or services
  - Action: On the booth setup page, add a product/service entry to the booth's list and save.
  - Expected: The new entry appears in the products/services list on the booth page.
- [ ] FT-04: Company can add images or videos
  - Action: On the booth setup page, upload an image or video file into the booth's media section and save.
  - Expected: The uploaded media is saved and displayed on the booth page.
- [ ] FT-05: Attendee can browse all booths
  - Action: Open the booths listing page as an attendee.
  - Expected: All default booths are listed, each identifiable by its company name (and logo where set).
- [ ] FT-06: Attendee can open a booth detail page
  - Action: Click a default booth entry in the listing.
  - Expected: That booth's detail page opens showing its logo, description, products/services, and media.
- [ ] FT-07: Attendee can send a text message to a booth
  - Action: On a booth page, type a question into the message field and click the send button.
  - Expected: The message is sent successfully to that booth.
- [ ] FT-08: Booth receives the attendee's message
  - Action: After an attendee sends a message, open the booth's messages view as the company user.
  - Expected: The sent message and its exact text are visible in the booth's received messages.

## Constraint
- [ ] CS-01: Booth cannot be saved with empty required fields
  - Action: On the booth setup page, clear a required field (e.g., company/booth name) and attempt to save.
  - Expected: Save is blocked with a validation message; the booth keeps its previous valid content.
- [ ] CS-02: Empty message cannot be sent
  - Action: On a booth page, leave the message field empty and click the send button.
  - Expected: No message is sent; the app prompts the attendee to enter message text.
- [ ] CS-03: Invalid media file is rejected
  - Action: On the booth setup page, attempt to upload a non-image/non-video file (e.g., a `.txt` file) as logo or media.
  - Expected: The upload is rejected with an error message and the file is not added to the booth.

## Interaction
- [ ] IX-01: Saving booth changes shows confirmation
  - Action: Make a valid edit on the booth setup page and save.
  - Expected: A success confirmation (toast/banner) appears with no error state.
- [ ] IX-02: Sending a message shows confirmation and clears the input
  - Action: Send a valid message from a booth page.
  - Expected: A success confirmation is shown and the message input is cleared.

## Content
- [ ] CT-01: Booth list entries identify their companies
  - Action: Review each default booth entry on the booths listing page.
  - Expected: Every entry shows a company name (and logo where set) that matches the same booth's detail page.
- [ ] CT-02: Booth detail content is relevant and intact
  - Action: Read the logo, description, and products/services list on a default booth page.
  - Expected: All text is complete (no placeholder text) and relevant to that booth's company.
- [ ] CT-03: Booth images and videos display correctly
  - Action: View all images and play all videos on a default booth page.
  - Expected: Every image renders and every video plays; media is relevant to the company with no broken items.