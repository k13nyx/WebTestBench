# Test Checklist

## Functionality
- [ ] FT-01: Student can create an account with a valid name, email, and password
  - Action: Open the app, click "Sign up", enter a new email, a password, and confirm password, submit the form.
  - Expected: Account is created and the user is taken to an authenticated view (not a login page), with a profile setup prompt shown.

- [ ] FT-02: Student can set up a profile with subjects, current level, and preferred study times
  - Action: From the profile/setup page, add at least one subject (e.g. Calculus), set the current level selector, and select at least one preferred study time slot.
  - Expected: All three fields are saved and displayed on the user's profile page.

- [ ] FT-03: User can create a study group with a topic and description
  - Action: Click "Create Group", enter a group name (e.g. "Calculus Study Group"), pick a topic, add a description, and submit.
  - Expected: The new group appears in the groups list and opens to a group workspace with the creator listed as a member.

- [ ] FT-04: User can join an existing group
  - Action: Navigate to the group browse/search list, open a group (e.g. the biology or literature group), and click "Join".
  - Expected: The group is added to "My Groups" and the user's name appears in the group's member list.

- [ ] FT-05: Member can create a labeled section in the group's shared space
  - Action: Open a joined group's "Shared Space" tab, click "Add Section", name it (e.g. "Week 3 - Integration"), and save.
  - Expected: The new labeled section appears in the shared space and is empty and ready for entries.

- [ ] FT-06: Member can add content (note, outline, or reading summary) to a labeled section
  - Action: Open a section, select the entry type (Note / Outline / Reading Summary), enter content, and save.
  - Expected: The entry appears under the correct section with its type label visible, and the section's item count increases.

- [ ] FT-07: Member can post a question and another member can reply in the discussion area
  - Action: Open the group's "Discussion" tab, post a question, then post a reply under that question.
  - Expected: The question appears in the discussion thread list with its replies nested beneath it, and both are visible to all group members.

- [ ] FT-08: Member can schedule an upcoming group study session using the time selector
  - Action: Go to the group's "Sessions" tab, click "Schedule Session", pick a future date and time from the selector, add a topic/title, and save.
  - Expected: The session appears in the upcoming sessions list with the chosen date, time, and title.

- [ ] FT-09: Member can mark themselves available for a scheduled session and availability is visible to the group
  - Action: Open a scheduled session, click "Mark Available" (or the availability toggle), then view the session as another member of the same group.
  - Expected: The member is listed under "Available" for that session and is shown on the session detail/availability list for the other member.

- [ ] FT-10: Member can RSVP to a scheduled session and attendance is visible to the group
  - Action: Open a scheduled session, click "RSVP" (Yes/Going), then reopen the session from another group member's view.
  - Expected: The member's name appears in the session's attendee/RSVP list, distinguishing attending from not attending.

- [ ] FT-11: User can mark their profile as a mentor
  - Action: Go to profile settings and enable/toggle the "Mentor" status.
  - Expected: The profile displays a mentor badge/label, and the account is listed among mentors (e.g. a mentors directory or filter).

- [ ] FT-12: Group member can invite a mentor to join the group
  - Action: Open a group's members/invite area, choose "Invite Mentor", select a mentor from the list, and send the invitation.
  - Expected: The mentor receives a pending invitation visible in their own invitations, and the group shows the pending invitee.

- [ ] FT-13: Invited mentor joins the group with a distinct mentor role
  - Action: Sign in as the invited mentor, open the pending invitation, and accept it.
  - Expected: The mentor appears in the group's member list with a "Mentor" role tag distinct from regular member roles, and mentor-only actions become available to them.

- [ ] FT-14: Mentor can highlight a recommended resource in the group
  - Action: Sign in as the mentor member, open a post/resource in the group's shared space or discussion, and use the "Recommend"/"Highlight Resource" action.
  - Expected: The item is marked as recommended/highlighted with a visible mentor-recommended indicator.

