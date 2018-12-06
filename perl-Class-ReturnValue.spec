#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-ReturnValue
Version  : 0.55
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/J/JE/JESSE/Class-ReturnValue-0.55.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JE/JESSE/Class-ReturnValue-0.55.tar.gz
Summary  : A smart return value object
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Module::Install)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Class-ReturnValue package.
Group: Development
Provides: perl-Class-ReturnValue-devel = %{version}-%{release}

%description dev
dev components for the perl-Class-ReturnValue package.


%prep
%setup -q -n Class-ReturnValue-0.55

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Class/ReturnValue.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::ReturnValue.3
