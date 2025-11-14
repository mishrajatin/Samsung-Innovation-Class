# Python Live Practice Examples - 3 Examples per Topic
# ----------------------------------------------------

# 1) Variable & Assignment
# example 1
a = 10
b = "hello"
print(a, b)

# example 2
count = 0
count = count + 5
print("count =", count)

# example 3
name = "Student"  # replace input for safe running
message = "Hi, " + name
print(message)


# 2) Multiple Assignment
# example 1
x, y, z = 1, 2, 3
print(x, y, z)

# example 2
a, b = "left", "right"
a, b = b, a
print(a, b)

# example 3
lst = [10, 20, 30]
p, q, r = lst
print(p, q, r)


# 3) Assignment & Reference
# example 1
L1 = [1,2]
L2 = L1
L2.append(3)
print("L1:", L1)

# example 2
L1 = [1,2]
L2 = L1.copy()
L2.append(9)
print("L1:", L1, "L2:", L2)

# example 3
s1 = "hi"
s2 = s1
s2 += "!"
print("s1:", s1, "s2:", s2)


# 4) Basic Data Types
a = 5; b = 3.2; c = "py"; d = None; e = False
for v in (a,b,c,d,e): print(v, type(v))

n = 3; m = 2.5
print(n + m, type(n+m))

flag = True
print("flag is", flag, "->", type(flag))


# 5) Type Casting
s = "100"; n = int(s); print(n, type(n))

f = float("2.7"); print(int(f), type(int(f)))

age = 20
print("Next year:", age + 1)


# 6) Tuple Examples
t = (10, 20, 30)
print(t[1], t[-1])

a, b, c = t
print(a+b+c)

x = (5,)
y = (5)
print(type(x), type(y))


# 7) Tuple Slicing
t = (0,1,2,3,4,5)
print(t[1:4])
print(t[::2])
print(t[::-1])


# 8) zip examples
names = ["A","B","C"]
scores = [90,80,70]
for n,s in zip(names,scores): print(n,s)

keys = ["k1","k2"]; vals = [1,2]
d = dict(zip(keys, vals))
print(d)

a = [1,2,3]; b = ["x","y"]
print(list(zip(a,b)))


# 9) List examples
L = [1,2,3]
L.append(4)
print(L)

L.pop()
L.insert(1, 99)
print(L)

L.extend([7,8])
print(L + [100])


# 10) Accessing lists
letters = list("python")
print(letters[0], letters[-1])

letters[1:3] = ["X","Y"]
print(letters)

nums = [1,2,3,4]
print(nums[::-1])


# 11) Dictionary Basics
d = {"name":"A","age":20}
print(d, list(d.keys()))

for k,v in d.items(): print(k, "->", v)

students = {"A": {"age":20}, "B":{"age":22}}
print(students["A"]["age"])


# 12) Modify Dictionary
d = {}
d["city"] = "Kanpur"
d["city"] = "Delhi"
print(d)

print(d.get("state", "unknown"))

d["temp"] = 1
del d["temp"]
print(d)


# 13) Set Basics
s = {1,2,2,3}
print(s)

s2 = set([1,1,2,3])
print(s2)

s2.add(4); s2.discard(1)
print(s2)


# 14) Set Operations
a = {1,2,3}; b = {2,3,4}
print("union", a | b)
print("inter", a & b)
print("diff a-b", a - b)


# 15) in operator
print(2 in [1,2,3])
print("zz" in "pizza")
d = {"k":1}
print("k" in d, 1 in d)


# 16) Arithmetic & comparison
a, b = 7, 3
print(a/b, a//b, a % b, a**b)
print(a > b, a == 7, b <= 2)

x = 5
x += 10
print(x)


# 17) Functions
def add(a,b): return a+b
print(add(2,3))

def greet(name="Student"): return f"Hi {name}"
print(greet(), greet("Asha"))

def stats(nums): return min(nums), max(nums), sum(nums)/len(nums)
print(stats([1,3,5]))


# 18) enumerate
colors = ["red","green","blue"]
for i,c in enumerate(colors): print(i,c)
for i,c in enumerate(colors, 1): print(i,c)
for i,c in enumerate(colors):
    if i % 2 == 0: print("even idx", i, c)


# 19) pass, break, continue
for i in range(3):
    if i==1: pass
    print("i", i)

for i in range(5):
    if i % 2 == 0: continue
    print("odd", i)

for i in range(10):
    if i == 4: break
    print(i)


# 20) if/elif/else
x = 12
if x < 10: print("low")
elif x < 20: print("mid")
else: print("high")

n = 5
if n % 2 == 0:
    print("even")
else:
    print("odd")

age = 17
status = "kid" if age < 18 else "adult"
print(status)


# 21) for loops
for i in range(1,6): print(i*i)

for item in ["a","b","c"]: print(item)

s = 0
for i in range(1,5): s += i
print(s)


# 22) while loops
i = 0
while i < 3:
    print(i); i += 1

# replaced input with fixed values
n = 1
while n != 0:
    n -= 1

i = 0
while True:
    if i > 2: break
    print(i); i += 1


# 23) Exception handling
try:
    n = int("10")
except ValueError:
    print("not a number")

try:
    x = 2
    y = 10 // x
except ValueError:
    print("bad int")
except ZeroDivisionError:
    print("divide by zero")

try:
    print("try block")
finally:
    print("always runs")


# 24) Mini-projects
students = {"A": [80,90], "B":[70,60]}
def avg(scores): return sum(scores)/len(scores)
for name,s in students.items(): print(name, avg(s))

text = "hello world hello ai"
words = set(text.split())
print("unique words:", words)

db = {}
db["Asha"] = 22
print(db)
