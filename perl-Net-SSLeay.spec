%include	/usr/lib/rpm/macros.perl
Summary:	Net-SSLeay perl module
Summary(pl):	Modu³ perla Net-SSLeay
Name:		perl-Net-SSLeay
Version:	1.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net_SSLeay.pm-%{version}.tar.gz
Patch0:		perl-Net-SSLeay-paths.patch
Patch1:		perl-Net-SSLeay-openssl_path.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	openssl-devel >= 0.9.4-2
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-SSLeay perl module

%description -l pl
Modul perla Net-SSLeay

%prep
%setup -q -n Net_SSLeay.pm-%{version}
%patch0 -p0
%patch1 -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Net/SSLeay/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/SSLeay
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Net/SSLeay.pm

%dir %{perl_sitearch}/auto/Net/SSLeay
%{perl_sitearch}/auto/Net/SSLeay/.packlist
%{perl_sitearch}/auto/Net/SSLeay/autosplit.ix
%{perl_sitearch}/auto/Net/SSLeay/*.al
%{perl_sitearch}/auto/Net/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/SSLeay/SSLeay.so

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
