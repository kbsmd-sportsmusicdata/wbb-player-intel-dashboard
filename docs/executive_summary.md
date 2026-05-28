# Executive Summary: WBB Player Intel Dashboard

## Project Objective

This repo packages a publishable WBB player-intel dashboard that combines player profiles, role-based comps, team roster mix, and coach-facing prompts in a single portable HTML artifact.

## Intended Audience


- sports analytics portfolio reviewers

- coaching staffs and scouting groups

- front office and roster-construction decision-makers


## Key Questions


- Which 2025-26 players share the strongest role-based comp profiles across the dashboard universe?

- How do percentile, role, and derived-metric layers translate into coach-facing player intel?

- How can team roster mix and embedded coach Q&A surfaces support faster scouting review?


## Decision-Support Value

This project turns a strong scouting dashboard into a portable review asset. For coaching staffs, scouts, and roster-build readers, it surfaces role identity, comp logic, team-mix context, and coach-facing prompts quickly enough to support triage and comparison work.

## Top Findings


1. The approved HTML artifact is already largely self-contained, with the player, team, comp, and coaching layers embedded directly into the page.

2. A slim exact-source JSON bundle is enough to document the player, comp, and coaching evidence without shipping the full upstream workspace or the heavy game-log JSON.

3. Visible CSV derivatives were intentionally left out of the canonical evidence bundle because their taxonomy drifts from the dashboard's six-role presentation.


## Recommended Use Cases


- player evaluation

- role-based comparison

- team roster-mix review

- coach-facing scouting prep


## Limitations


- This repo ships a static dashboard and a slim exact-source evidence bundle, not the full upstream build workspace.

- Remote presentation assets still rely on Google Fonts, Chart.js CDN, and ESPN-hosted logos/headshots.

- The team-intel and coach-Q&A views are embedded inside the HTML artifact rather than exposed as separate public tables in this first publish pass.

- Visible CSV derivatives from the source folder were intentionally excluded because their taxonomy does not cleanly match the shipped dashboard.
