#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires IMAP server)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	xAP
Summary:	Net::xAP Perl module - interface to IMAP/ACAP/IMSP/ICAP protocol family
Summary(pl):	Modu³ Perla Net::xAP - interfejs do rodziny protoko³ów IMAP/ACAP/IMSP/ICAP
Name:		perl-Net-xAP
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	df6ddaa8dad8d366784bf9a2a1f8eed1
BuildRequires:	perl-devel >= 1:5.8.0
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
Ten modu³ udostêpnia interfejs do rodziny protoko³ów reprezentowanej
przez IMAP, IMSP, ACAP i ICAP. Do³±czony jest tak¿e u¿ywalny modu³
IMAP. Uwaga: to jest wersja alpha!

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
