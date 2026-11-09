# Test Checklist

## Functionality
- [ ] FT-01: A visitor can create a new student account
  - Action: Open the sign-up form, enter a unique email and password, and submit.
  - Expected: The account is created and the user is signed in, landing on the profile setup or home page.
- [ ] FT-02: A student can set up their profile with subjects, level, and preferred study times
  - Action: Open the profile settings, add subjects (e.g., "Calculus"), select a current level (e.g., "Intermediate"), set preferred study times (e.g., "Weekday evenings"), and save.
  - Expected: The profile page displays the saved subjects, level, and preferred study times.
- [ ] FT-03: A student can create a new study group around a topic
  - Action: Click the create-group option, enter a topic name (e.g., "Calculus"), and submit.
  - Expected: A new group page for "Calculus" is created and the creator is listed as a member.
- [ ] FT-04: A student can join an existing study group
  - Action: Open a default existing group (e.g., "Biology") and click the join option.
  - Expected: The student becomes a member of the group and gains access to its shared space and discussion.
- [ ] FT-05: A member can add content to a labeled section of the group's shared space
  - Action: In the group's shared space, select a section (e.g., "Reading Summaries"), add a note entry with a title, and save.
  - Expected: The new entry appears inside the "Reading Summaries" section of the shared space.
- [ ] FT-06: Members can ask and answer questions in the group discussion area
  - Action: Post a question (e.g., "How do I solve integrals by parts?") in the discussion area, then reply to it from another member's account.
  - Expected: The question appears in the discussion feed, and the reply is displayed under it.
- [ ] FT-07: A member can schedule an upcoming group study session
  - Action: Open the session scheduling form, pick a date and time with the time selector, and save.
  - Expected: The new session is listed under the group's upcoming sessions with the selected date and time.
- [ ] FT-08: A group member can RSVP to a scheduled session
  - Action: Open an upcoming session and select an RSVP response (e.g., "Attending").
  - Expected: The member's response is recorded and displayed in the session's attendee list.
- [ ] FT-09: A student can mark their profile as a mentor
  - Action: Open profile settings and enable the mentor option (e.g., a "I'm a mentor" toggle), then save.
  - Expected: The profile displays a mentor indicator/role.
- [ ] FT-10: A group can invite a mentor, and the mentor receives the mentor role in the group
  - Action: From a group page, send an invitation to a user whose profile is marked as mentor; accept the invitation from that mentor's account.
  - Expected: The mentor joins the group and is shown with the mentor role.

## Constraint
- [ ] CS-01: Account creation is blocked when required fields are empty
  - Action: Submit the sign-up form with an empty email or password.
  - Expected: No account is created and an error message identifies the missing required field.
- [ ] CS-02: A group cannot be created without a topic name
  - Action: Submit the create-group form with the topic/name field empty.
  - Expected: No group is created and an error message prompts for the topic name.
- [ ] CS-03: A study session cannot be scheduled without selecting a time
  - Action: Submit the session scheduling form without choosing a date/time in the time selector.
  - Expected: The session is not created and an error prompts the user to select a time.
- [ ] CS-04: Non-mentor members cannot pin posts or highlight recommended resources
  - Action: As a regular (non-mentor) group member, attempt to pin a discussion post or mark a resource as recommended.
  - Expected: The pin/highlight option is unavailable or blocked with a message indicating a mentor role is required; the post/resource is not pinned or highlighted.

## Interaction
- [ ] IX-01: The session time selector shows who has marked themselves as available
  - Action: Open the scheduling/time selector view after at least one member has marked availability for a time slot.
  - Expected: The availability display lists the names of members who marked themselves available for that time.
- [ ] IX-02: RSVP action gives immediate confirmation and updates attendance
  - Action: Select an RSVP response on an upcoming session.
  - Expected: A confirmation feedback (toast/label) appears, and the attendee list and count update to include the member.
- [ ] IX-03: A pinned post is visually distinguished in the group's space
  - Action: As a mentor, pin a post in the group's space, then reload the page.
  - Expected: The pinned post is shown at the top (or clearly marked with a "Pinned" indicator) of the group's space.

## Content
- [ ] CT-01: The group shared space provides the three labeled sections for study materials
  - Action: Open a group's shared space.
  - Expected: Sections labeled "Notes," "Outlines," and "Reading Summaries" (or equivalent clear labels) are present and display the entries filed under them.
- [ ] CT-02: Profile content correctly reflects the student's setup data
  - Action: View a profile after setup (subjects: "Biology," level: "Advanced," preferred time: "Weekend mornings").
  - Expected: All three data points are displayed accurately on the profile with no missing or mismatched values.
- [ ] CT-03: Mentor-highlighted resources are relevant to the group's topic
  - Action: As a mentor, highlight a recommended resource in a topic group (e.g., a calculus resource in the "Calculus" group), then view the group's resources list.
  - Expected: The highlighted resource appears under a "Recommended" area, is labeled as mentor-recommended, and matches the group's subject topic.