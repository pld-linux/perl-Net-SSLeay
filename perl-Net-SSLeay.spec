%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSLeay - Perl extension for using OpenSSL or SSLeay
Summary(pl):	Net::SSLeay - rozszerzenie perla do u�ywania OpenSSL lub SSLeay
Name:		perl-Net-SSLeay
Version:	1.20
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	openssl-tools
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers some high level convinience functions for accessing web
pages on SSL servers, a sslcat() function for writing your own clients,
and finally access to the SSL api of SSLeay/OpenSSL package so you can
write servers or clients for more complicated applications.

# %description -l pl
# TODO

%prep
%setup -q -n Net_SSLeay.pm-%{version}
%patch0 -p0

%build
perl Makefile.PL %{_prefix}
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/*.{pl,conf} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Net/SSLeay.pm
%{perl_sitearch}/Net/SSLeay
%{perl_sitearch}/Net/ptrtstrun.pl
%dir %{perl_sitearch}/auto/Net/SSLeay
%{perl_sitearch}/auto/Net/SSLeay/autosplit.ix
%{perl_sitearch}/auto/Net/SSLeay/*.al
%{perl_sitearch}/auto/Net/SSLeay/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/SSLeay/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
