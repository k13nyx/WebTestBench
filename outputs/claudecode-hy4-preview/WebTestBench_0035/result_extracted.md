# Test Result

## Functionality

- [ ] FT-01: Company can create a new booth with name and description
  - Action: Open the booth setup/create page, enter company name "Acme Robotics" and a short description, click Save/Create.
  - Expected: Booth is created and its booth page displays the entered company name and description.
  - Bug Report:
    - Issue: Missing Feature — no booth creation/setup page exists
    - Actual: The application has only two routes (`/` browse page and `/booth/:id` detail page; verified in `src/App.tsx`, which contains no other `<Route>` entries). There is no "Create Booth", "Set up booth", "Add booth" or "Register" link/button anywhere: the header nav contains only `Browse Booths -> /`, and the home page buttons are `Explore Booths`, `All Booths`, `Technology`, `Sustainability`, `Healthcare`, `Finance`. Candidate URLs `/create`, `/setup`, `/admin`, `/dashboard`, `/new`, `/create-booth`, `/exhibitor` all return the 404 page ("Oops! Page not found"). No input for company name or description exists, so no booth could be created.

- [ ] FT-02: Company can add a logo to its booth
  - Action: On the booth setup page, upload an image file in the Logo field and save.
  - Expected: The uploaded image is displayed as the booth logo on the booth page.
  - Bug Report:
    - Issue: Missing Feature — no logo upload control
    - Actual: No booth setup page exists (see FT-01) and the booth detail page contains 0 `input[type=file]` elements. Booth logos are hard-coded Unsplash URLs in `src/data/booths.ts` (e.g. TechVision AI logo `https://images.unsplash.com/photo-1677442136019-...`). No upload field is present, so a logo cannot be added.

- [ ] FT-03: Company can add an item to the products/services list
  - Action: On a default booth's setup page, add a product/service entry "Industrial Arm X1" and save.
  - Expected: "Industrial Arm X1" appears as a list item in the booth's Products/Services section.
  - Bug Report:
    - Issue: Missing Feature — products list is read-only
    - Actual: No booth setup/edit page exists. On `/booth/techvision` the Products & Services section renders only the static items from `src/data/booths.ts` ("VisionML Platform", "DataSense Analytics", "AutoML Studio"). There is no "Add product" button or text input, and the only inputs on the page are `name`, `email`, `message` (the attendee message form). "Industrial Arm X1" could not be added.

- [ ] FT-04: Company can add an image to the booth media section
  - Action: In the booth's media/images section, upload or add an image and save.
  - Expected: The image appears in the booth's media gallery and renders visibly on the booth page.
  - Bug Report:
    - Issue: Missing Feature — media gallery is read-only, no add/upload control
    - Actual: No booth setup page exists and there are 0 `input[type=file]` elements on the booth page. The Gallery section on each booth renders a fixed, hard-coded list from `src/data/booths.ts` with no "Add media" button or URL field. Media cannot be added by a company.

- [ ] FT-05: Company can add a video to the booth media section
  - Action: In the booth's media section, add a video (file upload or video link) and save.
  - Expected: The video appears in the booth's media gallery with a visible player; pressing play starts playback.
  - Bug Report:
    - Issue: Missing Feature — no video upload and no playable video player
    - Actual: No booth setup page and no media-add control exist (see FT-04). Additionally, no booth in the app contains any video: all 5 booths' `mediaGallery` entries are `type: 'image'` only, and `document.querySelectorAll('video')` returned an empty array on every booth page. `MediaGallery.tsx` renders video items as a `<video>` element with a decorative Play icon overlay and **no `controls` attribute and no click handler**, so even a video item would not be playable.

- [ ] FT-06: Booth edits persist after reloading the page
  - Action: Edit the short description of a default booth, save, then reload the booth page.
  - Expected: The updated description is shown and the previous text is no longer displayed.
  - Bug Report:
    - Issue: Missing Feature — booth content is not editable
    - Actual: The booth detail page exposes no editable field and no Save control: the only inputs are `name`, `email`, `message`, the only button is `Send Message`, there are no `contenteditable` elements and no file inputs. Booth data comes from the static `booths` array in `src/data/booths.ts` with no mutation/persistence layer. The description could not be edited, so no change could persist across a reload.

- [X] FT-07: Attendee can browse all booths
  - Action: Open the booth directory / browse page as an attendee.
  - Expected: All existing booths are listed (grid or list), each showing at least a company name and logo, and the count matches the number of booths in the app.

- [X] FT-08: Attendee can click into a booth to read more
  - Action: From the browse page, click any booth card/name.
  - Expected: The page navigates to that booth's detail page showing its logo, description, products/services list, and media section.

- [X] FT-09: Attendee can send a text message to a booth
  - Action: On a booth detail page, type "Do you ship to Europe?" in the message box and click Send.
  - Expected: The message is accepted and a success confirmation is shown.

