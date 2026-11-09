# Test Checklist

## Functionality
- [ ] FT-01: Keyword search returns matching pets
  - Action: Type a breed or pet name from the default data (e.g., "Labrador") in the search box and click Search.
  - Expected: Only pets whose name or breed matches the keyword are listed, and the result count reflects them.
- [ ] FT-02: Species filter limits results to the selected species
  - Action: Set the Species filter to "Dog" and apply.
  - Expected: Every listed pet shows Species: Dog, and no cats or other species appear.
- [ ] FT-03: Age range filter limits results to the entered range
  - Action: Set Min Age to 1 and Max Age to 3 and apply.
  - Expected: Every listed pet shows an age from 1 to 3 years inclusive, and pets outside the range are excluded.
- [ ] FT-04: Size filter limits results to the selected size
  - Action: Set the Size filter to "Small" and apply.
  - Expected: Every listed pet shows Size: Small.
- [ ] FT-05: "Good with kids" filter limits results to pets that are good with kids
  - Action: Check "Good with kids" and apply.
  - Expected: Every listed pet shows "Good with kids: Yes".
- [ ] FT-06: "Good with other pets" filter limits results to pets that are good with other pets
  - Action: Check "Good with other pets" and apply.
  - Expected: Every listed pet shows "Good with other pets: Yes".
- [ ] FT-07: Sort by Relevance orders results by match to the search
  - Action: Search for a breed present in the default data, then select Sort: "Relevance".
  - Expected: Pets whose name or breed matches the search appear before pets that match only loosely.
- [ ] FT-08: Sort by Recently Listed orders results newest first
  - Action: Clear all filters and select Sort: "Recently Listed".
  - Expected: Pets are ordered by listing date, newest first, and each card shows its listed date.
- [ ] FT-09: Pet profile opens with photos and full details
  - Action: Click the name of any pet in the results list.
  - Expected: A profile page shows the pet's name, species, breed, age, size, good-with-kids and good-with-other-pets status, shelter name, at least one photo, and a description. Clicking the next arrow on the photo gallery shows the next photo.
- [ ] FT-10: Saved favorites appear on the Favorites list
  - Action: On a pet's profile, click "Save to Favorites"; then open the "Favorites" page.
  - Expected: The pet appears in the Favorites list. Clicking "Remove" on that pet removes it from the list.
- [ ] FT-11: Adoption inquiry form submits successfully with valid input
  - Action: On a pet's profile, enter Name "Test User", Email "test@example.com", and Message "Is this pet available?", then click "Send Inquiry".
  - Expected: A confirmation message "Your inquiry has been sent" appears, and the form fields are cleared.

## Constraint
- [ ] CS-01: Inquiry cannot be sent with a required field empty
  - Action: On a pet's profile, enter a name and message, leave Email empty, and click "Send Inquiry".
  - Expected: The Email field shows "Email is required", no confirmation appears, and no inquiry is sent.
- [ ] CS-02: Inquiry cannot be sent with an invalid email address
  - Action: Enter Email "user@" with valid Name and Message, then click "Send Inquiry".
  - Expected: The Email field shows "Enter a valid email address", and no inquiry is sent.
- [ ] CS-03: Minimum age cannot be greater than maximum age
  - Action: Set Min Age to 5 and Max Age to 2, then apply.
  - Expected: The message "Minimum age cannot be greater than maximum age" is shown, and the results are not filtered by the invalid range.

## Interaction
- [ ] IX-01: Favorite button toggles its state visually
  - Action: On a pet's profile, click the "Save to Favorites" button, then click it again.
  - Expected: After the first click the button changes to "Saved" with a filled heart icon; after the second click it reverts to "Save to Favorites" with an empty heart icon.
- [ ] IX-02: Empty results show a message with a way to reset
  - Action: Apply a combination of filters that matches no default pets (e.g., Species: "Rabbit" with Size: "Giant" if none exist; otherwise choose any combination with zero results).
  - Expected: The message "No pets match your filters" appears in place of the list, and a "Clear Filters" button is shown. Clicking "Clear Filters" resets all controls and restores the full list.

## Content
- [ ] CT-01: Pet photos match the listed species
  - Action: Review the photo on each pet card in the results list, filtering to Dog and then to Cat.
  - Expected: Each photo shows an animal of the species listed for that pet, with no broken images or unrelated pictures.
- [ ] CT-02: Pet descriptions are real and relevant to the pet
  - Action: Open the profile of at least five different pets.
  - Expected: Each description refers to the pet's name or species and contains no placeholder text such as "lorem ipsum", "TBD", or "N/A".
- [ ] CT-03: Results show shelter names from multiple shelters
  - Action: Clear all filters and review the shelter name on each card in the results list.
  - Expected: Every card displays a shelter name, and at least two different shelter names appear across the results.
- [ ] CT-04: Age and size values are displayed in readable form
  - Action: Review the age and size fields on several cards and on the profile page of a pet.
  - Expected: Age shows a value with units (e.g., "2 years" or "8 months"), size shows a named category (e.g., "Small"), and no field displays "undefined", "null", "NaN", or is blank.