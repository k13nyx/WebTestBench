# Test Result

## Functionality

- [X] FT-01: Keyword search returns matching pets
  - Action: Type a breed or pet name from the default data (e.g., "Labrador") in the search box and click Search.
  - Expected: Only pets whose name or breed matches the keyword are listed, and the result count reflects them.

- [X] FT-02: Species filter limits results to the selected species
  - Action: Set the Species filter to "Dog" and apply.
  - Expected: Every listed pet shows Species: Dog, and no cats or other species appear.

- [ ] FT-03: Age range filter limits results to the entered range
  - Action: Set Min Age to 1 and Max Age to 3 and apply.
  - Expected: Every listed pet shows an age from 1 to 3 years inclusive, and pets outside the range are excluded.
  - Bug Report:
    - Issue: Missing Control / Incorrect Age Boundary
    - Actual: No Min Age or Max Age inputs exist. Only preset checkboxes are shown ("Baby (< 1 year)", "Young (1-3 years)", "Adult (4-7 years)", "Senior (8+ years)"). With "Young (1-3 years)" checked, Luna (3 years) and Shadow (3 years) are excluded, so the inclusive upper bound of 3 is not honored. With "Senior (8+ years)" checked, Duke (7 years) is listed, so the bucket boundaries are also inconsistent.

- [X] FT-04: Size filter limits results to the selected size
  - Action: Set the Size filter to "Small" and apply.
  - Expected: Every listed pet shows Size: Small.

- [ ] FT-05: "Good with kids" filter limits results to pets that are good with kids
  - Action: Check "Good with kids" and apply.
  - Expected: Every listed pet shows "Good with kids: Yes".
  - Bug Report:
    - Issue: Incorrect Label Format / Profile Data Inconsistency
    - Actual: The filter correctly excludes Whiskers, but Whiskers' profile lists "Good with kids" under Compatibility, and its description says "She prefers a quiet home without young children." Cards and profiles show a "Good with kids" tag, not the literal "Good with kids: Yes" text. The Compatibility block on every profile shows both tags, regardless of the pet's data.

- [ ] FT-06: "Good with other pets" filter limits results to pets that are good with other pets
  - Action: Check "Good with other pets" and apply.
  - Expected: Every listed pet shows "Good with other pets: Yes".
  - Bug Report:
    - Issue: Profile Data Inconsistency / Incorrect Label Format
    - Actual: The filter excludes Max and Sunny, but their profiles list "Good with other pets" under Compatibility. Sunny's description says "He needs a home without cats or other pets." The profile shows a "Good with other pets" tag, not the literal "Good with other pets: Yes" text.

- [X] FT-07: Sort by Relevance orders results by match to the search
  - Action: Search for a breed present in the default data, then select Sort: "Relevance".
  - Expected: Pets whose name or breed matches the search appear before pets that match only loosely.

- [ ] FT-08: Sort by Recently Listed orders results newest first
  - Action: Clear all filters and select Sort: "Recently Listed".
  - Expected: Pets are ordered by listing date, newest first, and each card shows its listed date.
  - Bug Report:
    - Issue: Missing Sort Option / Missing Listing Date
    - Actual: The sort dropdown offers only "Relevance", "Newest First", "Oldest First", and "Name A-Z"; there is no "Recently Listed" option. "Newest First" reorders the list, but cards show only relative text such as "Listed almost 2 years ago" or "Listed about 2 years ago", never a date.

- [X] FT-09: Pet profile opens with photos and full details
  - Action: Click the name of any pet in the results list.
  - Expected: A profile page shows the pet's name, species, breed, age, size, good-with-kids and good-with-other-pets status, shelter name, at least one photo, and a description. Clicking the next arrow on the photo gallery shows the next photo.

- [ ] FT-10: Saved favorites appear on the Favorites list
  - Action: On a pet's profile, click "Save to Favorites"; then open the "Favorites" page.
  - Expected: The pet appears in the Favorites list. Clicking "Remove" on that pet removes it from the list.
  - Bug Report:
    - Issue: Missing Button Label
    - Actual: No "Save to Favorites" button exists on the profile. There is an icon-only heart button over the photo with no text or aria-label. The favorite flow works functionally: Luna appeared on /favorites, and clicking the icon-only heart on her card removed her. No "Remove" control exists, only an unlabeled heart icon.

