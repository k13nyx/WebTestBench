# Test Result

## Functionality
- [X] FT-01: View devices grouped/filtered by room
  - Action: Select a room (e.g., "Living Room") from the room view option
  - Expected: The device list shows only devices assigned to that room
  - Actual: Clicking the "Living Room" room filter changed the count to "Showing 5 of 20 devices" and the list contained only Main Ceiling Light, Floor Lamp, Smart Thermostat, Living Room Speaker, Motion Sensor — all "living room".

- [X] FT-02: View devices grouped/filtered by device type
  - Action: Select a device type (e.g., "Lights" or "Thermostats") from the type view option
  - Expected: The device list shows only devices of the selected type
  - Actual: With "All Rooms" reset and "Lights" selected, "Showing 9 of 20 devices" was displayed and all 9 entries were light devices (Main Ceiling Light, Floor Lamp, Bedroom Light, Bedside Lamp, Kitchen Light, Under Cabinet Lights, Bathroom Light, Desk Lamp, Garage Light).

- [X] FT-03: Adjust light brightness
  - Action: Open a light device's settings and change the brightness to a new value (e.g., 75%)
  - Expected: The brightness setting is saved and the device card reflects the new value
  - Actual: Brightness control is inline on the device card (no separate settings dialog). Changed Desk Lamp from 85% → 75%; the card displayed "Brightness 75%" and the slider aria-valuenow="75". Value persisted across filter changes.

- [X] FT-04: Adjust thermostat target temperature
  - Action: Open a thermostat's settings and change the target temperature to a new value (e.g., 22°C)
  - Expected: The target temperature is saved and the device card reflects the new value
  - Actual: App uses °F. Changed Smart Thermostat target from 70°F → 75°F; the card displayed "Target 75°F" (Current 72°F), and the value persisted.

- [X] FT-05: Create a schedule for a light
  - Action: Create a schedule selecting a light device, a time, and a target state (e.g., On at 18:00)
  - Expected: The schedule is created and appears in the schedules list with the correct device, time, and state
  - Actual: Created schedule "Floor Lamp / Turn on / 18:00 / Mon, Wed"; Active Schedules went from (4) to (5) and the entry appears in the list with correct device, time and state.

- [X] FT-06: Create a schedule for a thermostat
  - Action: Create a schedule selecting a thermostat, a time, and a target temperature/state
  - Expected: The schedule is created and appears in the schedules list with the correct details
  - Actual: Created "Smart Thermostat / Set to 72°F / 07:30 / Tue, Fri"; Active Schedules went from (5) to (6) and the entry is listed with correct details.

- [X] FT-07: View recent activity
  - Action: Navigate to the recent activity section
  - Expected: A list of recent device events is displayed (e.g., which device was used and when)
  - Actual: /activity shows "Activity Log — Showing 6 recent activities" with entries (Main Ceiling Light – Turned on – 8 minutes ago, Smart Thermostat, Smart Lock, Bedroom Speaker, Kitchen Camera, Garage Light).

- [X] FT-08: Filter devices by status "Offline"
  - Action: Apply the "Offline" status filter
  - Expected: Only devices with offline status are shown in the device list
  - Actual: "Showing 2 of 20 devices" — Bedroom Speaker and Garage Light, both labeled "offline".

- [X] FT-09: Filter devices by status "Idle"
  - Action: Apply the "Idle" status filter
  - Expected: Only devices with idle status are shown in the device list
  - Actual: "Showing 2 of 20 devices" — Living Room Speaker and Exhaust Fan, both labeled "idle".

## Constraint
- [ ] CS-01: Schedule form cannot be submitted with missing required fields
  - Action: Attempt to save a schedule without selecting a device, time, or target state
  - Expected: The schedule is not created and a validation error identifies the missing field(s)
  - Bug Report:
    - Issue: Missing validation feedback on schedule form
    - Actual: Clicking "Create Schedule" with all fields empty does not create the schedule (Active Schedules stays at 4), but no validation error is displayed — no error/alert nodes, no aria-invalid, no field messages, no form `required` attributes (form has no validation UI at all). The same silent no-op occurred when device/action/time were filled but no day was checked; the requirement was only discoverable by trial and error.

