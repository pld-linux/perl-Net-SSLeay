#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSLeay - Perl extension for using OpenSSL or SSLeay
Summary(pl):	Net::SSLeay - rozszerzenie Perla do u¿ywania OpenSSL lub SSLeay
Name:		perl-Net-SSLeay
Version:	1.25
Release:	1
# same as openssl
License:	Apache-style License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
# Source0-md5:	87de8a06802fbb63c7c85e89eedbe139
Patch0:		%{name}-paths.patch
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers some high level convinience functions for accessing
web pages on SSL servers, a sslcat() function for writing your own
clients, and finally access to the SSL api of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%description -l pl
Ten modu³ oferuje kilka wygodnych funkcji wysokiego poziomu s³u¿±cych
do dostêpu do stron WWW na serwerach SSL, funkcjê sslcat() do pisania
w³asnych klientów, oraz dostêp do API SSL pakietu SSLeay/OpenSSL, co
pozwala na pisanie serwerów lub klientów dla bardziej skomplikowanych
aplikacji.

%prep
%setup -q -n Net_SSLeay.pm-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL %{_prefix} \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/*.{pl,conf} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README
%{perl_vendorarch}/Net/SSLeay.pm
%{perl_vendorarch}/Net/SSLeay
%{perl_vendorarch}/Net/ptrtstrun.pl
%dir %{perl_vendorarch}/auto/Net/SSLeay
%{perl_vendorarch}/auto/Net/SSLeay/autosplit.ix
%{perl_vendorarch}/auto/Net/SSLeay/*.al
%{perl_vendorarch}/auto/Net/SSLeay/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/SSLeay/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
