def find_unique_filenames(filename: str) -> str:
    with open(filename, 'r') as file:
        file_content = file.read()
        lines = file_content.strip().split('\n')
        result = []

        for line in lines:
            if not line.strip():
                continue

            filenames = line.split('|')
            name_count = {}

            for filename in filenames:
                name = filename.split('.')[0]
                if name in name_count:
                    name_count[name] += 1
                else:
                    name_count[name] = 1

            unique_filenames = [filename for filename in filenames if name_count[filename.split('.')[0]] == 1]
            if unique_filenames:
                result.append('|'.join(unique_filenames))

        return "\n".join(result)
