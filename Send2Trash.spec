#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Send2Trash
Version  : 1.8.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/49/2c/d990b8d5a7378dde856f5a82e36ed9d6061b5f2d00f39dc4317acd9538b4/Send2Trash-1.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/2c/d990b8d5a7378dde856f5a82e36ed9d6061b5f2d00f39dc4317acd9538b4/Send2Trash-1.8.0.tar.gz
Summary  : Send file to trash natively under Mac OS X, Windows and Linux.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Send2Trash-bin = %{version}-%{release}
Requires: Send2Trash-license = %{version}-%{release}
Requires: Send2Trash-python = %{version}-%{release}
Requires: Send2Trash-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==================================================
Send2Trash -- Send files to trash on all platforms
==================================================

%package bin
Summary: bin components for the Send2Trash package.
Group: Binaries
Requires: Send2Trash-license = %{version}-%{release}

%description bin
bin components for the Send2Trash package.


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
%setup -q -n Send2Trash-1.8.0
cd %{_builddir}/Send2Trash-1.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629141631
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Send2Trash
cp %{_builddir}/Send2Trash-1.8.0/LICENSE %{buildroot}/usr/share/package-licenses/Send2Trash/c5ae6f02e99bafb0c28a83cf9ba7ce6a81f2872e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/send2trash

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Send2Trash/c5ae6f02e99bafb0c28a83cf9ba7ce6a81f2872e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
