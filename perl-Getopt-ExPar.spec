%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	ExPar
Summary:	Getopt-ExPar perl module
Summary(pl):	Modu³ perla Getopt-ExPar
Name:		perl-Getopt-ExPar
Version:	0.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-ExPar - Extended Parameters command line parser.

%description -l pl
Modu³ perla Getopt-ExPar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
