All tests executed. Final results:

# Test Result

## Functionality
- [X] FT-01: Attendees can browse all booths on the main listing page
  - Action: Open the site's home/browse page.
  - Expected: A list/grid of all booths is displayed, each entry showing at least the company name and logo; every pre-seeded booth appears.
  - Verified: "Explore Exhibitors" grid shows 5 cards (TechVision AI, GreenLeaf Sustainability, CloudNine Solutions, MedTech Innovations, FinancePlus), each with loaded logo image + company name. The seed data (`/src/data/booths.ts`) contains exactly these 5 booth slugs — all appear.

- [X] FT-02: Clicking a booth in the list opens that booth's detail page
  - Action: Click the first booth card in the listing.
  - Expected: The booth's own page loads and its company name matches the card that was clicked.
  - Verified: Clicked TechVision AI card → URL `/booth/techvision`, page `<h1>` = "TechVision AI", matching the clicked card.

- [X] FT-03: Booth page displays the company logo
  - Action: Visit a booth detail page.
  - Expected: The logo image is visible on the page (not replaced by a text-only header).
  - Verified: `<img alt="TechVision AI logo">` rendered and loaded (naturalWidth > 0) on the detail page header; same pattern confirmed on all 5 booth pages.

- [X] FT-04: Booth page displays the short company description
  - Action: Visit a booth detail page.
  - Expected: A description paragraph for that company is shown; it is non-empty and belongs to that company.
  - Verified: Non-empty company-specific description paragraph shown ("TechVision AI is at the forefront of machine learning innovation…" on techvision; GreenLeaf/company-specific text on other booths).

- [X] FT-05: Booth page displays the list of products or services
  - Action: Visit a booth detail page.
  - Expected: A product/service list is shown with all items defined for that booth visible (name of each item readable).
  - Verified: "Products & Services" section lists all seeded items with readable names: TechVision (VisionML Platform, DataSense Analytics, AutoML Studio — 3/3), GreenLeaf (Carbon Tracker Pro, EcoSupply Chain — 2/2), CloudNine (CloudNine Managed Kubernetes, SecureVault, CloudWatch 360 — 3/3), MedTech (VitalSync Monitor, CareFlow EHR — 2/2), FinancePlus (InvoiceFlow, CashFlow Pro, ExpenseTrack — 3/3).

- [X] FT-06: Booth page displays images or videos
  - Action: Visit a booth detail page that has media defined.
  - Expected: At least one image or video player is rendered in the booth's media section.
  - Verified: Gallery section on every booth page renders at least 2 loaded images (e.g., TechVision: "AI Research Lab", "Team Collaboration"). No video media is defined in the seed data (0 `<video>`/`<iframe>` elements site-wide), so the image branch applies and passes.

- [X] FT-07: Attendee can send a text question to the booth
  - Action: On a booth page, type a question (e.g., "Do you ship internationally?") into the message field and press the send/submit button.
  - Expected: The submission is accepted (form clears or closes) with no error.
  - Verified: With name/email filled and message "Do you ship internationally?" submitted → accepted; all form fields cleared; no error indication.

- [ ] FT-08: The sent message is recorded against that booth
  - Action: After sending a message on Booth A, reload the page / open the booth's messages or inbox area.
  - Expected: The message text, exactly as typed, is listed under Booth A (not under another booth).
  - Bug Report:
    - Issue: Message persistence / inbox absent
    - Actual: After sending and reloading `/booth/techvision`, the text "Do you ship internationally?" appears nowhere in the page. No messages/inbox area exists on any booth page; `localStorage` is empty; candidate routes `/inbox`, `/messages`, `/booth/techvision/messages`, `/exhibitor`, `/admin` all render "404 Oops! Page not found". The sent message is not recorded or retrievable against any booth.

- [X] FT-09: Attendee can return from a booth page back to the full booth listing
  - Action: From a booth detail page, use the "Back to all booths"/listing link or the browser back control.
  - Expected: The browse-all-booths page is shown again with the full list intact.
  - Verified: From `/booth/greenleaf`, clicking "Back to all booths" → `http://localhost:6035/` with all 5 booth cards intact.

## Constraint
- [X] CS-01: Message cannot be sent with empty content
  - Action: On a booth page, leave the message field blank and press send/submit.
  - Expected: The message is not accepted; a validation indication appears and no empty message is stored.
  - Verified: With name/email filled but message blank, submit shows toast "Please fill in all fields"; form retained, message not accepted.

