%define	module	Net-Server
%define	name	perl-%{module}
%define	version	0.94
%define	release	%mkrel 3

%define	_provides_exceptions perl(My\\|perl(Sample

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extensible, general Perl server engine
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
Requires:	perl-IO-Multiplex
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net::Server is an extensible, generic Perl server engine.  Net::Server combines
the good properties from Net::Daemon (0.34), NetServer::Generic (1.03), and
Net::FTPServer (1.0), and also from various concepts in the Apache Webserver.

%prep
%setup -q -n %{module}-%{version}  

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes examples README
%{_mandir}/*/*
%{perl_vendorlib}/Net

