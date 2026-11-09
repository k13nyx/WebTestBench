All test items executed. Here is the complete checklist with verified statuses:

# Test Result

## Functionality
- [ ] FT-01: Company can set up a new booth with basic company info.
  - Action: Open the booth setup form, enter a company name (e.g., "Acme Corp") and save.
  - Expected: The booth is created and appears in the booth listing.
  - Bug Report:
    - Issue: Missing Feature — Booth Setup Form
    - Actual: No booth setup form exists anywhere in the application. The app only has 3 routes: `/` (browse list), `/booth/:id` (detail), and a 404 page. Probed `/setup`, `/create`, `/booth/new`, `/new-booth`, `/booths/new`, `/admin`, `/host`, `/exhibitor`, `/register`, `/dashboard`, `/edit` — all return "Oops! Page not found" or "Booth Not Found". No button or link for creating a booth exists on any page, so a booth named "Acme Corp" cannot be created.
- [ ] FT-02: Company can add a logo to their booth.
  - Action: In the booth setup form, upload a logo image and save.
  - Expected: The logo is accepted and saved to the booth without error.
  - Bug Report:
    - Issue: Missing Feature — Logo Upload
    - Actual: No booth setup form and no logo upload control exists in the application. All 5 booths are static pre-existing data; there is no UI to upload or change a logo.
- [ ] FT-03: Company can add a short company description.
  - Action: Type a short company description in the booth form and save.
  - Expected: The description is saved with the booth without error.
  - Bug Report:
    - Issue: Missing Feature — Description Input
    - Actual: No booth setup form exists; company descriptions are static hard-coded data with no editable field anywhere in the UI.
- [ ] FT-04: Company can add products or services to the booth.
  - Action: Add one product/service entry (name and details) to the booth's products/services list and save.
  - Expected: The entry is saved and listed in the booth's products/services section.
  - Bug Report:
    - Issue: Missing Feature — Products/Services Management
    - Actual: The "Products & Services" section on booth pages is read-only display of static data. No "add product/service" control, input fields, or save action exists.
- [ ] FT-05: Company can add images or videos to the booth.
  - Action: Upload an image and add a video in the booth's media section, then save.
  - Expected: Both media items are saved to the booth without error.
  - Bug Report:
    - Issue: Missing Feature — Media Upload
    - Actual: The booth "Gallery" section is read-only with static images. No media upload control exists on any page; images and videos cannot be added.
- [X] FT-06: Attendee can browse all booths.
  - Action: Open the booth browse/listing page.
  - Expected: A list of all booths (including the default pre-existing booths) is displayed.
- [X] FT-07: Attendee can click into a booth to read more.
  - Action: Click the first default booth entry in the browse list.
  - Expected: The booth's detail page opens and shows the booth's content.
- [X] FT-08: Attendee can send a text message to a booth.
  - Action: On a booth page, type a question in the message text field and click "Send".
  - Expected: The message is sent to the booth and accepted without error.

## Constraint
- [ ] CS-01: Booth cannot be saved with missing required information.
  - Action: Open the booth setup form, leave the company name empty, click Save.
  - Expected: Saving is blocked and a validation error identifies the missing required field.
  - Bug Report:
    - Issue: Missing Feature — Booth Setup Form Validation
    - Actual: The booth setup form does not exist (see FT-01), so the save/validation flow cannot be exercised at all — there is no Save button or required-field validation to observe.
- [ ] CS-02: Empty product/service entries are not accepted.
  - Action: In the products/services list, try to add an entry with all fields empty.
  - Expected: The empty entry is rejected and not added; a validation message is shown.
  - Bug Report:
    - Issue: Missing Feature — Product/Service Entry Form
    - Actual: No product/service entry form exists in the application; products are static display-only data, so an empty entry cannot be attempted and no validation message can appear.
- [ ] CS-03: Booth media accepts only images and videos.
  - Action: In the booth media section, try to upload a non-media file (e.g., a .txt or .pdf file).
  - Expected: The upload is rejected with an error; the file is not added to the booth.
  - Bug Report:
    - Issue: Missing Feature — Media Upload Control
    - Actual: No file upload control exists on any page (media is static display-only), so uploading a non-media file cannot be attempted and no rejection error can occur.
- [X] CS-04: Empty message cannot be sent.
  - Action: On a booth page, leave the message text field empty and click "Send".
  - Expected: No message is sent and a validation error prompts for message text.

## Interaction
- [ ] IX-01: Success confirmation appears after saving booth setup.
  - Action: Complete the booth setup form and save it.
  - Expected: A success confirmation (e.g., "Booth saved" toast or message) is displayed.
  - Bug Report:
    - Issue: Missing Feature — Booth Save Confirmation
    - Actual: The booth setup form does not exist (see FT-01); no save action can be performed, so no "Booth saved" confirmation can ever be displayed.
- [X] IX-02: Success confirmation appears after sending a message.
  - Action: Send a valid text message on a booth page.
  - Expected: A success confirmation (e.g., "Message sent") is displayed.
- [X] IX-03: Booth cards show a hover state in the browse list.
  - Action: Move the mouse cursor over a booth card in the browse list.
  - Expected: The card shows a visual hover indication (highlight and/or pointer cursor) marking it as clickable.

## Content
- [X] CT-01: Booth page displays the company logo.
  - Action: Open the detail page of a booth that has a logo (default booth or one from FT-02).
  - Expected: The booth's logo image is displayed on the page.
- [X] CT-02: Booth page displays the company description.
  - Action: Open a booth's detail page and view the description section.
  - Expected: The saved description text is displayed exactly as entered.
- [X] CT-03: Booth page displays the products/services list.
  - Action: Open a booth's detail page and view the products/services section.
  - Expected: All saved product/service entries are displayed with their names and details.
- [ ] CT-04: Booth page displays the added images/videos.
  - Action: Open a booth with media and view its media section.
  - Expected: Saved images render as images and saved videos are present and playable.
  - Bug Report:
    - Issue: Missing Media Type — No Videos Present
    - Actual: Gallery images render correctly as `<img>` elements (e.g., "AI Research Lab", "Team Collaboration" on TechVision AI), but zero `<video>` elements exist on any of the 5 booths (verified on all booth pages). No video content is present or playable, and there is no UI to add video (see FT-05).
- [X] CT-05: Browse list shows booth identity for each booth.
  - Action: View the browse page containing the default booths.
  - Expected: Each booth entry displays its company name and logo (or logo placeholder if none).