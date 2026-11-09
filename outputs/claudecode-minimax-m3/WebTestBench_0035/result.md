I have enough data to compile the test results. Let me provide the final report.

# Test Result

## Functionality

- [X] **FT-01:** Browse-all-booths list shows every default booth
  - Action: Open the app home / booth browse page.
  - Expected: A grid/list of all existing booths is rendered, each card showing the company's name and logo/thumbnail; no booth from the default data is missing.

- [X] **FT-02:** Clicking a booth card opens that booth's detail page
  - Action: Click the name/thumbnail of any booth card in the browse list.
  - Expected: The app navigates to that booth's own page (URL changes to that booth) and the page shows that company's details.

- [X] **FT-03:** Booth page displays the company logo
  - Action: Open any booth detail page.
  - Expected: The company's logo image is visible near the top of the page, matching the logo of the booth clicked.

- [X] **FT-04:** Booth page displays the company description
  - Action: Open any booth detail page and read the area under the company name.
  - Expected: The short company description entered for that company is displayed in full.

- [X] **FT-05:** Booth page displays the list of products/services
  - Action: Open any booth detail page and locate the products/services section.
  - Expected: Every product or service on that booth is listed as a separate item, in the order entered, with its name/text.

- [ ] **FT-06:** Booth page displays the booth's images and videos
  - Action: Open a booth detail page and scroll to the media/gallery area.
  - Expected: All images and videos added to that booth appear as visible thumbnails/players; both an image item and a video item are present for a default booth that has them.
  - Bug Report:
    - Issue: Missing Video Media Items
    - Actual: Gallery sections across all 5 default booths (TechVision AI, GreenLeaf, CloudNine, MedTech, FinancePlus) contain ONLY image items. No `<video>` elements exist on any booth page (verified via `document.querySelectorAll('video').length === 0` on every booth). No video thumbnails, players, or posters are rendered, despite the checklist assumption that default booth data includes both image and video media.

- [ ] **FT-07:** Company can set up a new booth via the setup form
  - Action: Open the booth creation form (e.g., "Create Booth"/"Add Booth" action) and fill company name, description, logo, at least one product/service, and one image; save.
  - Expected: A success confirmation appears and the new booth is immediately listed in the browse list and openable at its own booth page with all entered data.
  - Bug Report:
    - Issue: Missing Feature — No Booth Creation UI
    - Actual: There is no "Create Booth", "Add Booth", or similar button anywhere in the application. The header navigation contains only "Browse Booths" and the company/site name. Probed `/admin`, `/create`, and `/booth/<id>/edit` — all return 404. No setup form route exists in the app, so the booth creation action cannot be performed at all.

- [ ] **FT-08:** Company can edit an existing booth and changes are reflected
  - Action: Open the edit/setup form for an existing booth, change the description and add another product/service, then save.
  - Expected: Confirmation of save is shown; the booth's public page displays the updated description and the additional product, and the old value is gone.
  - Bug Report:
    - Issue: Missing Feature — No Booth Editing UI
    - Actual: No "Edit Booth" button or link is rendered on any booth detail page (e.g., `/booth/techvision` shows only "Visit Website", email, products, gallery, and message form). The edit/setup route `/booth/techvision/edit` returns 404. Without an edit form the booth cannot be modified.

- [ ] **FT-09:** Attendee can send a text message to a booth and the booth receives it
  - Action: Open a booth detail page, type a question into the message box, click "Send".
  - Expected: The message is accepted and stored against that booth, and it becomes visible in that booth's message list/inbox (viewable by the booth owner); the message does not appear on other booths.
  - Bug Report:
    - Issue: Missing Inbox / No Message Storage Visibility
    - Actual: Sending a message with name, email, and body produces a "Message sent!" toast notification and a "Message Sent!" success panel, and the form is cleared. However, there is no booth-side inbox, message list, or message history anywhere — verified `/inbox` returns 404, no "Inbox"/"Messages" link exists in the navigation, and the sent text never appears anywhere in the DOM after submission. The booth owner has no way to view received messages, so the storage-and-display criterion is not met.

## Constraint

- [ ] **CS-01:** Booth cannot be saved with required company info missing
  - Action: In the booth setup form, leave company name (or description) empty and attempt to save.
  - Expected: Save is blocked, a clear field-level validation message names the missing field, and no empty/partial booth is created.
  - Bug Report:
    - Issue: Missing Feature — No Booth Setup Form
    - Actual: The booth setup form required to test this constraint does not exist in the application. No "Create Booth"/"Edit Booth" form is reachable, so the required-field validation behavior cannot be exercised.

- [ ] **CS-02:** Booth cannot be saved with an empty products/services list
  - Action: In the booth setup form, enter company name and description, add no product or service, and attempt to save.
  - Expected: Save is blocked with a validation message about products/services; the booth is not created or updated without a list.
  - Bug Report:
    - Issue: Missing Feature — No Booth Setup Form
    - Actual: There is no booth setup form reachable from any page. The products/services required-list validation cannot be triggered because the form itself does not exist.

- [X] **CS-03:** Blank message cannot be sent to a booth
  - Action: On a booth page, leave the message field empty (or enter only spaces) and click "Send".
  - Expected: The send action is rejected with a validation prompt, and no empty/blank message is recorded in the booth's inbox.
  - Bug Report:
    - Issue: (none — passed)

