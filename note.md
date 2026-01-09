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