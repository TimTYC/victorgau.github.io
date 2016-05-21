### Pelican 的一些設定

1.Pelican 的安裝及設定方式請參照 [這裡](http://victorgau.github.io/setting-up-pelican-for-github-pages.html)。

2.fabric 的使用方式，請參照上面的 fabfile.py 然後自行修改。目前大致如下：


建立新的貼文：
```bash
fab new_post:"the title of the post"
```


Preview 目前的網站 (http://localhost:8000)：
```bash
fab reserve
```


將結果 push 到 github 上面去：
```bash
fab github
```
