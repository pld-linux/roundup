Summary:	Roundup Issue Tracker
Summary(pl.UTF-8):	Roundup - narzędzie do śledzenia zgłoszeń
Name:		roundup
Version:	1.4.8
Release:	2
License:	distributable (BSD-like, see COPYING.txt)
Group:		Applications/WWW
Source0:	http://pypi.python.org/packages/source/r/roundup/%{name}-%{version}.tar.gz
# Source0-md5:	a35e85dc3328d8c7ff774672f5f8a2e8
URL:		http://roundup.sourceforge.net/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
Requires:	pydoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple-to-use and -install issue-tracking system with command-line,
web and e-mail interfaces. Highly customisable.

%description -l pl.UTF-8
Łatwy w użyciu i instalacji system śledzenia zgłoszeń z interfejsami
linii poleceń, WWW i e-mail. Wysoko konfigurowalny.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.txt doc/*txt
%attr(755,root,root) %{_bindir}/roundup-*
%{py_sitescriptdir}/roundup
%{py_sitescriptdir}/roundup-%{version}-*.egg-info
%{_datadir}/roundup
%{_mandir}/man1/*
