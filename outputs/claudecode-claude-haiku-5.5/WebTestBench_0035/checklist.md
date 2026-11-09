# Test Checklist

## Functionality
- [ ] FT-01: Attendee can view all booths on the booth listing page.
  - Action: Open the trade show home page and click "Booths" (or the equivalent listing link).
  - Expected: Every default booth appears as a card showing its company name and logo.
- [ ] FT-02: Attendee can open a booth to read its details.
  - Action: Click the name or card of any default booth.
  - Expected: The booth page opens and shows the logo, company name, description, products/services list, and image/video section.
- [ ] FT-03: Booth owner can change the booth logo.
  - Action: Log in as the owner of a default booth, open "Edit Booth," upload a new valid image in the "Logo" field, and click "Save."
  - Expected: The new logo appears on the booth page and on the booth listing card.
- [ ] FT-04: Booth owner can edit the description and products/services list.
  - Action: Log in as a booth owner, open "Edit Booth," change the text in "Description" and add one item to "Products/Services," then click "Save."
  - Expected: The updated description and new list item appear on the booth page.
- [ ] FT-05: Booth owner can add images and videos to the booth.
  - Action: Log in as a booth owner, open "Edit Booth," upload one image and one video in the "Media" section, then click "Save."
  - Expected: Both files appear in the booth's media section on the booth page.
- [ ] FT-06: Attendee can send a text message to a booth, and the owner receives it.
  - Action: On a booth page, type "What are your pricing options?" in the message box and click "Send." Then log in as that booth's owner and open "Messages."
  - Expected: The message is accepted, and the owner's Messages list shows the exact text and sender.

## Constraint
- [ ] CS-01: Empty messages cannot be sent.
  - Action: On a booth page, leave the message box blank and click "Send."
  - Expected: The message is not sent, and the message "Message cannot be empty" appears. No entry is added to the owner's Messages.
- [ ] CS-02: A company cannot edit another company's booth.
  - Action: Log in as the owner of Booth A, then enter the edit URL of Booth B in the address bar (or try to access "Edit Booth" for Booth B).
  - Expected: Access is denied with an "Access denied" or "Not authorized" message, and Booth B's form does not open.
- [ ] CS-03: Logo upload rejects non-image files.
  - Action: Log in as a booth owner, open "Edit Booth," attempt to upload a .txt or .pdf file in the "Logo" field, and click "Save."
  - Expected: The upload is rejected with an error such as "Logo must be an image file," and the previous logo remains on the booth page.
- [ ] CS-04: Media upload rejects unsupported file types.
  - Action: Log in as a booth owner, open "Edit Booth," attempt to upload a .docx or .exe file in the "Media" section, and click "Save."
  - Expected: The file is rejected with an error such as "Unsupported file type," and it does not appear in the booth's media section.
- [ ] CS-05: Invalid booth URLs show an error page.
  - Action: Enter a booth page address for a booth that does not exist (e.g., /booths/does-not-exist) in the address bar.
  - Expected: A "Booth not found" message appears, and no booth details are displayed.

## Interaction
- [ ] IX-01: Sending a message gives confirmation and clears the field.
  - Action: On a booth page, type "Do you ship internationally?" in the message box and click "Send."
  - Expected: A "Message sent" confirmation appears, and the message box is empty.
- [ ] IX-02: Booth cards respond to hovering.
  - Action: On the booth listing page, move the mouse over any booth card.
  - Expected: The card is visually highlighted, and the cursor changes to a pointer.
- [ ] IX-03: Media items open and play correctly.
  - Action: On a booth page, click an image in the media section, then close it with the close button. Click a video.
  - Expected: The image opens in an enlarged view and closes with the close button. The video starts playing and shows playback controls.
- [ ] IX-04: Saving booth edits gives confirmation.
  - Action: Log in as a booth owner, change any field in "Edit Booth," and click "Save."
  - Expected: A "Booth saved" confirmation appears, and the booth page reflects the change.

## Content
- [ ] CT-01: All default booth logos and media load.
  - Action: Open the booth listing page, then open each default booth page.
  - Expected: All logos, images, and videos display without broken-image icons or playback errors.
- [ ] CT-02: Each booth appears once in the listing with matching details.
  - Action: Compare the booth listing card for each default booth with its booth page.
  - Expected: Each booth appears exactly once, and the card's company name and logo match the booth page.
- [ ] CT-03: Booth pages contain no placeholder or test text.
  - Action: Read the company name, description, and products/services on every default booth page.
  - Expected: No placeholder text such as "Lorem ipsum," "TBD," "test," or "sample" appears.
- [ ] CT-04: Booth media is relevant to the company.
  - Action: On each default booth page, compare the images and videos with the company's listed products or services.
  - Expected: Each image and video clearly relates to that company's products or services.
- [ ] CT-05: Booth descriptions are relevant to a trade show exhibitor.
  - Action: Read the description on each default booth page.
  - Expected: Each description describes the company or its offerings, and does not contain unrelated content.