# Test Checklist

## Functionality

- [ ] FT-01: New student can create an account and sign in
  - Action: Open the sign-up page, enter a valid name, email, and password, submit, then sign in with the same credentials.
  - Expected: Account is created, the user is signed in, and the app shows the signed-in home/dashboard with profile setup prompted or accessible.

- [ ] FT-02: Student can set up a profile with subjects, current level, and preferred study times
  - Action: Open profile setup, add at least one subject (e.g., Biology), select a current level (e.g., Beginner/Intermediate/Advanced), select a preferred study time, and save.
  - Expected: Profile saves successfully and the profile page displays the entered subjects, current level, and preferred study times.

- [ ] FT-03: Student can create a focused study group around a topic
  - Action: Go to the groups area, choose "Create Group", enter a topic name (e.g., Calculus), a description, and submit.
  - Expected: The new group is created and appears in the group list and in the creator's "My Groups"; the group page opens showing its shared space and discussion area.

- [ ] FT-04: Student can join an existing study group from the default group list
  - Action: From the groups directory, open a default group the user has not joined (e.g., Biology) and select "Join Group".
  - Expected: The user becomes a member; the group appears in "My Groups" and the join button changes to a member state (e.g., "Leave" or "Joined").

- [ ] FT-05: Members can organize notes, outlines, and reading summaries into labeled sections
  - Action: In a joined group's shared space, create a labeled section (e.g., "Exam Prep"), then add one note, one outline, and one reading summary into that section.
  - Expected: All three items appear inside the "Exam Prep" section, each with its title and content visible and grouped under that section label.

- [ ] FT-06: Members can post questions and answers in the group discussion area
  - Action: In the group discussion area, post a question; then open that question and post a reply/answer.
  - Expected: The question appears in the discussion list; opening it shows the posted answer under it, attributed to the member who replied.

- [ ] FT-07: Members can schedule an upcoming study session with the time selector
  - Action: In the group, open the scheduling/session area, pick a future date and time using the time selector, add a title, and confirm.
  - Expected: The session is created and appears in the group's "Upcoming Sessions" list with the chosen date, time, and title.

- [ ] FT-08: Members can mark themselves as available for proposed times
  - Action: In the scheduling view, mark yourself as available for at least one proposed time slot and save/confirm.
  - Expected: Your name is recorded as available for that slot and is shown in the availability display for that time slot.

- [ ] FT-09: Members can RSVP to a scheduled session and appear in the attendee list
  - Action: Open an existing upcoming session in a joined group and select "RSVP"/"Going".
  - Expected: Your name appears in the session's attendee list and the session shows you as attending to all viewers.

- [ ] FT-10: A user can mark their profile as a mentor
  - Action: Open profile settings, enable the "Mentor" option (e.g., "I am available as a mentor"), and save.
  - Expected: The profile displays a mentor indicator/badge and the user is identified as a mentor elsewhere in the app.

- [ ] FT-11: A group can invite a mentor and the mentor can accept and join with a mentor role
  - Action: From a group's members area, open "Invite Mentor", select a default user who is marked as a mentor, send the invite; then sign in as that mentor and accept the invite.
  - Expected: The mentor joins the group and is listed in the member list with a distinct mentor role label (different from regular member).

- [ ] FT-12: A mentor can pin important posts and highlight recommended resources in the group space
  - Action: Signed in as a mentor member of a group, pin an existing discussion post, and mark an existing resource/item in the shared space as a recommended resource.
  - Expected: The pinned post appears at the top of the discussion area with a "Pinned" indicator, and the resource appears with a "Recommended"/highlighted indicator visible to all members.

## Constraint

- [ ] CS-01: Profile cannot be saved with required profile fields empty
  - Action: Open profile setup, clear/leave subjects, current level, and preferred study times empty, and attempt to save.
  - Expected: Save is blocked; inline validation messages appear for each empty required field and the profile is not updated.

- [ ] CS-02: Only users marked as mentors are offered in the "Invite Mentor" list
  - Action: From a group, open the "Invite Mentor" picker/search and review the selectable users.
  - Expected: Every listed user is marked as a mentor; default users without the mentor flag are not selectable.

- [ ] CS-03: Non-mentor members cannot pin posts or highlight resources
  - Action: Sign in as a regular (non-mentor) member of a group and look for pin and highlight/recommend controls on a discussion post and a shared-space item.
  - Expected: Pin and highlight controls are not available to the regular member (hidden or disabled/rejected), so no post becomes pinned and no resource becomes highlighted.

- [ ] CS-04: A member cannot hold duplicate RSVPs for the same session
  - Action: RSVP "Going" to an upcoming session, then change the RSVP (e.g., to "Not Going" and back to "Going"), and check the attendee list.
  - Expected: The member appears only once in the attendee list and the latest RSVP state is the one displayed; no duplicate entries are created.

## Interaction

- [ ] IX-01: Selecting a proposed time slot reveals who marked themselves available
  - Action: In the scheduling view, click/select each proposed time slot that has availability.
  - Expected: The selected slot immediately displays the list/names of members who marked themselves available for that slot, without a page reload; slots with no availability show an empty state.

- [ ] IX-02: Mentor invite shows pending status and updates to a mentor role after acceptance
  - Action: Send a mentor invite from a group, view the invite/member area before acceptance, then accept as the mentor and refresh the view.
  - Expected: Before acceptance the invite shows a pending state; after acceptance the pending state clears and the member list shows the user with the mentor role label.

## Content

- [ ] CT-01: Group directory content is study-topic focused and relevant
  - Action: Browse the groups directory and open at least three default groups.
  - Expected: Groups are centered on study subjects (e.g., Calculus, Biology, Literature) with relevant titles and descriptions; no placeholder text (e.g., "lorem ipsum") or off-theme content is displayed.

- [ ] CT-02: Profile content matches the saved profile data and reflects mentor status
  - Action: Open a default user's profile and your own saved profile.
  - Expected: Displayed subjects, current level, and preferred study times match what was saved (accurate labels, no placeholder or mismatched values); profiles marked as mentors show a mentor badge/label, others do not.