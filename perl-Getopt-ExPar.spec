%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	ExPar
Summary:	Getopt::ExPar - extended parameters command line parser
Summary(pl):	Getopt::ExPar - analizator rozszerzonych parametrów w linii polecenia
Name:		perl-Getopt-ExPar
Version:	0.01
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fffd02338188405e89d52f855cae8fc
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::ExPar Perl module is extended parameters command line parser.

%description -l pl
Modu³ Perla Getopt::ExPar jest analizatorem rozszerzonych parametrów w
linii polecenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/ExPar.pm
%{perl_vendorlib}/Getopt/Reference_Parser.pm
%{perl_vendorlib}/Getopt/expar_test.pl
%{_mandir}/man3/*
