# Test Checklist

## Functionality
- [ ] FT-01: View all smart home devices grouped by room
  - Action: Open the dashboard and select the "By Room" grouping view.
  - Expected: Devices are listed under their assigned room headings (e.g., Living Room, Bedroom), each device showing its name and current state.
- [ ] FT-02: View all smart home devices grouped by device type
  - Action: Switch the grouping view to "By Device Type".
  - Expected: Devices are grouped under type headings (e.g., Lights, Thermostats, Sensors), each device showing its name and current state.
- [ ] FT-03: Adjust a light's brightness setting
  - Action: On a light device, change the brightness control and confirm the change.
  - Expected: The light's brightness updates to the selected value and the device detail reflects the new brightness.
- [ ] FT-04: Adjust a thermostat's target temperature
  - Action: On a thermostat device, change the target temperature and confirm the change.
  - Expected: The thermostat's target temperature updates to the selected value and the device detail reflects the new target.
- [ ] FT-05: Create a schedule for a light
  - Action: Open "Create Schedule", select a light, set a time and desired state (on/off), then save.
  - Expected: The schedule is saved and listed with the selected light, time, and action.
- [ ] FT-06: Create a schedule for a thermostat
  - Action: Open "Create Schedule", select a thermostat, set a time and target temperature, then save.
  - Expected: The schedule is saved and listed with the selected thermostat, time, and target temperature.
- [ ] FT-07: View recent activity / last-used time of devices
  - Action: Open the recent activity section of the dashboard.
  - Expected: A list of devices shows their last-used/state-change time, with the most recent activity visible.
- [ ] FT-08: Filter devices by "Offline" status
  - Action: Apply the status filter and select "Offline".
  - Expected: Only devices currently marked offline are displayed.
- [ ] FT-09: Filter devices by "Idle" status
  - Action: Apply the status filter and select "Idle".
  - Expected: Only devices currently marked idle are displayed.

## Constraint
- [ ] CS-01: Brightness input is bounded to a valid range
  - Action: Attempt to set brightness below 0% or above 100%.
  - Expected: The value is rejected or clamped to 0–100; no out-of-range brightness is applied or saved.
- [ ] CS-02: Target temperature input is bounded to a valid range
  - Action: Attempt to set a target temperature outside the allowed range (e.g., below the minimum or above the maximum).
  - Expected: The value is rejected or clamped to the allowed range; no out-of-range temperature is applied or saved.
- [ ] CS-03: Schedule cannot be saved with missing required fields
  - Action: Open "Create Schedule" and attempt to save without selecting a device, time, or action.
  - Expected: Save is blocked, an inline validation message identifies the missing field(s), and no schedule is created.
- [ ] CS-04: Status filter results contain only matching devices
  - Action: Apply the "Offline" filter, then the "Idle" filter.
  - Expected: The list never contains a device whose status does not match the active filter.
- [ ] CS-05: Devices that are offline cannot be controlled or scheduled into an active change
  - Action: Attempt to change brightness/temperature or create an active schedule on a device marked offline.
  - Expected: The control/schedule is blocked with a clear message that the device is offline.

## Interaction
- [ ] IX-01: Confirmation feedback after a settings change
  - Action: Adjust brightness on a light and confirm the change.
  - Expected: A success notification (e.g., toast/message) confirms the setting was applied.
- [ ] IX-02: Newly created schedule appears without page reload
  - Action: Create and save a schedule.
  - Expected: The schedule list updates immediately to include the new entry.
- [ ] IX-03: Device list updates dynamically when a status filter is applied or cleared
  - Action: Apply a status filter, then clear/reset it.
  - Expected: The device list refreshes to show only matching devices when filtered, and all devices when cleared.
- [ ] IX-04: Device cards provide visible hover/selection feedback
  - Action: Hover over and click a device card.
  - Expected: The card shows a visible hover state and a distinct selected/expanded state on click.

## Content
- [ ] CT-01: Device icons/images match their device type
  - Action: Inspect device cards and list entries across all device types.
  - Expected: Every icon/image is relevant to its device type (e.g., a bulb icon for lights, a thermostat icon for thermostats); no mismatched or placeholder imagery.
- [ ] CT-02: Status labels and last-used data are relevant and coherent
  - Action: Review the displayed status labels and recent-activity timestamps across devices.
  - Expected: Labels reflect the smart-home domain (e.g., Online, Offline, Idle, Active) and each device's last-used time is present and consistent with its activity entry.