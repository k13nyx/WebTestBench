# Test Result

## Functionality
- [ ] FT-01: Company can set up a virtual booth
  - Action: From the booth management area, create a new booth and save it.
  - Expected: A new booth is created and a booth page exists for it.
  - Bug Report:
    - Issue: Missing Feature / No Create Functionality
    - Actual: The application has no booth management or create-booth area. Defined routes are only "/" (browse) and "/booth/:id" (detail) plus a 404 catch-all (verified in App.tsx). There is no UI or route to create a booth, so the action cannot be performed.

- [ ] FT-02: Company can add a logo to the booth
  - Action: On the booth edit page, upload/select a logo and save.
  - Expected: The booth page displays the uploaded logo.
  - Bug Report:
    - Issue: Missing Feature / No Edit Functionality
    - Actual: No booth edit page or logo upload control exists. Booths (including logos) are loaded from static data (src/data/booths.ts) and are read-only.

- [ ] FT-03: Company can add a short company description
  - Action: Enter text in the company description field and save.
  - Expected: The booth page shows the entered company description.
  - Bug Report:
    - Issue: Missing Feature / No Edit Functionality
    - Actual: There is no description editing form. Descriptions are part of static booth data and cannot be modified by a user.

- [ ] FT-04: Company can add a list of products or services
  - Action: Add one or more product/service entries and save.
  - Expected: The booth page lists the added products or services.
  - Bug Report:
    - Issue: Missing Feature / No Edit Functionality
    - Actual: Products/services are pre-defined in static data and there is no interface to add entries to a booth.

- [ ] FT-05: Company can add images or videos to the booth
  - Action: Add at least one image or video to the booth media area and save.
  - Expected: The booth page displays the added image(s) or video(s).
  - Bug Report:
    - Issue: Missing Feature / No Edit Functionality
    - Actual: Booth media (gallery) is static and read-only; there is no media upload/add control anywhere in the app.

- [X] FT-06: Attendee can browse all booths
  - Action: Open the booth listing/browse page.
  - Expected: A list of all available booths is displayed.
  - (Verified: Home page lists 5 booths — TechVision AI, GreenLeaf Sustainability, CloudNine Solutions, MedTech Innovations, FinancePlus.)

- [X] FT-07: Attendee can click into a booth to view details
  - Action: Click on a booth from the browse list.
  - Expected: The booth's detail page opens showing its content.
  - (Verified: Clicking the TechVision AI card navigated to /booth/techvision and rendered its logo, name, description, products, gallery, and contact/message sections.)

- [X] FT-08: Attendee can send a text message to a booth
  - Action: On a booth page, enter a text question and submit the message form.
  - Expected: The message is sent to the booth and recorded.
  - (Verified: Filled name/email/message and submitted; success confirmation "Message Sent!" appeared and message was added via addMessage store.)

## Constraint
- [X] CS-01: Cannot send an empty booth message
  - Action: Open a booth page and submit the message form with no text.
  - Expected: Submission is blocked and a required-field error is shown.
  - (Verified: Empty submit triggered toast "Please fill in all fields" and the form remained, not submitted.)

- [ ] CS-02: Booth requires a name/title to be created
  - Action: Attempt to create a booth without entering a name/title.
  - Expected: Creation is blocked and a required-name error is shown.
  - Bug Report:
    - Issue: Missing Feature / No Create Functionality
    - Actual: There is no booth creation feature at all, so the required-name validation cannot be exercised. No create form or "name required" error exists in the application.

- [X] CS-03: Booth message accepts text only
  - Action: Attempt to attach a file or non-text content to the message.
  - Expected: Non-text content is rejected; only plain text can be submitted.
  - (Verified: The message form exposes only three text inputs — Your Name, Your Email, Your Message. There is no file/attachment control, so non-text content cannot be attached; only plain text can be submitted.)

## Interaction
- [X] IX-01: Success confirmation after message is sent
  - Action: Send a valid text message to a booth.
  - Expected: A success toast/confirmation appears and the form clears.
  - (Verified: After submit, a toast "Message sent! — Your message has been sent to TechVision AI." appeared and the form was replaced by a "Message Sent!" confirmation panel.)

- [ ] IX-02: New booth appears in browse list after creation
  - Action: Create a new booth, then open the browse page.
  - Expected: The newly created booth is visible in the list immediately.
  - Bug Report:
    - Issue: Missing Feature / No Create Functionality
    - Actual: Booth creation is not supported, so a newly created booth can never appear in the browse list.

- [X] IX-03: Clicking a booth navigates to its own detail page
  - Action: Click a specific booth in the browse list.
  - Expected: The detail page shown corresponds to the clicked booth (correct logo/name/content).
  - (Verified: Clicking the TechVision AI card opened /booth/techvision showing TechVision AI's logo, name, tagline, description, products, and gallery — content matches the clicked booth.)

## Content
- [X] CT-01: Booth detail page displays all required content blocks
  - Action: Open a booth detail page.
  - Expected: Logo, company description, products/services list, and images/videos are all present.
  - (Verified on /booth/techvision: logo present, description paragraph present, "Products & Services" list with 3 items present, "Gallery" with 2 images present.)

- [X] CT-02: Browse page shows relevant booth summary info
  - Action: Open the browse page.
  - Expected: Each booth entry shows its name and logo (and a brief identifier).
  - (Verified: Each of the 5 booth cards displays a logo image, the company name heading, and a category tag as identifier.)

- [X] CT-03: Booth media is relevant to the company
  - Action: Review the images/videos on a booth page.
  - Expected: All displayed media are directly relevant to that company's theme/offerings.
  - (Verified: TechVision AI's gallery shows "AI Research Lab" and "Team Collaboration" — thematically aligned with an AI company's offerings.)
