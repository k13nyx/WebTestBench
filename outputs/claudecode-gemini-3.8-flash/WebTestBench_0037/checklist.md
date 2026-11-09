# Test Checklist

## Functionality
- [ ] FT-01: Filter pets by species, age range, and size
  - Action: Select options from the "Species" (e.g., Dog), "Age Range" (e.g., Young), and "Size" (e.g., Medium) filter controls on the listing page.
  - Expected: Pet listing dynamically updates to show only animals matching all selected criteria.
- [ ] FT-02: Filter pets by compatibility with children and other animals
  - Action: Check the "Good with Kids" and "Good with Other Pets" filter checkboxes.
  - Expected: Only pets tagged as compatible with both kids and other pets are displayed in the results.
- [ ] FT-03: Filter pets by shelter organization
  - Action: Select a specific shelter name from the "Shelter" filter dropdown.
  - Expected: The list updates to display only pets housed by the selected shelter.
- [ ] FT-04: Sort pets by relevance and time listed
  - Action: Select "Time Listed (Newest)" from the sort dropdown, then switch to "Relevance".
  - Expected: The list reorders pets chronologically by listing date, then re-sorts according to search match relevance.
- [ ] FT-05: Open pet detailed profile
  - Action: Click on a pet card from the listing results.
  - Expected: Navigates to the pet's dedicated profile page displaying full details, photos, and shelter information.
- [ ] FT-06: Add pet to favorites list
  - Action: Click the "Save to Favorites" (heart) button on a pet card or profile page.
  - Expected: The pet is added to the user's favorites list.
- [ ] FT-07: View saved favorites list
  - Action: Click on the "Favorites" navigation link/icon.
  - Expected: Navigates to the favorites page displaying all previously saved pet cards.
- [ ] FT-08: Remove pet from favorites list
  - Action: Click the "Remove" button on a saved pet item within the favorites list.
  - Expected: The pet is immediately removed from the favorites list and no longer appears there.
- [ ] FT-09: Submit adoption inquiry form
  - Action: Fill in all required fields (Name, Email, Phone, Message) on the pet profile's inquiry form and click "Send Inquiry".
  - Expected: The form submits successfully and clears the input fields.

## Constraint
- [ ] CS-01: Prevent inquiry form submission with missing required fields
  - Action: Leave mandatory fields empty on the inquiry form and click "Send Inquiry".
  - Expected: Form is not submitted, and inline error messages indicate that required fields cannot be blank.
- [ ] CS-02: Validate email address format on adoption inquiry form
  - Action: Enter an invalid email format (e.g., "user@notanemail") into the email field and click "Send Inquiry".
  - Expected: Submission is blocked and an "Enter a valid email address" validation error is displayed.
- [ ] CS-03: Display empty state for zero matching filter results
  - Action: Select a combination of filters that yields no matching animals.
  - Expected: The pet list area displays a "No adoptable pets found matching your criteria" message with a "Reset Filters" button.

## Interaction
- [ ] IX-01: Favorite button active state visual toggle
  - Action: Click the "Save to Favorites" button on a pet card.
  - Expected: The button icon immediately changes to a filled/active state to visually confirm the action.
- [ ] IX-02: Adoption inquiry submission confirmation feedback
  - Action: Complete and submit a valid adoption inquiry form.
  - Expected: A confirmation modal or toast notification appears displaying "Your inquiry has been sent to the shelter".
- [ ] IX-03: Pet profile photo gallery thumbnail switching
  - Action: Click on a secondary photo thumbnail in the pet profile gallery.
  - Expected: The main photo display updates smoothly to show the clicked image.

## Content
- [ ] CT-01: Display accurate pet metadata on listing cards and profile
  - Action: Inspect the information shown on pet cards and the detail profile.
  - Expected: Each pet displays a name, species, age group, size, shelter name, and compatibility tags.
- [ ] CT-02: Display complete pet profile bio and imagery
  - Action: View the body content of a pet's profile page.
  - Expected: The page displays at least one high-resolution pet photo and a descriptive adoption background story.