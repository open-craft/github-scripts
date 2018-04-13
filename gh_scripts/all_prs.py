import csv
import uuid

import click
from github import Github


# TODO: Move this out to a conf.
DEFAULT_USERS = [
    'akovari',
    'afzaledx',  # note: was in edX before; pre-opencraft PRs will show; join date ~2018 april
    'aliciaopencraft17',
    'bradenmacdonald',
    'jcdyer',  # note: was in edX before; pre-opencraft PRs will show; join date ~2017 august
    'clemente',
    'e-kolpakov',
    'gabrieldamours',
    'pomegranited',
    'ciuin',
    'kaizoku',
    'xitij2000',
    'mtyaka',
    'macornwell',
    'rocioar',
    'smarnach',
    'itsjeyd',
    'tomaszgy',
    'UmanShahzad',
    'antoviaque',
    'haikuginger',
    'agaylard',
    'arbrandes',
    'bdero',
    'BogdanL',
    'bradmerlin',
    'carlio',
    'cgopalan',
    'jbzdak',
    'jkozera',
    'kelketek',
    'omarkhan',
    'replaceafill',
    'bitsblaster',  # was snowcrshd
]

@click.command()
@click.option(
    '--users', '-u',
    multiple=True, default=DEFAULT_USERS,
    help='List of users to retrieve PRs of. Use `-u` multiple times.')
@click.option(
    '--target-org', '-o',
    default='edx',
    help='The organization against which we count PRs.')
@click.option(
    '--csv-name', '-c',
    default='{}.csv'.format(uuid.uuid4()),
    help='The name of the CSV file to save PRs to.')
@click.option(
    '--since', '-s',
    default='2008-01-01',
    help='The date from which we should start counting.')
@click.option(
    '--github-token', '-gh',
    envvar='GITHUB_TOKEN', required=True,
    help='The Github API token.')
def main(users, target_org, csv_name, since, github_token):
    github = Github(github_token)
    with open(csv_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['username', 'title', 'merge_date'])
        for user in users:
            issues = github.search_issues(
                'is:pr is:merged org:{} author:{} created:>={}'.format(target_org, user, since)
            )
            for issue in issues:
                writer.writerow([user, issue.title, issue.as_pull_request().merged_at.strftime('%d/%m/%Y')])


if __name__ == "__main__":
    main()
