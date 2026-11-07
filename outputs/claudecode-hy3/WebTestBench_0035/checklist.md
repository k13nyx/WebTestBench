# Test Checklist

## Functionality
- [ ] FT-01: Company can set up a virtual booth
  - Action: From the booth management area, create a new booth and save it.
  - Expected: A new booth is created and a booth page exists for it.

- [ ] FT-02: Company can add a logo to the booth
  - Action: On the booth edit page, upload/select a logo and save.
  - Expected: The booth page displays the uploaded logo.

- [ ] FT-03: Company can add a short company description
  - Action: Enter text in the company description field and save.
  - Expected: The booth page shows the entered company description.

- [ ] FT-04: Company can add a list of products or services
  - Action: Add one or more product/service entries and save.
  - Expected: The booth page lists the added products or services.

- [ ] FT-05: Company can add images or videos to the booth
  - Action: Add at least one image or video to the booth media area and save.
  - Expected: The booth page displays the added image(s) or video(s).

- [ ] FT-06: Attendee can browse all booths
  - Action: Open the booth listing/browse page.
  - Expected: A list of all available booths is displayed.

- [ ] FT-07: Attendee can click into a booth to view details
  - Action: Click on a booth from the browse list.
  - Expected: The booth's detail page opens showing its content.

- [ ] FT-08: Attendee can send a text message to a booth
  - Action: On a booth page, enter a text question and submit the message form.
  - Expected: The message is sent to the booth and recorded.

## Constraint
- [ ] CS-01: Cannot send an empty booth message
  - Action: Open a booth page and submit the message form with no text.
  - Expected: Submission is blocked and a required-field error is shown.

- [ ] CS-02: Booth requires a name/title to be created
  - Action: Attempt to create a booth without entering a name/title.
  - Expected: Creation is blocked and a required-name error is shown.

- [ ] CS-03: Booth message accepts text only
  - Action: Attempt to attach a file or non-text content to the message.
  - Expected: Non-text content is rejected; only plain text can be submitted.

## Interaction
- [ ] IX-01: Success confirmation after message is sent
  - Action: Send a valid text message to a booth.
  - Expected: A success toast/confirmation appears and the form clears.

- [ ] IX-02: New booth appears in browse list after creation
  - Action: Create a new booth, then open the browse page.
  - Expected: The newly created booth is visible in the list immediately.

- [ ] IX-03: Clicking a booth navigates to its own detail page
  - Action: Click a specific booth in the browse list.
  - Expected: The detail page shown corresponds to the clicked booth (correct logo/name/content).

## Content
- [ ] CT-01: Booth detail page displays all required content blocks
  - Action: Open a booth detail page.
  - Expected: Logo, company description, products/services list, and images/videos are all present.

- [ ] CT-02: Browse page shows relevant booth summary info
  - Action: Open the browse page.
  - Expected: Each booth entry shows its name and logo (and a brief identifier).

- [ ] CT-03: Booth media is relevant to the company
  - Action: Review the images/videos on a booth page.
  - Expected: All displayed media are directly relevant to that company's theme/offerings.