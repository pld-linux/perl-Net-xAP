#
# Conditional build:
# _with_tests - perform "make test" (requires IMAP server)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	xAP
Summary:	Net::xAP Perl module - interface to IMAP/ACAP/IMSP/ICAP protocol family
Summary(pl):	Modu� Perla Net::xAP - interfejs do rodziny protoko��w IMAP/ACAP/IMSP/ICAP
Name:		perl-Net-xAP
Version:	0.02
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-MIME-Base64 >= 2.11
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Digest-MD5 >= 2.01
Requires:	perl-MIME-Base64 >= 2.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the protocol family represented
by IMAP, IMSP, ACAP, and ICAP. A usable IMAP module is also provide.
Warning: this is an alpha release!

%description -l pl
Ten modu� udost�pnia interfejs do rodziny protoko��w reprezentowanej
przez IMAP, IMSP, ACAP i ICAP. Do��czony jest tak�e u�ywalny modu�
IMAP. Uwaga: to jest wersja alpha!

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE BUGS CREDITS NEWS README TODO
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}