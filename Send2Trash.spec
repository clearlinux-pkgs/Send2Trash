#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x177FE67DB65D89FE (hsoft@hardcoded.net)
#
Name     : Send2Trash
Version  : 1.4.2
Release  : 1
URL      : https://pypi.python.org/packages/6a/32/7e7f66ed420fabefd7b2f30dd21f4b58689eb080704fc93cfb5319cbc054/Send2Trash-1.4.2.tar.gz
Source0  : https://pypi.python.org/packages/6a/32/7e7f66ed420fabefd7b2f30dd21f4b58689eb080704fc93cfb5319cbc054/Send2Trash-1.4.2.tar.gz
Source99 : https://pypi.python.org/packages/6a/32/7e7f66ed420fabefd7b2f30dd21f4b58689eb080704fc93cfb5319cbc054/Send2Trash-1.4.2.tar.gz.asc
Summary  : Send file to trash natively under Mac OS X, Windows and Linux.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Send2Trash-python3
Requires: Send2Trash-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Send2Trash -- Send files to trash on all platforms
        ==================================================
        
        Send2Trash is a small package that sends files to the Trash (or Recycle Bin) *natively* and on
        *all platforms*. On OS X, it uses native ``FSMoveObjectToTrashSync`` Cocoa calls, on Windows, it
        uses native (and ugly) ``SHFileOperation`` win32 calls. On other platforms, if `PyGObject`_ and
        `GIO`_ are available, it will use this.  Otherwise, it will fallback to its own implementation
        of the `trash specifications from freedesktop.org`_.
        
        ``ctypes`` is used to access native libraries, so no compilation is necessary.
        
        Send2Trash supports Python 2.7 and up (Python 3 is supported).
        
        Installation
        ------------

%package python
Summary: python components for the Send2Trash package.
Group: Default
Requires: Send2Trash-python3
Provides: send2trash-python

%description python
python components for the Send2Trash package.


%package python3
Summary: python3 components for the Send2Trash package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Send2Trash package.


%prep
%setup -q -n Send2Trash-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517760977
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
