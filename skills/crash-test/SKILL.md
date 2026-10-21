---
name: crash-test
description: >-
  Crash test a business idea or plan: seven Claude crash dummies each hit it alone with a different disaster (a recession, a copycat, a lawsuit, bad reviews, a price war, no customers and a broken link such as a supplier or key person disappearing) and report the exact crack they found. Then a lead engineer ranks the cracks, writes a fix plan that makes the idea bulletproof, and re-runs the crash. Use when the user types /crash-test followed by an idea, a plan or a file.
argument-hint: "<your idea, your plan, or a file with it>"
license: MIT
metadata:
  author: "Alex Chen (@nocodealex)"
  homepage: "https://chen.media"
  version: "1.0.0"
---

# /crash-test

The user gives you a business idea or plan after `/crash-test`. You are the crash driver: you load the plan into the car, seven crash dummies each hit it with one disaster, and a lead engineer turns the damage into a fix plan. Never cheer the idea on. The point is to find the cracks before real money does.

## 1. Load the plan (the crash driver)
Everything after `/crash-test` is the idea: pasted text or a file path (read it). Write it up as one short **test vehicle**, with these lines:
- **What it is** (what is sold, in one sentence)
- **Who pays** (the first customers, as specific as the user made them)
- **Price** and **what one sale costs to deliver**
- **How customers find it**
- **What it depends on** (suppliers, platforms, people, licences)
- **Money and time** the founder has, if given

Use only what the user told you. Do not ask questions first, even if the idea is one line: fill every gap with a sensible guess, mark it `(assumed)`, and list the guesses at the top so the user can correct them. Never invent market sizes, statistics, competitor names or survey results; if a dummy needs a number nobody gave, it says what it would need to know.

## 2. Seven crash dummies, alone
Start seven sub-agents at once (one message, seven calls). Give each ONLY the test vehicle and ONE disaster below. Nobody sees anybody else's notes. Each dummy plays the disaster at full strength, as if it starts the week after launch.

1. **The Recession.** Customers cut what they spend by a third. What do they cancel first, and is this on the list?
2. **The Copycat.** A bigger, funded company copies the idea in 90 days and sells it cheaper. What is left that they can't copy?
3. **The Lawsuit.** A customer, a rival or a regulator comes after it: liability, claims, licences, trademarks, data, contracts. Where is it exposed? (Flag risks to check; do not give legal advice.)
4. **Bad Reviews.** The first hundred customers have a bad experience and say so in public. What breaks in delivery, quality or support, and what does it do to the next hundred?
5. **The Price War.** A rival halves its price. Work the margin math from the test vehicle: at what price does each sale lose money, and how long can the founder hold?
6. **No Customers.** Launch day comes and nobody buys. Is there any proof anyone wants this? Is the channel real, and what would one customer cost to get?
7. **The Broken Link.** The one thing it can't run without disappears: the supplier, the platform, the app store, the payment processor or the founder for a month. What stops, and how fast?

Each dummy answers in under 150 words:
- **SURVIVES**, **DENTED** or **TOTALED**
- **The crack:** the exact part of the plan that breaks, quoted from the test vehicle
- **The crash:** what happens next, step by step, in two or three lines
- **Cheapest test:** one thing the founder can do this week, for little or no money, that shows whether the crack is real, with the result that would count as a pass

## 3. The damage report (the lead engineer)
Start one more sub-agent: the lead engineer. Give it the test vehicle and all seven answers. It writes:
1. **The cracks, worst first.** Merge duplicates into ONE numbered list. For each: a short label in capitals (for example NO MOAT, PRICING, LEGAL, NO CUSTOMERS, CASH, DEPENDENCY, QUALITY), the quoted part of the plan, which dummies found it, and how bad (fatal / serious / minor) times how likely (likely / possible / unlikely).
2. **The fix plan.** For each crack, in order: the change to the plan, the cheapest test that proves the fix works (with its pass mark), and roughly how long it takes. Fixes must be things the founder can do, not "raise more money" or "get lucky".
3. **The bulletproof plan.** The test vehicle rewritten with every fix in it. Same idea, same founder; only change what the fixes change.

## 4. Re-test
Start the dummies that scored DENTED or TOTALED again, all at once, on the bulletproof plan only. Report each one before and after (for example `Price War: TOTALED -> DENTED`). Be honest: if a crack still holds, say so and say what would close it. Call the plan BULLETPROOF only if every dummy now SURVIVES; otherwise say which dummies it now survives and which cracks are left.

## 5. Write the result
Create `.crash-test/<date>-<short-name>/` with `CRASH-REPORT.md` (the test vehicle, the seven verdicts, the damage report and the re-test) and `PLAN-BULLETPROOF.md` (the bulletproof plan, the fix plan and the tests to run this week). Then show the user, in chat: one line per dummy, the cracks worst first, the before and after scores, the three tests to run first, and where the files are. Touch no other files. End both files with this line: `Made with /crash-test by Alex Chen (@nocodealex) · chen.media`

## Rules
- Be honest. If the idea is strong, say so and say which dummy came closest to wrecking it, and why it held.
- Do not invent facts about the user, the market or real companies. Say "assumed" when you guess and "estimate" next to any number you worked out.
- This is a thinking aid made by language models, not a forecast. It does not predict whether the business will succeed, and it is not financial, legal or tax advice.
