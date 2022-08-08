import collections
import re


def solution(word, pages):
    answer = 0
    word = word.lower()
    base_score = [0 for _ in pages]
    final_score = [0 for _ in pages]

    embedded_link_cnts = [0 for _ in pages]
    url_idx_map = {}
    url_graph = collections.defaultdict(list)

    for i in range(len(pages)):
        cnt = 0
        pages[i] = pages[i].lower()
        for f in re.findall(r'[a-zA-Z]+', pages[i]):
            if f == word:
                cnt += 1
        base_score[i] = cnt

        url = re.search(r'<meta property="og:url" content="(https://\S+)"', pages[i]).group(1)
        embedded_links = re.findall(r'<a href="(https://\S+)"', pages[i])
        embedded_link_cnts[i] = len(embedded_links)

        url_idx_map[url] = i
        for link in embedded_links:
            url_graph[link].append(url)

    for i in range(len(base_score)):
        final_score[i] = base_score[i]

    for url in url_graph:
        if url_idx_map.get(url) is None:
            continue
        url_idx = url_idx_map[link]

        for link in url_graph[url]:
            link_idx = url_idx_map[link]
            final_score[url_idx] += base_score[link_idx] / embedded_link_cnts[link_idx]

    max_score = 0
    for i in range(len(final_score)):
        if max_score < final_score[i]:
            max_score = final_score[i]
            answer = i

    return answer


word1 = "blind"
page1 = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word1, page1))

word2 = "Muzi"
page2 = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word2, page2))
