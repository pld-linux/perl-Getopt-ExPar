%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-ExPar perl module
Summary(pl):	Modu� perla Getopt-ExPar
Name:		perl-Getopt-ExPar
Version:	0.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-ExPar-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-ExPar - Extended Parameters command line parser.

%description -l pl
Modu� perla Getopt-ExPar.

%prep
%setup -q -n Getopt-ExPar-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Getopt/ExPar.pm
%{perl_sitelib}/Getopt/Reference_Parser.pm
%{perl_sitelib}/Getopt/expar_test.pl
%{_mandir}/man3/*
