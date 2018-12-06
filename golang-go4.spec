# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath         go4.org
%global forgeurl        https://github.com/go4org/go4
%global commit          12aee241e64e68a7ceffb342f85290bc3d69d083

%global common_description %{expand:
Collection of packages for Go programmers.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Collection of packages for Go programmers
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/sys/windows)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/option)
BuildRequires: golang(google.golang.org/api/storage/v1)

%if %{with check}
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/option)
BuildRequires: golang(google.golang.org/api/storage/v1)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git12aee24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2-20180422git12aee24
- Upstream snapshot 12aee241e64e68a7ceffb342f85290bc3d69d083

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2-20180421git9599cf2
- Make multiarch

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180421git9599cf2
- First package for Fedora

