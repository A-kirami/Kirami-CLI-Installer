# Kirami CLI Installer

[![Netlify Status](https://api.netlify.com/api/v1/badges/98d5b5b3-47dc-4c1b-a62d-99ea08d37801/deploy-status)](https://app.netlify.com/sites/install-kirami/deploys)

该存储库包含 Kirami CLI 的官方安装脚本和相关托管配置。

该脚本托管在 [Netlify](https://www.netlify.com) 上，并可在 https://install.kiramibot.dev/ 上获取。

## 使用方法

Kirami CLI 提供了一个自定义的安装器，将会安装在你系统的隔离环境中。

> [!WARNING]
> 此安装程序不支持 Python 版本 < 3.10。

### osx / linux / bashonwindows / Windows+MinGW 安装指南

```bash
curl -sSL https://install.kiramibot.dev | python3 -
```

### Windows PowerShell 安装指南

```powershell
(Invoke-WebRequest -Uri https://install.kiramibot.dev -UseBasicParsing).Content | py -
```

> [!NOTE]
> 如果你通过 Microsoft Store 安装了 Python，请在上述命令中用 `python` 替代 `py`。

安装程序将 `kirami-cli` 工具安装在 Kirami CLI 的 `bin` 目录下。此位置取决于你的系统：

- Unix 系统：`$HOME/.local/bin`
- Windows 系统：`%APPDATA%\Python\Scripts`

如果此目录不在你的 `PATH` 中，并且你想通过简单的 `kirami` 命令来调用 Kirami CLI，那么你需要手动添加该目录。

或者，你可以使用完整路径来使用 `kirami`。

一旦安装了 Kirami CLI，你可以执行以下操作：

```bash
kirami -V
```

如果你看到类似 `Kirami CLI, version 0.1.0` 的信息，那么你就可以使用 Kirami CLI 了。

如果你决定不再使用 Kirami CLI，你可以通过再次运行安装程序并使用 `--uninstall` 选项，
或者在执行安装程序之前设置 `KIRAMI_UNINSTALL` 环境变量来从系统中彻底删除它：

```bash
curl -sSL https://install.kiramibot.dev | python3 - --uninstall
curl -sSL https://install.kiramibot.dev | KIRAMI_UNINSTALL=1 python3 -
```

默认情况下，Kirami CLI 安装在用户特定的平台主目录下。
如果你希望更改此设置，可以定义 `KIRAMI_HOME` 环境变量：

```bash
curl -sSL https://install.kiramibot.dev | KIRAMI_HOME=/etc/kirami python3 -
```

如果你希望安装预发布版本，可以通过传递 `--preview` 选项或使用 `KIRAMI_PREVIEW` 环境变量来执行：

```bash
curl -sSL https://install.kiramibot.dev | python3 - --preview
curl -sSL https://install.kiramibot.dev | KIRAMI_PREVIEW=1 python3 -
```

类似地，如果你想安装特定版本，可以使用 `--version` 选项或 `KIRAMI_VERSION` 环境变量：

```bash
curl -sSL https://install.kiramibot.dev | python3 - --version 0.1.0
curl -sSL https://install.kiramibot.dev | KIRAMI_VERSION=0.1.0 python3 -
```

你还可以通过使用 `--git` 选项从 `git` 存储库安装 Kirami CLI：

```bash
curl -sSL https://install.kiramibot.dev | python3 - --git https://github.com/A-kirami/KiramiCLI.git@main
```

## 已知问题

### Debian/Ubuntu

在 Debian 和 Ubuntu 系统上，由于各种原因，可能会出现各种问题，这些问题可能是由于 Python 标准库组件的打包和配置方式而引起的。
以下是我们目前已经了解到的问题以及潜在的解决方法。

> [!WARNING]
> 这也可能影响 Windows 上的 WSL 用户。

#### 安装布局

如果遇到类似以下错误的情况，可能是由于 [pypa/virtualenv#2350](https://github.com/pypa/virtualenv/issues/2350) 导致的：

```console
FileNotFoundError: [Errno 2] No such file or directory: '/root/.local/share/kirami-cli/venv/bin/python'
```

你可以通过将 `DEB_PYTHON_INSTALL_LAYOUT` 环境变量设置为 `deb` 来解决此问题，以模拟先前的工作行为：

```bash
export DEB_PYTHON_INSTALL_LAYOUT=deb
```

#### 缺少 `distutils` 模块

在某些 Debian/Ubuntu 环境中，你可能会在错误日志 (`kirami-installer-error-*.log`) 中遇到以下错误消息：

```console
ModuleNotFoundError: No module named 'distutils.cmd'
```

这可能是由于 [此 bug](https://bugs.launchpad.net/ubuntu/+source/python3.10/+bug/1940705) 导致的。
还请参阅 [pypa/get-pip#124](https://github.com/pypa/get-pip/issues/124)。

已知解决此问题的方法是重新安装发行版提供的 `distutils` 包：

```bash
apt-get install --reinstall python3-distutils
```

如果你安装了特定的 Python 版本，例如 `3.10`，你可能需要使用包名 `python3.10-distutils`。

## 声明

本项目代码基于 [python-poetry/install.python-poetry.org](https://github.com/python-poetry/install.python-poetry.org) 修改而来。
