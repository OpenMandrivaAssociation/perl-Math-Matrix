
%define realname   Math-Matrix
%define version    0.5
%define release    %mkrel 2

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


