#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSLeay - Perl extension for using OpenSSL or SSLeay
Summary(pl.UTF-8):	Net::SSLeay - rozszerzenie Perla do używania OpenSSL lub SSLeay
Name:		perl-Net-SSLeay
Version:	1.55
Release:	1
# same as openssl
License:	Apache-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/Net-SSLeay-%{version}.tar.gz
# Source0-md5:	473b8d66ca69d5784bb0e428721f58e0
Patch0:		%{name}-no_zlib.patch
URL:		http://search.cpan.org/dist/Net-SSLeay/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Test-Simple >= 0.60_01
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers some high level convinience functions for accessing
web pages on SSL servers, a sslcat() function for writing your own
clients, and finally access to the SSL api of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%description -l pl.UTF-8
Ten moduł oferuje kilka wygodnych funkcji wysokiego poziomu służących
do dostępu do stron WWW na serwerach SSL, funkcję sslcat() do pisania
własnych klientów, oraz dostęp do API SSL pakietu SSLeay/OpenSSL, co
pozwala na pisanie serwerów lub klientów dla bardziej skomplikowanych
aplikacji.

%prep
%setup -q -n Net-SSLeay-%{version}
%patch0 -p1

%build
echo "n" | %{__perl} Makefile.PL %{_prefix} \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:echo "n" | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.{pl,conf} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Net/SSLeay.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README
%{perl_vendorarch}/Net/SSLeay.pm
%{perl_vendorarch}/Net/SSLeay
%dir %{perl_vendorarch}/auto/Net/SSLeay
%{perl_vendorarch}/auto/Net/SSLeay/autosplit.ix
%{perl_vendorarch}/auto/Net/SSLeay/*.al
%{perl_vendorarch}/auto/Net/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/SSLeay/SSLeay.so
%{_mandir}/man3/Net::SSLeay*.3pm*
%{_examplesdir}/%{name}-%{version}
