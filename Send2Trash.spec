#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x177FE67DB65D89FE (hsoft@hardcoded.net)
#
Name     : Send2Trash
Version  : 1.5.0
Release  : 23
URL      : https://pypi.python.org/packages/13/2e/ea40de0304bb1dc4eb309de90aeec39871b9b7c4bd30f1a3cdcb3496f5c0/Send2Trash-1.5.0.tar.gz
Source0  : https://pypi.python.org/packages/13/2e/ea40de0304bb1dc4eb309de90aeec39871b9b7c4bd30f1a3cdcb3496f5c0/Send2Trash-1.5.0.tar.gz
Source1  : https://pypi.python.org/packages/13/2e/ea40de0304bb1dc4eb309de90aeec39871b9b7c4bd30f1a3cdcb3496f5c0/Send2Trash-1.5.0.tar.gz.asc
Summary  : Send file to trash natively under Mac OS X, Windows and Linux.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Send2Trash-license = %{version}-%{release}
Requires: Send2Trash-python = %{version}-%{release}
Requires: Send2Trash-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

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

%package license
Summary: license components for the Send2Trash package.
Group: Default

%description license
license components for the Send2Trash package.


%package python
Summary: python components for the Send2Trash package.
Group: Default
Requires: Send2Trash-python3 = %{version}-%{release}
Provides: send2trash-python

%description python
python components for the Send2Trash package.


%package python3
Summary: python3 components for the Send2Trash package.
Group: Default
Requires: python3-core
Provides: pypi(send2trash)

%description python3
python3 components for the Send2Trash package.


%prep
%setup -q -n Send2Trash-1.5.0
cd %{_builddir}/Send2Trash-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603404010
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Send2Trash
cp %{_builddir}/Send2Trash-1.5.0/LICENSE %{buildroot}/usr/share/package-licenses/Send2Trash/3b185ec50f38a3a5da4f3be3f62eff8198fe31a5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Send2Trash/3b185ec50f38a3a5da4f3be3f62eff8198fe31a5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
