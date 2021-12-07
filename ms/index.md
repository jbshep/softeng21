# Milestone Instructions

Table of Contents:
* [Introduction to the Project](#introduction-to-the-project)
* [General Milestone Instructions](#general-milestone-instructions)
* [The Issues Backlog](#the-issues-backlog)
* [Grading of Milestones](#grading-of-milestones)
* [Milestone 1](#milestone-1)
* [Milestone 2](#milestone-2)
* [Milestone 3](#milestone-3)
* [Milestone 4 - the Rendezvous](#milestone-4)
* [Milestone 5](#milestone-5)
* [Milestone 6](#milestone-6)

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

## Milestone 3

*Stand-up: 10/12, Due: 10/28*

There are two major thematic activities in this milestone.  The first is supporting the presence of multiple diaries into which users may log their entries.  The second is the introduction of unit tests that will persist for the remainder of the project.

Your program should have an "active" diary at all times.  Your program should have a default diary, and its name should be `default`.  When users log a diary entry, it should log that entry to the "active" diary.  When users remove entries or list entries, those subcommands should only refer to the "active" diary.

With this in mind, complete the following.


1. Create a `switch` subcommand that switches from one active diary to another active diary given the required argument of the diary's name.  If a diary of that name does not exist, this command should create the new diary.

1. Create a `wipe` subcommand.  `wipe` deletes a diary without creating a new one in its place, unless the user "wipes" the `default` diary.  "Wiping" the `default` diary should recreate it as an empty diary since `default` must always exist.  `wipe` should have an optional argument, which is the name of the diary.  Without the argument, `wipe` deletes the `default` diary.  Thus, `diary wipe` is be synonymous with `diary wipe default`.  If the user wipes the active diary, the active diary should be automatically switched back to the default diary.

1. In [Milestone 2](#milestone-2), you gave your diary program a subcommand that provided statistics about the current diary including the dates of the first and last entries and how many total entries there are.  In Milestone 3, you will enhance this command to show all available diaries and their statistics, along with some indicator (like an asterisk) that shows which diary is the "active" diary.

1. Implement *unit tests* using `pytest` as we did in class.  Cumulatively, your tests should run as much of your project code as possible.  You will want to clearly separate your code into two subfolders: one for your project code itself, and one for testing (name your testing folder `tests`).  Your tests must be *isolated*.  This means that the tests should run in their own environment and should not affect or pollute any pre-existing diary data that you have tracked.

1. Create a StarUML class diagram of your classes, and place the `.mdj` file into a folder named `doc`.  Use the class diagram to refactor your code and make it more object-oriented.  This will ultimately make your code easier to test.

1. Keep your `README.md` file up to date (do this always!). One thing to think about is whether moving your project code to a separate folder requires you to modify how you are now running the program (e.g., `python -m diary log I had a good day`).

1. Identify bugs introduced in [Milestone 2](#milestone-2), if any.  Create issues for them (labeled 'bug') and fix them.

## Milestone 4                                                                        

*Stand-up: 10/28, Due: 11/23*

This is the *Rendezvous* milestone. Beginning with this milestone, we have our [new merged teams](../teams-rend.md).  The major overarching activity of the Rendezvous milestone is transforming our single-user personal diary software into multi-user (yet still command-line) blog-like software.  This software shall henceforth be named `blurg`.

Rather than merging our code, we will only merge teams.  This will allow each team to start from a common starting point.  Your team's GitHub repository is of the form https://github.com/jbshep/blurg-TEAM where `TEAM` is one of `huarizo`, `liger`, or `mule`.

The new starting code base stores all local information in a filesystem rather than a database.  We will use this approach since it is consistent with the prerequisites of the course (i.e., CMSC 321 is *not* a prerequisite for CMSC 360).  Your instructor will describe in detail during class how this code base stores local diaries (e.g. a configuration file named `config` and `.blurg` directory and its subdirectories).

A diary may now have one or more users that can log diary entries, and a diary will either be local or remote.  A local diary will store all of its entry log data locally in the filesystem.  The client program that you have been developing will continue to work in much they same way it does now.  A remote diary will be accessible through a Web server interface.  That is, your client program will "talk to" the Web server, and the Web server application will be responsible for logging remote diary entries.

The Web server interface has been programmed mostly by your instructor.  It can be found in `blurg/server/__main__.py` and it can be run using the command `./run-server.sh`. We will discuss *at length* the interfaces present in the Web server such that one does not need to understand how to build Web applications in order to interface with it.

A local diary will have one user (a "default" user).  A remote diary will have one or more users.  With respect to remote diaries, one user will create a remote diary.  This process will generate a "secret key" for the diary.  The user diary creator may share this diary key with other users so that they can "join" the diary and log their own entries.

When a users create a diary, they choose their own username for the diary (see requirements below).  Thus, a user could have different usernames for different remote diaries, or they could reuse the same username.

When a user connects to an existing remote diary (that is, the creating user has given them the diary key), they also get to choose a username.

Thus, a diary now tracks not just log entries, but also log entries for a particular user.  For example, jbshep's log entries for the remote diary `softeng` would be different from jbshepspam's log entries for the remote diary `softeng`.

The features/tasks to be implemented in this milestone are as follows.

1. Test-first: One of your first commits for this milestone should be the `pytest` tests you need for implementing all other features in this milestone.  Your instructor has created *some* tests already in order to guide your efforts.

1. The `switch` subcommand should have two forms.

    `blurg switch local_diary` should create a local diary named `local_diary` much the same way as it does today.  There should be something internal that identifies `local_diary` as a locally stored diary (again, on your filesystem).

    `blurg switch --remote=URL --user=USERNAME remote_diary` should create a remote diary `remote_diary` using the Web server application found at `URL`.  An example of this might be:

    ```
    blurg switch --remote=http://localhost:5000 --user=jbshep team_panda_work_diary
    ```

    The `blurg switch --remote` version of the `switch` subcommand should store the diary key locally and then print to the screen the diary key.

    A remote diary named `remote_diary` should have information stored at the directory `~/.blurg/remote_diary` containing a single file named `remote`.  That file will be a text file (no `.txt` extension, however), and the file's contents should be lines containing colon-separated key-value pairs.  The keys should be `url`, `key`, and `username`.

    *NOTE:* In this milestone, users can only create new remote diaries.  They cannot yet share the key with another user so that the other user can "connect" to the remote diary.  In other words, although in this milestone we are building in support for multiple users, we are not yet allowing additional users to connect to remote diaries.  That will happen in the next milestone..

1. The `switch`, `wipe`, `log`, `rm`, and `ls` subcommands should still work regardless of whether a diary is local or remote.  You will implement a `RemoteDiary` class that is a subclass of `AbstractDiary` to accomplish this.  Again, we will discuss this at length in class.

1. You can abandon the `diaries` subcommand for this milestone.  It will come back in a future milestone.

If you're trying to think of ways to split up this milestone into issues and pairs for programming, consider these:                                                         

* Implement tests (this needs to happen right away).  Your instructor has given you some good initial tests.  You should run them to see what they do and if any of them fail at first.
* Implement code in `blurg/cli.py` to support the "remote" version of the `switch` subcommand.
* Implement code in `blurg/config.py` to fully implement the `switch` subcommand.
* Implement RemoteDiary (different methods can be parceled out into separate issues if you so choose, e.g., one pair can do `add_entry`, another can do `remove_entry`, etc.).
* The server route /api/rm/&lt;id&gt; should return correct error codes.See `blurg/server/__main__.py` for  comments documenting errors returned from this URL).

*Features not in this milestone*: There is no `diaries` subcommand that is fully functional.  There is also no way for a user to "connect" to a remote diary that is created by another user.

You will always need to keep up your README.md file.  It should maintain instructions for installing and running your code (both the client and the server), as well as running your tests.  You will always need to keep up the UML documentation as well. *Your instructor will provide a starting README.md and a starting UML file shortly after the start of the milestone.*

## Milestone 5

*Stand-up: 11/23, Due: ~~12/07~~ extended to 12/08 by 5:00 p.m.*

Features to be implemented in this milestone are as follows.

1. We will revisit the subcommand `diaries`. It should list all diaries with the currently active diary prefixed with an asterisk.  For each diary, it should also show the number of entries as well as the dates of the first and last entries.  If the diary is remote, the line should be suffixed with the string "(remote)".

    If the server is not running and there are remote diaries, the subcommand should not crash.  Rather, the CLI should print "\*cannot connect to server\*" in place of the entries statistics.

    Your `diaries` subcommand will produce its output in roughly the same form as what is shown below.

    ```
    $ blurg diaries
    default         (3 entries, from 11-18-2021 to 11-20-2021) 
    localtest       (2 entries, from 11-20-2021 to 11-20-2021) 
    * remotetest    (2 entries, from 11-19-2021 to 11-20-2021) (remote)
    remotetest2     (1 entries, from 11-20-2021 to 11-20-2021) (remote)
    ```
    If the server is not running, the user would see the following.

    ```
    $ blurg diaries
    default         (3 entries, from 11-18-2021 to 11-20-2021) 
    localtest       (2 entries, from 11-20-2021 to 11-20-2021) 
    * remotetest    (*cannot connect to server*) (remote)
    remotetest2     (*cannot connect to server*) (remote)
    ```
2. Support multiple users by adding a `connect` subcommand that allows users to connect to remote diaries previously created by another user.  The format of this subcommand is:

    ```
    blurg connect --remote=HOST --user=USERNAME --key=KEY
    ```

    You will need to add a URL route to the server to verify the diary key and return the actual name of the diary.  For example, a diary key of `8ax01cvz29` may be associated with a remote diary named `softeng` created by a user named `jbshep`.  The route should be `GET /api/verify` and the parameter name should be `key`.

    The actual name of the diary returned will be the name the user will use locally.  In other words, if `jbshep` creates a diary named `softeng`, any user that connects to `softeng` using its diary key will also see the diary's name as `softeng`.

    The result returned by `GET /api/verify' should be a JSON object of the form

    ```
    {
        'result': 'ok',
        'diaryname': DIARY_NAME,
    }
    ```

    or, in the case of an error,

    ```
    {
        'result': 'error'
    }
    ```

    Ensuring the URL route can return an error is important for the situation where users send a diary key that is invalid.

    If users already have a diary named `softeng` locally, this command should fail.

    If this subcommand completes successfully, the program should notify the user of the name of their newly connected diary, like this:

    ```
    Now connected to diary named "softeng"
    ```

3.  `blurg ls` should show the log author next to the date, like this:

    ```
    [11-20-2021 08:19 by jbshep (#1)]
    This is jbshep's first entry.


    [11-20-2021 08:19 by otheruser (#2)]
    This is otheruser's first entry. Can you see the different username
    next to the date?


    [11-20-2021 08:27 by jbshep (#3)]
    This is another jbshep entry.
    ```

    To support this, the filename of each log entry should somehow include the username of the user making the log entry.

4.  Diary entries should log the identity of the user making entry regardless of whether the entry is made to a local diary or a remote diary. This will allow your software to display local diary entries and remote diary entries the same way.

    The following Python code will allow you to obtain the local user's username for logging to local diaries.

    ```
    import getpass
    username = getpass.getuser()
    ```
5.  Keep the UML and README up to date.  Keep all help messages up to date.

6.  Your instructor will be paying close attention to commit messages.  Commit messages should be informative.

    Good examples are "connect subcommand" or "multiple users for remote diaries".

    Bad examples are "added stuff" or "fixing bad things" or "Jane Smith fixes".


Here is one final thought on supporting multiple users.  It would be beneficial to change the signature of the AbstractDiary class's `add_entry` method to something like:

```
def add_entry(self, content, date=datetime.now(), username=None) 
```

This would enable the calling code to specify the username to use.  If no username is given, the diary could use a reasonable default (like the local username or the username specified in the `remote` file).

## Milestone 6

*Stand-up: 12/07, Due: 12/16*

This is the final milestone.  There are two graded "deliverables" that are due.  The first is the milestone itself.  The second is an oral presentation that will be given during the final exam period.

Requirements for the <strong>milestone</strong> are:

1. Ensure that `blurg switch` when used with the ` --remote` option prints the generated diary key to the screen.

1. Create a new subcommand `blurg key` that prints the key of the current diary to the screen. If the current diary is remote, it prints the key.  If the current diary is local, it prints "The current diary is not remote."

1. Choose a "feature group" to implement.  Choices are listed below.

* Feature group 1: backup/restore

    `blurg backup` makes a backup of all local diaries and stores it somewhere within the directory `~/.blurg-backup`.

    `blurg backups` (note the plural subcommand) shows the dates of all available backups that have been made with `blug backup`.

    `blurg restore DATE` restores all local diaries backed up on DATE.  You may choose whatever date format you wish, but it should match the output of `blurg backups`.

* Feature group 2: promote/demote

    `blurg promote LOCALDIARY --remote=HOST --user=USER` should move LOCALDIARY and all its log entries to HOST.

    `blurg demote REMOTEDIARY` should move REMOTEDIARY and all its entries from its server to a local diary of the same name and then wipe it from the server.


Requirements for the <strong>oral presentation</strong> are:

* The presentation will be 10 - 20 minutes.  All students in the team must have a significant speaking role.
* Talk about the most technically challenging feature to implement *prior to* Milestone 6.
* Talk about which feature group you chose to implement in Milestone 6, why you chose it, and what you had to change in your design to implement it.
* Demo your software.
* Invite suggestions from the audience on how to crash your software.
* Lessons learned: how has the experience in this class changed how you will build software in the future?

As you craft your presentation, you will want to consider the presentation's [grading rubric](presentrubric.md). 