- [X] CS-02: Brightness cannot be set outside its valid range
  - Action: Attempt to set brightness below 0% or above 100%
  - Expected: The value is rejected or clamped to the valid range; invalid input is not saved
  - Actual: Slider bounds aria-valuemin=0, aria-valuemax=100. Excessive incrementing clamped at "100%" and excessive decrementing clamped at "0%"; no out-of-range value was ever shown or saved.

- [X] CS-03: Target temperature cannot be set outside its valid range
  - Action: Attempt to set a target temperature outside the allowed range (e.g., below minimum or above maximum)
  - Expected: The value is rejected or clamped to the valid range; invalid input is not saved
  - Actual: Thermostat slider bounds aria-valuemin=60, aria-valuemax=85. Attempts below/above clamped to "60°F" and "85°F"; no out-of-range temperature displayed or persisted.

- [X] CS-04: Status filter shows only matching devices
  - Action: With the "Offline" filter active, inspect the returned device list
  - Expected: No device with a non-offline status (e.g., online, idle) appears in the list
  - Actual: Offline filter returned exactly Bedroom Speaker and Garage Light, both carrying the "offline" badge; no online/idle device present.

## Interaction
- [X] IX-01: Device list updates immediately when a filter or view option is changed
  - Action: Switch between room view, type view, or a status filter
  - Expected: The device list refreshes right away to reflect the selection without requiring a manual reload
  - Actual: Each button click updated the list within the same tick — "Showing 20 → 5 of 20" (Living Room), → "9 of 20" (Lights), → "2 of 20" (Offline), → "2 of 20" (Idle), with no page reload.

- [ ] IX-02: Confirmation feedback after saving a device setting
  - Action: Change a device setting (brightness or temperature) and save
  - Expected: A visible success confirmation (toast or message) appears indicating the setting was saved
  - Bug Report:
    - Issue: No success confirmation after saving a device setting
    - Actual: After changing Desk Lamp brightness (85%→75%) and Smart Thermostat target (70°F→75°F), DOM polling for 2+ seconds found no `[data-sonner-toaster]`, no `[role="status"]`/`[role="alert"]`/toast elements, and no "saved/updated" text anywhere. The app's "Notifications (F8)" region remains permanently empty (even power toggles produce no confirmation).

- [ ] IX-03: Confirmation feedback after creating a schedule
  - Action: Submit a valid new schedule
  - Expected: A visible success confirmation appears and the new schedule is shown in the list
  - Bug Report:
    - Issue: Missing success confirmation after schedule creation
    - Actual: The new schedule does appear in the list (Floor Lamp 18:00; Smart Thermostat 07:30) and the dialog closes, but no toast/message/role=status confirmation element was rendered at any point during a 1-second post-submit poll (toaster node never mounted).

## Content
- [X] CT-01: Recent activity entries include device name and timestamp
  - Action: Open the recent activity section
  - Expected: Each entry clearly shows which device was used and the time of last use
  - Actual: Every entry shows device + event + time, e.g. "Main Ceiling Light / Turned on / 8 minutes ago", "Smart Lock / Locked remotely / about 1 hour ago", "Garage Light / Connection lost / 1 day ago".

- [X] CT-02: Device status labels are accurate and consistent
  - Action: Inspect device cards/list against their status filter results
  - Expected: Each device displays a status label (e.g., Online, Idle, Offline) that matches its actual state
  - Actual: Each card carries a status badge (online/idle/offline); Offline filter returned only badges reading "offline", Idle filter only badges reading "idle", matching Dashboard stats (Offline: 2). Labels are consistent between card display and filter results.

- [X] CT-03: Schedule entries display correct device, time, and action details
  - Action: Open the schedules list and inspect an existing schedule
  - Expected: Each schedule shows the target device name, scheduled time, and the state/temperature it will apply
  - Actual: Each row shows all three, e.g. "Main Ceiling Light / Turn off / 23:00", "Smart Thermostat / Set to 68°F / 22:00", "Bedroom Light / Turn on at 20% / 06:30", plus recurrence days.

---
**Summary:** 15 PASS, 3 FAIL (CS-01 missing form validation messages, IX-02 no save confirmation, IX-03 no creation confirmation). Tool calls used: ~35 / 100.