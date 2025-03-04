# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['index.py'],
    pathex=[],
    binaries=[],
    datas=[('home.ui', '.'), ('login.ui', '.'), ('library_data.db', '.'), ('themes/*', 'themes/'), ('icons/*', 'icons/'), ('icons.qrc', '.')],
    hiddenimports=['icons_rc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LibrarySystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icons/library.icns'],
)
app = BUNDLE(
    exe,
    name='LibrarySystem.app',
    icon='icons/library.icns',
    bundle_identifier=None,
)
