# Test Checklist

## Functionality
- [ ] FT-01: New student can create an account
  - Action: Open the Sign Up page, enter a valid name, email, and password, and click "Sign Up".
  - Expected: Account is created, user is logged in, and is redirected to the dashboard/profile page.

- [ ] FT-02: Student can set up a study profile
  - Action: On the profile page, add subjects (e.g., "Calculus", "Biology"), select a current level, and set preferred study times; click "Save".
  - Expected: Profile is saved and the entered subjects, level, and preferred study times are shown on the profile.

- [ ] FT-03: Student can create a study group
  - Action: Click "Create Group", enter a group name and topic (e.g., "Literature"), and submit the form.
  - Expected: New group appears in the group list with the entered name/topic and the creator is listed as a member.

- [ ] FT-04: Student can join an existing study group
  - Action: Open a default group (e.g., the "Calculus" group) and click "Join Group".
  - Expected: User is added to the group's member list and can access its shared space and discussion area.

- [ ] FT-05: Member can add a note into a labeled section
  - Action: In a default group's shared space, click "Add Note", choose a labeled section, enter note content, and save.
  - Expected: Note appears filed under the chosen labeled section alongside other notes/outlines/summaries.

- [ ] FT-06: Members can ask and answer questions in the discussion area
  - Action: In a default group's discussion area, post a question, then post a reply as another group member.
  - Expected: Question and reply appear as a running Q&A thread visible to all group members.

- [ ] FT-07: Member can schedule a study session showing availability
  - Action: As one member, mark yourself as available for a time slot; as another member, click "Schedule Session", pick the date/time with the time selector, and save.
  - Expected: Time selector indicates which members marked themselves as available for that time; session is listed under upcoming sessions.

- [ ] FT-08: Member can RSVP to a scheduled session
  - Action: Open a default upcoming session and click "RSVP"/"Going".
  - Expected: RSVP is recorded and the user's name appears in the session's attendee list ("who plans to attend").

- [ ] FT-09: Advanced student can mark their profile as mentor
  - Action: On your own profile, enable the "Mentor" toggle and save.
  - Expected: Profile is updated to mentor status and the user is now discoverable/selectable as a mentor.

- [ ] FT-10: Group can invite a mentor to join
  - Action: As a group member, open "Invite Members", select a default mentor from the mentor list, send the invite, and accept it as that mentor.
  - Expected: Mentor is added to the group's member list.

- [ ] FT-11: Mentor can highlight resources and pin posts
  - Action: As the group's mentor, click "Highlight as Recommended" on a note in the shared space and "Pin" on a discussion post.
  - Expected: The note is marked as a recommended resource and the post appears pinned at the top of the discussion area.

## Constraint
- [ ] CS-01: Sign-up requires all mandatory fields
  - Action: On the Sign Up page, leave name/email/password empty and click "Sign Up".
  - Expected: No account is created; validation messages identify each missing required field.

- [ ] CS-02: Group creation requires required fields
  - Action: Open "Create Group" with an empty name/topic and submit.
  - Expected: Group is not created; an error message requires the missing information.

- [ ] CS-03: Pin and highlight actions are restricted to the mentor role
  - Action: As a regular (non-mentor) member, view notes and discussion posts in a default group and look for "Pin" / "Highlight as Recommended" actions.
  - Expected: These controls are unavailable (hidden or disabled) to regular members.

- [ ] CS-04: RSVP state stays consistent
  - Action: RSVP to a default session, then toggle RSVP off and on again.
  - Expected: Attendee list always lists the user exactly once; toggling off removes the name entirely.

## Interaction
- [ ] IX-01: Success feedback after account and profile actions
  - Action: Complete the sign-up (FT-01) and save the profile (FT-02).
  - Expected: A success message/toast (e.g., "Account created", "Profile saved") appears after each action.

- [ ] IX-02: RSVP updates are visible to all group members
  - Action: RSVP to a default session in one account, then open the same session page as another group member.
  - Expected: The attendee list reflects the new RSVP so everyone knows who plans to attend.

## Content
- [ ] CT-01: Default groups are organized around study topics
  - Action: Browse the default group list.
  - Expected: Every group's name, topic, and labels correspond to a study subject (e.g., calculus, biology, literature); no irrelevant groups.

- [ ] CT-02: Group content matches the group's subject
  - Action: Open a default group (e.g., the "Literature" group) and review its labeled sections, notes, and discussion posts.
  - Expected: All notes/outlines/reading summaries and Q&A posts are relevant to that group's subject.

- [ ] CT-03: Mentor role is visibly labeled
  - Action: View a default mentor's profile and a group member list containing that mentor (after FT-10).
  - Expected: A "Mentor" badge/label appears in both places, clearly distinguishing them from regular members.