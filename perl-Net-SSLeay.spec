%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSLeay perl module
Summary(pl):	Modu³ perla Net::SSLeay
Name:		perl-Net-SSLeay
Version:	1.16
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	openssl-tools
BuildRequires:	perl >= 5.6.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSLeay perl module.

%description -l pl
Modul perla Net::SSLeay.

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

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Net/SSLeay.pm
%{perl_sitearch}/Net/SSLeay
%{perl_sitearch}/Net/ptrtstrun.pl
%{perl_sitearch}/auto/Net/SSLeay
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
