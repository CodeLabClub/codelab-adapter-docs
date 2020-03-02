# note
```
pip install mkdocs mkdocs-material
pip install jieba
pip install pyembed-markdown 
```

# 将视频保存到本地
cd /Users/wuwenjie/mylab/changxue/scratch3-adapter-docs/docs

ack -ho "http:.*\.mp4" > /tmp/adapter_video_url_list.txt

取得视频列表保存下来


python3

```python
import subprocess
with open("/tmp/adapter_video_url_list.txt") as png_url_list:
    urls_all = png_url_list.readlines()
    urls_set = set(urls_all)
    print("urls_all:",len(urls_all),"urls_set:",len(urls_set))
for url in urls_set:
    cmd = f"wget {url}"
    # print(cmd)
    subprocess.call(cmd,shell=True)
```


# 找到所有mp4文件下载到存入本地
ack -ho "http://scratch3-files.just4fun.site.+\.mp4" > mp4_list.txt

### 下载
[博客迁移:从Pelican到Hugo](https://blog.just4fun.site/post/%E5%B7%A5%E5%85%B7/from-pelican-to-hugo/)

```
import subprocess
with open("/tmp/mp4_list.txt") as mp4_url_list:
    urls = set(mp4_url_list.readlines()) # 去重
for url in urls: 
        cmd = f"wget {url} --directory-prefix=docs/video/"
        subprocess.call(cmd,shell=True)
```

#  参考
*  [基于mkdocs-material实现的帮助中心(markdown + 中文搜索 + 图片放大)](https://segmentfault.com/a/1190000018592279)
*  [pymdown](https://squidfunk.github.io/mkdocs-material/extensions/pymdown/)
    *  [critic](https://facelessuser.github.io/pymdown-extensions/extensions/critic/)
*  [Customize MkDocs-Material with Javascript](https://cainmagi.github.io/playground/20190225mkdocs/)
*  [3os.org](https://github.com/fire1ce/3os.org)
*  左右分栏：https://yakworks.github.io/mkdocs-material-components/cheat-sheet/

