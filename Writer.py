import string

NUMERALS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lesson = 0
header = 1
sentence = 1

Text = ''

Text += NUMERALS[lesson] + '. ' + input("Lesson Name: ") + '\n'
lesson += 1

Text += '    ' + str(header) + '. ' + input('Header: ') + '\n'
header += 1

while True:
    try:
        Text += '        ' + str(sentence) + '. ' + input('Sentence: ') + '\n'
        sentence += 1
    except KeyboardInterrupt:
        Command = input('L for new Lesson, H for new header, Q for quit: ').lower()
        if Command == 'l':
            Text += NUMERALS[lesson] + '. ' + input("Lesson Name: ") + '\n'
            lesson += 1
            header = 1
            sentence = 1
        elif Command == 'h':
            Text += '    ' + str(header) + '. ' + input('Header: ') + '\n'
            header += 1
            sentence = 1
        elif Command == 'q':
            with open("Outline.txt", "a", encoding="utf-8") as f:
                f.write(Text)
                f.close()
            quit()
        else:
            pass
