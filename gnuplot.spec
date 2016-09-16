#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnuplot
Version  : 5.0.4
Release  : 3
URL      : http://downloads.sourceforge.net/project/gnuplot/gnuplot/5.0.4/gnuplot-5.0.4.tar.gz
Source0  : http://downloads.sourceforge.net/project/gnuplot/gnuplot/5.0.4/gnuplot-5.0.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : gnuplot
Requires: gnuplot-bin
Requires: gnuplot-data
Requires: gnuplot-doc
BuildRequires : emacs
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(pango)
BuildRequires : readline-dev

%description
The Gnuplot Plotting Utility
****************************
Gnuplot is a command-line driven interactive function plotting utility
for linux, OSX, MSWin, VMS, and many other platforms.  The software is
copyrighted but freely distributed (i.e., you don't have to pay for it).
It was originally intended as graphical program to allow scientists
and students to visualize mathematical functions and data.  Gnuplot
supports many different types of terminals, plotters, and printers
(including many color devices, and pseudo-devices like LaTeX) and is
easily extensible to include new devices.

%package bin
Summary: bin components for the gnuplot package.
Group: Binaries
Requires: gnuplot-data

%description bin
bin components for the gnuplot package.


%package data
Summary: data components for the gnuplot package.
Group: Data

%description data
data components for the gnuplot package.


%package doc
Summary: doc components for the gnuplot package.
Group: Documentation

%description doc
doc components for the gnuplot package.


%prep
%setup -q -n gnuplot-5.0.4

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnuplot
/usr/libexec/gnuplot/5.0/gnuplot_x11

%files data
%defattr(-,root,root,-)
/usr/share/gnuplot/5.0/PostScript/8859-1.ps
/usr/share/gnuplot/5.0/PostScript/8859-15.ps
/usr/share/gnuplot/5.0/PostScript/8859-2.ps
/usr/share/gnuplot/5.0/PostScript/8859-9.ps
/usr/share/gnuplot/5.0/PostScript/aglfn.txt
/usr/share/gnuplot/5.0/PostScript/cp1250.ps
/usr/share/gnuplot/5.0/PostScript/cp1251.ps
/usr/share/gnuplot/5.0/PostScript/cp1252.ps
/usr/share/gnuplot/5.0/PostScript/cp437.ps
/usr/share/gnuplot/5.0/PostScript/cp850.ps
/usr/share/gnuplot/5.0/PostScript/cp852.ps
/usr/share/gnuplot/5.0/PostScript/koi8r.ps
/usr/share/gnuplot/5.0/PostScript/koi8u.ps
/usr/share/gnuplot/5.0/PostScript/prologue.ps
/usr/share/gnuplot/5.0/PostScript/utf-8.ps
/usr/share/gnuplot/5.0/app-defaults/Gnuplot
/usr/share/gnuplot/5.0/colors_default.gp
/usr/share/gnuplot/5.0/colors_mono.gp
/usr/share/gnuplot/5.0/colors_podo.gp
/usr/share/gnuplot/5.0/gnuplot.gih
/usr/share/gnuplot/5.0/gnuplotrc
/usr/share/gnuplot/5.0/js/README
/usr/share/gnuplot/5.0/js/canvasmath.js
/usr/share/gnuplot/5.0/js/canvastext.js
/usr/share/gnuplot/5.0/js/gnuplot_common.js
/usr/share/gnuplot/5.0/js/gnuplot_dashedlines.js
/usr/share/gnuplot/5.0/js/gnuplot_mouse.css
/usr/share/gnuplot/5.0/js/gnuplot_mouse.js
/usr/share/gnuplot/5.0/js/gnuplot_svg.js
/usr/share/gnuplot/5.0/js/grid.png
/usr/share/gnuplot/5.0/js/help.png
/usr/share/gnuplot/5.0/js/nextzoom.png
/usr/share/gnuplot/5.0/js/previouszoom.png
/usr/share/gnuplot/5.0/js/return.png
/usr/share/gnuplot/5.0/js/textzoom.png
/usr/share/gnuplot/5.0/lua/gnuplot-tikz.lua

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
