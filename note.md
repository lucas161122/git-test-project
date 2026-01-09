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

### git command 
- git status: 查看文件是否有改动以及是否被追踪
- git add 文件名1 文件名2: 追踪文件1，文件2
- git status: 查看文件是否追踪成功(成功=全绿)
- git commit -m "存档说明": 存档
- git log: 确认存档成功并查看所有历史存档
- git push origin main : 推送到远程main分支
- 
