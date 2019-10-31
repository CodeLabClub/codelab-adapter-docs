# 将 Scratch 项目嵌入网站

服务于教学和内容设计，也可用于构建和发布 microworld(《Mindstorms》)。

开发者和教师可以利用 CodeLab Scratch，将 sb3 项目嵌入到自己的网站和课程中。

## 一些例子

### Pong Starter

[Pong Starter](https://scratch3.codelab.club/embed/?sb3url=https://adapter.codelab.club/sb3/Pong_Starter.sb3)

```html
<iframe
  src="https://scratch3v2.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/Pong_Starter.sb3"
  allowtransparency="true"
  width="500"
  height="450"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

<iframe src="https://scratch3.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/Pong_Starter.sb3" allowtransparency="true" width="500" height="450" frameborder="0" scrolling="no" allowfullscreen></iframe>

### Dress Up Tera

```html
<iframe
  src="https://scratch3v2.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/Dress_Up_Tera.sb3"
  allowtransparency="true"
  width="500"
  height="450"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

<iframe src="https://scratch3v2.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/Dress_Up_Tera.sb3" allowtransparency="true" width="500" height="450" frameborder="0" scrolling="no" allowfullscreen></iframe>


### 交响乐

[交响乐](https://scratch3v2.codelab.club/?sb3url=https://adapter.codelab.club/sb3/交响乐.sb3)

```html
<iframe
  src="https://scratch3v2.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/交响乐.sb3"
  allowtransparency="true"
  width="500"
  height="450"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

<iframe src="https://scratch3v2.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/交响乐.sb3" allowtransparency="true" width="500" height="450" frameborder="0" scrolling="no" allowfullscreen></iframe>

## 如何将 sb3 文件保存到线上

可以保存到任何服务器上(https), 只要允许跨域资源共享(CORS), 以下是 nginx 的配置:

```
add_header Access-Control-Allow-Origin *;
add_header Access-Control-Allow-Methods 'GET, OPTIONS';
```

如果你没有自己的服务器, 可以将你的 sb3 文件提交到 CodeLab 的仓库里:[codelab-adapter-docs](https://github.com/Scratch3Lab/codelab-adapter-docs/), 我们将为你代为托管。

当然你也可以将其放在云存储上(诸如七牛云)。

## 参考

- [How to Embed a Project](https://en.scratch-wiki.info/wiki/How_to_Embed_a_Project)
- [phosphorus](https://phosphorus.github.io/)
    - [phosphorus](https://phosphorus.github.io/#11397100)
    - [3D Remix: Experimental render-ordering using clones](https://scratch.mit.edu/projects/11397100)
    - [Mario Land 2 - gb.sb2](https://phosphorus.github.io/#34791164)
    - [3D Framework v0.48h +timings](https://scratch.mit.edu/projects/16205373)
    - [Alone in the depths](https://phosphorus.github.io/#16207935)
    - [Epic Ninja v1.12](https://scratch.mit.edu/projects/21554369)
