# Postmortem: Website Outage Incident

## Issue Summary:
Duration: April 12, 2024, 10:00 AM - April 12, 2024, 2:00 PM (GMT)
Impact: Our primary web application experienced intermittent downtime, with users reporting slow response times and 30% of our user base being affected.
Root Cause: A misconfiguration in our load balancer settings led to improper distribution of incoming traffic.

## Timeline:
•	10:00 AM: Issue detected through monitoring alerts indicating increased latency.
•	10:15 AM: Engineers noticed intermittent connection timeouts during routine checks.
•	10:30 AM: Assumed it could be a database overload due to recent feature release; investigated database performance.
•	11:00 AM: Misleading path taken: Focused on optimizing database queries and scaling up database resources.
•	12:00 PM: Issue escalated to the Infrastructure team as more alerts poured in.
•	1:30 PM: Resolved the incident by correcting load balancer settings and restarting affected services.

## Root Cause and Resolution:
Root Cause: The load balancer was misconfigured to route traffic inefficiently, causing some servers to be overloaded while others remained underutilized.
Resolution: Corrected load balancer configuration to evenly distribute traffic among servers and restarted services for changes to take effect.

## Corrective and Preventative Measures:
Improvements/Fixes: Implement better load balancing algorithms and enhance monitoring capabilities to catch such issues early.


## Tasks to Address the Issue:
•	Patch Load Balancer: Ensure it is configured with proper algorithms and settings.
•	Enhance Monitoring: Add alerts for abnormal traffic patterns and server health.
•	Documentation: Update documentation to include best practices for load balancer configurations.
•	Training: Conduct training sessions to educate the team on load balancer management and troubleshooting.

# SUMMARY:
On April 12th, our primary web application experienced intermittent downtime, affecting 30% of our users with slow response times. The root cause was identified as a misconfigured load balancer, which was not distributing traffic efficiently among our servers. Initially, we focused on optimizing our database due to a recent feature release, which turned out to be a misleading investigation path. The issue was eventually escalated to the Infrastructure team, who corrected the load balancer settings and restarted affected services, resolving the incident by 2:00 PM GMT.
Moving forward, we plan to implement better load balancing algorithms and enhance our monitoring capabilities to catch such issues early. Tasks to address this incident include patching the load balancer, enhancing monitoring with alerts for abnormal traffic patterns, updating documentation with best practices, and conducting training sessions for the team on load balancer management and troubleshooting.
