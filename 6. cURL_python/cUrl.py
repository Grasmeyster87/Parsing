from curl_fetch2py import CurlFetch2Py
import requests


test_cUrl = 'curl "https://habr.com/ru/articles/832566/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: https://www.google.com/" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: cross-site" -H "Connection: keep-alive" -H "Cookie: hl=ru; fl=ru; habr_uuid=udaaX2e1R51ugf8zLxFFXTJxksCay7in22uevSnR^%^2FEFbbNeWf3JNXbbRy5o5IP5QISUi2wLoA9w1SIaSjeVg4g; visited_articles=718662:273089:713458:544828:582758:839406:491770:459822:755096:151783" -H "If-None-Match: W/""34e28-MfVFz6R6WMgfjKuxGr2wgYgbio0""" -H "Priority: u=0, i"'

context_fetch = CurlFetch2Py.parse_curl_context (test_cUrl)
print(context_fetch, '\n')
print(context_fetch.headers, '\n')
print(context_fetch.cookies)
print(context_fetch.url)