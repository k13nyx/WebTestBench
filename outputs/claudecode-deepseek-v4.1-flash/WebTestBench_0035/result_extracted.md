# Test Result

## Functionality
- [X] FT-01: Booth list page displays all pre-existing booths
  - Action: Open the website home/booths page with default data loaded.
  - Expected: Every default booth is listed, each showing at least a company name and logo thumbnail.
- [X] FT-02: Attendee can open a booth detail page
  - Action: Click a booth card/list item on the booths page.
  - Expected: The booth's detail page opens, showing that company's booth content.
- [X] FT-03: Booth page shows company logo
  - Action: View any default booth detail page.
  - Expected: The company's logo image is displayed on the page.
- [X] FT-04: Booth page shows a short company description
  - Action: View any default booth detail page.
  - Expected: A short text description of the company is displayed.
- [X] FT-05: Booth page shows a list of products or services
  - Action: View any default booth detail page that has products/services.
  - Expected: The products/services are listed with their names (and details if provided).
- [X] FT-06: Booth page shows images or videos
  - Action: View a default booth detail page that has media.
  - Expected: At least one image or video is displayed on the page.
- [X] FT-07: Attendee can send a text message to a booth
  - Action: On a booth detail page, type a question into the message field and submit it.
  - Expected: The message is accepted and a confirmation of submission is shown or the message appears in the booth's message area.
- [ ] FT-08: Company can set up a new booth
  - Action: Use the booth creation flow, enter a company name, and save.
  - Expected: A new booth is created and appears on the booths list.
  - Bug Report:
    - Issue: Missing Feature (no booth creation flow)
    - Actual: No booth creation flow exists. The application defines only three routes — `/` (Index), `/booth/:id` (BoothDetail), and `*` (NotFound) — and the home page exposes no "create/set up booth" control. Navigating to `/create`, `/create-booth`, and `/setup` all return a "404 — Oops! Page not found" page. There is no way to create a booth.
- [ ] FT-09: Company can add booth content fields when setting up a booth
  - Action: In the booth setup flow, provide a logo, description, products/services list, and media, then save.
  - Expected: All provided fields are saved and later display on the booth detail page.
  - Bug Report:
    - Issue: Missing Feature (no booth setup/content form)
    - Actual: There is no booth setup flow or content-entry form (no fields for logo, description, products/services, or media). Only pre-seeded data is rendered; no UI exists to add or edit booth content.

## Constraint
- [ ] CS-01: Booth setup rejects submission without a company name
  - Action: Attempt to save a new booth with the company name field left empty.
  - Expected: Submission is blocked and a validation message identifies the missing required field.
  - Bug Report:
    - Issue: Untestable / Missing Feature (no booth setup form)
    - Actual: No booth creation or setup form exists anywhere in the app (only routes `/`, `/booth/:id`, `*`), so there is no "company name" field and no save action to validate. The constraint cannot be satisfied because the underlying feature is absent.
- [X] CS-02: Message cannot be sent when empty
  - Action: On a booth detail page, attempt to submit a blank text message.
  - Expected: Submission is blocked; no empty message is created.
- [ ] CS-03: Invalid media cannot be added to a booth
  - Action: Attempt to upload a non-image, non-video file as booth media.
  - Expected: The file is rejected and an error indicates only image/video files are allowed.
  - Bug Report:
    - Issue: Missing Feature (no media upload control)
    - Actual: No file-upload control exists for booth media on any page (booth pages only render pre-seeded images). With no upload input, a non-image/non-video file cannot be supplied and no validation/rejection of invalid media occurs anywhere in the app.

## Interaction
- [X] IX-01: Booth detail page provides a way back to the full list
  - Action: From a booth detail page, use the back/browse navigation control.
  - Expected: The attendee returns to the booths list page.
- [X] IX-02: Message field gives clear feedback on submit
  - Action: Send a valid text message from a booth page.
  - Expected: A success indication (confirmation message or toast) appears after sending.

## Content
- [X] CT-01: Booths display trade-show-relevant company content
  - Action: Review the default booths and their content.
  - Expected: All booth text, logos, and media relate to exhibiting companies/products, with no unrelated or placeholder content.
- [X] CT-02: Booth media renders fully and correctly
  - Action: View the images/videos on each default booth page.
  - Expected: Media load without broken links, blank frames, or error icons.
