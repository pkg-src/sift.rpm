%global goipath github.com/svent/sift
Version:        0.9.0

%gometa

Name:           sift
Release:        1%{?dist}
Summary:        A fast and powerful alternative to grep.
License:        GPLv3
URL:            https://sift-tool.org/
Source0:        %{gosource}
ExclusiveArch:  x86_64

# https://github.com/svent/go-flags
%global goipath_goflags github.com/svent/go-flags
%global commit_goflags  4bcbad344f0318adaf7aabc16929701459009aa3
Source10: https://%{goipath_goflags}/archive/%{commit_goflags}/go-flags-%{commit_goflags}.tar.gz
Provides: bundled(golang(%{goipath_goflags})) = %{commit_goflags}

# https://github.com/svent/go-nbreader
%global goipath_gonbreader github.com/svent/go-nbreader
%global commit_gonbreader  7cef48da76dca6a496faa7fe63e39ed665cbd219
Source11: https://%{goipath_gonbreader}/archive/%{commit_gonbreader}/go-nbreader-%{commit_gonbreader}.tar.gz
Provides: bundled(golang(%{goipath_gonbreader})) = %{commit_gonbreader}

# https://golang.org/x/crypto
%global goipath_crypto golang.org/x/crypto
%global commit_crypto  8dd112bcdc25174059e45e07517d9fc663123347
Source12: https://github.com/golang/crypto/archive/%{commit_crypto}/crypto-%{commit_crypto}.tar.gz
Provides: bundled(golang(%{goipath_crypto})) = %{commit_crypto}

# https://golang.org/x/sys
%global goipath_sys golang.org/x/sys
%global commit_sys  b6889370fb1098ed892bd3400d189bb6a3355813
Source13: https://github.com/golang/sys/archive/%{commit_sys}/sys-%{commit_sys}.tar.gz
Provides: bundled(golang(%{goipath_sys})) = %{commit_sys}

%description
sift has a slightly different focus than most other grep alternatives.
Code search, log search / digital forensics and data processing are the main use cases,
but the primary goal is to provide safe defaults and to make it easily configurable for a specific use case. 

%prep
%setup -q -a 10 -a 11 -a 12 -a 13
rm -rf vendor
mkdir -p vendor/`dirname %{goipath_goflags}`
mv go-flags-%{commit_goflags} vendor/%{goipath_goflags}
mkdir -p vendor/`dirname %{goipath_gonbreader}`
mv go-nbreader-%{commit_gonbreader} vendor/%{goipath_gonbreader}
mkdir -p vendor/`dirname %{goipath_crypto}`
mv crypto-%{commit_crypto} vendor/%{goipath_crypto}
mkdir -p vendor/`dirname %{goipath_sys}`
mv sys-%{commit_sys} vendor/%{goipath_sys}

%build
%gobuildroot
%gobuild -o _bin/sift %{goipath}

%install
install -Dpm 0755 _bin/sift %{buildroot}%{_bindir}/sift

%files
%license LICENSE
%doc README.md
%{_bindir}/sift

%changelog
* Sat Mar 02 2019 Florian Kaiser <florian.kaiser@fnkr.net> - 0.9.0-1
- Initial RPM release
