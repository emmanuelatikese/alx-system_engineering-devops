#### The Port 80 Debacle
### Summary about the incident
![frs](https://github.com/emmanuelatikese/alx-system_engineering-devops/assets/104688960/ec8185c6-9388-46b6-b183-5a254a5be320)
## Issue Summary
## Duration: From April 13, 2024, 10:00 PM (UTC+0) to April 14, 2024, 2:30 AM (UTC+0).
## Impact:
* Service Down: Our primary web service was inaccessible due to the port 80 failure.
* User Experience: Users encountered timeouts, failed requests, and frustration.
## Timeline
* 10:00 PM: Port 80 issue detected.
* 11:00 PM: Investigated Nginx settings.
* 2:30 AM: Fixed reverse proxy config.
## Root Cause and Resolution
 Cause: A misconfigured reverse proxy (Nginx) was blocking traffic on port 80.
Specifically, a recent deployment introduced conflicting rules.
*Resolution:
Corrected Nginx configuration, allowing traffic through.

## Improvements:
Documentation: Detailed Nginx configuration guidelines.
Testing: Rigorous testing of deployments before production rollout.
Redundancy: Set up a secondary port 80 proxy for failover.


