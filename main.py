import execjs

at = execjs.compile(open('./res.js').read()).call('getAntiContent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
print(at)
