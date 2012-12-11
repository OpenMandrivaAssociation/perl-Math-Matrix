
%define realname   Math-Matrix
%define version    0.5
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Matrix data type (transpose, multiply etc)
Source:     http://www.cpan.org/modules/by-module/Math/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
The following methods are available:

new
    Constructor arguments are a list of references to arrays of the same
    length. The arrays are copied. The method returns *undef* in case of
    error.

            $a = new Math::Matrix ([rand,rand,rand],
                                   [rand,rand,rand],
                                   [rand,rand,rand]);

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.5-3mdv2011.0
+ Revision: 655044
- rebuild for updated spec-helper

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.5-2mdv2011.0
+ Revision: 375942
- rebuild

* Sun Mar 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.5-1mdv2009.1
+ Revision: 355187
- import perl-Math-Matrix


* Sun Mar 15 2009 cpan2dist 0.5-1mdv
- initial mdv release, generated with cpan2dist