- [ ] FT-11: Adoption inquiry form submits successfully with valid input
  - Action: On a pet's profile, enter Name "Test User", Email "test@example.com", and Message "Is this pet available?", then click "Send Inquiry".
  - Expected: A confirmation message "Your inquiry has been sent" appears, and the form fields are cleared.
  - Bug Report:
    - Issue: Incorrect Confirmation Message
    - Actual: The submission succeeded, and the form was replaced by a panel headed "Inquiry Submitted!" with the text "Happy Tails Rescue has received your inquiry about Luna." A toast reads "Inquiry Sent! Happy Tails Rescue will contact you soon about Luna." The text "Your inquiry has been sent" never appears.

## Constraint

- [ ] CS-01: Inquiry cannot be sent with a required field empty
  - Action: On a pet's profile, enter a name and message, leave Email empty, and click "Send Inquiry".
  - Expected: The Email field shows "Email is required", no confirmation appears, and no inquiry is sent.
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: The inquiry was not sent and no confirmation appeared. The Email field shows only the browser's native tooltip, "Please fill out this field." No "Email is required" text is rendered in the page.

- [ ] CS-02: Inquiry cannot be sent with an invalid email address
  - Action: Enter Email "user@" with valid Name and Message, then click "Send Inquiry".
  - Expected: The Email field shows "Enter a valid email address", and no inquiry is sent.
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: The inquiry was not sent. The browser's native validation blocked submission with "Please enter a part following '@'. 'user@' is incomplete." The page never shows "Enter a valid email address".

- [ ] CS-03: Minimum age cannot be greater than maximum age
  - Action: Set Min Age to 5 and Max Age to 2, then apply.
  - Expected: The message "Minimum age cannot be greater than maximum age" is shown, and the results are not filtered by the invalid range.
  - Bug Report:
    - Issue: Missing Control
    - Actual: The page has no Min Age or Max Age inputs, so the invalid range cannot be entered. The validation message cannot be triggered, and the test could not be executed.

## Interaction

- [ ] IX-01: Favorite button toggles its state visually
  - Action: On a pet's profile, click the "Save to Favorites" button, then click it again.
  - Expected: After the first click the button changes to "Saved" with a filled heart icon; after the second click it reverts to "Save to Favorites" with an empty heart icon.
  - Bug Report:
    - Issue: Incomplete Visual State Change
    - Actual: The heart icon is the only element that changes. It gains the class `fill-accent text-accent` on the first click and reverts on the second. The text "Saved" never appears, and the "Save to Favorites" label does not exist.

- [ ] IX-02: Empty results show a message with a way to reset
  - Action: Apply a combination of filters that matches no default pets (e.g., Species: "Rabbit" with Size: "Giant" if none exist; otherwise choose any combination with zero results).
  - Expected: The message "No pets match your filters" appears in place of the list, and a "Clear Filters" button is shown. Clicking "Clear Filters" resets all controls and restores the full list.
  - Bug Report:
    - Issue: Missing Empty-State Message / Missing Reset Button
    - Actual: With Birds + Large selected, the counter shows "0 adorable pets available for adoption" and no cards appear. The text "No pets match your filters" does not appear, and no "Clear Filters" button exists. Only a sidebar link labeled "Clear all filters" is present. Clicking it restored the full list.

## Content

- [ ] CT-01: Pet photos match the listed species
  - Action: Review the photo on each pet card in the results list, filtering to Dog and then to Cat.
  - Expected: Each photo shows an animal of the species listed for that pet, with no broken images or unrelated pictures.
  - Bug Report:
    - Issue: Unverifiable Content (DOM-only constraint)
    - Actual: All 12 card images load (complete with naturalWidth > 0), so none are broken. However, the images are Unsplash URLs with alt text equal to the pet name only, with no species or content metadata. Whether each picture shows the listed species cannot be confirmed from the DOM.

- [X] CT-02: Pet descriptions are real and relevant to the pet
  - Action: Open the profile of at least five different pets.
  - Expected: Each description refers to the pet's name or species and contains no placeholder text such as "lorem ipsum", "TBD", or "N/A".

- [ ] CT-03: Results show shelter names from multiple shelters
  - Action: Clear all filters and review the shelter name on each card in the results list.
  - Expected: Every card displays a shelter name, and at least two different shelter names appear across the results.
  - Bug Report:
    - Issue: Missing Shelter Name on Cards
    - Actual: Cards show the pet's name, breed, size, age, and city (e.g., "Portland, OR") but no shelter name. Shelter names appear only on profile pages, where three distinct shelters are shown: Happy Tails Rescue, Second Chance Animal Haven, and Furry Friends Forever.

- [X] CT-04: Age and size values are displayed in readable form
  - Action: Review the age and size fields on several cards and on the profile page of a pet.
  - Expected: Age shows a value with units (e.g., "2 years" or "8 months"), size shows a named category (e.g., "Small"), and no field displays "undefined", "null", "NaN", or is blank.
