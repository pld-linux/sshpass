Summary:	Non-interactive ssh password auth
Name:		sshpass
Version:	1.06
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://downloads.sourceforge.net/sshpass/%{name}-%{version}.tar.gz
# Source0-md5:	f59695e3b9761fb51be7d795819421f9
URL:		http://sshpass.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sshpass is a tool to non-interactivly perform a password
authentication with SSH's so called "interactive keyboard password
authentication". Most users should use SSH's more secure public key
authentiaction instead.

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
%attr(755,root,root) %{_bindir}/sshpass
%{_mandir}/man1/sshpass.1*
