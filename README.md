# GitHub Scripts

Some scripts you can run to get random data through the GitHub API.

## Usage

You'll need a GitHub API token in order to be able to use these scripts. [See this article for creating a token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).

Get a virtual environment running, and see what's available in the options for some command you'd like to use.

```bash
$ virtualenv --python=python3 venv
$ . venv/bin/activate
$ pip install -r requirements.txt

# Let's check out `all_prs.py`.
$ python gh_scripts/all_prs.py --help
```
