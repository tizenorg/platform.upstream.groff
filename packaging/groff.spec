#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

%{!?with_x:%define with_x 0}

Name:           groff
Version:        1.20.1
Release:        1
License:        GPLv3+ and GFDL and BSC and MIT
Summary:        A document formatting system
Url:            http://groff.ffii.org
Group:          Applications/Publishing
Source:         %{name}-%{version}.tar.bz2
Patch1:         groff-info-missing-x11.patch
Patch2:         groff-japanese-charclass.patch
Patch3:         groff-japanese-wcwidth.patch
BuildRequires:  bison
BuildRequires:  zlib-devel
Requires:       /usr/bin/mktemp

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more.

Groff can also be used to format man pages. If you are going to use
groff with the X Window System, you will also need to install the
groff-gxditview package.

%package perl
Summary:        Parts of the groff formatting system that require Perl
Group:          Applications/Publishing

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor
for creating PostScript font files, the grog utility that can be used
to automatically determine groff command-line options, and the
troff-to-ps print filter.

%if %{with_x}
%package gxditview
Summary:        An X previewer for groff text processor output
Group:          Applications/Publishing
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel

%description gxditview
Gxditview displays the groff text processor's output on an X Window
System display.
%endif

%package doc
Summary:        Documentation for groff document formatting system
Group:          Documentation
Requires:       groff = %{version}

%description doc
The groff-doc package includes additional documentation for groff
text processor package. It contains examples, documentation for PIC
language and documentation for creating PDF files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure --enable-multibyte
make

%install
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_infodir}
make install manroot=%{buildroot}%{_mandir} \
			bindir=%{buildroot}%{_bindir} \
			mandir=%{buildroot}%{_mandir} \
			prefix=%{buildroot}/usr \
			exec_prefix=%{buildroot}/usr \
			sbindir=%{buildroot}%{_exec_prefix}/sbin \
			sysconfdir=%{buildroot}/etc \
			datadir=%{buildroot}/usr/share \
			infodir=%{buildroot}/%{_prefix}/info \
			sysconfdir=%{buildroot}/etc \
			includedir=%{buildroot}/usr/include \
			libdir=%{buildroot}/%{_libdir} \
			libexecdir=%{buildroot}/usr/libexec \
			localstatedir=%{buildroot}/var \
			sharedstatedir=%{buildroot}/usr/com \
			infodir=%{buildroot}/usr/share/info

#install -m 644 doc/groff.info* %{buildroot}/%{_infodir}
ln -s s.tmac %{buildroot}%{_datadir}/groff/%{version}/tmac/gs.tmac
ln -s mse.tmac %{buildroot}%{_datadir}/groff/%{version}/tmac/gmse.tmac
ln -s m.tmac %{buildroot}%{_datadir}/groff/%{version}/tmac/gm.tmac
ln -s troff	%{buildroot}%{_bindir}/gtroff
ln -s tbl %{buildroot}%{_bindir}/gtbl
ln -s pic %{buildroot}%{_bindir}/gpic
ln -s eqn %{buildroot}%{_bindir}/geqn
ln -s neqn %{buildroot}%{_bindir}/gneqn
ln -s refer %{buildroot}%{_bindir}/grefer
ln -s lookbib %{buildroot}%{_bindir}/glookbib
ln -s indxbib %{buildroot}%{_bindir}/gindxbib
ln -s soelim %{buildroot}%{_bindir}/gsoelim
ln -s soelim %{buildroot}%{_bindir}/zsoelim
ln -s nroff	%{buildroot}%{_bindir}/gnroff


find %{buildroot}%{_bindir} -type f -o -type l | \
	grep -v afmtodit | grep -v grog | grep -v mdoc.samples |\
	grep -v mmroff |\
	grep -v gxditview |\
	sed "s|%{buildroot}||g" | sed "s|\.[0-9]|\.*|g" > groff-files

ln -sf doc.tmac %{buildroot}%{_datadir}/groff/%{version}/tmac/docj.tmac
# installed, but not packaged in rpm
mkdir -p %{buildroot}%{_datadir}/groff/%{version}/groffer/
chmod 755 %{buildroot}%{_libdir}/groff/groffer/version.sh
mv %{buildroot}%{_libdir}/groff/groffer/* %{buildroot}/%{_datadir}/groff/%{version}/groffer/


%remove_docs

%files -f groff-files
%defattr(-,root,root,-)
%{_datadir}/groff

%files perl
%defattr(-,root,root,-)
%{_bindir}/grog
%{_bindir}/mmroff
%{_bindir}/afmtodit
