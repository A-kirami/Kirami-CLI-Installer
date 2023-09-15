from pathlib import Path

import python_minifier

dist = Path("dist")
dist.mkdir(exist_ok=True)

installer = Path("install-kirami.py")
installer_min = dist / "install-kirami.min.py"

installer_min.write_text(python_minifier.minify(installer.read_text()))
