Summary:	Non-interactive ssh password auth
Name:		sshpass
Version:	1.04
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/sshpass/%{name}-%{version}.tar.gz
# Source0-md5:	87e7c72e319691c5fdf219f6c7effb4a
URL:		http://sshpass.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sshpass is a tool for non-interactivly performing password authentication
with SSH's so called "interactive keyboard password authentication". Most
user should use SSH's more secure public key authentiaction instead. 

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
