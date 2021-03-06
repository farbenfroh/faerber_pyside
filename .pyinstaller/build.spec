# -*- mode: python ; coding: utf-8 -*-
import sys

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(
    ["../src/main.py"],
    pathex=[],
    binaries=[],
    datas=[] + collect_data_files("ImageGoNord"),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["PySide6.QtQml"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=os.path.join("dist", ("faerber" if sys.platform == "linux" else "faerber")),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name="faerber.app",
        icon=None,
        info_plist={
                'CFBundleURLTypes': [{
                    'CFBundleURLName': 'faerber',
                    'CFBundleTypeRole': 'Viewer',
                    'CFBundleURLSchemes': ['faerber']
                }]
            }
        )
