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

1. **What problem does this project solve, and what is its unit of work?** Explain compare basketball performance fairly, identify sports analysts as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Normalize scoring per 36 minutes instead of ranking raw totals alone. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** A Gamma-Poisson model shrinks small samples toward the global scoring rate. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Keep the prior exposure and uncertainty assumptions visible beside player rankings. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Synthetic players and box scores. Constant-rate Poisson assumptions ignore pace, opponent quality, teammate effects and within-game dependence. True shooting uses the conventional approximate 0.44 free-throw coefficient. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add per-game bootstrapped uncertainty and compare it with the Gamma-Poisson intervals.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated compare basketball performance fairly using pandas · scipy · Flask, with possession normalization and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
