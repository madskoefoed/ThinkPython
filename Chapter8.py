from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename

download('https://www.gutenberg.org/cache/epub/345/pg345.txt')

reader = open('pg345.txt', encoding="utf-8")
writer = open('pg345_cleaned.txt', 'w', encoding="utf-8")

def is_special_line(line):
        return line.startswith('*** ')

for line in reader:
    if is_special_line(line):
        break

for line in reader:
    if is_special_line(line):
        break
    writer.write(line)

reader.close()
writer.close()

for line in open('pg345_cleaned.txt', encoding="utf-8"):
    line = line.strip()
    if len(line) > 0:
        print(line)
    if line.endswith('Stoker'):
        break

### Exercise 1 ###

# See if you can write a function that does the same thing as the
# shell command !head. It should take as arguments the name of a
# file to read, the number of lines to read, and the name of the
# file to write the lines into. If the third parameter is None, it
# should display the lines rather than write them to a file.

def head(filename, number, output = None):
    if number <= 0:
        ValueError("'number' must be a strictly positive integer")

    total = 0
    reader = open(filename, encoding="utf-8")
    filename = filename[:len(filename)]

    if not (output is None):
        writer = open(output, 'w', encoding="utf-8")
        for line in reader:
            total += 1
            writer.write(line)
            if total >= number:
                break
        writer.close()

    else:
        for line in reader:
            total += 1
            print(line)
            if total >= number:
                break

    reader.close()
        

print("Solution 1")
head('pg345.txt', 10)
head('pg345_cleaned.txt', 100, 'pg345_cleaned_100_lines.txt')