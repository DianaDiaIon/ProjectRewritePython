import sys

i = 1


def hello_world():
    return "Hello, World!"


def hello(name):
    if name:
        say_what = "Hello, " + name + "!"
    else:
        say_what = "Hello, World!"
    return say_what


def print_hello(name):
    say_what = hello(name)
    if say_what:
        print(say_what)


def task():
    global i
    print("\nTASK NO", i)
    i += 1


task()  # 1
hi_you = hello_world()
print(hi_you)

task()  # 2
name = input("Hi! What's your name?: ")
hi_you = hello(name)

task()  # 3
print_hello(name)

task()  # 4
try:
    hi_you = hello(sys.argv[1])
    print(hi_you)
except IndexError:
    print("No argument passed on command line.")

task()  # 5
j = 1
names = ""
while j < len(sys.argv):
    if not names:
        names = sys.argv[1]
    else:
        names = names + " " + sys.argv[j]
    j += 1
if names:
    hi_you = hello(names)
    print(hi_you)
else:
    print("No argument passed on command line.")
    