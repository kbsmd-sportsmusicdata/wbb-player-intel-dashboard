# Executive Summary: WBB Player Intel Dashboard

## Project Objective

This repo packages a publishable WBB Player Intel Dashboard that combines player profiles, role-based comparisons, percentile indicators, team roster mix, and coach-facing prompts in a single static dashboard.

The goal is to make player evaluation faster to scan, easier to compare, and more useful for basketball operations, scouting, player development, and portfolio review.

## Live Project

* **Dashboard:** https://kbsmd-sportsmusicdata.github.io/wbb-player-intel-dashboard/
* **GitHub Repo:** https://github.com/kbsmd-sportsmusicdata/wbb-player-intel-dashboard

## Intended Audience

* Player development and coaching staff
* Basketball operations and scouting reviewers
* Front office and roster construction decision makers
* Sports analytics portfolio reviewers

## Why This Project Matters

Player intel work is most valuable when it connects the numbers to basketball context. This dashboard turns a player dataset into a scouting style review surface by combining role labels, percentile signals, player comps, team context, and coach-facing prompts.

For a lean basketball operation, this type of tool can support first pass player evaluation, opponent prep, tryout review, roster tracking, and player development conversations without requiring a full internal analytics department.

## Key Questions

* Which 2025-26 players share similar role-based profiles?
* How do percentile, role, and derived metric layers translate into player intel?
* Which players stand out by role, team context, or comparable player profile?
* How can coach-facing prompts support faster scouting and development review?

## Decision Support Value

This project works as a first pass intelligence layer for evaluating players across a broad WBB universe. Instead of forcing reviewers to interpret raw stats in isolation, the dashboard organizes player information into role identity, comp logic, percentile context, and coaching implications.

The dashboard is useful for:

* Quickly identifying player archetypes
* Comparing similar players by role profile
* Reviewing team roster mix
* Translating metrics into coach-facing questions
* Building scouting or player development shortlists
* Creating a reusable template for future player intel tools

## Top Takeaways

1. **The dashboard is strongest as a scouting triage tool.** It helps reviewers quickly narrow a broad player pool into role based groups, comparable profiles, and players worth deeper review.

2. **Role labels and comps make the data easier to interpret.** Instead of presenting metrics as disconnected numbers, the dashboard translates player data into basketball facing profiles.

3. **Percentile indicators add useful context.** They help show where a player stands out relative to the dashboard universe without requiring the reviewer to manually benchmark every metric.

4. **Team roster mix adds another layer of interpretation.** Player evaluation becomes more useful when individual profiles are connected to team context, role availability, and roster construction.

5. **Coach-facing prompts make the dashboard more practical.** The embedded questions help bridge the gap between analytics output and real basketball conversations.

## Recommended Use Cases

* Player evaluation
* Role-based comparison
* Team roster mix review
* Coach-facing scouting prep
* Tryout or player pool review
* Player development conversations
* Portfolio demonstration of basketball analytics workflow

## Limitations

* The dashboard should be treated as a first pass review tool, not a final scouting grade.
* Public or static data may not fully capture film context, defensive assignments, injuries, lineup roles, or coaching intent.
* Percentiles and comps depend on the dashboard universe and available data fields.
* Remote presentation assets may rely on Google Fonts, Chart.js CDN files, and externally hosted logos or headshots.
* The team intel and coach Q&A views are embedded inside the dashboard rather than exposed as separate public tables in this first publish pass.

## Future Extensions

* Add a one-page player intel brief for scouting or player development review.
* Add a short role taxonomy guide explaining each player archetype.
* Add a lightweight user guide for coaches or front office reviewers.
* Expand the comp layer with clearer role family explanations.
