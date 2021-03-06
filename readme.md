# readme.md
[CodeLab Adapter](https://adapter.codelab.club) 的项目文档，基于 [mkdocs](https://www.mkdocs.org/)。

欢迎大家一起来维护文档（new_v2分支）


# Usage

```
git clone https://github.com/CodeLabClub/codelab-adapter-docs
cd codelab-adapter-docs
pip3 install mkdocs pymdown-extensions mkdocs-material markdown_include

# debug
mkdocs serve

# build
mkdocs build

# publish
make push
```

# 如何编辑文档
参考 [mkdocs docs](https://www.mkdocs.org/#getting-started)

# 图片资源
参考 [Linking to images and media](https://www.mkdocs.org/user-guide/writing-your-docs/#linking-to-images-and-media)

# 参与翻译
[CodeLab Adapter](https://adapter.codelab.club)的海外用户目前使用`谷歌翻译`阅读该文档。

如果你愿意将其翻译为英文，十分欢迎。

可以参考已翻译的部分：[Our Values](/about/value/#our-values)。

# push to github
```bash
git checkout gh-pages
ghp-import -r github -p site
```

# 提交
PR 到 new_v2 分支
