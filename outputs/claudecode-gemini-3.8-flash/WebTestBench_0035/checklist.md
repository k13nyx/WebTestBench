# Test Checklist

## Functionality
- [ ] FT-01: Browse virtual booths directory
  - Action: Navigate to the trade show home / booths directory page.
  - Expected: A list of all available company booths is displayed with booth cards showing company name and preview info.
- [ ] FT-02: Access individual booth detail page
  - Action: Click on any booth card in the directory.
  - Expected: The browser navigates to the selected booth's dedicated page displaying full booth information.
- [ ] FT-03: Upload company logo in booth setup
  - Action: In the booth setup editor, select an image via the "Upload Logo" input and click "Save Booth".
  - Expected: The uploaded logo is saved and displayed in the booth header.
- [ ] FT-04: Add company description in booth setup
  - Action: Enter text into the "Company Description" field in booth setup and click "Save Booth".
  - Expected: The entered company description is saved and appears on the booth page.
- [ ] FT-05: Add product or service item
  - Action: Enter an item name into the "Add Product/Service" input and click the "Add" button.
  - Expected: The item is added to the booth's products and services list.
- [ ] FT-06: Add images or videos to booth media gallery
  - Action: Upload an image file or enter a video link in the "Media" section and click "Save Booth".
  - Expected: The media item is saved and visible in the booth's media showcase section.
- [ ] FT-07: Send text message inquiry to booth
  - Action: On a booth detail page, type a question into the "Send a Message" text area and click "Submit".
  - Expected: The message submits successfully, and a delivery confirmation notification appears.

## Constraint
- [ ] CS-01: Prevent submitting empty attendee message
  - Action: Leave the message input blank on a booth page and click "Submit".
  - Expected: The message is not sent, and a validation message stating "Message cannot be empty" is displayed.
- [ ] CS-02: Enforce required fields on booth setup
  - Action: Clear the "Company Description" field in booth setup and click "Save Booth".
  - Expected: The form submission is blocked, and an error prompt highlights the field as required.
- [ ] CS-03: Prevent adding blank product or service entry
  - Action: Click "Add" in the products/services section without typing any text into the input field.
  - Expected: No blank entry is added to the list, and a field validation warning is shown.
- [ ] CS-04: Reject unsupported media file types
  - Action: Attempt to upload an unsupported file format (e.g., .pdf or .txt) in the logo/media upload field.
  - Expected: The upload is rejected, and an error message stating "Invalid file format" is displayed.

## Interaction
- [ ] IX-01: Booth card hover feedback
  - Action: Hover the mouse cursor over a booth card on the directory page.
  - Expected: The booth card visually changes (e.g., shadow elevation or border highlight) to indicate it is clickable.
- [ ] IX-02: Instant removal of product or service item
  - Action: Click the "Delete" (trash icon) button next to a product or service item in the booth editor list.
  - Expected: The item is immediately removed from the list display.
- [ ] IX-03: Message form clear on successful send
  - Action: Send a valid message via the booth inquiry form.
  - Expected: The message text input clears automatically after the message is sent.
- [ ] IX-04: Media lightbox / video player playback
  - Action: Click on an image or video thumbnail within the booth media gallery.
  - Expected: The media item opens in an enlarged modal/lightbox or begins playing in-place.

## Content
- [ ] CT-01: Directory booth card content completeness
  - Action: Inspect the booth cards displayed on the directory page.
  - Expected: Each card displays the company logo, company name, and a short descriptive snippet.
- [ ] CT-02: Booth detail page sections display
  - Action: View an existing booth detail page.
  - Expected: All core sections—company logo, description, products/services list, media gallery, and message form—are present and organized.
- [ ] CT-03: Products and services list presentation
  - Action: Check the products and services section on a booth detail page.
  - Expected: Products and services are displayed as readable, distinct list items without missing or overlapping text.
- [ ] CT-04: Media display integrity
  - Action: Examine all images and videos loaded on the booth page.
  - Expected: All images render without broken image icons, and videos display working playback controls.