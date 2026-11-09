# Test Checklist

## Functionality
- [ ] FT-01: Dashboard loads with pre-existing smart home devices visible
  - Action: Open the admin dashboard.
  - Expected: A list/grid of devices is displayed, each showing device name, room, device type, and current status.
- [ ] FT-02: User can view devices grouped by room
  - Action: Select the "By Room" view option (e.g., a toggle or tab labeled "Room").
  - Expected: Devices are organized/filtered under room headings (e.g., "Living Room", "Bedroom") with each device appearing under its correct room.
- [ ] FT-03: User can view devices grouped by device type
  - Action: Select the "By Type" view option (e.g., a toggle or tab labeled "Device Type").
  - Expected: Devices are organized under type headings (e.g., "Lights", "Thermostats") with each device under its correct type.
- [ ] FT-04: User can adjust a light's brightness
  - Action: Open a light device's controls and move the brightness slider (or input) to a new value (e.g., 70%).
  - Expected: The light's brightness value updates to the new setting and remains displayed after the interaction.
- [ ] FT-05: User can adjust a thermostat's target temperature
  - Action: Open a thermostat's controls and set the target temperature to a new value (e.g., 22°C / 72°F).
  - Expected: The displayed target temperature updates to the newly set value.
- [ ] FT-06: User can create a schedule for a light
  - Action: Open the schedule creation UI, select a light device, pick a time (e.g., 08:00), choose a state change (e.g., turn ON), and save.
  - Expected: The schedule is created and appears in the schedules list with the device name, time, and action.
- [ ] FT-07: User can create a schedule for a thermostat
  - Action: Create a schedule selecting a thermostat, a time (e.g., 21:30), and a target temperature change (e.g., 20°C), then save.
  - Expected: The schedule is created and appears in the schedules list with device, time, and temperature action.
- [ ] FT-08: User can view recent device activity
  - Action: Open the "Recent Activity" section/panel.
  - Expected: A list of activity entries is shown, including device name, what happened (e.g., "Brightness set to 70%"), and when it occurred.
- [ ] FT-09: User can filter devices to show only offline devices
  - Action: Apply the status filter "Offline" from the status filter control.
  - Expected: Only devices with offline status are shown; all online/idle devices are hidden.
- [ ] FT-10: User can filter devices to show only idle devices
  - Action: Apply the status filter "Idle".
  - Expected: Only devices with idle status are shown; other devices are hidden.

## Constraint
- [ ] CS-01: Brightness input cannot accept values outside the valid range
  - Action: Attempt to set a light's brightness to 150% (or below 0%).
  - Expected: The value is clamped to 0–100% or rejected with a validation message; an out-of-range value is never saved/displayed.
- [ ] CS-02: Thermostat target temperature is limited to a valid range
  - Action: Attempt to set a target temperature outside the allowed range (e.g., 90°C).
  - Expected: The value is clamped or rejected with a validation message; the saved target stays within the valid range.
- [ ] CS-03: Schedule cannot be saved with missing required fields
  - Action: Open the schedule creation form and click "Save" without selecting a device and/or a time.
  - Expected: The schedule is not created; required-field validation messages are shown next to the empty fields.
- [ ] CS-04: Controls for offline devices cannot change their state
  - Action: Open an offline device and attempt to change its setting (e.g., move brightness slider or press a toggle).
  - Expected: The change is not applied; the device indicates it is unavailable (control disabled or an error/unavailable message shown).

## Interaction
- [ ] IX-01: Status filter updates the device list immediately
  - Action: Click a status filter option (e.g., "Offline").
  - Expected: The visible device list updates instantly without requiring a page reload, and the active filter is visually highlighted.
- [ ] IX-02: Switching between Room and Type views re-renders the device list
  - Action: Toggle from "By Room" to "By Type" view.
  - Expected: The same set of devices is displayed, re-organized by the newly selected grouping.
- [ ] IX-03: Saving a device setting shows visible confirmation feedback
  - Action: Change a device setting (e.g., brightness) and confirm/save.
  - Expected: A success indication (toast, message, or visual state change on the device card) confirms the setting was applied.

## Content
- [ ] CT-04: Activity entries include accurate timestamps
  - Action: Inspect entries in the Recent Activity list.
  - Expected: Each entry displays a readable timestamp (e.g., "Today 14:32" or a date/time) and corresponds to the stated device action; entries are ordered most recent first.
- [ ] CT-05: Each device displays a clear status label
  - Action: Inspect device cards/rows in the default view.
  - Expected: Every device shows a legible status indicator (Online / Offline / Idle) consistent with the filterable statuses.