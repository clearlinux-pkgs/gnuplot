#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnuplot
Version  : 5.4.4
Release  : 35
URL      : https://sourceforge.net/projects/gnuplot/files/gnuplot/5.4.4/gnuplot-5.4.4.tar.gz
Source0  : https://sourceforge.net/projects/gnuplot/files/gnuplot/5.4.4/gnuplot-5.4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : gnuplot
Requires: gnuplot-bin = %{version}-%{release}
Requires: gnuplot-data = %{version}-%{release}
Requires: gnuplot-libexec = %{version}-%{release}
Requires: gnuplot-license = %{version}-%{release}
Requires: gnuplot-man = %{version}-%{release}
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : emacs-x11
BuildRequires : libcerf-dev
BuildRequires : llvm
BuildRequires : lua-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdlib)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libturbojpeg)
BuildRequires : pkgconfig(xpm)
BuildRequires : texlive

%description
The Gnuplot Plotting Utility
============================
Gnuplot is a command-line driven interactive function plotting utility
for linux, OSX, MSWin, VMS, and many other platforms.  The software is
copyrighted but freely distributed (i.e., you don't have to pay for it).
It was originally written to allow scientists and students to visualize
mathematical functions and data.  Gnuplot supports many different types
of terminals, plotters, and printers (including pseudo-devices like
LaTeX) and is easily extensible to include new devices.

%package bin
Summary: bin components for the gnuplot package.
Group: Binaries
Requires: gnuplot-data = %{version}-%{release}
Requires: gnuplot-libexec = %{version}-%{release}
Requires: gnuplot-license = %{version}-%{release}

%description bin
bin components for the gnuplot package.


%package data
Summary: data components for the gnuplot package.
Group: Data

%description data
data components for the gnuplot package.


%package libexec
Summary: libexec components for the gnuplot package.
Group: Default
Requires: gnuplot-license = %{version}-%{release}

%description libexec
libexec components for the gnuplot package.


%package license
Summary: license components for the gnuplot package.
Group: Default

%description license
license components for the gnuplot package.


%package man
Summary: man components for the gnuplot package.
Group: Default

%description man
man components for the gnuplot package.


%prep
%setup -q -n gnuplot-5.4.4
cd %{_builddir}/gnuplot-5.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658153975
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --with-readline=builtin \
--enable-history-file
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1658153975
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnuplot
cp %{_builddir}/gnuplot-5.4.4/Copyright %{buildroot}/usr/share/package-licenses/gnuplot/414913c1ed698f7c8f0a08c0e5d447c8bd0d66f4
cp %{_builddir}/gnuplot-5.4.4/config/MacOSX/PkgResources/License.rtf %{buildroot}/usr/share/package-licenses/gnuplot/ec56950fb609cf315c739166cf0ce4b80f4bf4d4
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnuplot

%files data
%defattr(-,root,root,-)
/usr/share/gnuplot/5.4/PostScript/8859-1.ps
/usr/share/gnuplot/5.4/PostScript/8859-15.ps
/usr/share/gnuplot/5.4/PostScript/8859-2.ps
/usr/share/gnuplot/5.4/PostScript/8859-9.ps
/usr/share/gnuplot/5.4/PostScript/aglfn.txt
/usr/share/gnuplot/5.4/PostScript/cp1250.ps
/usr/share/gnuplot/5.4/PostScript/cp1251.ps
/usr/share/gnuplot/5.4/PostScript/cp1252.ps
/usr/share/gnuplot/5.4/PostScript/cp437.ps
/usr/share/gnuplot/5.4/PostScript/cp850.ps
/usr/share/gnuplot/5.4/PostScript/cp852.ps
/usr/share/gnuplot/5.4/PostScript/koi8r.ps
/usr/share/gnuplot/5.4/PostScript/koi8u.ps
/usr/share/gnuplot/5.4/PostScript/prologue.ps
/usr/share/gnuplot/5.4/PostScript/utf-8.ps
/usr/share/gnuplot/5.4/app-defaults/Gnuplot
/usr/share/gnuplot/5.4/colors_default.gp
/usr/share/gnuplot/5.4/colors_mono.gp
/usr/share/gnuplot/5.4/colors_podo.gp
/usr/share/gnuplot/5.4/gnuplot.gih
/usr/share/gnuplot/5.4/gnuplotrc
/usr/share/gnuplot/5.4/js/README
/usr/share/gnuplot/5.4/js/canvasmath.js
/usr/share/gnuplot/5.4/js/canvastext.js
/usr/share/gnuplot/5.4/js/gnuplot_common.js
/usr/share/gnuplot/5.4/js/gnuplot_dashedlines.js
/usr/share/gnuplot/5.4/js/gnuplot_mouse.css
/usr/share/gnuplot/5.4/js/gnuplot_mouse.js
/usr/share/gnuplot/5.4/js/gnuplot_svg.js
/usr/share/gnuplot/5.4/js/gnuplot_svg_2018.js
/usr/share/gnuplot/5.4/js/grid.png
/usr/share/gnuplot/5.4/js/help.png
/usr/share/gnuplot/5.4/js/nextzoom.png
/usr/share/gnuplot/5.4/js/previouszoom.png
/usr/share/gnuplot/5.4/js/return.png
/usr/share/gnuplot/5.4/js/textzoom.png
/usr/share/gnuplot/5.4/lua/gnuplot-tikz.lua
/usr/share/gnuplot/5.4/qt/qtgnuplot_fr.qm
/usr/share/gnuplot/5.4/qt/qtgnuplot_ja.qm
/usr/share/texmf-local/tex/latex/gnuplot/gnuplot-lua-tikz-common.tex
/usr/share/texmf-local/tex/latex/gnuplot/gnuplot-lua-tikz.sty
/usr/share/texmf-local/tex/latex/gnuplot/gnuplot-lua-tikz.tex
/usr/share/texmf-local/tex/latex/gnuplot/gnuplot.cfg
/usr/share/texmf-local/tex/latex/gnuplot/t-gnuplot-lua-tikz.tex

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnuplot/5.4/gnuplot_qt
/usr/libexec/gnuplot/5.4/gnuplot_x11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnuplot/414913c1ed698f7c8f0a08c0e5d447c8bd0d66f4
/usr/share/package-licenses/gnuplot/ec56950fb609cf315c739166cf0ce4b80f4bf4d4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnuplot.1
