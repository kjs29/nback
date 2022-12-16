# N back game

# The purpose of the project

### I believe that an individual's intelligence can increase with practice the same you would exercise and build muscle. I created this game with some hope to improve my intelligence and I want everyone to try this game and get smarter. Or just have fun.

### This game is my first project that I have ever created since I started learning python. I heard that people can make games with [pygame module](##To-play-the-game,-download-`pygame`-module-please.), and creating games can teach a lot about programming in general so I decided to give it a try.

# What is 'N back'?

> The n-back task is a continuous performance task that is commonly used as an assessment in psychology and cognitive neuroscience to measure a part of working memory and working memory capacity. The n-back was introduced by Wayne Kirchner in 1958. N-Back can also be used as a training method to improve working memory and working memory capacity and also increase fluid intelligence.
>
> ...
>
> The n-back task was developed by Wayne Kirchner for his research into short-term memory; he used it to assess age differences in memory tasks of "rapidly changing information".

source - https://en.wikipedia.org/wiki/N-back

# How to play

Let's say that there will be numbers called to you.

`3 5 3 2 4`

One number will show at a time and disappears.

`3`

`5`

`3`

`2`

`4`

If you are playing 2 back, you have to memorize two sequence back and if that two sequence back number is the same as the current number, you press `O`, if not press `X`.

In this case, the correct answer would be `O`, `X`, `X`.

|3|5|3|2|4|
|--|--|--|--|--|
| | |O|X|X|

There will be tutorial inside the game for a clearer explanation.

[N - back on Wikipedia](https://en.wikipedia.org/wiki/N-back)

---

# Download the game

## Download Python.
##
> If you already have python 3.0 or higher, skip this part. If you don't have python, download python first [https://www.python.org](https://www.python.org/downloads/).

To check the version of the python installed in your computer,

```
python --version
```

```
python3 --version
```

## To play the game, download `pygame` module please.

## 1. Install `pygame`

For **Windows** users, write the code below in the command prompt,

```
py -m pip install -U pygame --user
```

For **Mac** users, write the code below in the terminal

```
python3 -m pip install -U pygame --user
```

or

```
pip3 install pygame --pre
```

for users who use python 3.11.

More information on [https://www.pygame.org](https://www.pygame.org/wiki/GettingStarted)

## 2. Download git (If you downloaded git already, skip this part)

### Download git

> Go to [https://git-scm.com](https://git-scm.com) and download git.

## 3. Create a folder to clone (download) the game files.

### - Create a folder 
or on Command Prompt / Terminal
```
$ mkdir programming
```

### - Open the Command Prompt / Terminal
### - Make sure that you are at folder directory in there and type
```
cd programming
git clone https://github.com/kjs29/nback.git
```
### - You will see that the files are downloaded
### - Open `main.py` and run it.