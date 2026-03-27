### f字符串
```python
name = "rabbit"
print(f"my name is {name}")

```

### string.find/title/replace.
```python
name = "rabbit jumps"
print(name.find('b'))  #返回b首次出现的索引(2)
print(name.title())    #返回字符串里的首字母大写(Rabbit Jumps)

```

### falsy values:0 "" None
```python
a = 0
b = ""
c = None

if a:
    print("good")

if not b:
    print("bad")

if c:
    print("ok")

# output: bad
```

### how to enter Ubuntu 24.04
1. 打开powershell
2. wsl -d Ubuntu-24.04


### git command 
- git status: 查看文件是否有改动以及是否被追踪
- git add 文件名1 文件名2: 追踪文件1，文件2
- git status: 查看文件是否追踪成功(成功=全绿)
- git commit -m "存档说明": 存档
- git log: 确认存档成功并查看所有历史存档
- git push origin main : 推送到远程main分支


### 类class
- instance实例化
- __init__初始化
- inhiritance继承

```python
class Player:
    def talk(self):
        print("I am a player")


class JumpPlayer(Player):
    def jump(self):
        print("I am jumpping")


class RunPlayer(Player):
    def run(self):
        print("I am runing")


lucas = JumpPlayer()
lucas.jump()


oscar = RunPlayer()
oscar.run()

```

### 模块
- 引用方式
- import 模块名
- from 模块名 import 函数名


### 包
##### 引用方式
- import 包名(要按顺序：包.模块.函数)
- from 包 import 模块
- from 包.模块 import 函数


### 随机数
- 导入方式：import random
- 0 - 1 之间的随机数 `random.random()`
- m - n 之间的随机整数`random.randint(m,n)`

