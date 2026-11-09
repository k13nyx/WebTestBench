# Test Checklist

## Functionality
- [ ] FT-01: Attendees can browse all booths on the main listing page
  - Action: Open the site's home/browse page.
  - Expected: A list/grid of all booths is displayed, each entry showing at least the company name and logo; every pre-seeded booth appears.

- [ ] FT-02: Clicking a booth in the list opens that booth's detail page
  - Action: Click the first booth card in the listing.
  - Expected: The booth's own page loads and its company name matches the card that was clicked.

- [ ] FT-03: Booth page displays the company logo
  - Action: Visit a booth detail page.
  - Expected: The logo image is visible on the page (not replaced by a text-only header).

- [ ] FT-04: Booth page displays the short company description
  - Action: Visit a booth detail page.
  - Expected: A description paragraph for that company is shown; it is non-empty and belongs to that company.

- [ ] FT-05: Booth page displays the list of products or services
  - Action: Visit a booth detail page.
  - Expected: A product/service list is shown with all items defined for that booth visible (name of each item readable).

- [ ] FT-06: Booth page displays images or videos
  - Action: Visit a booth detail page that has media defined.
  - Expected: At least one image or video player is rendered in the booth's media section.

- [ ] FT-07: Attendee can send a text question to the booth
  - Action: On a booth page, type a question (e.g., "Do you ship internationally?") into the message field and press the send/submit button.
  - Expected: The submission is accepted (form clears or closes) with no error.

- [ ] FT-08: The sent message is recorded against that booth
  - Action: After sending a message on Booth A, reload the page / open the booth's messages or inbox area.
  - Expected: The message text, exactly as typed, is listed under Booth A (not under another booth).

- [ ] FT-09: Attendee can return from a booth page back to the full booth listing
  - Action: From a booth detail page, use the "Back to booths"/listing link or the browser back control.
  - Expected: The browse-all-booths page is shown again with the full list intact.

## Constraint
- [ ] CS-01: Message cannot be sent with empty content
  - Action: On a booth page, leave the message field blank and press send/submit.
  - Expected: The message is not accepted; a validation indication appears and no empty message is stored.

- [ ] CS-02: Message body is treated as plain text only
  - Action: Send a message containing markup, e.g. `<b>hello</b>` or `<script>alert(1)</script>`.
  - Expected: The text is displayed literally as typed; no markup is rendered, styled, or executed.

- [ ] CS-03: Requesting a booth that does not exist does not produce a blank/broken page
  - Action: Navigate directly to a booth detail URL/booth ID that is not in the data set.
  - Expected: A clear "not found"/error state (or redirect to the listing) is shown instead of an empty page or unhandled error.

## Interaction
- [ ] IX-01: Success feedback after sending a message
  - Action: Complete FT-07 (valid message submit).
  - Expected: The UI shows an explicit confirmation (toast/inline success message such as "Message sent") that the question reached the booth.

- [ ] IX-02: Booth list entries signal they are clickable
  - Action: Hover the pointer over a booth card in the listing.
  - Expected: A visible hover/pointer state change (cursor, border, elevation, or highlight) indicates the card can be opened.

- [ ] IX-03: Booth media is playable/viewable in place
  - Action: On a booth page with a video, click the play control; on a page with an image, click the image.
  - Expected: The video plays (or image opens a larger view) without navigating away from the booth page.

## Content
- [ ] CT-01: All logos and media assets load
  - Action: Walk the listing and each booth detail page, checking every image/video element.
  - Expected: No broken-image icons, empty media frames, or missing asset errors anywhere.

- [ ] CT-02: Booth content matches its company
  - Action: For two different booths, compare logo, description, product list, and media.
  - Expected: Each booth's text and images are specific to that company; no content is duplicated or swapped between booths.

- [ ] CT-03: No placeholder or filler content is present
  - Action: Scan the listing and all booth pages, including product/service entries and the message form.
  - Expected: No "Lorem ipsum", "TBD", "Coming soon", "placeholder", or default sample/lorem text appears.