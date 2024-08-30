def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf8')
    i = 0
    if len(strings) > 0:
        for stroka in strings:
            i += 1
            position = file.tell()
            file.write(f'{stroka}\n')
            key = (i, position)
            strings_positions[key] = stroka
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