- [X] CS-02: Message body is treated as plain text only
  - Action: Send a message containing markup, e.g. `<b>hello</b>` or `<script>alert(1)</script>`.
  - Expected: The text is displayed literally as typed; no markup is rendered, styled, or executed.
  - Verified: Submitted `<b>hello</b> <script>alert(1)</script>` on GreenLeaf — no JS dialog fired, no `<b>` element rendered, no injected `<script>alert(1)</script>` in the DOM; the value is held only as a plain-text string (submission accepted with normal toast). (Note: post-send re-display is not testable because of the FT-08 persistence defect, but no markup was ever rendered/styled/executed.)

- [X] CS-03: Requesting a booth that does not exist does not produce a blank/broken page
  - Action: Navigate directly to a booth detail URL/booth ID that is not in the data set.
  - Expected: A clear "not found"/error state (or redirect to the listing) is shown instead of an empty page or unhandled error.
  - Verified: `/booth/nonexistent-company-xyz` renders a proper error state: `<h1>` "Booth Not Found", paragraph "The booth you're looking for doesn't exist or has been removed.", plus a "Back to all booths" link.

## Interaction
- [X] IX-01: Success feedback after sending a message
  - Action: Complete FT-07 (valid message submit).
  - Expected: The UI shows an explicit confirmation (toast/inline success message such as "Message sent") that the question reached the booth.
  - Verified: Toast notification appeared: "Message sent! Your message has been sent to TechVision AI." (booth name correctly interpolated; also observed "…sent to GreenLeaf Sustainability" on the second booth).

- [X] IX-02: Booth list entries signal they are clickable
  - Action: Hover the pointer over a booth card in the listing.
  - Expected: A visible hover/pointer state change (cursor, border, elevation, or highlight) indicates the card can be opened.
  - Verified: Card link has `cursor: pointer`; on hover the inner article changes to `transform: translateY(-4px)` with elevation shadow `rgba(15,23,41,0.15) 0px 12px 40px -8px` (lift + shadow state change).

- [X] IX-03: Booth media is playable/viewable in place
  - Action: On a booth page with a video, click the play control; on a page with an image, click the image.
  - Expected: The video plays (or image opens a larger view) without navigating away from the booth page.
  - Verified: Clicking gallery image "AI Research Lab" on `/booth/techvision` opened it in an enlarged in-place view (>400px-wide image overlay) with the URL unchanged (`/booth/techvision`); dismissed with Escape. No booth defines a video (0 `<video>`/`<iframe>` across all pages), so the image branch is the applicable path.

## Content
- [X] CT-01: All logos and media assets load
  - Action: Walk the listing and each booth detail page, checking every image/video element.
  - Expected: No broken-image icons, empty media frames, or missing asset errors anywhere.
  - Verified: Programmatic check of every `<img>` (naturalWidth > 0) on the home listing (5 logos, all loaded) and all 5 booth detail pages (6/5/5/5/5 images respectively) — zero broken images, zero empty media frames; no video elements exist.

- [X] CT-02: Booth content matches its company
  - Action: For two different booths, compare logo, description, product list, and media.
  - Expected: Each booth's text and images are specific to that company; no content is duplicated or swapped between booths.
  - Verified: TechVision AI vs GreenLeaf Sustainability — distinct logo URLs, distinct descriptions (AI/ML vs environmental footprint), distinct product lists (VisionML Platform/DataSense Analytics/AutoML Studio vs Carbon Tracker Pro/EcoSupply Chain), distinct gallery media (AI Research Lab/Team Collaboration vs Forest Conservation/Solar Installation). Full sweep of all 5 booths shows unique h1/description/product/logo per company, with no cross-booth duplication or swapping.

- [X] CT-03: No placeholder or filler content is present
  - Action: Scan the listing and all booth pages, including product/service entries and the message form.
  - Expected: No "Lorem ipsum", "TBD", "Coming soon", "placeholder", or default sample/lorem text appears.
  - Verified: Regex scan for "lorem|ipsum|TBD|coming soon|placeholder|sample" over visible text of the home page and all 5 booth pages returned zero matches. The contact form's input hints ("John Doe", "john@example.com", "I'm interested in learning more about your products…") are standard field placeholder hints, not filler body content.

**Summary: 16 PASS / 1 FAIL** — the single defect is FT-08: sent attendee messages are never persisted or viewable anywhere (no inbox route, no storage, cleared on reload), so the core "send a basic text message to the booth" loop cannot be verified end-to-end.