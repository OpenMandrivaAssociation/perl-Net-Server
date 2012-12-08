%define	upstream_name	 Net-Server
%define upstream_version 0.99

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(My(.*)\\)|perl\\(Sample(.*)\\)'
%else
%define	_provides_exceptions perl(My\\|perl(Sample
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Extensible, general Perl server engine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
BuildRequires:	perl-devel
Requires:	perl-IO-Multiplex
BuildArch:	noarch

%description
Net::Server is an extensible, generic Perl server engine.  Net::Server combines
the good properties from Net::Daemon (0.34), NetServer::Generic (1.03), and
Net::FTPServer (1.0), and also from various concepts in the Apache Webserver.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes examples README
%{_mandir}/*/*
%{perl_vendorlib}/Net


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.990.0-6mdv2012.0
+ Revision: 765533
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.990.0-5
+ Revision: 764057
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.990.0-4
+ Revision: 763096
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.990.0-3
+ Revision: 667280
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.990.0-2mdv2011.0
+ Revision: 564753
- rebuild for perl 5.12.1

* Fri Jul 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.990.0-1mdv2011.0
+ Revision: 554302
- update to 0.99

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.970.0-1mdv2010.1
+ Revision: 404244
- rebuild using %%perl_convert_version

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.97-4mdv2010.0
+ Revision: 400298
- rebuild for properly versioned dependencies

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.97-3mdv2009.0
+ Revision: 223905
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.97-2mdv2008.1
+ Revision: 180529
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.97-1mdv2008.0
+ Revision: 55819
- update to new version 0.97

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.96-1mdv2008.0
+ Revision: 20672
- 0.96


* Sun Sep 03 2006 Scott Karns <scottk@mandriva.org> 0.94-3mdv2007.0
- Added Requires perl-IO-Multiplex (fixes bug #25086)

* Sun Sep 03 2006 Scott Karns <scottk@mandriva.org> 0.94-2mdv2007.0
- Added BuildRequires and _provides_exceptions

* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.94-1mdv2007.0
- new version

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.93-1mdk
- New release 0.93

* Fri Mar 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdk
- New release 0.91

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.90-1mdk
- New release 0.90
- spec cleanup
- fix directory ownership
- rpmbuildupdate aware

* Mon Dec 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.89-1mdk
- 0.89

* Tue Jun 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.88-1mdk
- 0.88
- spec cleanup

* Fri Jun 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.87-3mdk
- Rebuild

* Fri Dec 10 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.87-2mdk 
- fix file permissions

* Fri Apr 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.87-1mdk
- 0.87
- initial package

* Thu Sep 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.85-3mdk
- requires perl-IO-Multiplex

