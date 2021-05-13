# git-practice

The team's sandbox repo for practicing Git stuff.

# Configuring Git
1. Set your username in Git (N.B. this is not your GitHub username) following [these directions](https://docs.github.com/en/free-pro-team@latest/github/using-git/setting-your-username-in-git).
2. Set your email address in Git and GitHub following [these directions](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address#setting-your-commit-email-address-in-git).
   1. `git config --global user.email "email@example.com"`
   2. Check it with `git config --global user.email`
3. Set your GitHub credentials:
   1. If you want to clone with HTTPS, [cache your GitHub credentials in Git](https://docs.github.com/en/free-pro-team@latest/github/using-git/caching-your-github-credentials-in-git).
   2. If you want to clone with SSH, you'll need to first [generate the SSH key](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), then you'll have to [add the key to your GitHub account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
4. [Optional] [Add VS Code to your PATH](https://stackoverflow.com/a/58377413/6310633) and set your default Git editor to VS Code with `git config --global core.editor "code --wait"`.

# Cloning the repo
1. Clone the repo using `git clone git@github.com:Digital-HR/git-practice.git` if you set up an SSH key in the configuration steps above, or using `git clone https://github.com/Digital-HR/git-practice.git` if you cached your GitHub credentials instead.
2. `cd git-practice`. All subsequent Git commands should be done while `git-practice` is your current directory.

# How to contribute

We use [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for organizing our work. Note that our branch names are slightly different, though - `master` from the Atlassian tutorial is `main` in our organization, and `develop` is `dev`.

## Contributing a Feature (fork from `dev`)
1. Assign yourself to the feature ticket.
2. Ensure you're checked out to the `dev` branch locally by running `git branch`. You should see a list of branches with a star (*) next to `dev`, indicating that you're checked out to it.
3. Pull in the latest changes from `dev` with `git pull origin dev`.
4. Create a branch to fix the issue and check out to it.
   1. Use the issue number in the branch name: `git checkout -b issue-1`
   2. Optionally include a description of the change in the branch name. It's sometimes difficult to anticipate what the change will be before you make it, so don't stress too much, but the issue title could be used if you think it provides enough detail: `git checkout -b issue-1-add-interesting-text`
   3. DO NOT use branch title like `fix-function1`. It's not descriptive enough, doesn't tie it to an issue, and is very vague.
   4. Johanan's preference is to use context, his initials and the issue number: `git checkout -b feat/ji/issue-1`.
5. Make your changes in that branch.
6. Stage your changes.
   1. If you want to include all your changes in a specific file in your commit: `git add Main.py`.
   2. If you instead wish to stage only hunks of your changes in a file, use the `-p` flag: `git add -p Main.py`
7. Check that your staged changes are the ones you intend to commit: `git diff --cached`.
8. Commit your changes with `git commit`. Remember to write an [informative commit message](https://forcepush.tech/missives-to-the-future-on-commit-messages-and-maintainability).
9. Push your changes to remote with `git push`.
10. Submit a pull request from your branch to `dev` (the trunk branch).
11. Once your PR has been approved, merge your branch into `dev`.
12. Locally checkout to `dev` with `git checkout dev` (note the `-b` flag is not needed since the branch already exists).
13. Pull the latest changes from origin with `git pull`.
14. Delete your local feature branch with `git branch -d feat/ji/issue-1`.

## Contributing a Hotfix (fork from `main`)
1. Assign yourself to the hotfix ticket.
2. Ensure you're checked out to the `main` branch locally by running `git branch`. You should see a list of branches with a star (*) next to `main`, indicating that you're checked out to it.
3. Pull in the latest changes from `main` with `git pull origin main`.
4. Create a branch to fix the issue and check out to it. Use the new version number in the branch name: `git checkout -b hotfix/v1.0.1`. The last digit of the tag is incremented for hotfixes.
5. Make your changes in that branch.
6. Stage your changes.
   1. If you want to include all your changes in a specific file in your commit: `git add Main.py`.
   2. If you instead wish to stage only hunks of your changes in a file, use the `-p` flag: `git add -p Main.py`
7. Check that your staged changes are the ones you intend to commit: `git diff --cached`.
8. Commit your changes with `git commit`. Remember to write an [informative commit message](https://forcepush.tech/missives-to-the-future-on-commit-messages-and-maintainability).
9. Push your changes to remote with `git push`.
10. Submit a pull request from your branch to `main`.
11. Once your PRs have been approved, merge your branch into `main` and `dev`. **Do not delete the hotfix branch!**
12. Review and merge the autogenerated PR into `dev` that you're tagged on.

## Making a Release Candidate (automated)
1. Click the "Run workflow" button for the [release-candidate workflow](https://github.com/Digital-HR/git-practice/actions/workflows/release-candidate.yml). Use the workflow from `dev`. The version number should be in the form `X.Y.Z` where X corresponds to the MAJOR version, Y corresponds to the MINOR version, and Z corresponds to the PATH version. See https://semver.org for more details on how these values should be incremented.
2. Review the pull request you're tagged on.
3. Merge the PR.
4. Review and merge the PR into `dev` that you're tagged on.
