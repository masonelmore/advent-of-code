def solve_part1(data):
    directory = build_dir(data)
    dirs = filter_dirs(directory, max_size=100000)
    size = sum(total_size(d) for d in dirs)
    return size


def solve_part2(data):
    directory = build_dir(data)
    total_space = 70000000
    unused_required = 30000000
    unused = total_space - total_size(directory)
    space_to_free = unused_required - unused
    dirs = filter_dirs(directory, min_size=space_to_free)
    size_to_delete = min(total_size(d) for d in dirs)
    return size_to_delete


def build_dir(data):
    root = {
        'parent': None,
        'dirs': {},
        'files': {},
        'size': 0,
    }
    cwd = root
    for cmd, arg, output in parse_commands(data):
        if cmd == 'cd':
            cwd = cd(cwd, arg)
        elif cmd == 'ls':
            ls(cwd, output)
            cwd['size'] = dir_size(cwd)
    return root


def parse_commands(data):
    cmd = None
    output_buffer = []

    for line in data:
        if cmd == 'ls' and line.startswith('$'):
            yield cmd, None, output_buffer
            output_buffer = []

        parts = line.split(' ')
        if parts[0] == '$' and parts[1] == 'cd':
            cmd, arg, output = parts[1], parts[2], None
            yield cmd, arg, output
        elif parts[0] == '$' and parts[1] == 'ls':
            cmd = 'ls'
        else:
            output_buffer.append(line)

    if cmd == 'ls' and output_buffer:
        yield cmd, None, output_buffer


def cd(cwd, dst):
    if dst == '..':
        return cwd['parent']

    if dst not in cwd['dirs']:
        cwd['dirs'][dst] = {
            'parent': cwd,
            'dirs': {},
            'files': {},
        }

    cwd = cwd['dirs'][dst]
    return cwd


def ls(cwd, output):
    for line in output:
        parts = line.split(' ')
        name = parts[1]
        if parts[0] == 'dir':
            cwd['dirs'][name] = {
                'parent': cwd,
                'dirs': {},
                'files': {},
                'size': 0,
            }
        else:
            size = int(parts[0])
            cwd['files'][name] = size


def filter_dirs(directory, max_size=None, min_size=None):
    dirs = []
    queue = list(directory['dirs'].values())
    for item in queue:
        size = total_size(item)
        if max_size and size <= max_size:
            dirs.append(item)
        if min_size and size >= min_size:
            dirs.append(item)
        queue.extend(list(item['dirs'].values()))
    return dirs


def dir_size(d):
    return sum(size for size in d['files'].values())


def total_size(directory):
    total = directory['size']

    for d in directory['dirs'].values():
        news = total_size(d)
        total += news

    return total
