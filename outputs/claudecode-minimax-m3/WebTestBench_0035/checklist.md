# Test Checklist

> **Assumptions:** The app is reachable at its local URL; default booth data (companies with logo, description, products, media) already exists. Do not create new booths unless an item explicitly requires it. Company-side editing uses the booth setup form reached from the booth list or a "Create Booth"/"Edit" action.

## Functionality
- [ ] **FT-01:** Browse-all-booths list shows every default booth
  - Action: Open the app home / booth browse page.
  - Expected: A grid/list of all existing booths is rendered, each card showing the company's name and logo/thumbnail; no booth from the default data is missing.

- [ ] **FT-02:** Clicking a booth card opens that booth's detail page
  - Action: Click the name/thumbnail of any booth card in the browse list.
  - Expected: The app navigates to that booth's own page (URL changes to that booth) and the page shows that company's details.

- [ ] **FT-03:** Booth page displays the company logo
  - Action: Open any booth detail page.
  - Expected: The company's logo image is visible near the top of the page, matching the logo of the booth clicked.

- [ ] **FT-04:** Booth page displays the company description
  - Action: Open any booth detail page and read the area under the company name.
  - Expected: The short company description entered for that company is displayed in full.

- [ ] **FT-05:** Booth page displays the list of products/services
  - Action: Open any booth detail page and locate the products/services section.
  - Expected: Every product or service on that booth is listed as a separate item, in the order entered, with its name/text.

- [ ] **FT-06:** Booth page displays the booth's images and videos
  - Action: Open a booth detail page and scroll to the media/gallery area.
  - Expected: All images and videos added to that booth appear as visible thumbnails/players; both an image item and a video item are present for a default booth that has them.

- [ ] **FT-07:** Company can set up a new booth via the setup form
  - Action: Open the booth creation form (e.g., "Create Booth"/"Add Booth" action) and fill company name, description, logo, at least one product/service, and one image; save.
  - Expected: A success confirmation appears and the new booth is immediately listed in the browse list and openable at its own booth page with all entered data.

- [ ] **FT-08:** Company can edit an existing booth and changes are reflected
  - Action: Open the edit/setup form for an existing booth, change the description and add another product/service, then save.
  - Expected: Confirmation of save is shown; the booth's public page displays the updated description and the additional product, and the old value is gone.

- [ ] **FT-09:** Attendee can send a text message to a booth and the booth receives it
  - Action: Open a booth detail page, type a question into the message box, click "Send".
  - Expected: The message is accepted and stored against that booth, and it becomes visible in that booth's message list/inbox (viewable by the booth owner); the message does not appear on other booths.

## Constraint
- [ ] **CS-01:** Booth cannot be saved with required company info missing
  - Action: In the booth setup form, leave company name (or description) empty and attempt to save.
  - Expected: Save is blocked, a clear field-level validation message names the missing field, and no empty/partial booth is created.

- [ ] **CS-02:** Booth cannot be saved with an empty products/services list
  - Action: In the booth setup form, enter company name and description, add no product or service, and attempt to save.
  - Expected: Save is blocked with a validation message about products/services; the booth is not created or updated without a list.

- [ ] **CS-03:** Blank message cannot be sent to a booth
  - Action: On a booth page, leave the message field empty (or enter only spaces) and click "Send".
  - Expected: The send action is rejected with a validation prompt, and no empty/blank message is recorded in the booth's inbox.

- [ ] **CS-04:** Only valid image/video files can be added to a booth
  - Action: In the booth setup form, attempt to add a file that is neither an image nor a video (e.g., a .txt or .pdf) as logo or gallery media.
  - Expected: The file is rejected with an error naming the accepted types (image/video); it is not added to the logo or media list and cannot be saved.

## Interaction
- [ ] **IX-01:** Product/service rows can be added and removed before saving
  - Action: In the booth setup form, click "Add Product/Service" twice, then remove one of the rows.
  - Expected: Each click adds one new empty input row immediately; removing a row deletes only that row, and the remaining rows stay in order.

- [ ] **IX-02:** Uploaded media appears as a preview before saving
  - Action: In the booth setup form, upload an image as the logo and add an image/video to the media list.
  - Expected: A thumbnail/preview of the uploaded logo and of each added media item is displayed in the form immediately, before the booth is saved.

- [ ] **IX-03:** Successful saves and sends give immediate feedback
  - Action: Save a booth setup form successfully; then send a message from a booth page.
  - Expected: A visible success confirmation appears for each action, the message input is cleared after sending, and the saved booth's page shows the newly saved content (no stale/unchanged data).

- [ ] **IX-04:** Booth media gallery is interactive
  - Action: On a booth page with multiple media items, click a gallery image, click a video's play control, and use any next/previous control on the gallery.
  - Expected: The clicked image opens enlarged/full-size, the video plays (not just a static poster), and next/previous moves to the neighbouring media item.

## Content
- [ ] **CT-01:** Booth page shows the exact submitted company content, no placeholders
  - Action: Compare a booth page's title, description, and product/service entries against the values entered in the setup form.
  - Expected: Text matches verbatim; no leftover template tokens (e.g., "{company_name}"), lorem ipsum, "TBD", or "Untitled" placeholders appear anywhere on the page.

- [ ] **CT-02:** All booth media loads and is relevant to that booth
  - Action: Inspect the logo and gallery images/videos on each default booth page; watch for broken-image icons or error placeholders.
  - Expected: Every media element renders (no broken image/player error), and the content depicts that specific company/logo rather than unrelated generic or placeholder imagery.

- [ ] **CT-03:** Message text is stored and displayed exactly as typed
  - Action: Send a message containing mixed case, punctuation, digits and a multi-line sentence from a booth page, then view it in the booth's message list.
  - Expected: The displayed message matches the typed text character-for-character, with no truncation, mojibake/garbled characters, or dropped characters.