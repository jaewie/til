import os


HEADER = '''# TIL

> Today I Learned

Little programming nuggets on how to do various tasks.

'''

FOOTER = '''## About

I shamelessly stole this idea from
[jbranchaud](https://github.com/jbranchaud).'''


def get_categories():
    all_files = os.listdir('.')
    return sorted([f for f in all_files if os.path.isdir(f) and not f.startswith('.')])


def get_nuggets(subdirname):
    path = os.path.join(os.getcwd(), subdirname)
    nuggets = [f for f in os.listdir(path) if f.endswith('md') and not f.startswith('.')]

    return sorted([(n, get_title(os.path.join(path, n))) for n in nuggets], key=lambda x: x[1])


def get_title(abspath):
    with open(abspath) as f:
        return f.readline().lstrip('#').strip()


def format_categories(categories):
    lines = ['---', '', '### Categories', '']
    lines.extend(['* [{}](#{})'.format(c.title(), c) for c in categories])
    lines.append('')
    lines.append('---')
    lines.append('')

    for i, c in enumerate(categories):
        lines.append('### {}'.format(c.title()))
        lines.append('')

        for f, title in get_nuggets(c):
            location = os.path.join(c, f)
            line = '- [{}]({})'.format(title, location)
            lines.append(line)

        if i != len(categories) - 1:
            lines.append('')

    lines.append('')
    lines.append('')
    return '\n'.join(lines)


def main():
    categories = get_categories()
    content = format_categories(categories)

    with open('README.md', 'w') as f:
        f.write(HEADER)
        f.write(content)
        f.write(FOOTER)


if __name__ == '__main__':
    main()