- [ ] FT-10: Sent message is delivered to the booth's messages
  - Action: Open the booth owner's messages/inbox view for the booth used in FT-09.
  - Expected: The message "Do you ship to Europe?" is listed as received for that booth.
  - Bug Report:
    - Issue: Missing Feature — no booth-owner messages/inbox view
    - Actual: Sent messages are stored in an in-memory array in `src/stores/messageStore.ts` (`let messages: Message[] = []`, "In-memory message storage (resets on page refresh)"). `getMessagesForBooth()` is never consumed by any component, and there is no route or UI for it — the only routes are `/` and `/booth/:id`, the booth page's links are `/`, `https://<site>`, `mailto:<email>`, `#`, `#`, and the page text contains no "Inbox" or "Messages" section. The message is never surfaced to any booth owner.

## Constraint

- [ ] CS-01: Booth cannot be created without a company name
  - Action: On the booth setup page, leave the company name field empty and submit.
  - Expected: Submission is blocked, a validation message about the missing company name is shown, and no new booth appears in the browse list.
  - Bug Report:
    - Issue: Missing Feature — no creation form to validate
    - Actual: No booth setup/create page exists (see FT-01), so there is no company name field and no submit action. No validation can occur. The browse list remains at the 5 hard-coded booths because there is no way to submit anything.

- [X] CS-02: Empty or whitespace-only message cannot be sent
  - Action: On a booth detail page, leave the message box empty (or enter only spaces) and click Send.
  - Expected: The message is not sent — either Send is disabled or an error message is shown; no new entry appears in the booth's messages.

- [ ] CS-03: Duplicate booth name is prevented
  - Action: Create a new booth using the exact company name of an existing default booth and submit.
  - Expected: Creation is rejected with a message stating the booth/company name already exists, and no duplicate booth is added to the browse list.
  - Bug Report:
    - Issue: Missing Feature — no creation form, no duplicate-name check
    - Actual: No booth creation page or form exists (see FT-01), so a duplicate name cannot be submitted. `src/data/booths.ts` contains no uniqueness validation, and `MessageForm.tsx` is the only form with validation (it checks name/email/message only). No duplicate-name rejection message is possible.

- [ ] CS-04: Unsupported file types are rejected for logo/media
  - Action: On the booth setup page, attempt to upload a non-image file (e.g., a .pdf or .txt file) as the logo or media image.
  - Expected: The upload is rejected with an error message and the invalid file is not added to the booth.
  - Bug Report:
    - Issue: Missing Feature — no file upload exists, therefore no file-type validation
    - Actual: There are 0 `input[type=file]` elements on the home page and on every booth detail page, and no booth setup page exists. No file of any type can be submitted, so no rejection error is ever produced.

## Interaction

- [ ] IX-01: Confirmation feedback appears after saving booth changes
  - Action: Change any booth field and click Save.
  - Expected: A success message/toast confirming the booth was saved is displayed.
  - Bug Report:
    - Issue: Missing Feature — no editable booth field and no Save action
    - Actual: Booth pages are read-only: the only button on a booth detail page is `Send Message`, the only inputs are `name`, `email`, `message`, and no `Save` button exists. The toast system is wired only to `MessageForm` (titles "Please fill in all fields" / "Message sent!"), so no booth-saved confirmation can appear.

- [X] IX-02: Message box clears and confirmation appears after sending
  - Action: Type a valid message and click Send.
  - Expected: A success confirmation is shown and the message input field is cleared.

- [ ] IX-03: Newly created booth appears in the browse list
  - Action: Create a new booth, then open the browse page without manually re-entering data.
  - Expected: The newly created booth is visible in the booth list among the existing booths.
  - Bug Report:
    - Issue: Missing Feature — booth creation does not exist, browse list is static
    - Actual: No booth can be created (see FT-01). `src/pages/Index.tsx` renders `filteredBooths` from the imported static `booths` array, and after any navigation the browse page still shows exactly the same 5 booths (TechVision AI, GreenLeaf Sustainability, CloudNine Solutions, MedTech Innovations, FinancePlus).

## Content

- [X] CT-01: Browse page shows complete, relevant booth information
  - Action: Open the browse page and inspect each booth card.
  - Expected: Every booth card shows its real company name, a rendered logo image (no broken-image icon), and its short description — with no unrelated or placeholder text.

- [X] CT-02: Booth detail page content matches the selected booth
  - Action: Open a specific default booth from the browse page and compare its content to the booth card clicked.
  - Expected: The detail page shows the same company name and logo as the card, plus that booth's own description, products/services list, and media — not another booth's data.

- [X] CT-03: All booth media renders correctly
  - Action: Open several default booths and view their logos and media galleries.
  - Expected: Every image loads and displays (no broken-image icons), every video shows a working player, and all media is relevant to that company/booth.