- [ ] FT-15: Mentor can pin an important post in the group's space
  - Action: Sign in as the mentor member, open a post in the group space, click "Pin", and view the group's pinned section.
  - Expected: The post appears in the group's pinned area/list and shows a pinned indicator.

## Constraint
- [ ] CS-01: Signup is rejected when required fields are missing or the email/password is invalid
  - Action: Submit the signup form with a blank email, then with a malformed email, then with a password shorter than the minimum.
  - Expected: Each attempt is blocked with a visible validation error naming the offending field, and no account is created.

- [ ] CS-02: Duplicate email cannot create a second account
  - Action: Attempt to sign up with the email of an existing account.
  - Expected: Registration is rejected with an "email already in use" style message and no duplicate account is created.

- [ ] CS-03: A user must select subjects, a level, and at least one preferred study time before the profile is saved
  - Action: Attempt to save the profile with the subject list empty, then with no level selected, then with no study time selected.
  - Expected: Saving is blocked with a validation message each time, and the profile is not saved in an incomplete state.

- [ ] CS-04: Sessions cannot be scheduled in the past
  - Action: Open "Schedule Session" and attempt to select a date/time that has already passed, then attempt to submit one.
  - Expected: Past date/time options are disabled or rejected with a validation error, and no past-dated session is created.

- [ ] CS-05: A user cannot RSVP to or mark availability for a session in a group they do not belong to
  - Action: Sign in as a user who has not joined the group and attempt to open the group's session and RSVP/mark available.
  - Expected: The RSVP and availability actions are not available (or the session is inaccessible), and the group is unaffected.

- [ ] CS-06: Non-mentor members cannot pin posts or highlight recommended resources
  - Action: Sign in as a regular (non-mentor) member of the group and look for pin and highlight/recommend actions on a post or resource.
  - Expected: Those mentor-only controls are absent or disabled for the regular member, and clicking them produces no pinned/recommended state.

## Interaction
- [ ] IX-01: Creating a group, adding a section, and posting show a success confirmation
  - Action: Complete group creation, section creation, and a discussion post in sequence.
  - Expected: Each action is confirmed by a visible success message/toast, and the new item is visible in the list without a manual page refresh.

- [ ] IX-02: Availability and RSVP states update immediately for the acting user
  - Action: As a member, click "Mark Available" and then "RSVP" on a session.
  - Expected: The buttons/toggles switch to an active/selected state, and the availability and RSVP lists update in place to include the user.

- [ ] IX-03: Switching between Shared Space and Discussion tabs preserves and shows the group's content
  - Action: In a group, switch from "Shared Space" to "Discussion" and back again.
  - Expected: The corresponding panel is displayed each time with existing sections/entries and discussion threads intact.

- [ ] IX-04: Empty states prompt the user to act when a group has no sections, posts, or sessions
  - Action: Open a newly created group that has no sections, no discussion posts, and no scheduled sessions.
  - Expected: Each area shows a clear empty-state message with a call to action (e.g. "Add Section", "Post a Question", "Schedule Session").

## Content
- [ ] CT-01: Group and profile content is directly relevant to studying and the chosen topic
  - Action: Review the default data across groups (calculus, biology, literature), profiles, sections, discussion posts, and sessions.
  - Expected: Group names, topics, notes, outlines, reading summaries, and discussion content relate to those academic subjects; no unrelated placeholder or lorem-ipsum content is displayed.

- [ ] CT-02: Session entries display complete and correct details
  - Action: Open a scheduled session and inspect the displayed title, topic, date, time, and attendee/availability names.
  - Expected: All fields are populated (no blanks or "undefined"/raw placeholders), and the date/time matches the values that were selected when scheduling.

- [ ] CT-03: Mentor status, role, pins, and recommended resources are labeled in clear, consistent text
  - Action: View a mentor's profile, the group's member list, a pinned post, and a highlighted resource.
  - Expected: Each state is communicated with readable text labels (e.g. "Mentor", "Pinned", "Recommended") rather than unlabeled color-only or icon-only indicators.