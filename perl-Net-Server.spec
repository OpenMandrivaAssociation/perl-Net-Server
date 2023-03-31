%define	modname	Net-Server
%define modver 2.008

%global __provides_exclude perl\\(My|perl\\(Sample

Summary:	Extensible, general Perl server engine
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(ExtUtils::MakeMaker)
Requires:	perl-IO-Multiplex

%description
Net::Server is an extensible, generic Perl server engine.  Net::Server combines
the good properties from Net::Daemon (0.34), NetServer::Generic (1.03), and
Net::FTPServer (1.0), and also from various concepts in the Apache Webserver.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes examples README
%{perl_vendorlib}/Net
%doc %{_mandir}/man3/*
%{_bindir}/net-server
%doc %{_mandir}/man1/net-server.1*
