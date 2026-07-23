import sys

def initialize_names(name: str) -> str:
    name_as_list = name.split(' ')

    if len(name_as_list) <= 2:
        return name

    final_name = [name_as_list[0]]
    for i in name_as_list[1:-1]:
        final_name.append(i[0].capitalize() + '.')

    final_name.append(name_as_list[-1])

    return ' '.join(final_name)

if __name__ == '__main__':

    for line in sys.stdin:
        line = line.strip()

        if line:
            print(initialize_names(line))