- [ ] **CS-04:** Only valid image/video files can be added to a booth
  - Action: In the booth setup form, attempt to add a file that is neither an image nor a video (e.g., a .txt or .pdf) as logo or gallery media.
  - Expected: The file is rejected with an error naming the accepted types (image/video); it is not added to the logo or media list and cannot be saved.
  - Bug Report:
    - Issue: Missing Feature — No Booth Setup Form / No File Upload UI
    - Actual: No booth setup form exists in the application, so there is no file input control for logo or gallery media to attempt uploading an invalid file against. The file-type validation behavior cannot be tested.

## Interaction

- [ ] **IX-01:** Product/service rows can be added and removed before saving
  - Action: In the booth setup form, click "Add Product/Service" twice, then remove one of the rows.
  - Expected: Each click adds one new empty input row immediately; removing a row deletes only that row, and the remaining rows stay in order.
  - Bug Report:
    - Issue: Missing Feature — No Booth Setup Form
    - Actual: There is no "Add Product/Service" button or removable row UI on any page because the booth setup form does not exist. The add/remove interaction cannot be tested.

- [ ] **IX-02:** Uploaded media appears as a preview before saving
  - Action: In the booth setup form, upload an image as the logo and add an image/video to the media list.
  - Expected: A thumbnail/preview of the uploaded logo and of each added media item is displayed in the form immediately, before the booth is saved.
  - Bug Report:
    - Issue: Missing Feature — No Booth Setup Form / No File Input
    - Actual: The booth setup form does not exist in the app, so there are no logo or gallery upload fields. The preview-before-save interaction cannot be exercised.

- [ ] **IX-03:** Successful saves and sends give immediate feedback
  - Action: Save a booth setup form successfully; then send a message from a booth page.
  - Expected: A visible success confirmation appears for each action, the message input is cleared after sending, and the saved booth's page shows the newly saved content (no stale/unchanged data).
  - Bug Report:
    - Issue: Partial — Save-side feedback missing (no setup form); Send-side passes
    - Actual: The "save a booth" half of this item cannot be exercised because the booth setup form does not exist. The "send a message" half does work: clicking "Send Message" with valid input shows a "Message sent!" toast and replaces the form with a "Message Sent!" success panel containing a "Send another message" button (i.e., the input is cleared). Because the save part is missing entirely, this combined item fails.

- [ ] **IX-04:** Booth media gallery is interactive
  - Action: On a booth page with multiple media items, click a gallery image, click a video's play control, and use any next/previous control on the gallery.
  - Expected: The clicked image opens enlarged/full-size, the video plays (not just a static poster), and next/previous moves to the neighbouring media item.
  - Bug Report:
    - Issue: Non-Interactive Gallery
    - Actual: The gallery on every booth page is a static grid. Clicking a gallery image produces no enlarged view, modal, lightbox, or any DOM change. Programmatic inspection confirms: `cursor: auto` on the images and their parents, `img.onclick === null`, and zero `<button>` elements inside the Gallery section. There are also no `<video>` elements anywhere, so there is no video play control to test. No next/previous buttons exist either.

## Content

- [ ] **CT-01:** Booth page shows the exact submitted company content, no placeholders
  - Action: Compare a booth page's title, description, and product/service entries against the values entered in the setup form.
  - Expected: Text matches verbatim; no leftover template tokens (e.g., "{company_name}"), lorem ipsum, "TBD", or "Untitled" placeholders appear anywhere on the page.
  - Bug Report:
    - Issue: Inconclusive — Cannot Submit Booth Content
    - Actual: The comparison against "values entered in the setup form" cannot be performed because the booth setup form does not exist; no new booth content can be submitted. The default booths render with their own static, non-template text (no `{company_name}`, lorem ipsum, or "TBD" placeholders visible), but the verbatim-submitted-content half of the check is unverifiable in this build.

- [ ] **CT-02:** All booth media loads and is relevant to that booth
  - Action: Inspect the logo and gallery images/videos on each default booth page; watch for broken-image icons or error placeholders.
  - Expected: Every media element renders (no broken image/player error), and the content depicts that specific company/logo rather than unrelated generic or placeholder imagery.
  - Bug Report:
    - Issue: Generic Stock Imagery, Not Company-Specific
    - Actual: All logos and gallery items load without broken-image errors (every `<img>` reports `complete: true` and non-zero `naturalWidth`). However, every media asset is a generic stock photograph sourced from `images.unsplash.com` (e.g., TechVision's "logo" is a generic Unsplash image, CloudNine's "Global Data Centers" is an unrelated stock photo, FinancePlus's "Financial Dashboard" is a stock photo). None of the images depict the actual company's brand, products, or logo — they are unrelated generic imagery, which violates the "relevant to that specific company/logo rather than unrelated generic or placeholder imagery" criterion.

- [ ] **CT-03:** Message text is stored and displayed exactly as typed
  - Action: Send a message containing mixed case, punctuation, digits and a multi-line sentence from a booth page, then view it in the booth's message list.
  - Expected: The displayed message matches the typed text character-for-character, with no truncation, mojibake/garbled characters, or dropped characters.
  - Bug Report:
    - Issue: Missing Inbox — Sent Text Cannot Be Viewed
    - Actual: After successfully submitting a message containing mixed case, punctuation, and digits from a booth page, the submitted text never appears anywhere in the application. There is no message list/inbox for the booth owner to view. Verified by DOM text scan: `hasJohnTester: false`, `hasTestMessage: false`, and no occurrence of the typed text in `document.body.innerText`. Because the displayed-text criterion is unmet, exact-character storage cannot be confirmed.