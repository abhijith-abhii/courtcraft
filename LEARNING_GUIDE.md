# CourtCraft — learning guide

## What it does

Compare basketball performance fairly. The intended user is sports analysts. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Compare raw points per 36 with shrunk points per 36. Increase minimum minutes and inspect how the rankings and intervals change. Export the complete result as JSON.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Normalize scoring per 36 minutes instead of ranking raw totals alone.
2. A Gamma-Poisson model shrinks small samples toward the global scoring rate.
3. Keep the prior exposure and uncertainty assumptions visible beside player rankings.

## Five interview questions

1. **Why use per-36-minute rates?** Raw totals depend on playing time. Rate normalization makes comparisons easier, but it does not adjust for role, opponents, pace or lineup quality.

2. **What problem does shrinkage solve?** A player with few minutes can have an extreme observed rate. A Gamma-Poisson model pulls low-exposure estimates toward a shared prior more strongly than high-exposure estimates.

3. **How should the uncertainty intervals be read?** They describe uncertainty under the count model and its assumptions. They do not include all contextual uncertainty about future basketball performance.

4. **What is true shooting percentage?** It relates points to field-goal attempts and an approximate free-throw possession adjustment. It measures scoring efficiency, not overall player value.

5. **Is this an analysis of a real league?** No. The 24-player dataset is synthetic. It supports transparent calculations and edge-case testing without claiming real player rankings.

## Independent exercise

Add per-game bootstrapped uncertainty and compare it with the Gamma-Poisson intervals.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented per-minute basketball comparisons and Gamma-Poisson shrinkage with uncertainty intervals on a transparent synthetic 24-player dataset.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
