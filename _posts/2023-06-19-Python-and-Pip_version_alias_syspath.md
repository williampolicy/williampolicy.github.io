---
layout: post
title:  "Understanding Python and Pip Versions, Aliases, and Storage Locations"
date:   2023-06-19
categories: [tutorial, python]
---


## English Version

### Python and Pip: What are they?

Python is a popular programming language, and Pip is Python's package manager. The Python interpreter runs Python code, and Pip installs, manages, and upgrades Python packages.

### Python and Pip Versions

Python and Pip both have their own versions. You can check the current versions of Python and Pip with the `python --version` and `pip --version` commands, respectively.

Sometimes, a system may have both Python 2 and Python 3. To distinguish between them, you can use `python2` or `python3`, and `pip2` or `pip3` to invoke specific versions of Python or Pip.

### Python and Pip Aliases

In your shell configuration file, you can set up aliases for easier invocation of Python and Pip. For example, if your system's default `python` command is Python 2, you may want to set an alias so that `python` actually invokes Python 3. You can do this by adding the following lines to your `.bash_profile`:

```bash
alias python=python3
alias pip=pip3
```

After setting these aliases, when you type `python` or `pip` into your terminal, you'll actually be invoking `python3` or `pip3`.

### Python and Pip System Paths

In Unix-like systems, the `PATH` environment variable defines where the shell looks for executable files. When you type a command into your terminal, the shell looks for that command in the directories listed in your `PATH`.

The executable files for Python and Pip are usually located in `/usr/local/bin` or your user's `~/.local/bin`. To ensure your shell can find Python and Pip, you need to make sure these directories are in your `PATH`.

You can use the `which` command to see the path of a specific command. For example, `which python` will show you the path to the Python interpreter, and `which pip` will show you the path to Pip.

Note that the `which` command ignores aliases. Even if you have `python` aliased to `python3`, `which python` will still show the path for Python 2. If you want to see the path of the actual command an alias refers to, you need to use `which python3`.

### Python and Pip Storage Locations

Python and Pip install packages to specific locations, which can be viewed via Python's `sys.path`. `sys.path` is a list containing the directories Python looks in for packages and modules. When you import a module, Python looks for that module in the directories listed in `sys.path`.

You can view `sys.path` by entering the following command into the Python interpreter:

```python
import sys
print(sys.path)
```

This will display a list of directories where Python looks for packages and modules.

Note that even though the executable files for Python and Pip may be in different directories, they can still work together. This is because Pip installs packages to locations in `sys.path`, which the Python interpreter can access.

## Chinese Version (中文版)

### Python和Pip：它们是什么？

Python是一种流行的编程语言，而Pip是Python的包管理器。Python的解释器负责运行Python代码，而Pip则用来安装、管理和升级Python包

。

### Python和Pip的版本

Python和Pip都有自己的版本。你可以通过`python --version`和`pip --version`命令来查看Python和Pip的当前版本。

有时候，一个系统可能同时有Python 2和Python 3。为了区分它们，你可以使用`python2`或`python3`，以及`pip2`或`pip3`来调用Python或Pip的特定版本。

### Python和Pip的别名

在你的shell配置文件中，你可以设置别名，以便更容易地调用Python和Pip。例如，如果你的系统的默认`python`命令是Python 2，你可能希望设置一个别名，让`python`实际上调用Python 3。你可以通过在`.bash_profile`中添加以下行来做到这一点：

```bash
alias python=python3
alias pip=pip3
```

设置这些别名后，当你在终端中输入`python`或`pip`时，实际上你会调用`python3`或`pip3`。

### Python和Pip的系统路径

在Unix-like的系统中，`PATH`环境变量定义了shell在哪里寻找可执行文件。当你在终端中输入一个命令时，shell会在`PATH`中列出的目录中查找该命令。

Python和Pip的可执行文件通常位于`/usr/local/bin`或用户的`~/.local/bin`。为了确保你的shell能找到Python和Pip，你需要确保这些目录在你的`PATH`中。

你可以使用`which`命令来查看特定命令的路径。例如，`which python`会显示Python解释器的路径，而`which pip`会显示Pip的路径。

注意，`which`命令忽略别名。即使你把`python`设置为`python3`的别名，`which python`仍然会显示Python 2的路径。如果你想查看一个别名实际指向的命令的路径，你需要使用`which python3`。

### Python和Pip的存储位置

Python和Pip会将包安装到特定的位置，这些位置可以通过Python的`sys.path`查看。`sys.path`是一个包含Python查找包和模块的目录的列表。当你导入一个模块时，Python会在`sys.path`中列出的目录中查找该模块。

你可以通过在Python解释器中输入以下命令查看`sys.path`：

```python
import sys
print(sys.path)
```

这将显示Python查找包和模块的目录列表。

注意，虽然Python和Pip的可执行文件可能存放在不同的目录，但它们都可以协同工作。这是因为Pip安装的包会被放在`sys.path`中，Python解释器可以在这些位置找到这些包。

### Conclusion (结论)

理解Python和Pip的版本、别名、系统路径和存储位置对于

有效使用Python和Pip是很重要的。希望这篇文章能帮助你更好地理解这些概念，并在以后的Python编程中派上用场。

