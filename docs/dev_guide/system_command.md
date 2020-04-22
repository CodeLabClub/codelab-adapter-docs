# codelab-message-pub 系统命令

安装完`codelab_adapter_client`之后，将生成`codelab-message-pub`系统命令，它方便用来将 CodeLab Adapter 与其他编程语言做集成，我们展示了与 30+ 种编程语言结合的例子。

Unix/Linux 操作系统仅仅使用信号（signal）便能构建非常复杂的协同程序。Erlang 从 SmallTalk 那儿学到仅使用 message 来协同程序，message 是个极其强大的概念。

CodeLab Adapter 的核心设计思路是：`Everything Is Message`（EIM），我们在最新的`codelab_adapter_client`版本中，为其加入系统命令，方便在其他语言构建的程序中往 CodeLab Adapter 发送消息，这样一来，你就可以使用任何编程语言为 Scratch 构建插件，或者为 CodeLab Adapter 构建插件。

## 典型使用案例：

在 CodeLab 内部，我们的魔杖程序（使用魔杖控制空间里的事物）的机器视觉（CV）部分是使用 C++ 写的（因为深度相机的 C++ SDK 比较完备），为了让深度相机与 Scratch 协同工作，`codelab-message-pub`便是理想的选择，它能够将消息的触角延伸到任何编程语言里。


## codelab-message-pub

### 安装
`pip install codelab_adapter_client --upgrade`

### 使用帮助
```bash
> codelab-message-pub -h
usage: codelab-message-pub [-h] [-i CODELAB_ADAPTER_IP_ADDRESS] [-n NAME]
                           [-p PUBLISHER_PORT] [-s SUBSCRIBER_PORT] [-t TOPIC]
                           [-c CONTENT] [-j JSON_MESSAGE]

optional arguments:
  -h, --help            show this help message and exit
  -i CODELAB_ADAPTER_IP_ADDRESS
                        None or IP address used by CodeLab Adapter
  -n NAME               Set name in banner
  -p PUBLISHER_PORT     Publisher IP port
  -s SUBSCRIBER_PORT    Subscriber IP port
  -t TOPIC              message topic
  -c CONTENT            payload['content']
  -j JSON_MESSAGE       json message(with topic and payload)
```

### 使用方法
```bash
> codelab-message-pub -t hello_topic
> codelab-message-pub -c hello_content
> codelab-message-pub -j '{"topic":"eim/test","payload":{"content":"test contenst"}}'
```

使用`codelab-message-pub`时记得先打开 CodeLab Adapter。

## 支持语言
以下是我们给出的主流/非主流编程语言与`codelab-message-pub`集成的范例，本质上是系统调用。

部分编程语言使用[labstack](https://code.labstack.com/bash)测试。

## C++

```c++
#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("codelab-message-pub -c hello_content");
}
```

## Rust

```rust
// https://doc.rust-lang.org/book/ch01-02-hello-world.html
// https://doc.rust-lang.org/std/process/struct.Command.html
// https://stackoverflow.com/questions/21011330/how-do-i-invoke-a-system-command-in-rust-and-capture-its-output
use std::process::Command;
fn main() {
    Command::new("codelab-message-pub")
        .arg("-c")
        .arg("hello_content")
        .spawn()
        .expect("command failed");
}
```

```bash
rustc main.rs
./main
```

## Golang

```go
// https://golang.org/pkg/os/exec/
// https://tutorialedge.net/golang/executing-system-commands-with-golang/
package main

import (
    "fmt"
    "os/exec"
    "runtime"
)

func execute() {
    out, err := exec.Command("codelab-message-pub", "-c","hello_content").Output()
    if err != nil {
        fmt.Printf("%s", err)
    }
    fmt.Println("Command Successfully Executed")
    output := string(out[:])
    fmt.Println(output)
}

func main() {
    if runtime.GOOS == "windows" {
        fmt.Println("Can't Execute this on a windows machine")
    } else {
        execute()
    }
}
```

```bash
go run main.go
```

## swift

```swift
//https://stackoverflow.com/questions/26971240/how-do-i-run-an-terminal-command-in-a-swift-script-e-g-xcodebuild
import Foundation

@discardableResult
func shell(_ args: String...) -> Int32 {
    let task = Process()
    task.launchPath = "/usr/bin/env"
    task.arguments = args
    task.launch()
    task.waitUntilExit()
    return task.terminationStatus
}

shell("codelab-message-pub", "-c","hello_content")
```

## c
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   char command[50];

   strcpy( command, "codelab-message-pub -c hello_content" );
   system(command);

   return(0);
} 
```

## bash
```bash
codelab-message-pub -c hello_content
```

## Racket

```racket
(system "codelab-message-pub -c hello_content")
```

## Scheme
```scheme
(system "codelab-message-pub -c hello_content")
```

## Elisp(Emacs)

```lisp
(shell-command "codelab-message-pub -c hello_content")
```

## [Hy](http://docs.hylang.org)
```
(import subprocess)
(.call subprocess ["codelab-message-pub" "-c" "hello_content"])
```

## SmallTalk(Pharo)

```smalltalk
command := OSProcess waitForCommand: 'codelab-message-pub -c hello_content'.
command exitStatus.
```

## Haskell
```Haskell
module Main where

