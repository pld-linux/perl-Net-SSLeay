%include	/usr/lib/rpm/macros.perl
Summary:	Net-SSLeay perl module
Summary(pl):	Modu� perla Net-SSLeay
Name:		perl-Net-SSLeay
Version:	1.05
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-openssl_path.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	openssl-devel >= 0.9.4-2
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-SSLeay perl module.

%description -l pl
Modul perla Net-SSLeay.

%prep
%setup -q -n Net_SSLeay.pm-%{version}
%patch0 -p0
%patch1 -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Net/SSLeay.pm
%dir %{perl_sitearch}/auto/Net/SSLeay
%{perl_sitearch}/auto/Net/SSLeay/autosplit.ix
%{perl_sitearch}/auto/Net/SSLeay/*.al
%{perl_sitearch}/auto/Net/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/SSLeay/SSLeay.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
