# Milestone Instructions

Table of Contents:
* [Introduction to the Project](#introduction-to-the-project)
* [General Milestone Instructions](#general-milestone-instructions)
* [The Issues Backlog](#the-issues-backlog)
* [Grading of Milestones](#grading-of-milestones)
* [Milestone 1](#milestone-1)
* [Milestone 2](#milestone-2)

## Introduction to the Project

The initial focus of your team project is to create a command-line utility that
allows people to organize their own personal diary.  Questions your team will want
to answer right away are:

1. What name should you give this command-line utility?
1. What arguments should drive its use?  That is, what is the command-line
interface for making and managing diary entries??

For example, if you gave your utility the incredibly boring name `diary`, you
might elect to have users write a diary entry like this:

```
diary log Today I had minestrone. It changed my life.
```

Or, possibly:

```
diary -l Today I had minestrone. It changed my life.
```

Or, even more simply:

```
diary Today I had minestrone. It changed my life.
```

This is just an example.  Again, you will determine what the command-line interface will look like, though over the course of the semester you will be restricted somewhat by the instructions for each milestone.

## General Milestone Instructions

The Project Manager (PM) for your first milestone will be the first person listed on the [team rosters](../teams.md).  The PM role will shift in round-robin fashion from there forward (i.e., the second person listed will be PM for milestone 2, the third will have milestone 3, etc.).  After the last person has served as PM, the rotation will start over with the first person serving as PM again.

All project issues, features, bugs, etc., will be described in separate GitHub Issues in your project's repository.  We will refer to this as your *backlog*.  Your PM will be responsible for adding these.  Some issues will come from individual milestone descriptions (see below).  Some may be entered by your instructor.  Some can come from your own creative ideas (e.g., "Wouldn't it be cool if we supported Feature X...?").

At the start of each milestone sprint, your team will have a stand-up meeting in your team's work location (to be assigned by the instructor).  Your PM will place the issues you will work on for the sprint into a GitHub Milestone.  Each issue will be assigned to no fewer than two developers.  The name of the acting PM should be specified in the milestone's description.

Coding work on an issue should be done in Git branches.  Branches should be merged through the creation of a Pull Request (PR).  One of the assigned developers should create the PR.  It is the responsibility of the PM to assign at least two reviewers to each PR.  There should be *substantive* discussion on each PR before the associated code is merged into the `main` branch.  A comment like "Looks good!" is only somewhat acceptable if the code is exceptionally bullet-proof and well-organized with respect to known design principles (e.g., coupling, cohesion, SOLID, etc.), and even then you should probably also comment on *why* the code looks exceptionally bullet-proof and well-organized.

All issues for the milestone should be closed by class time on the due date.  If for some reason an issue is not completed, the reason should be thoroughly documented via a comment on the GitHub Issue itself.

## The Issues Backlog

Over time, it is likely that you will have more issues in GitHub Issues than you have as part of your current milestone.  Issues are a great way to track not only needed code for features and bug fixes, but also needed design discussions (e.g., "Where should we store our diary entry information and what should the format look like?").

## Grading of Milestones

Milestones will be evaluated on the following criteria.

* How well you curate issues and group them into a milestone.
* How well you participate in evaluation of Pull Requests, and whether issues are closed using Pull Requests whenever the issue is resolved by merging code into the `main` branch.  Issues should be automatically closed by the closing of a PR provided you properly reference the issue number in the body of the PR (see ["Closing issues using keywords"](https://help.github.com/en/articles/closing-issues-using-keywords))
* How well you code.  Did you close issues, and to what degree is your code *reliable* and *maintainable*?  This includes the elimination of debugging code, junk files, etc.  Is your code easy to crash, or does it properly check inputs and preconditions?  Does your code comply with PEP8 (hint: use the `pycodestyle` tool or the `flake8` tool to check code for you)?

Starting with milestone 3, you will also be judged on the presence of unit tests and the test coverage of your code base.

Also, starting in a future milestone (to be determined), you will be judged on your design documentation.  You will be notified in that future milestone description when it is posted.

Finally, you will be judged based on your participation on the team for each milestone.  If it's clear an individual is not participating adequately, that individual's grade will be reduced.

## Milestone 1

*Stand-up: 9/21, Due: 9/28*

For this milestone, your primary focus is to do three things. Each of the three should reside in its own issue.

1. Give your diary program a "log an entry" subcommand that works.  You get to choose the name and syntax.  It should be clearly documented in your issue description and/or issue comments.
1. Give your diary program a "remove an entry" subcommand that works.  You get to choose the name and syntax.  It should be clearly documented in your issue description and/or issue comments.
1. Agree on where you will store the data your diary entries and the format of that data.  This should be documented in its own issue.  Note that this issue will not be closed by a PR since it is not resolved through code.  Your PM will close the issue manually.  However, you may want to finish this issue first through commentary as a team since the previous issues depend on it.

Separate developer pairs should work on each of the above.

After you have completed the above two things, you must update your project's
`README.md` file.  At a bare minimum, the `README.md` file must briefly describe
the project and then provide specific information on how to run your diary program
including examples.

## Milestone 2

*Stand-up: 9/28, Due: 10/5*

Prior to beginning this milestone, please consider the following reminders.

* The code in `main` should always be runnable code.  It should never produce errors (type errors, runtime errors, etc.).  This should be true not just at the end of each sprint/milestone, but throughout the entire life of the project.

* *All* code changes must be reviewed as part of a pull request.  If you create issues and fix them via code beyond the issues your instructor assigns, that code must still be reviewed as part of a pull request.  All code gets reviewed by other developers before it gets merged into `main`.  All PRs should automatically close one or more issues (again, see ["Closing issues using keywords"](https://help.github.com/en/articles/closing-issues-using-keywords)).

* Code should be reliable and maintainable. It should be reliable in that it is devoid of bugs.  It should be maintainable in the sense that it is organized in such a way that it anticipates the addition of future features.

With these considerations in mind, in this milestone you will complete the following.

1. Give your diary program a subcommand that lists the entries in the diary.  Each entry should be prefixed in some way with the date (day and time) that the entry was made. You get to choose the name and syntax.  It should be clearly documented in your issue description and/or issue comments.  For now, the subcommand should list *all* entries in the diary, and it must list the entries in *chronological order* from oldest to newest.  Each entry should be shown with enough information so that the user can easily determine how to remove one or more of them using the "remove an entry" subcommand you completed in [Milestone 1](#milestone-1).

1. Give your diary program a subcommand that provides statistics about the current diary including the dates of the first and last entries and how many total entries there are.

1. Ensure that your diary program still works if your data gets deleted.  In other words, if your data gets deleted or corrupted, the program should be able to detect that and then be able to "start over."  You may want to utilize one pair of programmers to try more aggressively breaking your program.

1. Update your `README.md` to include precise instructions on installing, developing, and running your code. One example of a GitHub repository with a fairly instructive README is [bvcompsci/cemetery-map](https://github.com/bvcompsci/cemetery-map).

1. Identify bugs introduced in [Milestone 1](#milestone-1), create issues for them (labeled 'bug'), and fix them.
