import click
from github import Github


DEFAULT_USERS = [
    'akovari',
    'afzaledx',
    'aliciaopencraft17',
    'bradenmacdonald',
    'jcdyer',
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
    'snowcrshd',
]

@click.command()
@click.option('--users', '-u', multiple=True, type=str)
@click.option('--github-token', '-gh', envvar='GITHUB_TOKEN', required=True)
def main(users, github_token):
    if not users:
        users = DEFAULT_USERS

    github = Github(github_token)
    for user in users:
        github_user = github.get_user(user)
        prs = github.search_issues('is:pr is:merged org:edx author:{}'.format(user))
        for pr in prs:
            print('{}: {}'.format(github_user.name, pr.title))


if __name__ == "__main__":
    main()
