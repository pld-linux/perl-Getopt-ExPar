%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	ExPar
Summary:	Getopt::ExPar perl module
Summary(pl):	Modu³ perla Getopt::ExPar
Name:		perl-Getopt-ExPar
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::ExPar - Extended Parameters command line parser.

%description -l pl
Modu³ perla Getopt::ExPar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/ExPar.pm
%{perl_vendorlib}/Getopt/Reference_Parser.pm
%{perl_vendorlib}/Getopt/expar_test.pl
%{_mandir}/man3/*
