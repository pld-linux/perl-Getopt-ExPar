%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-ExPar perl module
Summary(pl):	Modu³ perla Getopt-ExPar
Name:		perl-Getopt-ExPar
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-ExPar-%{version}.tar.gz
Patch:		perl-Getopt-ExPar-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-ExPar - Extended Parameters command line parser.

%description -l pl
Modu³ perla Getopt-ExPar.

%prep
%setup -q -n Getopt-ExPar-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Getopt/ExPar
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Getopt/ExPar.pm
%{perl_sitelib}/Getopt/Reference_Parser.pm
%{perl_sitelib}/Getopt/expar_test.pl
%{perl_sitearch}/auto/Getopt/ExPar

%{_mandir}/man3/*
