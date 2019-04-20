#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : assimp
Version  : 4.1.0
Release  : 3
URL      : https://github.com/assimp/assimp/archive/v4.1.0.tar.gz
Source0  : https://github.com/assimp/assimp/archive/v4.1.0.tar.gz
Summary  : Import various well-known 3D model formats in an uniform manner.
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 LGPL-2.1 LGPL-3.0 MIT Unlicense
Requires: assimp-bin
Requires: assimp-lib
Requires: assimp-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cmake(Qt5Widgets)
BuildRequires : freeglut-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : python3
BuildRequires : qtbase-extras
BuildRequires : zlib-dev

%description
See Readme.md

%package bin
Summary: bin components for the assimp package.
Group: Binaries
Requires: assimp-license

%description bin
bin components for the assimp package.


%package dev
Summary: dev components for the assimp package.
Group: Development
Requires: assimp-lib
Requires: assimp-bin
Provides: assimp-devel

%description dev
dev components for the assimp package.


%package doc
Summary: doc components for the assimp package.
Group: Documentation

%description doc
doc components for the assimp package.


%package lib
Summary: lib components for the assimp package.
Group: Libraries
Requires: assimp-license

%description lib
lib components for the assimp package.


%package license
Summary: license components for the assimp package.
Group: Default

%description license
license components for the assimp package.


%prep
%setup -q -n assimp-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536618915
mkdir -p clr-build
pushd clr-build
%cmake .. -DASSIMP_LIB_INSTALL_DIR=lib64
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536618915
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/assimp
cp LICENSE %{buildroot}/usr/share/doc/assimp/LICENSE
cp contrib/clipper/License.txt %{buildroot}/usr/share/doc/assimp/contrib_clipper_License.txt
cp contrib/gtest/LICENSE %{buildroot}/usr/share/doc/assimp/contrib_gtest_LICENSE
cp contrib/openddlparser/LICENSE %{buildroot}/usr/share/doc/assimp/contrib_openddlparser_LICENSE
cp contrib/poly2tri/LICENSE %{buildroot}/usr/share/doc/assimp/contrib_poly2tri_LICENSE
cp contrib/rapidjson/license.txt %{buildroot}/usr/share/doc/assimp/contrib_rapidjson_license.txt
cp contrib/zip/UNLICENSE %{buildroot}/usr/share/doc/assimp/contrib_zip_UNLICENSE
cp packaging/windows-innosetup/LICENSE.rtf %{buildroot}/usr/share/doc/assimp/packaging_windows-innosetup_LICENSE.rtf
cp samples/DevIL/COPYING %{buildroot}/usr/share/doc/assimp/samples_DevIL_COPYING
cp test/models-nonbsd/Ogre/OgreSDK/LICENSE %{buildroot}/usr/share/doc/assimp/test_models-nonbsd_Ogre_OgreSDK_LICENSE
cp test/models-nonbsd/PLY/ant-half.ply.license %{buildroot}/usr/share/doc/assimp/test_models-nonbsd_PLY_ant-half.ply.license
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/assimp

%files dev
%defattr(-,root,root,-)
/usr/include/assimp/Compiler/poppack1.h
/usr/include/assimp/Compiler/pstdint.h
/usr/include/assimp/Compiler/pushpack1.h
/usr/include/assimp/DefaultIOStream.h
/usr/include/assimp/DefaultIOSystem.h
/usr/include/assimp/DefaultLogger.hpp
/usr/include/assimp/Defines.h
/usr/include/assimp/Exporter.hpp
/usr/include/assimp/IOStream.hpp
/usr/include/assimp/IOSystem.hpp
/usr/include/assimp/Importer.hpp
/usr/include/assimp/LogStream.hpp
/usr/include/assimp/Logger.hpp
/usr/include/assimp/NullLogger.hpp
/usr/include/assimp/ProgressHandler.hpp
/usr/include/assimp/SceneCombiner.h
/usr/include/assimp/ai_assert.h
/usr/include/assimp/anim.h
/usr/include/assimp/camera.h
/usr/include/assimp/cexport.h
/usr/include/assimp/cfileio.h
/usr/include/assimp/cimport.h
/usr/include/assimp/color4.h
/usr/include/assimp/color4.inl
/usr/include/assimp/config.h
/usr/include/assimp/defs.h
/usr/include/assimp/importerdesc.h
/usr/include/assimp/light.h
/usr/include/assimp/material.h
/usr/include/assimp/material.inl
/usr/include/assimp/matrix3x3.h
/usr/include/assimp/matrix3x3.inl
/usr/include/assimp/matrix4x4.h
/usr/include/assimp/matrix4x4.inl
/usr/include/assimp/mesh.h
/usr/include/assimp/metadata.h
/usr/include/assimp/postprocess.h
/usr/include/assimp/quaternion.h
/usr/include/assimp/quaternion.inl
/usr/include/assimp/scene.h
/usr/include/assimp/texture.h
/usr/include/assimp/types.h
/usr/include/assimp/vector2.h
/usr/include/assimp/vector2.inl
/usr/include/assimp/vector3.h
/usr/include/assimp/vector3.inl
/usr/include/assimp/version.h
/usr/lib64/cmake/assimp-4.1/assimp-config-version.cmake
/usr/lib64/cmake/assimp-4.1/assimp-config.cmake
/usr/lib64/libassimp.so
/usr/lib64/pkgconfig/assimp.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/assimp/contrib_clipper_License.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libassimp.so.4
/usr/lib64/libassimp.so.4.1.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/assimp/LICENSE
/usr/share/doc/assimp/contrib_gtest_LICENSE
/usr/share/doc/assimp/contrib_openddlparser_LICENSE
/usr/share/doc/assimp/contrib_poly2tri_LICENSE
/usr/share/doc/assimp/contrib_rapidjson_license.txt
/usr/share/doc/assimp/contrib_zip_UNLICENSE
/usr/share/doc/assimp/packaging_windows-innosetup_LICENSE.rtf
/usr/share/doc/assimp/samples_DevIL_COPYING
/usr/share/doc/assimp/test_models-nonbsd_Ogre_OgreSDK_LICENSE
/usr/share/doc/assimp/test_models-nonbsd_PLY_ant-half.ply.license