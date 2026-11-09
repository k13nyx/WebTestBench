# Test Result

## Functionality

- [ ] FT-01: Company can save a virtual booth with its basic company information.
  - Action: Open the booth setup page for an available company booth, enter valid booth information, and select **“Save Booth”**.
  - Expected: The booth saves successfully and the saved information is available when the booth is reopened.
  - Bug Report:
    - Issue: Missing Booth Setup Page
    - Actual: Navigating to `/setup` displays a 404 “Oops! Page not found” page, so booth information cannot be entered or saved.

- [ ] FT-02: Company can add and display a logo.
  - Action: Use the **“Add Logo”** control to select a valid logo image, save the booth, and open the booth page.
  - Expected: The selected logo is displayed on the booth page.
  - Bug Report:
    - Issue: Missing Logo Management Controls
    - Actual: The booth setup page is unavailable with a 404 response, and no **“Add Logo”** control is available.

- [ ] FT-03: Company can add and display a short description.
  - Action: Enter text in the **“Company Description”** field, save the booth, and reopen the booth page.
  - Expected: The saved description is displayed in the booth’s company information section.
  - Bug Report:
    - Issue: Missing Booth Description Form
    - Actual: The booth setup page is unavailable with a 404 response, and no **“Company Description”** field is available.

- [ ] FT-04: Company can add multiple products or services.
  - Action: Add at least two entries through the **“Products or Services”** control and save the booth.
  - Expected: Each product or service appears as a separate entry on the booth page.
  - Bug Report:
    - Issue: Missing Product or Service Management Controls
    - Actual: The booth setup page is unavailable with a 404 response, and no **“Products or Services”** control is available.

- [ ] FT-05: Company can add and display booth media.
  - Action: Add a valid image and a valid video through the booth’s media controls, save the booth, and open the booth page.
  - Expected: The image is viewable and the video is available to play on the booth page.
  - Bug Report:
    - Issue: Missing Booth Media Controls and Video
    - Actual: The booth setup page is unavailable with a 404 response. The existing booth detail page displays static images only; no video element or video playback control is present.

- [X] FT-06: Attendee can browse the booth directory.
  - Action: Open the trade show’s booth browsing page.
  - Expected: The page displays all available default booths, with each booth identifiable by its company name or booth title.

- [X] FT-07: Attendee can open a booth from the directory.
  - Action: Select a booth from the booth directory.
  - Expected: The selected booth’s detail page opens and shows information belonging to that company.

- [X] FT-08: Attendee can send a text message to a booth.
  - Action: Open a booth, enter a valid question in the booth’s text message field, and select **“Send Message”**.
  - Expected: The message is submitted to the selected booth without requiring an attachment or another message type.

## Constraint

- [X] CS-01: Empty booth messages cannot be submitted.
  - Action: Leave the booth’s message field empty or enter only spaces, then select **“Send Message”**.
  - Expected: The message is not sent and the interface identifies the message field as requiring text.

- [X] CS-02: A message is addressed to the booth currently being viewed.
  - Action: Open Booth A, send a valid text message, and inspect the recipient or confirmation shown after submission.
  - Expected: The submission identifies Booth A as the recipient; it is not attributed to another booth.

- [ ] CS-03: Saved booth information remains consistent after navigation.
  - Action: Save booth details, navigate to the booth directory, reopen the same booth, and refresh the page.
  - Expected: The logo, description, products or services, and media remain unchanged after navigation and refresh.
  - Bug Report:
    - Issue: Booth Details Cannot Be Saved
    - Actual: The setup route `/setup` returns a 404 page, so configured booth details cannot be saved and their persistence after navigation or refresh cannot be verified.

## Interaction

- [ ] IX-01: Booth setup provides clear save feedback.
  - Action: Save a booth containing valid information.
  - Expected: A visible success indication appears, and the interface reflects the saved state without requiring a second save.
  - Bug Report:
    - Issue: Missing Save Booth Interaction
    - Actual: The booth setup page returns a 404 response, so the **“Save Booth”** action and success feedback are unavailable.

- [ ] IX-02: Booth media controls respond correctly.
  - Action: Select the booth image and use the video’s play control.
  - Expected: The image opens or enlarges for viewing, and the video starts playback when **“Play”** is selected.
  - Bug Report:
    - Issue: Non-interactive Images and Missing Video Control
    - Actual: The booth page contains `img` elements without click handlers or links, and no `video` element or **“Play”** control is present.

- [X] IX-03: Message submission provides clear completion feedback.
  - Action: Send a valid text message from a booth page.
  - Expected: A visible confirmation states that the message was sent, and the message field is cleared or otherwise shows that submission completed.

- [X] IX-04: Booth directory selection provides clear navigation.
  - Action: Select different booths from the directory one at a time.
  - Expected: Each selection opens the corresponding booth detail page, and the page does not remain on the previously selected booth.

## Content

- [X] CT-01: Each booth displays complete company information when configured.
  - Action: Review the booth page for a default booth that contains configured content.
  - Expected: The page presents the company logo, short description, products or services, and available images or videos in clearly identifiable sections.

- [X] CT-02: Booth media is relevant to the booth’s company.
  - Action: Review every image and video displayed on a default booth page.
  - Expected: Each media item is directly related to the company, its products, or its services; unrelated or broken media is not displayed.

- [X] CT-03: Booth directory and detail content identify the same company.
  - Action: Note a company name in the booth directory, open that booth, and compare the detail page.
  - Expected: The company or booth identity matches in both locations, with no mismatched title, logo, or company description.
