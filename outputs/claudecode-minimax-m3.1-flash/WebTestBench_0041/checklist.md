# Test Checklist

## Functionality
- [ ] FT-01: Dashboard displays all default smart home devices
  - Action: Open the admin dashboard home page.
  - Expected: A device list/grid shows every default device with its name, room, device type, and status; no default device is missing.

- [ ] FT-02: Devices can be viewed by room
  - Action: Select a room (e.g., "Living Room") from the room filter/group control.
  - Expected: Only devices belonging to that room are shown; devices in other rooms are hidden.

- [ ] FT-03: Devices can be viewed by device type
  - Action: Select a device type (e.g., "Light", "Thermostat") from the device type filter/group control.
  - Expected: Only devices of the selected type are shown; devices of other types are hidden.

- [ ] FT-04: Light brightness can be adjusted
  - Action: Open a light device and set a new brightness value (e.g., 60%).
  - Expected: The device's brightness is updated and the new value is displayed on the device entry.

- [ ] FT-05: Thermostat target temperature can be adjusted
  - Action: Open a thermostat device and set a new target temperature (e.g., 22°C).
  - Expected: The thermostat's target temperature is updated and the new value is displayed on the device entry.

- [ ] FT-06: A schedule can be created for a light
  - Action: Open the schedule creation form, choose a light device, set a time, and define the light action (e.g., turn on / set brightness).
  - Expected: The schedule is created and appears in the schedules list identifying the light, time, and action.

- [ ] FT-07: A schedule can be created for a thermostat
  - Action: Open the schedule creation form, choose a thermostat device, set a time, and set a target temperature for that time.
  - Expected: The schedule is created and appears in the schedules list identifying the thermostat, time, and target temperature.

- [ ] FT-08: Recent activity shows when devices were last used
  - Action: Open the recent activity panel/tab.
  - Expected: Entries list a device name, the action that occurred, and a last-used timestamp for each recent activity record.

- [ ] FT-09: Devices can be filtered to show only offline devices
  - Action: Apply the status filter with "offline" selected.
  - Expected: Only devices whose status is offline are listed; online and idle devices are excluded.

- [ ] FT-10: Devices can be filtered to show only idle devices
  - Action: Apply the status filter with "idle" selected.
  - Expected: Only devices whose status is idle are listed; online and offline devices are excluded.

## Constraint
- [ ] CS-01: Schedule cannot be saved with required fields empty
  - Action: Open the schedule creation form, leave device/time/action blank, and attempt to save.
  - Expected: The schedule is not created and a clear validation error identifies the missing field(s).

- [ ] CS-02: Brightness cannot be set outside the valid range
  - Action: Attempt to set a light's brightness below the minimum (e.g., negative) and above the maximum (e.g., greater than 100).
  - Expected: The invalid value is rejected or clamped to the valid range, and an error message states the allowed range.

- [ ] CS-03: Target temperature cannot be set outside the valid range
  - Action: Attempt to set a thermostat's target temperature below the minimum (e.g., 5°C) and above the maximum (e.g., 40°C).
  - Expected: The invalid value is rejected or clamped to the valid range, and an error message states the allowed range.

- [ ] CS-04: Schedule action options match the selected device type
  - Action: Open the schedule form, select a light, and review the action options; then select a thermostat and review them again.
  - Expected: Light schedules offer light-specific actions (on/off, brightness) and thermostat schedules offer temperature-related actions; no irrelevant option is offered.

## Interaction
- [ ] IX-01: Selecting a device opens its detail/control view
  - Action: Click a device entry in the device list.
  - Expected: A detail view opens showing that device's controls (brightness for lights, target temperature for thermostats) and its current values.

- [ ] IX-02: Changing a filter immediately updates the displayed device set
  - Action: Select a room filter, then switch to a status filter (e.g., offline) without a page reload.
  - Expected: The device list updates to reflect the newly selected filter and shows only matching devices.

- [ ] IX-03: Saving a setting or schedule gives visible confirmation
  - Action: Save a brightness change, then create a schedule, observing the screen after each action.
  - Expected: A success confirmation (e.g., toast/message) appears after each successful save, and the new value or schedule is visible in the UI.

## Content
- [ ] CT-01: Device entries use correct and relevant labels
  - Action: Review the device list and open a device's detail view.
  - Expected: Each device shows a name, room, and type consistent with its purpose (e.g., a light is labeled as a light), with no placeholder, lorem-ipsum, or unrelated text.

- [ ] CT-02: Activity entries describe device actions with device names and timestamps
  - Action: Read each entry in the recent activity panel.
  - Expected: Every entry names the specific device, describes what happened (e.g., "turned on", "brightness changed"), and shows a last-used time; no entry is blank or generic.

- [ ] CT-03: Schedule entries clearly state device, time, and scheduled action
  - Action: Read each entry in the schedules list, including one created during FT-06 and FT-07.
  - Expected: Each entry states which device is scheduled, the time, and what state/value it will change to, with no missing or contradictory fields.