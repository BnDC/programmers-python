import re


def solution(files):
    def sort_key(name):
        name = name.lower()
        number = re.findall('\d+', name)[0]
        return [name[:name.find(number)], int(number)]

    files.sort(key=sort_key)

    return files


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