import System.Process

main = callCommand "codelab-message-pub -c hello_content"
```

## MATLAB
```matlab
% https://www.mathworks.com/help/matlab/ref/system.html
system("codelab-message-pub -c hello_content")
```

## Julia
```Julia
run(`codelab-message-pub -c hello_content`)
```

## Lua
```lua
os.execute("codelab-message-pub -c hello_content")
```

## Perl
```perl
system("codelab-message-pub -c hello_content")
```

## PHP
```php
<?php
  system("codelab-message-pub -c hello_content"); 
?>
```

## Dart
```dart
import 'dart:io';

main() {
  Process.run('codelab-message-pub', ['-c', 'hello_content']);
}
```


## R
```R
system("codelab-message-pub -c hello_content")
```

## Ruby

```ruby
system("codelab-message-pub -c hello_content")
```

## Crystal
```crystal
system "codelab-message-pub -c hello_content"
```

## Python
```python
import subprocess
subprocess.call(["codelab-message-pub -c hello_content"], shell=True)
```

## JavaScript(NodeJS)

```js
const {execSync} = require('child_process');
execSync('codelab-message-pub -c hello_content');
```

## Prolog
```prolog
shell('codelab-message-pub -c hello_content').
```

## Erlang

```erlang
!/usr/bin/env escript

main(_) ->
  output = os:cmd("codelab-message-pub -c hello_content"),
  io:fwrite(output).
```

## Java
```java
Runtime r = Runtime.getRuntime();
Process p = r.exec("codelab-message-pub -c hello_content");
p.waitFor();
```

## Kotlin
the same as Java

## Clojure
```Clojure
(use '[clojure.java.shell :only [sh]])
(sh "codelab-message-pub"  "-c" "hello_content")
```

## Scala
```Scala
import sys.process._
val cmd = "codelab-message-pub -c hello_content"
val output = cmd.! // Captures the output
```

## Groovy

```Groovy
"codelab-message-pub -c hello_content".execute()
```

## Processing
```c
// https://forum.processing.org/two/discussion/24401/how-can-i-run-a-command-in-terminal-from-within-processing
exec("codelab-message-pub", "-c","hello_content");
```

## Fortran
```Fortran
CALL execute_command_line('codelab-message-pub -c hello_content') 
```

## Ada
```ada
-- https://www.pegasoft.ca/resources/boblap/13.html
function system( cmd : string ) returns integer;
pragma Import( C, system );
Result := system( "codelab-message-pub -c hello_content" & ASCII.NUL );
```

## Brainfuck
```
ref : https://kimiyuki.net/blog/2016/04/01/bash-on-brainfuck-on-anarchy-golf/
```

## `C#`

```c#
// https://docs.microsoft.com/en-us/dotnet/core/tutorials/using-with-xplat-cli
// https://kimsereyblog.blogspot.com/2018/01/start-processes-from-c-in-dotnet-core.html
// https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-run?tabs=netcore21#examples
```

## Pascal
```
ref :https://wiki.freepascal.org/Executing_External_Programs
```

## Assembly
```
ref: https://stackoverflow.com/questions/9342410/sys-execve-system-call-from-assembly
```

## SQL
```
ref: https://stackoverflow.com/questions/43205594/running-system-command-with-argument-in-a-postgresql-function
```
