# Test Checklist

## Functionality
- [ ] FT-01: Attendee can view the booth directory
  - Action: Open the website's home / "Browse Booths" page.
  - Expected: A list/grid of all default booths is displayed, each showing at least a company name (and logo if available).
- [ ] FT-02: Attendee can open a booth's detail page
  - Action: Click on any booth card in the directory.
  - Expected: The booth's detail page opens, showing that company's name, logo, description, products/services, and media.
- [ ] FT-03: Booth page displays the full company description and product/service list
  - Action: Open any default booth's detail page and read the content sections.
  - Expected: The "About/Description" section shows the company's short description, and a "Products/Services" section lists each item as separate, readable entries.
- [ ] FT-04: Company can create/set up a new booth
  - Action: Use the "Create Booth" / "Set Up Booth" flow, fill in company name, description, and upload a logo image, then save.
  - Expected: The booth is saved and appears in the booth directory with the entered name and uploaded logo.
- [ ] FT-05: Company can add products/services items to a booth
  - Action: Edit a booth, add one or more products/services entries (e.g., "Product A", "Service B"), and save.
  - Expected: The booth's detail page lists all added items under Products/Services.
- [ ] FT-06: Company can add images and videos to a booth
  - Action: Edit a booth, upload at least one image and one video, and save.
  - Expected: The image is visible in the booth's media/gallery section and the video is present with playable controls.
- [ ] FT-07: Company edits to a booth persist
  - Action: Edit a booth's description, save, navigate away, then reopen the booth.
  - Expected: The detail page shows the updated description (not the old one).
- [ ] FT-08: Attendee can send a text message to a booth
  - Action: Open a booth's detail page, type a question (e.g., "What is the pricing of Product A?") into the message box, and submit.
  - Expected: The message is accepted and the attendee sees indication it was sent (sent state/confirmation).

## Constraint
- [ ] CS-01: Booth cannot be saved with empty required fields
  - Action: Open the booth setup form and submit with the company name and/or description left empty.
  - Expected: Submission is blocked and a validation error is shown; no booth is created.
- [ ] CS-02: Empty message cannot be sent
  - Action: On a booth page, click the message send button with the text box empty (or only spaces).
  - Expected: The message is not sent and an error/disable state is shown; no empty message is recorded.
- [ ] CS-03: Invalid file types are rejected in booth media upload
  - Action: In the booth edit form, attempt to upload a non-media file (e.g., a .txt or .exe) as a logo/image.
  - Expected: The file is rejected with an error message and is not attached to the booth.
- [ ] CS-04: Product/service entry cannot be blank
  - Action: In the booth edit form, add a product/service item with an empty name and save.
  - Expected: The blank item is rejected or ignored; no empty row appears on the booth page.

## Interaction
- [ ] IX-01: Booth cards respond to hover
  - Action: Move the mouse cursor over a booth card in the directory.
  - Expected: The card gives visible hover feedback (e.g., shadow, highlight, or cursor change) indicating it is clickable.
- [ ] IX-02: Success feedback is shown after a message is sent
  - Action: Submit a valid text message to a booth.
  - Expected: A visible confirmation appears (e.g., success toast, "Message sent" text, or the message appearing in a sent list) without page reload errors.
- [ ] IX-03: Video in a booth plays on demand
  - Action: Open a booth containing a video and click the play control.
  - Expected: The video starts playing in the page (progress/audio indicates playback).
- [ ] IX-04: Message box retains text if submission fails
  - Action: Trigger a failed message submission (e.g., send while disconnected or with a blocked input per CS-02 behavior) after typing text.
  - Expected: The typed text remains in the input box so the user does not lose it.

## Content
- [ ] CT-01: Booth media is relevant to the company
  - Action: Open each default booth's detail page and compare its images/videos to the company name, description, and products.
  - Expected: All displayed images/videos are directly relevant to that company's theme (no unrelated placeholder or broken images).
- [ ] CT-02: All booth text is complete and uncorrupted
  - Action: Read the description, product list, and any sent message text on booth pages.
  - Expected: Text is fully readable with no truncated sentences, HTML/markup artifacts, garbled characters, or missing special characters.
- [ ] CT-03: Logo images render correctly everywhere shown
  - Action: View each booth's logo in the directory list and on its detail page.
  - Expected: The logo renders as a real, non-broken image in both locations and matches the company.