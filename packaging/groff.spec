Name:           groff
Version:        1.22.2
Release:        0
License:        BSD-3-Clause and GPL-2.0+
Summary:        A document formatting system
Url:            http://groff.ffii.org
Group:          Base/Utilities
Source:         %{name}-%{version}.tar.gz
Source1001:     groff.manifest
BuildRequires:  bison
BuildRequires:  zlib-devel
BuildRequires:  fdupes
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

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor
for creating PostScript font files, the grog utility that can be used
to automatically determine groff command-line options, and the
troff-to-ps print filter.


%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --enable-multibyte
%__make

%install
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_infodir}
%make_install manroot=%{buildroot}%{_mandir} \
              bindir=%{buildroot}%{_bindir} \
              mandir=%{buildroot}%{_mandir} \
              prefix=%{buildroot}%{_prefix} \
              exec_prefix=%{buildroot}%{_prefix} \
              sbindir=%{buildroot}%{_exec_prefix}/sbin \
              sysconfdir=%{buildroot}%{_sysconfdir} \
              datadir=%{buildroot}%{_datadir} \
              infodir=%{buildroot}%{_prefix}/info \
              sysconfdir=%{buildroot}%{_sysconfdir}\
              includedir=%{buildroot}%{_includedir} \
              libdir=%{buildroot}%{_libdir} \
              libexecdir=%{buildroot}%{_prefix}/libexec \
              localstatedir=%{buildroot}/var \
              sharedstatedir=%{buildroot}%{_prefix}/com \
              infodir=%{buildroot}%{_infodir}

#install -m 644 doc/groff.info* %%{buildroot}%%{_infodir}
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
    grep -v afmtodit | grep -v grog | grep -v mdoc.samples | \
    grep -v mmroff | \
    grep -v gxditview | \
    sed "s|%{buildroot}||g" | sed "s|\.[0-9]|\.*|g" > groff-files

ln -sf doc.tmac %{buildroot}%{_datadir}/%{name}/%{version}/tmac/docj.tmac
# installed, but not packaged in rpm
mkdir -p %{buildroot}%{_datadir}/%{name}/%{version}/groffer/
chmod 755 %{buildroot}%{_libdir}/%{name}/groffer/version.sh
mv %{buildroot}%{_libdir}/%{name}/groffer/* %{buildroot}/%{_datadir}/%{name}/%{version}/groffer/

%fdupes %{buildroot}

%remove_docs

%files -f %{name}-files
%license COPYING LICENSES
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_datadir}/%{name}

%files perl
%license COPYING LICENSES
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_bindir}/grog
%{_bindir}/mmroff
%{_bindir}/afmtodit
